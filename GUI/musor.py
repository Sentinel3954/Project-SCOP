# @app.post('/reg_teacher_check')
# def reg_teacher_check():
#     data = json.loads(request.data)
#     print(data)
#     email = data['email']
#     password = data['password']
#     FIO = data['FIO']
#     SchoolSubject = schoolSubjects.index(data['SchoolSubjects'])
#     laboratorie = laboratories.index(data['laboratories'])
#     if '@' in email and password != '' and FIO != '' and SchoolSubject != '' and laboratorie != '':
#         contract.functions.registrationForTeacher(email, password, FIO, [SchoolSubject], [laboratorie], email, session['addr']).transact({'from': session['addr']})
#         time.sleep(6)
#         block = w3.eth.block_number
#         ev = contract.events.Result.createFilter(fromBlock=block, toBlock="latest")
#         if ev.get_all_entries()[0]['args']['text'] != 'Teacher successfully registered':
#             print(ev.get_all_entries())
#             print(ev.get_all_entries()[0]['args']['text'])
#             return render_template("reg_teacher.html", listt=laboratories, subject=schoolSubjects, message=ev.get_all_entries()[0]['args']['text'])
#         # try:
#         #     if ev.get_all_entries()[0]['args']['text'] != 'Teacher successfully registered':
#         #         print(ev.get_all_entries())
#         #         print(ev.get_all_entries()[0]['args']['text'])
#         #         return {'error': ev.get_all_entries()[0]['args']['text']}
#         # except:
#         #     return {'error':"Заполнены не все поля"}
#         return {'status': 'ok'}
#     else:
#         return render_template("reg_teacher.html", listt=laboratories, subject=schoolSubjects, message='Неверно ведены данные')

# @app.route('/go_to_reg_check_email', methods=['POST'])
# def go_to_reg_check_email(email, password, FIO, subjects, labs, log, addr):
#     # email = request.form['email']
#     send_email(email, text=rand_string)
#     return render_template('check_email.html', email=email, password=password, FIO=FIO, subjects=subjects, labs=labs, log=log, addr=addr)   
