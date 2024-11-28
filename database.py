from tkinter import messagebox
import pymysql
import pyodbc

def connect_database():
    global mycursor,con
    try:
        con = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4')
        mycursor = con.cursor()
    except pymysql.Error as e:
        messagebox.showerror('Connection Error', f'Error connecting to MySQL database: {e}')
        return None  # Return None or handle the error appropriately
    mycursor.execute('Create database if not exists data')
    mycursor.execute('use employee_data')
    mycursor.execute('create table if not exists data (ID varchar(20),Name varchar(50),gender varchar(20), varchar(50),salary decimal(10,2)')
def id_exists(id):
    mycursor.execute('Select count(*) from data where id=%s',id)
    result=mycursor.fetchone()
    return result[0] >0
def fetch_employees():
    mycursor.excute('Select * from data')
    result=mycursor.fetchall()
    return result

def update(id,phone,Name,Salary,role,gender):
    mycursor.execute('UPDATE data SET Name = ?, phone = ?, role = ?, gender = ?, salary = ? WHERE ID = ?',
                   (Name, phone, role, gender, Salary, id))
    con.commit()


def insert(id,phone,name,salary,role,gender):
    mycursor.execute('Insert into data values (%s,%s,%s,%s,%s,%s)',(id,phone,name,salary,role,gender))
    con.commit()
def delete(id):
    mycursor.execute('Delete from data where id=%s', id,)
    con.commit()
def search(option,value):
    mycursor.execute(f'Select * from data where {option}=%s',value)
    result=mycursor.fetchall()
    return result
def deleteall_records():
    mycursor.execute('Truncate table data')
    con.commit

connect_database()
