__author__ = 'user'

import cx_Oracle
import datetime
from classes import Customer,Book
from connection import con,cur

def make_all_tables():
    sql = """create table customers(
                  customer_id number(5) primary key,
                  first_name varchar2(10),
                  last_name varchar2(10),
                  address varchar2(40),
                  password varchar2(20))"""
    cur.execute(sql)
    con.commit()
    
def make_all_tables1():
    sql = """create table book(
            title varchar2(15),
            author varchar2(30),
                  publisher varchar2(30),
                  pub_year number(4),
                  book_id varchar2(30) primary key,
                  status varchar2(10) CHECK (status in('Issued','Due','Available')))"""
    cur.execute(sql)
    con.commit()
    
def make_all_tables2():    
    sql = """create table admin(
                  admin_id number(5),
                  password varchar2(10))"""
    cur.execute(sql)
    con.commit()
    sql = "insert into admin values(227,'helloadmin')"
    cur.execute(sql)
    con.commit()

def make_all_tables3():    
    sql = """create table issuehistory(
                  book_id varchar2(5),
                  customer_id number(5),
                  status varchar2(15) check (status in('Issued','Returned')),
                  )"""
    cur.execute(sql)
    con.commit()

def sign_up_customer(customer):
    fname = customer.get_first_name()
    lname = customer.get_last_name()
    address=customer.get_address()
    password = customer.get_password()
    sql = "select customer_id_sequence.nextval from dual"
    cur.execute(sql)
    res = cur.fetchall()
    c_id = res[0][0]
    sql = "insert into customers values(:id,:fname,:lname,:address,:password)"
    cur.execute(sql, {"id":c_id, "fname":fname, "lname":lname, "password":password, "address":address})
    con.commit()
    print("Congratulations ! Your Account was Created Successfully")
    print("Your Customer ID : ",c_id)

def login_customer(id,password):
    sql = "select count(*) from customers where customer_id = :id and password = :password"
    cur.execute(sql, {"id":id, "password":password})
    res = cur.fetchall()
    count = res[0][0]
    if count == 1:
        return True
    else:
        return False

def issuebook(c_id):
    b_id=input("ENTER BOOK ID TO BE ISSUED\n")
    sql="""update book set status='Issued' where book_id= :id"""
    cur.execute(sql,{"id":b_id})
    con.commit
    sql="Select * from book where book_id= :id"
    cur.execute(sql,{"id":b_id})
    data=cur.fetchall()
    for line in data:
        print(line[0],line[1],line[2],line[3],line[4],line[5])
    cur.execute("""insert into issuehistory values(:bid,:cid,:stat)""",{'bid':b_id,'cid':c_id,'stat':"Issued"})
    con.commit
    print("BOOK ISSUED\n")
    
def returnbook(c_id):
    b_id=input("ENTER BOOK ID TO BE RETURNED\n")
    sql="""update book set status='Available' where book_id= :id"""
    cur.execute(sql,{"id":b_id})
    con.commit
    sql="Select * from book where book_id= :id"
    cur.execute(sql,{"id":b_id})
    data=cur.fetchall()
    for line in data:
        print(line[0],line[1],line[2],line[3],line[4],line[5])
    cur.execute("""insert into issuehistory values(:bid,:cid,:stat)""",{'bid':b_id,'cid':c_id,'stat':"Returned"})
    con.commit
    print("BOOK RETURNED\n")

def issued_books(c_id):
    sql="""select a.book_id,a.title,b.status from book a,issuehistory b where a.book_id=b.book_id and b.customer_id= :c_id"""
    cur.execute(sql,{"c_id":c_id})
    data=cur.fetchall()
    for line in data:
        print(line[0],line[1],line[2]) 
    con.commit
def avail_book():
    sql="select * from book where status='Available'"
    cur.execute(sql)
    data=cur.fetchall()
    for line in data:
        print(line[0],line[1],line[2],line[3],line[4],line[5])
    con.commit

def all_books():
    sql="select * from book"
    cur.execute(sql)
    data=cur.fetchall()
    for line in data:
        print(line[0],line[1],line[2],line[3],line[4],line[5])
    con.commit

def check_book_exists(id):
    sql = "select count(*) from book where book_id = :id"
    cur.execute(sql, {"id":id})
    res = cur.fetchall()
    count = res[0][0]
    if count == 1:
        return True
    else:
        return False
def change_password(id,addr):
        sql = "update customers set password = :pass where customer_id = :id"
        cur.execute(sql, {"pass":addr, "id":id})
        con.commit()
        print("Password Updated Successfully")

def login_admin(id,password):
    sql = "select count(*) from admin where admin_id = :id and password = :password"
    cur.execute(sql , {"id":id, "password":password})
    res = cur.fetchall()
    count = res[0][0]
    if count == 1:
        return True
    else:
        return False

def get_all_info_customer(id):
    sql = "select * from customers where customer_id = :id"
    cur.execute(sql, {"id":id})
    res = cur.fetchall()
    if len(res) == 0:
        return None
    customer = Customer()
    status = res[0][3]
    att = res[0][4]
    customer.set_customer_id(id)
    return customer












