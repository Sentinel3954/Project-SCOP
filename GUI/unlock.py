from web3 import Web3, middleware, parity, exceptions
from web3.middleware import geth_poa_middleware



w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


w3.geth.personal.unlock_account('0xA8368d91ce67D60b9e1288eB2ba2555C0e09EE94', '1', 1000000)
w3.geth.personal.unlock_account('0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7', '1', 1000000)
w3.geth.personal.unlock_account('0xE2449a03bFa5A89dA6295EB6547e91A15c63Ac8B', '1', 1000000)
w3.geth.personal.unlock_account('0x6D7Bd28346ceDB712Fa6811C4e16332A8fD38f26', '1', 1000000)



