import time
import Config as conf
from token_decimal import get_token_decimal


class ADDLiquidity:
    def __init__(self, tokenA, tokenB, tokenA_amount, tokenB_amount, wallet_address, private_key):
        self.tokenA = tokenA
        self.tokenB = tokenB
        self.tokenA_amount = tokenA_amount
        self.tokenB_amount = tokenB_amount
        self.wallet_address = wallet_address
        self.private_key = private_key

    def add_liquidity(self):
        tokenA_contract = conf.w3.eth.contract(address=self.tokenA, abi=conf.BEP20_ABI)
        tokenB_contract = conf.w3.eth.contract(address=self.tokenB, abi=conf.BEP20_ABI)
        decimal = tokenA_contract.functions.decimals().call()
        decimal = get_token_decimal(decimal)
        tokenA_amount = conf.w3.toWei(self.tokenB_amount, decimal)
        decimal_1 = tokenB_contract.functions.decimals().call()
        decimal_1 = get_token_decimal(decimal_1)
        tokenB_amount = conf.w3.toWei(self.tokenB_amount, decimal_1)
        router_contract = conf.w3.eth.contract(address=conf.TESTNET_ROUTER_ADDRESS, abi=conf.TESTNET_ROUTER_ABI)
        TokenInAccount = tokenA_contract.functions.totalSupply().call()
        approve = tokenA_contract.functions.approve(conf.TESTNET_ROUTER_ADDRESS, TokenInAccount).buildTransaction({
            'from': self.wallet_address,
            'gas': 750000,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(self.wallet_address)
        })
        print(approve)
        signed_txn = conf.w3.eth.account.sign_transaction(approve, private_key=self.private_key)
        print(signed_txn)
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
            return result
        time.sleep(10)
        add_liquidity = router_contract.functions.addLiquidity(
            tokenA, tokenB, tokenA_amount, tokenB_amount, 0, 0, self.wallet_address, (int(time.time()) + 1000000)
        )
        estimated_gas = add_liquidity.estimateGas({'from': self.wallet_address})
        add_liquidity = add_liquidity.buildTransaction({
            'from': self.wallet_address,
            'gas': estimated_gas,
            'gasPrice': conf.w3.toWei('10', 'gwei'),
            'nonce': conf.w3.eth.get_transaction_count(self.wallet_address)
        })
        signed_txn = conf.w3.eth.account.sign_transaction(
            add_liquidity, private_key=self.private_key)
        print(signed_txn)
        time.sleep(5)
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
            return result
