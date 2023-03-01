# from web3 import Web3, middleware, parity, exceptions
# from test_abi import abi_suport, abi_teacher
# from test_conts import conn_add_teacher, conn_adr_suport
# from web3.middleware import geth_poa_middleware
import re
import string


# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# contract_suport = w3.eth.contract(address=conn_adr_suport, abi=abi_suport)
# contract_teacher = w3.eth.contract(address=conn_add_teacher, abi=abi_teacher)
letters_and_numbers = string.ascii_uppercase + string.ascii_lowercase + '1234567890'
ang_letters = string.ascii_uppercase + string.ascii_lowercase
rus_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
nums = '1234567890'



def check_password(password):
    if len(password) < 8:
        return False
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).*$')
    match = pattern.search(password)
    return bool(match)

def check_email(email):
    pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
    return pattern.match(email) is not None


def check_name(name_str):
    if len(name_str) < 8 or len(name_str) > 100: return False

    # проверяем, что строка содержит только буквы русского алфавита и пробелы
    if not re.match(r'^[а-яА-Я ]+$', name_str): return False

    words = name_str.split()

    if not words: return False

    # проверяем, что первое слово - фамилия, содержит только буквы русского алфавита и начинается с заглавной буквы
    if not re.match(r'^[А-Яа-я]+$', words[0]) or not words[0].istitle(): return False

    # если есть хотя бы два слова, то второе - имя, должно содержать только буквы русского алфавита и начинаться с заглавной буквы
    if len(words) >= 2 and (not re.match(r'^[А-Яа-я]+$', words[1]) or not words[1].istitle()): return False

    # если есть три слова, то третье - отчество, должно содержать только буквы русского алфавита и начинаться с заглавной буквы
    if len(words) == 3 and (not re.match(r'^[А-Яа-я]+$', words[2]) or not words[2].istitle()): return False

    if len(words) > 3: return False
    return True


print(check_email('2301@mai.ru'))

