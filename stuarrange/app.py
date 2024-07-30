from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

res='HELLO'

app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key='114514'

@app.route('/')
def slct():
    print("enter")
    return render_template('select.html')

@app.route("/stu_index",methods=['GET','POST'])
def stuidx():
    return render_template('stu_index.html')

@app.route("/stu_register",methods=['GET','POST'])
def stu_register():
    user=request.form.get('id1')
    pwd1=request.form.get('pwd1')
    pwd2=request.form.get('pwd2')
    print(user)
    print(pwd1)
    print(pwd2)
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8',autocommit=True)
    cursor = conn.cursor()
    if user and pwd1 and pwd2:
        if pwd1==pwd2:
            print("相等")
            sql = "SELECT ID FROM STUUSER WHERE ID = '" + user + "'"
            print(sql)
            cursor.execute(sql)
            check = cursor.fetchall()
            #checkpwd = check[0][0]
            print(check)
            if len(check)==0:
                print("进入")
                sql1 = "INSERT INTO STUUSER VALUES('%s','%s')"%(user,pwd1)
                print(sql1)
                cursor.execute(sql1)
                return render_template('stu_register.html')
    return redirect('/stu_index')

@app.route("/adm_register",methods=['GET','POST'])
def adm_register():
    user = request.form.get('id1')
    pwd1 = request.form.get('pwd1')
    pwd2 = request.form.get('pwd2')
    print(user)
    print(pwd1)
    print(pwd2)
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8',
                           autocommit=True)
    cursor = conn.cursor()
    if user and pwd1 and pwd2:
        if pwd1 == pwd2:
            print("相等")
            sql = "SELECT ID FROM ADMUSER WHERE ID = '" + user + "'"
            print(sql)
            cursor.execute(sql)
            check = cursor.fetchall()
            # checkpwd = check[0][0]
            print(check)
            if len(check) == 0:
                print("进入!")
                sql1 = "INSERT INTO ADMUSER VALUES('%s','%s')" % (user, pwd1)
                print(sql1)
                cursor.execute(sql1)
                return render_template('adm_register.html')
    return redirect('/adm_index')

@app.route("/stu_welcome",methods=['GET','POST'])
def stu_welcome():
    global Suser
    user = request.form.get('account')
    pwd = request.form.get('password')
    Suser=user
    print("!!%s"%user)
    print(pwd)
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8')
    cursor = conn.cursor()
    if user and pwd:
        sql0 = "select ID from STUUSER WHERE ID = '" + user + "'"
        cursor.execute(sql0)
        exist = cursor.fetchall()
        print(exist)
        if len(exist):
            sql1 = "select PASSWORD from STUUSER WHERE ID = '" + user + "'"
            print(sql1)
            cursor.execute(sql1)
            check = cursor.fetchall()
            checkpwd = check[0][0]
            print(checkpwd)
            if len(check) != 0:
                print("yes")
                if pwd == checkpwd:
                    print("yesyes")
                    return render_template('stu_welcome.html')
    return redirect('/stu_index')


@app.route("/adm_welcome",methods=['GET','POST'])
def adm_welcome():
    user = request.form.get('account')
    pwd = request.form.get('password')
    print("!!%s" % user)
    print(pwd)
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8')
    cursor = conn.cursor()
    if user and pwd:
        sql0 = "select ID from ADMUSER WHERE ID = '" + user + "'"
        cursor.execute(sql0)
        exist = cursor.fetchall()
        print(exist)
        if len(exist):
            sql1 = "select PASSWORD from ADMUSER WHERE ID = '" + user + "'"
            print(sql1)
            cursor.execute(sql1)
            check = cursor.fetchall()
            checkpwd = check[0][0]
            print(checkpwd)
            if len(check) != 0:
                print("yes")
                if pwd == checkpwd:
                    print("yesyes")
                    return render_template('adm_welcome.html')
    return redirect('/adm_index')

@app.route("/adm_index",methods=['GET','POST'])
def admidx():
    return render_template('adm_index.html')

@app.route("/stu_system",methods=['GET','POST'])
def stusys():
    global Suser
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * from COURSES"
    cursor.execute(sql1)
    items = cursor.fetchall()
    sql2 = "select * from sinfo WHERE ID = '" + Suser + "'"
    print(sql2)
    cursor.execute(sql2)
    stu_infor = cursor.fetchall()
    return render_template('stu_system.html',items=items,stu_infor=stu_infor)

@app.route("/search_result",methods=['GET','POST'])
def searchresult():

    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8')
    cursor = conn.cursor()
    keyword =  request.form.get('q')
    sql1 = "select name from courses"
    if keyword:
        sql1 = sql1 + " where name like '%" + keyword + "%'"
        print(sql1)
    cursor.execute(sql1)
    items = cursor.fetchall()
    return render_template('search_result.html',items=items)

@app.route("/adm_system",methods=['GET','POST'])
def admsys():
    return render_template('adm_system.html')

