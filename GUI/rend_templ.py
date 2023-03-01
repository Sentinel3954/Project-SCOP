from web3 import Web3, middleware, parity, exceptions
from flask import Flask, render_template, request, redirect, url_for, session
from secret_key import key
from web3.middleware import geth_poa_middleware

app = Flask(__name__)
app.secret_key = key

@app.route('/')
@app.route('/<message>')
def index(message=''):
    # status_class_wrong
    # status_class_good
    # status_class_neyt
    message = "Wrong address"
    # return render_template('first_walet.html', message=message, mes_type="status_class_wrong")
    # message = "Wrong address"
    return render_template('first_walet.html', message=message, mes_type="status_class_wrong")

# #************************************Авторизация кошелька*********************************
@app.post('/walet')
def walet():
    return render_template('auth.html', message='fmnksnfiks')


#************************************Авторизация аккаунта*********************************

@app.get('/go_to_auth/')
def go_to_auth(message=''):
    mes_type="status_class_wrong"
    message = "aaaaaa"
    return render_template('auth.html', addr=session.get('addr', ""), 
        message=message, mes_type=mes_type)

@app.get('/check_email')
def check_email():
    message ="Wrong code"
    return render_template('check_email.html',message=message, mes_type="status_class_wrong")

@app.get('/reg_teacher_check')
def reg_teacher_check():
    laboratories = {1:"ЛабФизики",2:"ЛабМатем",3:"ЛабИнфо"}
    schoolSubjects = {1:"Математика",2:"Русский",3:"Информатика"}
    return render_template("reg_teacher.html", listt=laboratories, subject=schoolSubjects, message='Aaaaaa',  mes_type="status_class_wrong")


@app.get('/go_to_teacher_cabinet')
def go_to_teacher_cabinet(message=''):
    name, lab, sub, projects = "Иванов И.И.", "Тест_лаб", "Предмет", ["Проект1","Проект2","Проект3",]
    return render_template('teacher_cabinet.html', message=message, name=name, lab=lab, sub=sub, projects=projects)


#************************************Регистрация аккаунта ученика*********************************
@app.get('/go_to_student_cabinet')
def go_to_student_cabinet():
    name, classnum = "Петров П.П.", "10"
    project_name = "Проект1"
    strong_side = {1:"сила1", 2:"сила2", 3:"сила3"}
    lab = "Тест_лаб"
    return render_template('student_cabinet.html', name=name, classnum=classnum, Project_name=project_name, 
    check_strong_side=True, login="123@yandex.ru",
    strong_side=strong_side, Laboratorie=lab, classletter="A", new_proj_avalible=True)


@app.get('/go_to_reg_student')
def go_to_reg_student(message=''):
    message ="Wrong code"
    return render_template('reg_student.html', message=message, mes_type="status_class_wrong")

@app.get('/reg_student')
def reg_student():
        return redirect(url_for('go_to_student_cabinet'))



#************************************Функция ученика********************************
@app.get('/go_to_create_projects')
def go_to_create_projects(message=''):
    laboratories = "Тест_лаб"
    message = "FFFFFuuuu"
    return render_template('create_project.html', listt=laboratories, message=message, 
        mes_type="status_class_wrong")

@app.get("/auth/")
def auth():
    pass

@app.get("/reg/")
def reg():
    pass

@app.get("/create_strong_side/")
def create_strong_side():
    strong_side = {1:"сила1", 2:"сила2", 3:"сила3"}
    if len(strong_side)<=7: len_tasks = 0
    else: len_tasks = 10
    message = "fffuuuu"
    return render_template('change_strong_side.html', slovar=strong_side, 
        str_sd_len=(len(strong_side)<3), len_tasks=len_tasks)

@app.get("/create_project_tut/")
def create_project():
    message = "Fuuuu"
    laboratories = {1:"ЛабФизики",2:"ЛабМатем",3:"ЛабИнфо"}
    login = "123@yandex.ru"
    return render_template('create_project_tut.html', listt=laboratories, 
        login=login, message=message, mes_type="status_class_wrong")
    

