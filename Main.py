from pickle import NONE
import sqlite3
from flask import Flask, render_template,request

app = Flask(__name__)

def DbConnection():
    con = NONE
    try:
        con=sqlite3.connect("DataBase.db")
    except sqlite3.Error as e:
        print(e)
    return con


@app.route("/",methods=['GET','POST'])
def Index():
    return render_template('Index.html')

@app.route("/test",methods=['GET','POST'])
def test():
    if request.method == 'POST':
        x = request.form.get('submit_button')
        print(x)


    return render_template('test.html')


@app.route("/Semster/<sem>",methods=['GET','POST'])
def SemstersSubsjects(sem):
    con = DbConnection()
    
    if int(sem) > 8 or int(sem) <0:
        return 'memes'
    else:
     Subjects = con.execute(f"SELECT * FROM Subjects where Semster = {sem}").fetchall()
     return render_template('Semesters.html',Subjects = Subjects,sem=sem)

@app.route("/Subject/<sub>",methods=['GET','POST'])
def Subject(sub):
    con = DbConnection()
    SubjectFound = con.execute(f"""SELECT * FROM Subjects where Name ='{sub}'""").fetchall()
    if SubjectFound:
        Data = con.execute(f"""SELECT * FROM '{sub}'""").fetchall()
        return render_template('Subject.html',Data = Data)
    else:
        return 'Not found'

        