@app.route("/course_adm",methods=['GET','POST'])
def courseadm():
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * from CINFO"
    cursor.execute(sql1)
    items = cursor.fetchall()
    return render_template('course_adm.html',items=items)

@app.route("/stu_adm",methods=['GET','POST'])
def stuadm():
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * from SINFO"
    cursor.execute(sql1)
    items = cursor.fetchall()
    return render_template('stu_adm.html',items=items)

@app.route("/tea_adm",methods=['GET','POST'])
def teaadm():
    conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * from TINFO"
    cursor.execute(sql1)
    items = cursor.fetchall()
    return render_template('tea_adm.html',items=items)

#待处理

#课程

@app.route("/del_course",methods=['GET','POST'])
def del_course():
    return render_template('del_course.html')

@app.route("/cdel_success",methods=['GET','POST'])
def cdelsucc():
    courseId=request.form.get('courseId')
    if courseId:
        conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8', autocommit=True)
        cursor = conn.cursor()    #0411mtxM+
        sql="DELETE FROM CINFO WHERE ID = '" + courseId + "'"
        print(sql)
        cursor.execute(sql)
        return render_template('cdel_success.html')
    return redirect('/del_course')

@app.route("/add_course",methods=['GET','POST'])
def add_course():
    return render_template('add_course.html')

@app.route("/cadd_success",methods=['GET','POST'])
def caddsucc():
    courseId = request.form.get('courseId')
    coursename = request.form.get('courseName')
    credit = request.form.get('credit')
    teacher = request.form.get('teacher')
    semester = request.form.get('semester')
    assessmentMethod=request.form.get('assessmentMethod')
    evaluate=request.form.get('evaluate')
    if courseId and coursename and credit and teacher and semester and assessmentMethod and evaluate:
        conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8', autocommit=True)
        cursor = conn.cursor()
        sql = "INSERT INTO CINFO VALUES('"+courseId+"','"+coursename+"','"+credit+"','"+teacher+"','"+semester+"','"+assessmentMethod+"','"+evaluate+"')"
        print(sql)
        cursor.execute(sql)
        return render_template('cadd_success.html')
    return redirect('/add_course')


#学生
'''
已经处理完
'''

@app.route("/add_stu",methods=['GET','POST'])
def add_stu():
    return render_template('add_stu.html')

@app.route("/sadd_success",methods=['GET','POST'])
def saddsucc():
    courseId = request.form.get('courseId')
    coursename = request.form.get('courseName')
    credit = request.form.get('credit')
    teacher = request.form.get('teacher')
    if courseId and coursename and credit and teacher:
        conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8', autocommit=True)
        cursor = conn.cursor()
        sql = "INSERT INTO SINFO VALUES('"+courseId+"','"+coursename+"','"+credit+"','"+teacher+"')"
        print(sql)
        cursor.execute(sql)
        return render_template('sadd_success.html')
    return redirect('/add_stu')

@app.route("/del_stu",methods=['GET','POST'])
def del_stu():
    return render_template('del_stu.html')

@app.route("/sdel_success",methods=['GET','POST'])
def sdelsucc():
    courseId=request.form.get('courseId')
    if courseId:
        conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8', autocommit=True)
        cursor = conn.cursor()
        sql="DELETE FROM SINFO WHERE ID = '" + courseId + "'"
        print(sql)
        cursor.execute(sql)
        return render_template('sdel_success.html')
    return redirect('/del_stu')

#教师

@app.route("/add_tea",methods=['GET','POST'])
def add_tea():
    return render_template('add_tea.html')

@app.route("/tadd_success",methods=['GET','POST'])
def taddsucc():
    courseId = request.form.get('courseId')
    coursename = request.form.get('courseName')
    credit = request.form.get('credit')
    teacher = request.form.get('teacher')
    semester = request.form.get('semester')
    assessmentMethod=request.form.get('assessmentMethod')
    evaluate=request.form.get('evaluate')
    if courseId and coursename and credit and teacher and semester and assessmentMethod and evaluate:
        conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8', autocommit=True)
        cursor = conn.cursor()
        sql = "INSERT INTO TINFO VALUES('"+courseId+"','"+coursename+"','"+credit+"','"+teacher+"','"+semester+"','"+assessmentMethod+"','"+evaluate+"')"
        print(sql)
        cursor.execute(sql)
        return render_template('tadd_success.html')
    return redirect('/add_tea')

@app.route("/del_tea",methods=['GET','POST'])
def del_tea():
    return render_template('del_tea.html')

@app.route("/tdel_success",methods=['GET','POST'])
def tdelsucc():
    courseId=request.form.get('courseId')
    if courseId:
        conn = pymysql.connect(host='120.46.3.93', user='root', password='0411mtxM+', database='SPIDER', charset='utf8', autocommit=True)
        cursor = conn.cursor()
        sql="DELETE FROM TINFO WHERE ID = '" + courseId + "'"
        print(sql)
        cursor.execute(sql)
        return render_template('tdel_success.html')
    return redirect('/del_tea')

if __name__ == "__main__":
    app.run()