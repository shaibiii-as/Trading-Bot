from web3 import Web3
import os

BSC_MAIN_NET = 'https://bsc-dataseed.binance.org/'
BSC_TEST_NET = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
w3 = Web3(Web3.HTTPProvider(BSC_TEST_NET))
YOUR_WALLET_ADDRESS = w3.toChecksumAddress('0x10780b34025a93927ae62776Fe43419166ec88D2')
YOUR_PRIVATE_KEY = '065006b3a500142836de1346435a79885e9c3a1751b36fd65bca788525968989'
ROUTER_ADDRESS = w3.toChecksumAddress('0x10ED43C718714eb63d5aA57B78B54704E256024E')
WBNB_ADDRESS = w3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c")
ROUTER_ABI = [{"inputs": [{"internalType": "address", "name": "_factory", "type": "address"},
                          {"internalType": "address", "name": "_WETH", "type": "address"}],
               "stateMutability": "nonpayable", "type": "constructor"},
              {"inputs": [], "name": "WETH", "outputs": [{"internalType": "address", "name": "", "type": "address"}],
               "stateMutability": "view", "type": "function"}, {
                  "inputs": [{"internalType": "address", "name": "tokenA", "type": "address"},
                             {"internalType": "address", "name": "tokenB", "type": "address"},
                             {"internalType": "uint256", "name": "amountADesired", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountBDesired", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "addLiquidity", "outputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                                                      {"internalType": "uint256", "name": "amountB", "type": "uint256"},
                                                      {"internalType": "uint256", "name": "liquidity",
                                                       "type": "uint256"}], "stateMutability": "nonpayable",
                  "type": "function"}, {"inputs": [{"internalType": "address", "name": "token", "type": "address"},
                                                   {"internalType": "uint256", "name": "amountTokenDesired",
                                                    "type": "uint256"},
                                                   {"internalType": "uint256", "name": "amountTokenMin",
                                                    "type": "uint256"},
                                                   {"internalType": "uint256", "name": "amountETHMin",
                                                    "type": "uint256"},
                                                   {"internalType": "address", "name": "to", "type": "address"},
                                                   {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                                        "name": "addLiquidityETH", "outputs": [
            {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"}], "stateMutability": "payable",
                                        "type": "function"},
              {"inputs": [], "name": "factory", "outputs": [{"internalType": "address", "name": "", "type": "address"}],
               "stateMutability": "view", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                             {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
                             {"internalType": "uint256", "name": "reserveOut", "type": "uint256"}],
                  "name": "getAmountIn",
                  "outputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"}],
                  "stateMutability": "pure", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                             {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
                             {"internalType": "uint256", "name": "reserveOut", "type": "uint256"}],
                  "name": "getAmountOut",
                  "outputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"}],
                  "stateMutability": "pure", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"}],
                  "name": "getAmountsIn",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "view", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"}],
                  "name": "getAmountsOut",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "view", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                             {"internalType": "uint256", "name": "reserveA", "type": "uint256"},
                             {"internalType": "uint256", "name": "reserveB", "type": "uint256"}], "name": "quote",
                  "outputs": [{"internalType": "uint256", "name": "amountB", "type": "uint256"}],
                  "stateMutability": "pure", "type": "function"}, {
                  "inputs": [{"internalType": "address", "name": "tokenA", "type": "address"},
                             {"internalType": "address", "name": "tokenB", "type": "address"},
                             {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "removeLiquidity",
                  "outputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                              {"internalType": "uint256", "name": "amountB", "type": "uint256"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                             {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "removeLiquidityETH",
                  "outputs": [{"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                              {"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                             {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "removeLiquidityETHSupportingFeeOnTransferTokens",
                  "outputs": [{"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                             {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                             {"internalType": "bool", "name": "approveMax", "type": "bool"},
                             {"internalType": "uint8", "name": "v", "type": "uint8"},
                             {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                             {"internalType": "bytes32", "name": "s", "type": "bytes32"}],
                  "name": "removeLiquidityETHWithPermit",
                  "outputs": [{"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                              {"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                             {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                             {"internalType": "bool", "name": "approveMax", "type": "bool"},
                             {"internalType": "uint8", "name": "v", "type": "uint8"},
                             {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                             {"internalType": "bytes32", "name": "s", "type": "bytes32"}],
                  "name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens",
                  "outputs": [{"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "address", "name": "tokenA", "type": "address"},
                             {"internalType": "address", "name": "tokenB", "type": "address"},
                             {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                             {"internalType": "bool", "name": "approveMax", "type": "bool"},
                             {"internalType": "uint8", "name": "v", "type": "uint8"},
                             {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                             {"internalType": "bytes32", "name": "s", "type": "bytes32"}],
                  "name": "removeLiquidityWithPermit",
                  "outputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                              {"internalType": "uint256", "name": "amountB", "type": "uint256"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapETHForExactTokens",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "payable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapExactETHForTokens",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "payable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapExactETHForTokensSupportingFeeOnTransferTokens", "outputs": [],
                  "stateMutability": "payable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapExactTokensForETH",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapExactTokensForETHSupportingFeeOnTransferTokens", "outputs": [],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapExactTokensForTokens",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapExactTokensForTokensSupportingFeeOnTransferTokens", "outputs": [],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapTokensForExactETH",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "nonpayable", "type": "function"}, {
                  "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                             {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
                             {"internalType": "address[]", "name": "path", "type": "address[]"},
                             {"internalType": "address", "name": "to", "type": "address"},
                             {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                  "name": "swapTokensForExactTokens",
                  "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                  "stateMutability": "nonpayable", "type": "function"},
              {"stateMutability": "payable", "type": "receive"}]

BEP20_ABI = [{'inputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'constructor'},
             {'anonymous': False,
              'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'},
                         {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'},
                         {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}],
              'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [
        {'indexed': True, 'internalType': 'address', 'name': 'previousOwner', 'type': 'address'},
        {'indexed': True, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}],
                                                     'name': 'OwnershipTransferred', 'type': 'event'},
             {'anonymous': False,
              'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'},
                         {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'},
                         {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}],
              'name': 'Transfer', 'type': 'event'}, {'constant': True, 'inputs': [], 'name': '_decimals', 'outputs': [
        {'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'payable': False, 'stateMutability': 'view',
                                                     'type': 'function'},
             {'constant': True, 'inputs': [], 'name': '_name',
              'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'payable': False,
              'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': '_symbol',
                                                               'outputs': [{'internalType': 'string', 'name': '',
                                                                            'type': 'string'}], 'payable': False,
                                                               'stateMutability': 'view', 'type': 'function'},
             {'constant': True, 'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'},
                                           {'internalType': 'address', 'name': 'spender', 'type': 'address'}],
              'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
              'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [
        {'internalType': 'address', 'name': 'spender', 'type': 'address'},
        {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [
        {'internalType': 'bool', 'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable',
                                                                                 'type': 'function'},
             {'constant': True, 'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}],
              'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
              'payable': False, 'stateMutability': 'view', 'type': 'function'},
             {'constant': False, 'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}],
              'name': 'burn', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'payable': False,
              'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'decimals',
                                                                     'outputs': [{'internalType': 'uint8', 'name': '',
                                                                                  'type': 'uint8'}], 'payable': False,
                                                                     'stateMutability': 'view', 'type': 'function'},
             {'constant': False, 'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'},
                                            {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}],
              'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
              'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'},
             {'constant': True, 'inputs': [], 'name': 'getOwner',
              'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'payable': False,
              'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [
        {'internalType': 'address', 'name': 'spender', 'type': 'address'},
        {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [
        {'internalType': 'bool', 'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable',
                                                               'type': 'function'},
             {'constant': False, 'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}],
              'name': 'mint', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'payable': False,
              'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'name',
                                                                     'outputs': [{'internalType': 'string', 'name': '',
                                                                                  'type': 'string'}], 'payable': False,
                                                                     'stateMutability': 'view', 'type': 'function'},
             {'constant': True, 'inputs': [], 'name': 'owner',
              'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'payable': False,
              'stateMutability': 'view', 'type': 'function'},
             {'constant': False, 'inputs': [], 'name': 'renounceOwnership', 'outputs': [], 'payable': False,
              'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'symbol',
                                                                     'outputs': [{'internalType': 'string', 'name': '',
                                                                                  'type': 'string'}], 'payable': False,
                                                                     'stateMutability': 'view', 'type': 'function'},
             {'constant': True, 'inputs': [], 'name': 'totalSupply',
              'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'payable': False,
              'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [
        {'internalType': 'address', 'name': 'recipient', 'type': 'address'},
        {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [
        {'internalType': 'bool', 'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable',
                                                               'type': 'function'}, {'constant': False, 'inputs': [
        {'internalType': 'address', 'name': 'sender', 'type': 'address'},
        {'internalType': 'address', 'name': 'recipient', 'type': 'address'},
        {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [
        {'internalType': 'bool', 'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'nonpayable',
                                                                                     'type': 'function'},
             {'constant': False, 'inputs': [{'internalType': 'address', 'name': 'newOwner', 'type': 'address'}],
              'name': 'transferOwnership', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable',
              'type': 'function'}]

"""        Testnet Credentials         """

TESTNET_ROUTER_ADDRESS = w3.toChecksumAddress('0xD99D1c33F9fC3444f8101754aBC46c52416550D1')
TESTNET_WBNB_ADDRESS = w3.toChecksumAddress('0xae13d989dac2f0debff460ac112a837c89baa7cd')
TESTNET_ROUTER_ABI = [{"inputs": [{"internalType": "address", "name": "_factory", "type": "address"},
                                  {"internalType": "address", "name": "_WETH", "type": "address"}],
                       "stateMutability": "nonpayable", "type": "constructor"},
                      {"inputs": [], "name": "WETH",
                       "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                       "stateMutability": "view", "type": "function"}, {
                          "inputs": [{"internalType": "address", "name": "tokenA", "type": "address"},
                                     {"internalType": "address", "name": "tokenB", "type": "address"},
                                     {"internalType": "uint256", "name": "amountADesired", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountBDesired", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "addLiquidity",
                          "outputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                                      {"internalType": "uint256", "name": "amountB", "type": "uint256"},
                                      {"internalType": "uint256", "name": "liquidity", "type": "uint256"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                                     {"internalType": "uint256", "name": "amountTokenDesired", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "addLiquidityETH",
                          "outputs": [{"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                                      {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
                                      {"internalType": "uint256", "name": "liquidity", "type": "uint256"}],
                          "stateMutability": "payable", "type": "function"},
                      {"inputs": [], "name": "factory",
                       "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                       "stateMutability": "view", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                                     {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
                                     {"internalType": "uint256", "name": "reserveOut", "type": "uint256"}],
                          "name": "getAmountIn",
                          "outputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"}],
                          "stateMutability": "pure", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                                     {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
                                     {"internalType": "uint256", "name": "reserveOut", "type": "uint256"}],
                          "name": "getAmountOut",
                          "outputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"}],
                          "stateMutability": "pure", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"}],
                          "name": "getAmountsIn",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "view", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"}],
                          "name": "getAmountsOut",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "view", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                                     {"internalType": "uint256", "name": "reserveA", "type": "uint256"},
                                     {"internalType": "uint256", "name": "reserveB", "type": "uint256"}],
                          "name": "quote",
                          "outputs": [{"internalType": "uint256", "name": "amountB", "type": "uint256"}],
                          "stateMutability": "pure", "type": "function"}, {
                          "inputs": [{"internalType": "address", "name": "tokenA", "type": "address"},
                                     {"internalType": "address", "name": "tokenB", "type": "address"},
                                     {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "removeLiquidity",
                          "outputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                                      {"internalType": "uint256", "name": "amountB",
                                       "type": "uint256"}], "stateMutability": "nonpayable",
                          "type": "function"},
                      {"inputs": [{"internalType": "address", "name": "token", "type": "address"},
                                  {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                                  {"internalType": "uint256", "name": "amountTokenMin",
                                   "type": "uint256"},
                                  {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                                  {"internalType": "address", "name": "to", "type": "address"},
                                  {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                       "name": "removeLiquidityETH",
                       "outputs": [{"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                                   {"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                       "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                                     {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "removeLiquidityETHSupportingFeeOnTransferTokens",
                          "outputs": [{"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                                     {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                                     {"internalType": "bool", "name": "approveMax", "type": "bool"},
                                     {"internalType": "uint8", "name": "v", "type": "uint8"},
                                     {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                                     {"internalType": "bytes32", "name": "s", "type": "bytes32"}],
                          "name": "removeLiquidityETHWithPermit",
                          "outputs": [{"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                                      {"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                                     {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                                     {"internalType": "bool", "name": "approveMax", "type": "bool"},
                                     {"internalType": "uint8", "name": "v", "type": "uint8"},
                                     {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                                     {"internalType": "bytes32", "name": "s", "type": "bytes32"}],
                          "name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens",
                          "outputs": [{"internalType": "uint256", "name": "amountETH", "type": "uint256"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "address", "name": "tokenA", "type": "address"},
                                     {"internalType": "address", "name": "tokenB", "type": "address"},
                                     {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                                     {"internalType": "bool", "name": "approveMax", "type": "bool"},
                                     {"internalType": "uint8", "name": "v", "type": "uint8"},
                                     {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                                     {"internalType": "bytes32", "name": "s", "type": "bytes32"}],
                          "name": "removeLiquidityWithPermit",
                          "outputs": [{"internalType": "uint256", "name": "amountA", "type": "uint256"},
                                      {"internalType": "uint256", "name": "amountB", "type": "uint256"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapETHForExactTokens",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "payable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapExactETHForTokens",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "payable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapExactETHForTokensSupportingFeeOnTransferTokens", "outputs": [],
                          "stateMutability": "payable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapExactTokensForETH",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapExactTokensForETHSupportingFeeOnTransferTokens", "outputs": [],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapExactTokensForTokens",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapExactTokensForTokensSupportingFeeOnTransferTokens", "outputs": [],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapTokensForExactETH",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "nonpayable", "type": "function"}, {
                          "inputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                                     {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
                                     {"internalType": "address[]", "name": "path", "type": "address[]"},
                                     {"internalType": "address", "name": "to", "type": "address"},
                                     {"internalType": "uint256", "name": "deadline", "type": "uint256"}],
                          "name": "swapTokensForExactTokens",
                          "outputs": [{"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}],
                          "stateMutability": "nonpayable", "type": "function"},
                      {"stateMutability": "payable", "type": "receive"}]
TESTNET_BEP20_ABI = [
    {
        "inputs": [
            {"internalType": "string", "name": "name_", "type": "string"},
            {"internalType": "string", "name": "symbol_", "type": "string"},
            {"internalType": "uint8", "name": "decimals_", "type": "uint8"},
            {
                "internalType": "uint256",
                "name": "initialBalance_",
                "type": "uint256"
            },
            {
                "internalType": "address payable",
                "name": "feeReceiver_",
                "type": "address"
            }
        ],
        "stateMutability": "payable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"}
        ],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {
                "internalType": "uint256",
                "name": "subtractedValue",
                "type": "uint256"
            }
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"}
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "newOwner", "type": "address"}
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
