from web3 import Web3, middleware, parity, exceptions
from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from abi import *
from const import *
from secret_key import key
from web3.middleware import geth_poa_middleware
import smtplib                                              # Импортируем библиотеку по работе с SMTP                       # Общий тип
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.multipart import MIMEMultipart              # Многокомпонентный объект
from secret import *
import random
import string
from work_to_date import *
import re
from web3.exceptions import InvalidAddress

#***************************************ОСНОВНЫЕ ПАРАМЕТРЫ***********************************************

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract_makestruct0 = w3.eth.contract(address=conn_adr_makestruct0, abi=abi_make_struct0)
contract_makestruct1 = w3.eth.contract(address=conn_adr_makestruct1, abi=abi_make_struct1)
contract_student0 = w3.eth.contract(address=conn_adr_student1, abi=abi_student0)
contract_student1 = w3.eth.contract(address=conn_adr_student2, abi=abi_student1)
contract_teacher = w3.eth.contract(address=conn_adr_teacher, abi=abi_teacher)
contract_guifunction = w3.eth.contract(address=conn_adr_guifunction, abi=abi_guifunction)

app = Flask(__name__)
app.secret_key = key

nums = '1234567890'
letters_and_numbers = string.ascii_uppercase + string.ascii_lowercase + nums
ang_letters = string.ascii_uppercase + string.ascii_lowercase
rus_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'




# #************************************Разное*********************************
@app.before_request
def before_request():
    if 'addr' in session:
        w3.geth.personal.unlock_account(session['addr'], session['password_addr'], 1000000)

@app.post('/exit')
def exit():
    session.update({'login': '', 'password': ''})
    session.update({'corectly_login': session['login'], 'corectly_pass': session['password_acc']})
    return redirect(url_for('go_to_auth'))

@app.post('/back')
def back():
    pass

def send_email(addr_to, text = ""):
    print(text)
    addr_from = login                         # Отправитель
    msg_subj = "Подтверждение почты"
    msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From']    = addr_from                              # Адресат
    msg['To']      = addr_to                                # Получатель
    msg['Subject'] = msg_subj                               # Тема сообщения
    #msg_text = "Ваш электронный договор"
    body = text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(login, passw_app)
    mail.send_message(msg)
    mail.quit()


# #************************************Проверки*********************************
def user_is_auth(func):
    def wrapper():
        if session.get('corectly_login', ''):
            func()
        else: 
            flash(f'Пользаватель не авторизирован', category='status_class_wrong')
            return render_template('auth.html', addr=session.get('addr', ""))
    return wrapper

def check_password(password):
    if len(password) < 8:
        return False
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).*$')
    match = pattern.search(password)
    return bool(match)

def check_emaill(email):
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


# #************************************Полиморфизм*********************************
def student_data():
    data = contract_student0.functions.checkStudent(session['addr']).call({'from': session['addr']})
    session['proj_num'] = data[-2]
    data2 = contract_student1.functions.checkProject(session['addr']).call({'from': session['addr']})
    print(data, '************************', data2, sep='\n')
    slovar={}
    k=0
    for i in data[3]:
        slovar.update({k: i})
        k+=1
    return data, data2, slovar

 
def student_sides():
    data = contract_student0.functions.checkStudent(session['addr']).call({'from': session['addr']})
    strong_side = data[3]
    if len(strong_side)<=7: len_tasks = 0
    else: len_tasks = 10
    slovar = {}
    k=0
    for i in data[3]:
        slovar.update({k: i})
        k+=1
    return strong_side, slovar, len_tasks