@app.get("/proj_student/")
def proj_student():
    project_name = "Проект1"
    goal_project = "Пролетарии всех стран объединяйтесь!"
    lab = "Тест_лаб"
    colaborants = ", ".join(["Petrov", "Ivanov", "Sidorov"])
    tutor = "Vasiliev"
    tasks = [[1,"Задача 1","2022-12-31","nochecked"], [2,"Задача 2","2022-12-31","nochecked"],
            [3,"Задача 3","2022-12-31","checked"],[4,"Задача 4","2022-12-31","checked"],
            [5,"Задача 4","2022-12-31","nochecked"],[6,"Задача 4","2022-12-31","nochecked"],
            [7,"Задача 4","2022-12-31","nochecked"],[8,"Задача 4","2022-12-31","nochecked"],
            [9,"Задача 4","2022-12-31","checked"],[10,"Задача 4","2022-12-31","nochecked"]]
    # tasks = [[1,"Задача 1","2022-12-31","nochecked"], [2,"Задача 2","2022-12-31","nochecked"],
    #         [3,"Задача 3","2022-12-31","checked"],[4,"Задача 4","2022-12-31","checked"]]
    if len(tasks)<5: len_tasks = 0
    else: len_tasks = 10
    roles = {"Petrov":", ".join(["Молодец", "Трудяга"]), "Ivanov":", ".join(["Лентяй"]), 
        "Sidorov":", ".join(["Лодырь"])}
    message = "Ffuuuuu"
    slovar = {}
    data = ["asdasd", "asdasd","asdasd","asdasd","asdasd"]
    datee= ["2023-07-22", "2023-12-31","2023-11-22","2023-11-30","2023-07-22"]
    ready = ["checked", "nochecked","nochecked","nochecked","nochecked"]
    for i in range(len(data)):
        slovar.update({i: [data[i], datee[i], ready[i]]})
    return render_template('proj_student.html',project_name=project_name, 
     laboratorie=lab, new_proj_avalible=True, tasks=tasks, goal_project=goal_project,
     colaborants=colaborants, tutor=tutor, roles=roles, len_tasks = len_tasks,
     message=message, slovar= slovar,
     mes_type="status_class_wrong")

@app.post("/go_to_change_projects/")
def go_to_change_projects():
    pass

# change_goal_project
@app.post("/change_goal_project/")
def change_goal_project():
    pass


@app.post("/change_strong_side/")
def change_strong_side():
    pass


@app.post("/go_to_create_strong_side/")
def go_to_create_strong_side():
    pass

@app.get("/proj_tutor/")
def proj_tutor():
    project_name = "Проект1"
    goal_project = "Пролетарии всех стран объединяйтесь!"
    lab = "Тест_лаб"
    colaborants = ", ".join(["Petrov", "Ivanov", "Sidorov"])
    tutor = "Vasiliev"
    tasks = [[1,"Задача 1","2022-12-31","nochecked"], [2,"Задача 2","2022-12-31","nochecked"],
            [3,"Задача 3","2022-12-31","checked"],[4,"Задача 4","2022-12-31","checked"],
            [5,"Задача 4","2022-12-31","nochecked"],[6,"Задача 4","2022-12-31","nochecked"],
            [7,"Задача 4","2022-12-31","nochecked"],[8,"Задача 4","2022-12-31","nochecked"],
            [9,"Задача 4","2022-12-31","checked"],[10,"Задача 4","2022-12-31","nochecked"]]
    # tasks = ["Задача 1", "Задача 2","Задача 3"]
    # tasks = ["Задача 1", "Задача 2","Задача 3","Задача 4","Задача 5",
    #         "Задача 6","Задача 7","Задача 3","Задача 4","Задача 5"]
    # if len(tasks)<5: len_tasks = 0
    # else: 
    len_tasks = 5
    roles = {"Petrov":", ".join(["Молодец", "Трудяга"]), "Ivanov":", ".join(["Лентяй"]), 
        "Sidorov":", ".join(["Лодырь"])}
    message = "fffffu"
    return render_template('proj_tutor.html',project_name=project_name, 
     laboratorie=lab, new_proj_avalible=True, tasks=tasks, goal_project=goal_project,
     colaborants=colaborants, tutor=tutor, roles=roles, len_tasks = len_tasks,message=message, 
     mes_type="status_class_wrong")


@app.get("/proj_all_tutor/")
def proj_all_tutor():
    project_list = [[1, "Проект1"],
                    [2, "Проект2"],
                    [3, "Проект3"]
                    ]
    tutor = "Vasiliev"
    return render_template('proj_all_tutor.html',project_list=project_list)

@app.get("/create_login_student/")
def create_login_student():
    message = "Ffffuuuuu"
    mes_type = "status_class_wrong"

    message = "0x000123103010230102301203123"
    mes_type="status_class_good"
    return render_template("create_login_student.html", message=message, 
     mes_type=mes_type)

@app.get("/create_role/")
def create_role():
    pass

@app.get("/changegoalproject/")
def changegoalproject():
    pass

@app.get("/create_task/")
def create_task():
    pass

@app.get("/changeTaskInProject/")
def changeTaskInProject():
    pass

@app.get("/back/")
def back():
    pass

@app.get("/go_to_look_teacher_project/")
def go_to_look_teacher_project():
    pass

@app.get("/go_to_create_projects_teacher/")
def go_to_create_projects_teacher():
    pass

@app.get("/go_to_create_acc_for_student/")
def go_to_create_acc_for_student():
    pass


if __name__ == '__main__':
    from secret_key import key
    app.config.SECRET_KEY = key
    app.run(debug = True)
