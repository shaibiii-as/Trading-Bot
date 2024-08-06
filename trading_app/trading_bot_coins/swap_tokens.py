from trading_app.trading_bot_coins.token_decimal import get_token_decimal
import trading_app.trading_bot_coins.Config as conf
import time


class Swapping:
    def __init__(self, wallet_address, private_key, tokenA_address, tokenB_address, amount):
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.tokenA = tokenA_address
        self.tokenB = tokenB_address
        self.amount = amount

    def buy(self):
        amount = self.amount
        wallet = self.wallet_address
        tokenA = conf.w3.toChecksumAddress(self.tokenA)
        tokenB = conf.w3.toChecksumAddress(self.tokenB)
        tokenA_contract = conf.w3.eth.contract(address=tokenA, abi=conf.TESTNET_BEP20_ABI)
        tokenB_contract = conf.w3.eth.contract(address=tokenB, abi=conf.TESTNET_BEP20_ABI)
        decimal = tokenA_contract.functions.decimals().call()
        decimal = get_token_decimal(decimal)
        decimal_2 = tokenB_contract.functions.decimals().call()
        decimal_2 = get_token_decimal(decimal_2)
        amount = conf.w3.toWei(amount, decimal)
        router_contract = conf.w3.eth.contract(address=conf.TESTNET_ROUTER_ADDRESS, abi=conf.TESTNET_ROUTER_ABI)

        # Approve Transaction

        TokenInAccount = tokenB_contract.functions.balanceOf(wallet).call()
        approve = tokenA_contract.functions.approve(conf.TESTNET_ROUTER_ADDRESS, TokenInAccount).buildTransaction({
            'from': wallet,
            'gas': 7500000,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(wallet)
        })
        signed_txn = conf.w3.eth.account.sign_transaction(approve, private_key=self.private_key)

        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            result = conf.w3.toHex(tx_token)
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
                print(result)
            return result

        time.sleep(10)
        TokenInAccount = conf.w3.toWei(TokenInAccount, decimal_2)

        # Swapping Tokens

        function = router_contract.functions.swapTokensForExactTokens(
            amount,
            TokenInAccount,
            [
                tokenB,
                tokenA
            ],
            wallet,
            int(time.time()) + 10 * 60)

        estimated_gas = function.estimateGas({'from': wallet})

        tx_params = {
            'from': wallet,
            'gas': estimated_gas,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.getTransactionCount(wallet)
        }

        transaction = function.buildTransaction(tx_params)

        signed_txn = conf.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)

        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            price = router_contract.functions.getAmountsOut(conf.w3.toWei(1, decimal), [tokenA, tokenB]).call()
            price = conf.w3.fromWei(price[1], decimal_2)
            out = router_contract.functions.getAmountsOut(amount, [tokenA, tokenB]).call()
            out = conf.w3.fromWei(out[1], decimal_2)
            # result = [conf.w3.toHex(tx_token), f" {out} of {tokenB_contract.functions.symbol().call()}   Swapped To
            # :  {conf.w3.fromWei(amount, decimal)} {tokenA_contract.functions.symbol().call()}"]
            result = {'Price': price, 'Quantity': out, 'Side': 'Buy', 'TXN': conf.w3.toHex(tx_token)}
            return result
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result

    def sell(self, quantity):
        amount = quantity
        wallet = self.wallet_address
        tokenA = conf.w3.toChecksumAddress(self.tokenA)
        tokenB = conf.w3.toChecksumAddress(self.tokenB)
        tokenA_contract = conf.w3.eth.contract(address=tokenA, abi=conf.TESTNET_BEP20_ABI)
        tokenB_contract = conf.w3.eth.contract(address=tokenB, abi=conf.TESTNET_BEP20_ABI)
        decimal = tokenA_contract.functions.decimals().call()
        decimal = get_token_decimal(decimal)
        amount = conf.w3.toWei(amount, decimal)
        decimal_2 = tokenB_contract.functions.decimals().call()
        decimal_2 = get_token_decimal(decimal_2)
        router_contract = conf.w3.eth.contract(address=conf.TESTNET_ROUTER_ADDRESS, abi=conf.TESTNET_ROUTER_ABI)

        # Approve Transaction

        TokenInAccount = tokenA_contract.functions.balanceOf(wallet).call()
        approve = tokenA_contract.functions.approve(conf.TESTNET_ROUTER_ADDRESS, TokenInAccount).buildTransaction({
            'from': wallet,
            'gas': 7500000,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(wallet)
        })

        signed_txn = conf.w3.eth.account.sign_transaction(approve, private_key=self.private_key)

        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            result = conf.w3.toHex(tx_token)
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result

        time.sleep(10)

        # Transaction Part

        function = router_contract.functions.swapExactTokensForTokens(
            amount,
            0,
            [
                tokenA,
                tokenB
            ],
            wallet,
            int(time.time()) + 10 * 60)

        estimated_gas = function.estimateGas({'from': wallet})

        tx_params = {
            'from': wallet,
            'gas': estimated_gas,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.getTransactionCount(wallet)
        }

        transaction = function.buildTransaction(tx_params)

        signed_txn = conf.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)

        try:
            tx_token = conf.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            out = router_contract.functions.getAmountsOut(amount, [tokenA, tokenB]).call()
            price = router_contract.functions.getAmountsOut(conf.w3.toWei(1, decimal), [tokenA, tokenB]).call()
            price = conf.w3.fromWei(price[1], decimal_2)
            out = conf.w3.fromWei(out[1], decimal_2)
            # result = [conf.w3.toHex(tx_token), f" {conf.w3.fromWei(amount, decimal)} {
            # tokenA_contract.functions.symbol().call()}  Swapped To : {out} of {tokenB_contract.functions.symbol(
            # ).call()} "]
            result = {'Price': price, 'Quantity': out, 'Side': 'Sell', 'TXN': conf.w3.toHex(tx_token)}
            return result
        except ValueError as e:
            if e.args[0].get('message') in 'intrinsic gas too low':
                result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
            else:
                result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            return result