def student_project():
    data = contract_student0.functions.checkStudent(session['addr']).call({'from': session['addr']})
    data2 = contract_student1.functions.checkProject(session['addr']).call({'from': session['addr']})
    data3 = contract_student1.functions.checkDataStudentInProject(session['addr']).call({'from': session['addr']})
    role = contract_makestruct1.functions.getRole(session['addr'], session['proj_num']).call({'from': session['addr']})
    login_teacher = contract_makestruct0.functions.getTeacherStruct(data2[2]).call({'from': session['addr']})[0]
    print(data, '*********************', data2, '*************', data3, '**********', role, '**********', login_teacher, '**********', sep='\n')
    slovar = {}
    k=0
    if len(data3[1])>0:
        for i in range(len(data3[1])):
            if data3[1][i] != "":
                if data3[3][i] == 1: slovar.update({k: [data3[1][i], unix_to_date(data3[2][i]), 'checked']})
                else: slovar.update({k: [data3[1][i], unix_to_date(data3[2][i]), 'nonchecked']})
        k+=1
    return data, data2, data3, slovar, login_teacher, role

def teacher_data():
    data = contract_teacher.functions.checkTeacher(session['addr']).call({'from': session['addr']})
    session['fio'], session['lab_name'], session['SchoolSubject'] = data[1], laboratories2[data[3][0]], *data[2]
    numActiveProjects = data[5]
    projects_name= []
    for i in numActiveProjects:
        k = contract_teacher.functions.checkProject(i).call({'from': session['addr']})
        if k[1]==session['login']:
            projects_name.append(k[0])
    print(data, '************************', projects_name,sep='\n')
    return data, projects_name
   



# #************************************Начало*********************************
@app.route('/')
def index():
    try:
        if session.get('addr', ''):
            return redirect(url_for('go_to_auth'))
        else:
            return render_template('first_walet.html')
    except: pass
    return render_template('first_walet.html')

# #************************************Авторизация кошелька*********************************
@app.post('/walet')
def walet():
    address = request.form['walet']
    password = request.form['password']
    try:
        w3.geth.personal.unlock_account(address, password, 1000000)
        session.update({'addr': address, 'password_addr': password})
        return redirect(url_for('go_to_auth'))
    except InvalidAddress  as e:
        flash(f'Кошелек не найден', category='status_class_wrong')
        return render_template('first_walet.html')
    except BaseException as e:
        flash(f'Кошелек не найден', category='status_class_wrong')
        return render_template('first_walet.html')


#************************************Авторизация аккаунта*********************************

@app.get('/go_to_auth/')
def go_to_auth():
    session.update({'url': request.url})
    try:
        if session.get('corectly_login', ''):
            number = contract_makestruct0.functions.getStatusAddress(session['addr']).call({'from': session['addr']})
            print(number)
            if int(number) == 5:
                return redirect(url_for('go_to_teacher_cabinet'))
            elif int(number) == 6:
                return redirect(url_for('go_to_student_cabinet'))
            else: 
                flash(f'НЕИЗВЕСТНЫЙ ПОЛЬЗОВАТЕЛЬ', category='status_class_wrong')
                return render_template('auth.html', addr=session.get('addr', ""))
        return render_template('auth.html', addr=session.get('addr', ""))
    except BaseException as e:
        flash(f'{e}', category='status_class_wrong')
        return render_template('auth.html', addr=session.get('addr', ""))

@app.post('/auth')
def auth(message=''):
    password = request.form['password']
    login = request.form['login']
    try:
        block = w3.eth.block_number
        tx_res = w3.eth.waitForTransactionReceipt(contract_teacher.functions.auth(login, password, session['addr']).transact({'from': session['addr']}))
        ev = contract_teacher.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries():
            print('11111111111111111111111111111111111111111')
            message = ev.get_all_entries()[0]['args']['text']
            flash(f'{message}', category='status_class_wrong')
            return redirect(url_for('go_to_auth'))
        print('2222222222222222222222222')
        number = contract_makestruct0.functions.getStatusAddress(session['addr']).call({'from': session['addr']})
        if int(number) == 5:
            session.update({'login': login, 'password_acc': password})
            session.update({'corectly_login': session['login'], 'corectly_pass': session['password_acc']})
            return redirect(url_for('go_to_teacher_cabinet'))
        elif int(number) == 6:
            session.update({'login': login, 'password_acc': password})
            session.update({'corectly_login': session['login'], 'corectly_pass': session['password_acc']})
            return redirect(url_for('go_to_student_cabinet'))
        else: 
            flash(f'Ошибка?', category='status_class_wrong')
            return redirect(url_for('go_to_auth'))
    except BaseException as e:
        flash(f'{e}', category='status_class_wrong')
        return redirect(url_for('go_to_auth'))
    
