import time
import trading_app.trading_bot_coins.Config as conf
from trading_app.trading_bot_coins.token_decimal import get_token_decimal


class BNBTrade:
    def __init__(self, token, wallet_address, private_key, amount):
        self.token = token
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.amount = amount

    def buy(self):
        trade_token_address = conf.w3.toChecksumAddress(self.token)
        contract_trade_token = conf.w3.eth.contract(address=trade_token_address, abi=conf.TESTNET_BEP20_ABI)
        router_contract = conf.w3.eth.contract(address=conf.TESTNET_ROUTER_ADDRESS, abi=conf.TESTNET_ROUTER_ABI)
        token_symbol = contract_trade_token.functions.symbol().call()
        trading_token_decimal = contract_trade_token.functions.decimals().call()
        trading_token_decimal = get_token_decimal(trading_token_decimal)
        tokens_to_buy = self.amount
        tokens_to_buy = conf.w3.toWei(tokens_to_buy, 'ether')
        # For tokens that need to be approved First
        # Get Token Balance
        TokenInAccount = contract_trade_token.functions.balanceOf(self.wallet_address).call()
        approve = contract_trade_token.functions.approve(conf.TESTNET_ROUTER_ADDRESS, TokenInAccount).buildTransaction({
            'from': self.wallet_address,
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
                print(result)
            return result
        time.sleep(10)
        pancakeSwap_txn = router_contract.functions.swapTokensForExactETH(
            tokens_to_buy, conf.w3.toWei(TokenInAccount, trading_token_decimal),
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
            out = router_contract.functions.getAmountsOut(tokens_to_buy,
                                                          [conf.TESTNET_WBNB_ADDRESS, trade_token_address]).call()
            price = router_contract.functions.getAmountsOut(conf.w3.toWei(1, 'ether'),
                                                            [conf.TESTNET_WBNB_ADDRESS, trade_token_address]).call()
            price = conf.w3.fromWei(price[1], trading_token_decimal)
            out = conf.w3.fromWei(out[1], trading_token_decimal)
            # result = [conf.w3.toHex(tx_token), f"Bought {tokens_to_buy} BNB for {conf.w3.fromWei(tokens_to_buy,
            # trading_token_decimal)} {token_symbol}"]
            result = {'Price': price, 'Quantity': out, 'Side': 'Buy', 'TXN': conf.w3.toHex(tx_token)}
            return result
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result

    def sell(self):
        token_to_trade_address = conf.w3.toChecksumAddress(self.token)
        token_to_buy_contract = conf.w3.eth.contract(address=token_to_trade_address, abi=conf.TESTNET_BEP20_ABI)
        token_symbol = token_to_buy_contract.functions.symbol().call()
        router_contract = conf.w3.eth.contract(address=conf.TESTNET_ROUTER_ADDRESS, abi=conf.TESTNET_ROUTER_ABI)
        to_sell_amount = self.amount
        to_sell_amount = conf.w3.toWei(to_sell_amount, 'ether')
        decimal = token_to_buy_contract.functions.decimals().call()
        decimal = get_token_decimal(decimal)
        pancakeSwap_txn = router_contract.functions.swapExactETHForTokens(0,
                                                                          [conf.TESTNET_WBNB_ADDRESS,
                                                                           token_to_trade_address],
                                                                          self.wallet_address,
                                                                          (int(time.time() + 10000)))
        pancakeSwap_txn = pancakeSwap_txn.buildTransaction({
            'from': self.wallet_address,
            'value': to_sell_amount,  # Amount of BNB
            'gas': 750000,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(self.wallet_address)
        })

        signed_txn = conf.w3.eth.account.sign_transaction(pancakeSwap_txn, private_key=self.private_key)
        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            out = router_contract.functions.getAmountsOut(to_sell_amount,
                                                          [conf.TESTNET_WBNB_ADDRESS, token_to_trade_address]).call()
            price = router_contract.functions.getAmountsOut(conf.w3.toWei(1, 'ether'),
                                                            [conf.TESTNET_WBNB_ADDRESS, token_to_trade_address]).call()
            price = conf.w3.fromWei(price[1], decimal)
            out = conf.w3.fromWei(out[1], decimal)
            # result = [conf.w3.toHex(tx_token),
            #           f"Bought {conf.w3.fromWei(to_sell_amount, 'ether')} BNB of {token_symbol}"]
            result = {'Price': price, 'Quantity': out, 'Side': 'Sell', 'TXN': conf.w3.toHex(tx_token)}
            return result
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result
