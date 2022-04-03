from flask import Flask, render_template,request
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user names'
app.config['MYSQL_PASSWORD'] = 'user password'
#app.config['MYSQL_DB'] = 'databse name'


mysql = MySQL(app)
@app.route("/")
def index():
    return render_template("index.html");   

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        firstname = request.form['firstname']
        #return render_template("result.html",result = result)
        middlename=request.form['middlename']
        lastname=request.form['lastname']
        courses=request.form['course']
        gender=request.form['gender']
        phone=str(request.form['phone'])
        currentAdd=request.form['currentAdd']


        # cursor = mysql.connection.cursor()
        # cursor.execute("create database studentReg")
        # cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute("use studentReg")
        cursor.close()

        #Create table
        # cursor = mysql.connection.cursor()
        # table="create table Studentdetails1(firstname VARCHAR(20),middleName VARCHAR(20),lastname VARCHAR(30),course VARCHAR(5), gender VARCHAR(5),phone VARCHAR(10),currentAdd TEXT(100))"
        # cursor.execute(table)
        # #Closing the cursor
        # cursor.close()

        #Inserting data recived from form into table
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO Studentdetails1 VALUES(%s,%s,%s,%s,%s,%s,%s)''',(firstname,middlename,lastname,courses,gender,phone,currentAdd))
        #Saving the Actions performed on the DB
        mysql.connection.commit()
        cursor.close()
        
        cursor = mysql.connection.cursor()
        query = "SELECT * from Studentdetails1"
        cursor.execute(query)
        data = cursor.fetchall()

        
        return render_template("result.html",data=data)

      

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