# #************************************Перессылка на егистрация аккаунта Пользавателя*********************************
@app.post('/reg')
def reg(message=''):
    session.update({'url': request.url})
    number = contract_makestruct0.functions.getStatusAddress(session['addr']).call({'from': session['addr']})
    print(number)
    if int(number) == 2:
        session.update({'status': 'teacher'})
        return render_template("reg_teacher.html", listt=laboratories2, subject=schoolSubjects)
    elif int(number) == 3:
        session.update({'status':'student'})
        return render_template('reg_student.html', message=message)
    elif int(number) == 0:
        return render_template('auth.html', addr=session.get('addr', ""), message='Этого кошеля нет в системе', mes_type="status_class_wrong")
    else:
        return render_template('auth.html', addr=session.get('addr', ""), message='Вы уже зарегистрированны', mes_type="status_class_good")
     
# #************************************Регистрация аккаунта ученика*********************************


@app.get('/go_to_student_cabinet')
@user_is_auth
def go_to_student_cabinet(message='',  mes_type=""):
    session.update({'url': 'http://127.0.0.1:5000/go_to_auth'})
    data, data2, slovar = student_data()
    return render_template('student_cabinet.html', message=message, mes_type=mes_type, login=data[0], name=data[1], classnum=data[-3], classletter=data[2], Project_name=data2[0], check_strong_side=len(data[3])<6 and len(data[3])>0, strong_side=slovar, Laboratorie=laboratories2[data2[6]], new_proj_avalible=data2[0]=='')


@app.post('/go_to_reg_student')
def go_to_reg_student(message='',):
    session.update({'url': request.url})
    return render_template('reg_student.html', message=message)


@app.post('/reg_student')
def reg_student():
    try:
        rep_password = request.form['rep_password']
        email = str(request.form['email'])
        password = request.form['password']
        fio = request.form['fio']
        clas = request.form['class']
        classletter = request.form['classletter']
        if clas and 1<=int(clas)<=11 and password == rep_password and check_password(password) and check_name(fio) and check_emaill(email) and len(classletter)==1 and classletter in rus_letters and classletter.isupper():
            session.update({'password_acc': password, 'login': email, 'fio':fio, 'clas':int(clas), 'classletter':classletter })
            rand_string = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
            session['rand-string'] = rand_string
            send_email(email, text=rand_string)
            return render_template('check_email.html')
        else:
            return render_template('reg_student.html', message='Неверные данные', mes_type="status_class_wrong")
    except BaseException as e:
        print('###########################', e, '#######################', sep='\n')
        return render_template('reg_student.html', message=f'Ошибка: {e}', mes_type="status_class_wrong")


# #************************************Создание и изменение сильной стороны ученика********************************
@user_is_auth
@app.post('/go_to_create_strong_side')
def go_to_create_strong_side(message=""):
    data = contract_student0.functions.checkStudent(session['addr']).call({'from': session['addr']})
    strong_side = data[3]
    if len(strong_side)<=7: len_tasks = 0
    else: len_tasks = 10
    slovar = {}
    k=0
    for i in data[3]:
        slovar.update({k: i})
        k+=1
    return render_template('change_strong_side.html', strong_side=strong_side, str_sd_len=(len(strong_side)<5), len_tasks=len_tasks, message=message, slovar=slovar)

