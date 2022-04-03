import mysql.connector as conn
#Connecting to the mysql and using mydb variable

def createDB():
    mydb=conn.connect(host='localhost',user='root',passwd='root123')
    #Creating a Data base
    cursor=mydb.cursor()
    cursor.execute("create database studentReg")


def createTable():
    mydb=conn.connect(host='localhost',user='root',passwd='root123',database='studentReg')
    #Creating a Data base
    table="create table Studentdetails1(firstname VARCHAR(20),middleName VARCHAR(20), lastname VARCHAR(30),course VARCHAR(5), gender VARCHAR(5),phone VARCHAR(10),currentAdd VARCHAR(150))"
    cursor=mydb.cursor()
    cursor.execute(table)
    return "table created"

if __name__ == "__main__":
    createDB()
    createTable()
    
    