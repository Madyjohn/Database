                                    #insert,update,delete,view data using python

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="",database="python_db1")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into user (name,age,city) values (%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Data inserted successfully")

def update(name,age,city,id):
    res=con.cursor()
    sql="update user set name=%s, age=%s, city=%s where id=%s" 
    user=(name,age,city,id)
    res.execute(sql,user)
    con.commit()
    print("Data update successfully")

def view():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE,CITY from user"
    res.execute(sql)
    result=res.fetchall()
    print(result)
    
def delete(id):
    res=con.cursor()
    sql="Delete from user WHERE id=%s" 
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("Data delete successfully")

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.View Data")
    print("4.Delete Data")
    print("5.Exit")

    choice=int(input("Enter Your Choice:"))
    if choice==1:
        name=input("Enter the Name:")
        age=int(input("Enter the Age:"))
        city=input("Enter the City:")
        insert(name,age,city)
    elif choice==2:
        id=int(input("Enter the ID to Update:"))
        name=input("Enter the Name:")
        age=int(input("Enter the Age:"))
        city=input("Enter the City:")
        update(name,age,city,id)

    elif choice==3:
        view()

    elif choice==4:
        id=int(input("Enter the Id to Delete:"))
        delete(id)    

    elif choice==5:
        quit()
    
    else:
        print("Invalid selection, Please try again...")