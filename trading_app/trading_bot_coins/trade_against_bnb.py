import time
import trading_app.trading_bot_coins.Config as conf
from trading_app.trading_bot_coins.token_decimal import get_token_decimal


class BEPTrade:
    def __init__(self, token, wallet_address, private_key, amount):
        self.token = token
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.amount = amount

    def buy(self):
        token_to_trade_address = conf.w3.toChecksumAddress(self.token)
        token_to_buy_contract = conf.w3.eth.contract(address=token_to_trade_address, abi=conf.TESTNET_BEP20_ABI)
        router_contract = conf.w3.eth.contract(address=conf.TESTNET_ROUTER_ADDRESS, abi=conf.TESTNET_ROUTER_ABI)
        to_sell_amount = self.amount
        decimal = token_to_buy_contract.functions.decimals().call()
        decimal = get_token_decimal(decimal)
        to_sell_amount = conf.w3.toWei(to_sell_amount, decimal)

        pancakeSwap_txn = router_contract.functions.swapETHForExactTokens(to_sell_amount,
                                                                          [conf.TESTNET_WBNB_ADDRESS,
                                                                           token_to_trade_address],
                                                                          self.wallet_address,
                                                                          10000000000)
        pancakeSwap_txn = pancakeSwap_txn.buildTransaction({
            'from': self.wallet_address,
            'value': 1000000000000000000,  # Amount of BNB
            'gas': 750000,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(self.wallet_address)
        })

        signed_txn = conf.w3.eth.account.sign_transaction(pancakeSwap_txn, private_key=self.private_key)
        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            out = router_contract.functions.getAmountsOut(to_sell_amount,
                                                          [token_to_trade_address, conf.TESTNET_WBNB_ADDRESS]).call()
            price = router_contract.functions.getAmountsOut(conf.w3.toWei(1, decimal),
                                                            [token_to_trade_address, conf.TESTNET_WBNB_ADDRESS]).call()
            price = conf.w3.fromWei(price[1], 'ether')
            out = conf.w3.fromWei(out[1], 'ether')
            # result = [conf.w3.toHex(tx_token), f"Bought  {token_symbol}"]
            result = {'Price': price, 'Quantity': out, 'Side': 'Buy', 'TXN': conf.w3.toHex(tx_token)}
            return result
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result

    def sell(self):
        trade_token_address = conf.w3.toChecksumAddress(self.token)
        contract_trade_token = conf.w3.eth.contract(address=trade_token_address, abi=conf.TESTNET_BEP20_ABI)
        router_contract = conf.w3.eth.contract(address=conf.TESTNET_ROUTER_ADDRESS, abi=conf.TESTNET_ROUTER_ABI)
        token_symbol = contract_trade_token.functions.symbol().call()
        trading_token_decimal = contract_trade_token.functions.decimals().call()
        trading_token_decimal = get_token_decimal(trading_token_decimal)
        tokens_to_sell = self.amount
        tokens_to_sell = conf.w3.toWei(tokens_to_sell, trading_token_decimal)
        # For tokens that need to be approved First
        # Get Token Balance
        TokenInAccount = contract_trade_token.functions.balanceOf(self.wallet_address).call()
        approve = contract_trade_token.functions.approve(conf.TESTNET_ROUTER_ADDRESS, TokenInAccount).buildTransaction({
            'from': conf.YOUR_WALLET_ADDRESS,
            'gas': 750000,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(self.wallet_address)
        })
        signed_txn = conf.w3.eth.account.sign_transaction(approve, private_key=self.private_key)
        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            result = conf.w3.toHex(tx_token)
            return result
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result
        time.sleep(10)
        pancakeSwap_txn = router_contract.functions.swapExactTokensForETH(
            tokens_to_sell, 0,
            [trade_token_address, conf.TESTNET_WBNB_ADDRESS],
            self.wallet_address,
            (int(time.time() + 1000000))
        ).buildTransaction({
            'from': self.wallet_address,
            'gas': 750000,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(self.wallet_address)
        })

        signed_txn = conf.w3.eth.account.sign_transaction(
            pancakeSwap_txn, private_key=self.private_key)

        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            out = router_contract.functions.getAmountsOut(tokens_to_sell,
                                                          [trade_token_address, conf.TESTNET_WBNB_ADDRESS]).call()
            price = router_contract.functions.getAmountsOut(conf.w3.toWei(1, trading_token_decimal),
                                                            [trade_token_address, conf.TESTNET_WBNB_ADDRESS]).call()
            price = conf.w3.fromWei(price[1], 'ether')
            out = conf.w3.fromWei(out[1], 'ether')
            # result = [conf.w3.toHex(tx_token),
            #           f"Sold {conf.w3.fromWei(tokens_to_sell, trading_token_decimal)} {token_symbol}"]
            result = {'Price': price, 'Quantity': out, 'Side': 'sell', 'TXN': conf.w3.toHex(tx_token)}
            return result
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result
