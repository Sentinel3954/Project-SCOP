# #16 строка:
# def read_address(name_file):
#     path = "/home/student/Загрузки/MegaProject-main/Contract/abi_address/"                                      #нужно сделать через абсолютный путь
#     with open (path + name_file) as fp:
#         address = json.load(fp)
#     return address

# def read_abi(name_file):
#     path = "/home/student/Загрузки/MegaProject-main/Contract/abi_address/"
#     with open (path + name_file) as fp:
#         abi = json.load(fp)
#     return abi

# #32 строка:
# contract_makestruct = w3.eth.contract(address=read_address("MakeStruct0_address"), abi=read_abi("MakeStruct0_abi"))
# contract_student = w3.eth.contract(address=read_address("Student_address"), abi=read_abi("Student_abi"))
# contract_teacher = w3.eth.contract(address=read_address("Teacher_address"), abi=read_abi("Teacher_abi"))

# #158 строка:
# try:

# #171 строка:
# except:
#     return redirect(url_for('go_to_auth'))

# #397 строка
# try:

# #412 строка
# except:
#     return redirect(url_for('go_to_auth'))

# #431 строка
# return render_template("reg_teacher.html", listt=laboratories, subject=schoolSubjects, message='Неверно введены данные')