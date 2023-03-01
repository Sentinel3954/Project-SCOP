from web3 import Web3, middleware, parity, exceptions
from test_abi import abi_suport, abi_teacher
from test_conts import conn_add_teacher, conn_adr_suport
from web3.middleware import geth_poa_middleware


#***************************************ОСНОВНЫЕ ПАРАМЕТРЫ***********************************************

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


