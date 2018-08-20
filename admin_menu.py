__author__ = 'user'
from connection import con,cur
import database_admin as db_admin
from classes import Customer,Book
def add_book():
    book=Book()
    title =input("ENTER TITLE OF BOOK")
    author =input("ENTER AUTHOR OF BOOK")
    publish=input("ENTER PUBLISHER OF BOOK")
    pub_year =input("ENTER PUBLISH YEAR OF BOOK")
    id=input("ENTER ID OF BOOK")
    status="Available"
    book.set_title(title)
    book.set_author(author)
    book.set_publish(publish)
    book.set_pub_year(pub_year)
    book.set_b_id(id)
    book.set_status(status)
    
    db_admin.add_book(book)
    
def remove_book():
    book=Book()
    b_id=input("ENTER BOOK ID TO BE REMOVED")
    book.set_b_id(b_id)
    
    db_admin.remove_book(book)

def remove_customer():
    c_id=input("ENTER CUSTOMER ID TO BE REMOVED")
    
    db_admin.remove_Customer(c_id)
    
def all_customers():
    sql="select * from customers"
    cur.execute(sql)
    data=cur.fetchall()
    for line in data:
        print("ID:",line[0],"FNAME:",line[1],"LNAME:",line[2],"ADDRESS:",line[3],"PASSWORD:",line[4])
    con.commit
    
def check_history():
    sql="""select * from issuehistory"""
    cur.execute(sql)
    data=cur.fetchall()
    for line in data:
        print("Book ID:",line[0],"Customer ID:",line[1],"STATUS:",line[2])
    con.commit()    
    