@user_is_auth
@app.post('/create_strong_side')
def create_strong_side(message=''):
    try:
        strong_side = request.form['strong_side']
        tx_res = w3.eth.waitForTransactionReceipt(contract_student0.functions.addStrongSide(session['login'], session['password_acc'], strong_side).transact({'from': session['addr']}))
        block = w3.eth.block_number
        ev = contract_student0.events.Action.createFilter(fromBlock=block,toBlock="latest")
        strong_side, slovar, len_tasks = student_sides()
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Add strong side':
            return render_template('change_strong_side.html', strong_side=strong_side, str_sd_len=(len(strong_side)<10), len_tasks=len_tasks, message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong", slovar=slovar)
        return render_template('change_strong_side.html', strong_side=strong_side, str_sd_len=(len(strong_side)<10), len_tasks=len_tasks, message='Сторона добавлена', mes_type="status_class_good", slovar=slovar)
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return render_template('change_strong_side.html', strong_side=strong_side, str_sd_len=(len(strong_side)<10), len_tasks=len_tasks, message=f'Ошибка: {e}', mes_type="status_class_wrong", slovar=slovar)

@user_is_auth
@app.post('/change_strong_side')
def change_strong_side(message=''):
    try:
        
        new_side = request.form['side']
        indexx = request.form['indexx']
        tx_res = w3.eth.waitForTransactionReceipt(contract_student0.functions.changeStrongSide(session['login'], session['password_acc'], new_side, int(indexx)).transact({'from': session['addr']}))
        block = w3.eth.block_number
        ev = contract_student1.events.Action.createFilter(fromBlock=block,toBlock="latest")
        strong_side, slovar, len_tasks = student_sides()
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Change strong side':
            
            return render_template('change_strong_side.html', strong_side=strong_side, str_sd_len=(len(strong_side)<10), len_tasks=len_tasks, message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong", slovar=slovar)
        return render_template('change_strong_side.html', strong_side=strong_side, str_sd_len=(len(strong_side)<10), len_tasks=len_tasks, message='Сторона изменена', mes_type="status_class_good", slovar=slovar)
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return render_template('change_strong_side.html', strong_side=strong_side, str_sd_len=(len(strong_side)<10), len_tasks=len_tasks, message=f'Ошибка: {e}', mes_type="status_class_wrong", slovar=slovar)


# #************************************Создание проекта ученика********************************
@user_is_auth
@app.route('/go_to_create_projects')
def go_to_create_projects(message=''):
    return render_template('create_project_for_student.html', dict_lab=laboratories2, dict_sub=schoolSubjects, message=message)

@user_is_auth
@app.post('/create_project')
def create_project(message=''):
    try:
        name_project = request.form['name_project']
        login_teacher = request.form['login']
        interest = [int(i) for i in request.form.getlist('interest')]
        laboratorie = request.form['lab']
        tx_hash = contract_student1.functions.createProject(session['login'], session['password_acc'], name_project, login_teacher, int(laboratorie), interest).transact({'from': session['addr']})
        tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
        block = w3.eth.block_number
        ev = contract_student1.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Project create':
            print(ev.get_all_entries()[0]['args']['text'])
            return render_template('create_project_for_student.html', dict_lab=laboratories2, dict_sub=schoolSubjects, message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong")
        return redirect(url_for('go_to_student_cabinet', message='Проект успешно создан')) 
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        # flash('Сообщение для пользователя')
        return render_template('create_project_for_student.html', dict_lab=laboratories2, dict_sub=schoolSubjects, message=e, mes_type="status_class_wrong")


# #************************************Функции по проекту ученика********************************
@user_is_auth
@app.route('/go_to_change_student_projects')
def go_to_change_student_projects(message=''):
    data, data2, data3, slovar, login_teacher, role = student_project()
    try:
        return render_template('proj_student.html', message=message, role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
    except BaseException as e:
        print('###########################', e, '#######################', sep='\n')
        return render_template('student_cabinet.html', message=e, mes_type="status_class_wrong", login=data[0], name=data[1], classnum=data[-3], classletter=data[2], Project_name=data2[0], check_strong_side=len(data[3])<6 and len(data[3])>0, strong_side=slovar, Laboratorie=laboratories[data2[6]], new_proj_avalible=data2[0]=='')

@user_is_auth
@app.post('/change_goal_project')
def change_goal_project(message=''):
    try:
        data, data2, data3, slovar, login_teacher, role = student_project()
        goal = request.form['goal']
        tx_res = w3.eth.waitForTransactionReceipt(contract_student1.functions.changeGoalProject(session['login'], session['password_acc'], goal).transact({'from': session['addr']}))
        block = w3.eth.block_number
        ev = contract_student1.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Change goal':
            return render_template('proj_student.html', message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
        return render_template('proj_student.html', message="Цель изменена", mes_type="status_class_good", role=data3[0], slovar=slovar, Goal=data2[1], login=data[0], tutor=data2[3], project_name=data2[0], laboratorie=laboratories2[data2[6]])
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        data, data2, data3, slovar, login_teacher, role = student_project()
        return render_template('proj_student.html', message=e, mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])

#role не изменятеся в контракте
@user_is_auth
@app.post('/create_role')
def create_role(message=''):
    role = request.form['role']
    data, data2, data3, slovar, login_teacher, role = student_project()
    try:
        tx_res = w3.eth.waitForTransactionReceipt(contract_student1.functions.changeRole(session['login'], session['password_acc'], role).transact({'from': session['addr']}))
        block = w3.eth.block_number
        ev = contract_student1.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Successfully change role':
            print(ev.get_all_entries()[0]['args']['text'])
            return render_template('proj_student.html', message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
        return render_template('proj_student.html', message="Роль успешно создана", mes_type="status_class_good", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return render_template('proj_student.html', message=e, mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])

#не работает
@user_is_auth
@app.post('/create_task')
def create_task(message=''):
    data, data2, data3, slovar, login_teacher, role = student_project()
    try:
        task = request.form['task']
        data = request.form['date'].replace('.', '-')
        tx_res = w3.eth.waitForTransactionReceipt(contract_student1.functions.addTask(session['login'], session['password_acc'], task, date_to_unix(data)).transact({'from': session['addr']}))
        block = w3.eth.block_number
        ev = contract_student1.events.Action.createFilter(fromBlock=block, toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Add task':
            print(ev.get_all_entries()[0]['args']['text'])
            return render_template('proj_student.html', message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
        return render_template('proj_student.html', message="Задание добавлено", mes_type="status_class_good", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return render_template('proj_student.html', message=e, mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])



#не работает
@user_is_auth
@app.post('/changeTaskInProject')
def changeTaskInProject(message=''):
    data, data2, data3, slovar, login_teacher, role = student_project()
    try:
        tasks = contract_student1.functions.checkProject(session['addr']).call({'from': session['addr']})[5]
        indexxx = request.form['indexxx']
        task = request.form['task']
        block = w3.eth.block_number
        tx_res = w3.eth.waitForTransactionReceipt(contract_student1.functions.changeTaskInProject(session['login'], session['password_acc'], int(indexxx), task, date_to_unix('2023-12-31')).transact({'from': session['addr']}))
        ev = contract_student1.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Successfully change text task':
            print(ev.get_all_entries()[0]['args']['text'])
            return render_template('proj_student.html', message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
        return render_template('proj_student.html', message="Задание изменено", mes_type="status_class_good", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return render_template('proj_student.html', message=e, mes_type="status_class_wrong", role=role, slovar=slovar, Goal=data2[1], login=data[0], tutor=login_teacher, project_name=data2[0], laboratorie=laboratories2[data2[6]])

# #************************************Проверка почты пользавателя*********************************

@app.post('/check_email')
def check_email():
    try:
        check = request.form['check']
        if check == session['rand-string']:
            if session['status']=='teacher':
                print('gmjjjjjjjjjjjjjjjjjjjjjjjjfldvlmdlv')
                print(session['login'], session['password_acc'], session['addr'], session['fio'], session['SchoolSubject'], session['laboratorie'])
                block = w3.eth.block_number
                tx_hash = contract_teacher.functions.registration(session['login'], session['password_acc'], session['fio'], [session['SchoolSubject']],  [session["laboratorie"]]).transact({'from': session['addr']})
                tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
                ev = contract_teacher.events.Action.createFilter(fromBlock=block, toBlock="latest")
                if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Teacher successfully registered':
                    print(ev.get_all_entries()[0]['args']['text'])
                    return render_template("reg_teacher.html", listt=laboratories, subject=schoolSubjects, message=ev.get_all_entries()[0]['args']['text'])
                session['student_addrs'] = []
                session.update({'corectly_login': session['login'], 'corectly_pass': session['password_acc']})
                return redirect(url_for('go_to_teacher_cabinet'))
            if session['status']=='student':
                print(session['login'], session['password_acc'], session['addr'], session['fio'])
                block = w3.eth.block_number
                tx_hash = contract_student0.functions.registration(session['login'], session['fio'], session['classletter'], session['password_acc'],  int(session['clas'])).transact({'from': session['addr']})
                tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
                ev = contract_student0.events.Action.createFilter(fromBlock=block,toBlock="latest")
                if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Student successfully registered':
                    print(ev.get_all_entries()[0]['args']['text'])
                    return render_template('reg_student.html', message=ev.get_all_entries()[0]['args']['text'], mes_type="status_class_wrong")
                session.update({'corectly_login': session['login'], 'corectly_pass':session['password_acc']})
                return redirect(url_for('go_to_student_cabinet'))
            return 'fgppmxghm[;fmlxmlm,b;cbx]'
        else:
            flash('Неверный коддддд', category='status_class_wrong')
            return render_template('check_email.html')
    except BaseException as e:
        print('###########################', e, '#######################', sep='\n')
        flash(f'{e}', category='status_class_wrong')
        return render_template('check_email.html')



# #************************************Регистрация аккаунта учителя*********************************

@user_is_auth
@app.get('/go_to_teacher_cabinet')
def go_to_teacher_cabinet(message=''):
    session.update({'url': request.url})
    data,  projects = teacher_data()
    return render_template('teacher_cabinet.html', message=message, projects=projects, login=data[0], fio=session['fio'], lab=session['lab_name'], sub=schoolSubjects[session['SchoolSubject']])

@app.post('/reg_teacher_check')
def reg_teacher_check():
    email = request.form['email']
    rep_password = request.form['rep_password']
    password = request.form['password']
    fio = request.form['fio']
    SchoolSubject = int(request.form['SchoolSubjects'])
    laboratorie = int(request.form['laboratories'])
    if password == rep_password and check_password(password) and check_emaill(login) and check_name(fio) and bool(SchoolSubject) and bool(laboratorie):
        rand_string = ''.join(random.choice(letters_and_numbers) for i in range(3))+''.join(random.choice(letters_and_numbers) for i in range(3))+''.join(random.choice(letters_and_numbers) for i in range(3))
        print(rand_string)
        session['rand-string'] = rand_string
        send_email(email, text=rand_string)
        session.update({'login': email, 'password_acc':password, 'fio':fio, 'SchoolSubject': SchoolSubject, 'laboratorie': laboratorie})
        print(session['login'], session['password_acc'], session['fio'], session['SchoolSubject'],  session["laboratorie"])
        return render_template('check_email.html')
    else:
        return render_template("reg_teacher.html", listt=laboratories, subject=schoolSubjects, message='Неверно ведены данные')


#**************************************************ФУНКЦИИ УЧИТЕЛЯ********************************
@user_is_auth
@app.post('/go_to_create_projects_teacher')
def go_to_create_projects_teacher(message=''):
    return render_template('create_project_for_teacher.html')
    

@user_is_auth
@app.post('/create_project_teacher')
def create_project_teacher(message=''):
    try:
        name_prject = request.form['name_project']
        block = w3.eth.block_number
        tx_res = w3.eth.waitForTransactionReceipt(contract_teacher.functions.createProject(session['login'], session['password_acc'], name_prject,session["laboratorie"]).transact({'from': session['addr']}))
        ev = contract_teacher.events.Action.createFilter(fromBlock=block, toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Create project':
            message = ev.get_all_entries()[0]['args']['text']
            flash(f'{message}', category='status_class_wrong')
            return redirect(url_for('go_to_create_projects_teacher'))
        flash(f'Проект создан', category='status_class_good')
        return redirect(url_for('go_to_teacher_cabinet'))
    except BaseException as e:
        flash(f'{e}', category='status_class_wrong')
        return redirect(url_for('go_to_create_projects_teacher'))

@user_is_auth
@app.post('/go_to_create_acc_for_student')
def go_to_create_acc_for_student(message=''):
    return render_template('create_acc_for_student.html', message=message)

@user_is_auth
@app.post('/create_acc_for_student')
def create_acc_for_student(message=''):
    try:
        pass_walet = request.form['pass_walet']
        new_acc = w3.geth.personal.new_account(pass_walet)
        print(new_acc)
        block = w3.eth.block_number
        tx_hash = contract_teacher.functions.generateAddressForStudent(session['login'], session['password_acc'], new_acc, pass_walet).transact({'from': session['addr']})
        tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
        ev = contract_teacher.events.Action.createFilter(fromBlock=block, toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Address generated':
            print(ev.get_all_entries()[0]['args']['text'])
            return redirect(url_for('go_to_create_acc_for_student', message='Ошибка'))
        contract_teacher.functions.myTransfer(new_acc).transact({'from': '0xff42Fc7fdB5928b63da0bF2340880369fE335bf0', 'value': '1000000000000000'})
        session.update({'student_addrs': session['student_addrs'].append(str(new_acc))})
        return redirect(url_for('go_to_teacher_cabinet', message='Успех'))
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return redirect(url_for('go_to_teacher_cabinet', message='Ошибка'))

@user_is_auth
@app.post('/addStudentInProject')
def addStudentInProject(message=''):
    try:
        login = request.form['login']
        block = w3.eth.block_number
        tx_hash = contract_teacher.functions.addStudentInProject(session['login'], session['password_acc'], session['index_project'], login).transact({'from': session['addr']})
        tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
        ev = contract_teacher.events.Action.createFilter(fromBlock=block, toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Already in the project':
            print(ev.get_all_entries()[0]['args']['text'])
            return redirect(url_for('go_to_change_teacher_project', message='Ошибка'))
        return redirect(url_for('go_to_change_teacher_project', message='Успех'))
    except BaseException as e:
        print('Ошибка:', e)
        return redirect(url_for('go_to_change_teacher_project', message='Ошибка'))

@user_is_auth
@app.post('/go_to_look_teacher_project')
def go_to_look_teacher_project(message=''):
    p = contract_teacher.functions.checkNumAllActiveProject().call({'from': session['addr']})
    projects_number = p
    projects_name= {}
    for i in projects_number:
        k=contract_teacher.functions.checkProject(i).call({'from': session['addr']})
        if k[2]==session['login']:
            projects_name.update({i : k[0]})
    return render_template('proj_all_tutor.html', project_list=projects_name)

@user_is_auth
@app.post('/go_to_change_teacher_project')
def go_to_change_teacher_project(message=''):
    indexxx = int(request.form['indexxx'])
    session['index_project'] = int(indexxx)
    project = contract_teacher.functions.checkProject(indexxx).call({'from': session['addr']})
    deadlines = contract_teacher.functions.checkTaskDeadline(session['index_project']).call({'from': session['addr']})
    strudent_addr = project[5]
    student_name = []
    for i in strudent_addr:
        data = contract_student0.functions.checkStudent(i).call({'from': session['addr']})[0]
        if data != '': student_name.append(data)
    tasks = {}
    for j in range(len(deadlines[0])):
        if deadlines[0][j] !='':
            tasks[j] = [deadlines[0][j], unix_to_date(int(str(deadlines[1][j]).replace('.', '-'))), deadlines[2][j]]
    return render_template('proj_tutor.html', task=tasks, students = student_name, project_name=project[0], tutor=session['fio'], laboratorie=session['lab_name'])

@user_is_auth
@app.post('/AddTaskInProjectTeacher')
def AddTaskInProjectTeacher(message=''):
    try:
        tasks = contract_teacher.functions.checkProject(session['index_project']).call({'from': session['addr']})[4]
        task = request.form['task']
        date = request.form['date'].replace('.', '-')
        tx_hash = contract_teacher.functions.changeTaskInProjectTeacher(session['login'], session['password_acc'], session['index_project'], task,  date_to_unix(date), tasks.index(''), 0).transact({'from': session['addr']})
        tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
        block = w3.eth.block_number
        ev = contract_teacher.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Task change':
            print(ev.get_all_entries()[0]['args']['text'])
            return redirect(url_for('go_to_change_teacher_project', message=ev.get_all_entries()[0]['args']['text']))
        return redirect(url_for('go_to_change_teacher_project', message='Задание Добавлено'))
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return redirect(url_for('go_to_change_teacher_project', message='Ошибка'))

@user_is_auth
@app.post('/changeTaskInProjectTeacher')
def changeTaskInProjectTeacher(message=''):
    # try:
        tasks = contract_teacher.functions.checkProject(session['index_project']).call({'from': session['addr']})[4]
        indexxx = request.form['indexxx']
        task = request.form['task']
        date = request.form['date'].replace('.', '-')
        complete = 1 if request.form['complete']=='on' else 0
        TypeError('gdmfgndpgpodfngsg')
        tx_hash = contract_teacher.functions.changeTaskInProjectTeacher(session['login'], session['password_acc'], session['index_project'],  tasks.index(''), task, date_to_unix(date), tasks.index(''), 0).transact({'from': session['addr']})
        tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
        block = w3.eth.block_number
        ev = contract_teacher.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Task change':
            print(ev.get_all_entries()[0]['args']['text'])
            return redirect(url_for('go_to_change_teacher_project', message=ev.get_all_entries()[0]['args']['text']))
        return redirect(url_for('go_to_change_teacher_project', message='Задание Добавлено'))
    # except BaseException as e:
    #     print('ОШИИИИИИБКААААААААА:', e)
    #     return redirect(url_for('go_to_change_teacher_project', message='Ошибка'))

@user_is_auth
@app.post('/change_goal_project_tutor')
def change_goal_project_tutor(message=''):
    try:
        goal = request.form['goal']
        tx_hash = contract_student1.functions.changeGoalProject(session['login'], session['password_acc'], goal).transact({'from': session['addr']})
        tx_res = w3.eth.waitForTransactionReceipt(tx_hash)
        block = w3.eth.block_number
        ev = contract_student1.events.Action.createFilter(fromBlock=block,toBlock="latest")
        if ev.get_all_entries() and ev.get_all_entries()[0]['args']['text'] != 'Change goal':
            print(ev.get_all_entries()[0]['args']['text'])
            return redirect(url_for('go_to_change_teacher_project', message=ev.get_all_entries()[0]['args']['text']))
        return redirect(url_for('go_to_change_teacher_project', message='Цель успешно заменена'))
    except BaseException as e:
        print('ОШИИИИИИБКААААААААА:', e)
        return e
#****************************************Запуск********************************************

if __name__ == '__main__':
    from secret_key import key
    app.config.SECRET_KEY = key
    app.config['FLASH_MESSAGES_KEY'] = 'myflashkey'

    # from watchminer import WatchMiner
    # WatchMiner().start() 
    
    app.run(debug = True)















