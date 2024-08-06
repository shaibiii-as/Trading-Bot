import multiprocessing
import os
import time
import requests
import numpy as np
import pandas_ta as ta
import pandas as pd
from trading_app.trading_bot_coins.trade_with_bnb import BNBTrade
from trading_app.trading_bot_coins.trade_against_bnb import BEPTrade
from trading_app.trading_bot_coins.swap_tokens import Swapping
from trading_app.models import OrderHistory

# client.API_URL = 'https://testnet.binance.vision/api'
LIMIT = 1000


class TradingBot:

    def __init__(self, wallet_address, wallet_secret_key, tokenA, tokenB, symbol, time_period, stop_profit, stop_loss,
                 quantity):
        self.wallet_address = wallet_address
        self.wallet_secret_key = wallet_secret_key
        self.symbol = symbol
        self.tokenA = tokenA
        self.tokenB = tokenB
        self.stop_loss = stop_loss
        self.stop_profit = stop_profit
        self.time_period = time_period
        self.remaining_quantity = quantity
        self.buy = False
        self.sell = False
        self.currency_price = None
        self.quantity = quantity / 4
        self.profit = None
        self.total_quantity = quantity
        self.loss = None
        self.thread = None
        if self.symbol.find("BNB") == 0:
            self.order = BNBTrade(self.tokenB, self.wallet_address, self.wallet_secret_key, self.total_quantity)
        elif self.symbol.find("BNB") > 0:
            self.order = BEPTrade(self.tokenA, self.wallet_address, self.wallet_secret_key, self.total_quantity)
        else:
            self.order = Swapping(self.wallet_address, self.wallet_secret_key, self.tokenA, self.tokenB,
                                  self.total_quantity)

    def start_process(self):
        self.thread = multiprocessing.Process(target=self.main)
        self.thread.start()

    def kill_process(self):
        self.thread.kill()

    def get_data(self):
        try:
            url = "https://api.binance.com/api/v3/klines?symbol={}&interval={}&limit={}".format(self.symbol,
                                                                                                self.time_period,
                                                                                                LIMIT)
        except Exception as e:
            url = "https://api.binance.com/api/v3/klines?symbol={}&interval={}&limit={}".format(self.symbol,
                                                                                                self.time_period,
                                                                                                LIMIT)
        res = requests.get(url)
        closed_data = []
        for each in res.json():
            closed_data.append(float(each[4]))
        return np.array(closed_data)

    def get_price(self):
        try:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}"
        except Exception as e:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}"
        res = requests.get(url)
        return float(res.json()['price'])

    def calculate_ema(self, prices, days, smoothing=2):
        ema = [sum(prices[:days]) / days]
        for price in prices[days:]:
            ema.append((price * (smoothing / (1 + days))) + ema[-1] * (1 - (smoothing / (1 + days))))
        return ema

    def buy_strategy(self, ema_9, ema_26, last_ema_9, last_ema_26, rsi, buy):
        if ema_9 > ema_26 and last_ema_9:
            if last_ema_9 < last_ema_26 and not buy:
                if rsi > 0 and rsi < 80:
                    self.currency_price = self.get_price()
                    order = self.order.buy()
                    print(order)
                    order_history_obj = OrderHistory(order_symbol=self.symbol, order_side="BUY",
                                                     order_price=float(order['Price']),
                                                     order_qty=str(self.total_quantity))
                    order_history_obj.save()
                    buy_price = self.currency_price
                    self.profit = buy_price + ((buy_price * self.stop_profit) / 100)
                    self.loss = buy_price - ((buy_price * self.stop_loss) / 100)
                    file = open(f'{self.symbol} order.txt', 'w')
                    file.write(str(self.profit))
                    file.write("\n" + str(self.loss))
                    file.write("\n" + str(self.remaining_quantity))
                    file.write("\n" + str(self.quantity))
                    file.close()
                    self.sell = True
                    self.buy = True
                    time.sleep(10)

    def sell_strategy(self, ema_9, ema_26, last_ema_9, last_ema_26, rsi):
        self.currency_price = self.get_price()
        if self.remaining_quantity > 0:
            if self.currency_price >= self.profit:
                order = self.order.sell(self.quantity)
                print(order)
                self.remaining_quantity = round((self.remaining_quantity - self.quantity), 4)
                self.profit *= 1.001
                order_history_obj = OrderHistory(order_symbol=self.symbol, order_side="SELL",
                                                 order_price=order['Price'],
                                                 order_qty=self.quantity)
                order_history_obj.save()
                os.remove(f'{self.symbol} order.txt')

                file = open(f'{self.symbol} order.txt', 'w')
                file.write(str(self.profit))
                file.write("\n" + str(self.loss))
                file.write("\n" + str(self.remaining_quantity))
                file.write("\n" + str(self.quantity))
                time.sleep(60)
                file.close()
        else:
            os.remove(f'{self.symbol} order.txt')
            self.buy = False
            self.sell = False
            time.sleep(20)
            return

        if self.currency_price <= self.loss:
            self.buy = False
            self.sell = False
            os.remove(f'{self.symbol} order.txt')
            order = self.order.sell(self.remaining_quantity)
            print(order)
            order_history_obj = OrderHistory(order_symbol=self.symbol, order_side="SELL", order_price=order['Price'],
                                             order_qty=self.remaining_quantity)
            order_history_obj.save()
            time.sleep(20)
            return

        if ema_26 > ema_9 and last_ema_26:
            if last_ema_26 < last_ema_9:
                if rsi < 50 and rsi > 20:
                    order = self.order.sell(self.remaining_quantity)
                    print(order)
                    order_history_obj = OrderHistory(order_symbol=self.symbol,
                                                     order_side="SELL",
                                                     order_price=order['Price'],
                                                     order_qty=self.remaining_quantity)
                    order_history_obj.save()
                    time.sleep(20)
                    self.buy = False
                    self.sell = False
                    os.remove(f'{self.symbol} order.txt')
                    return

    def main(self):
        last_ema_9 = None
        last_ema_26 = None
        while True:
            try:
                if os.path.exists(f"{self.symbol} order.txt"):
                    file = open(f"{self.symbol} order.txt", 'r')
                    v, w, x, y = file.readlines()
                    self.profit = float(v)
                    self.loss = float(w)
                    self.remaining_quantity = float(x)
                    self.quantity = float(y)
                    file.close()
                    self.sell = True
                    self.buy = True

                closing_data = self.get_data()
                self.currency_price = self.get_price()
                ema_9 = self.calculate_ema(closing_data, 9)[-1]
                ema_26 = self.calculate_ema(closing_data, 26)[-1]
                rsi = list(ta.rsi(close=pd.Series(closing_data), length=14))[-1]

                print("\n--------- Currency ---------")
                print(self.symbol, ":", self.currency_price)
                print("----------------------------")
                print("\n************** Strategy Result ***********")
                print("EMA-9 Strategy : ", ema_9)
                print("EMA-26 Signal  : ", ema_26)
                print("RSI Strategy   : ", rsi)

                self.buy_strategy(
                    ema_9=ema_9,
                    ema_26=ema_26,
                    last_ema_9=last_ema_9,
                    last_ema_26=last_ema_26,
                    rsi=rsi,
                    buy=self.buy
                )
                last_ema_9 = ema_9
                last_ema_26 = ema_26
                while self.sell:
                    closing_data = self.get_data()
                    self.currency_price = self.get_price()
                    ema_9 = self.calculate_ema(closing_data, 9)[-1]
                    ema_26 = self.calculate_ema(closing_data, 26)[-1]
                    rsi = list(ta.rsi(close=pd.Series(closing_data), length=14))[-1]
                    self.sell_strategy(
                        ema_9=ema_9,
                        ema_26=ema_26,
                        last_ema_9=last_ema_9,
                        last_ema_26=last_ema_26,
                        rsi=rsi
                    )
                    print("\n--------- Currency ---------")
                    print(self.symbol, ":", self.currency_price)
                    print("----------------------------")
                    print("\n************** Sell Strategy Result ***********")
                    print("EMA-9 Strategy : ", ema_9)
                    print("EMA-26 Signal  : ", ema_26)
                    print("RSI Strategy   : ", rsi)
                    last_ema_9 = ema_9
                    last_ema_26 = ema_26
                    time.sleep(30)
                time.sleep(30)
            except Exception as e:
                time.sleep(10)
                print(e)
