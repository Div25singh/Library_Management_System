__author__ = 'user'
from connection import con,cur
from classes import Customer,Book
def check_customer_exists(id):
    sql = "select count(*) from customers where customer_id = :id"
    cur.execute(sql, {"id":id})
    res = cur.fetchall()
    count = res[0][0]
    if count == 1:
        return True
    else:
        return False

def add_book(book):
    title = book.get_title()
    author = book.get_author()
    publish=book.get_publish()
    pub_year = book.get_pub_year()
    b_id=book.get_b_id()
    status=book.get_status()
    sql = "insert into book values(:title,:author,:publish,:pub_year,:id,:status)"
    cur.execute(sql, {"title":title, "author":author, "publish":publish , "pub_year":pub_year, "id":b_id, "status":status})
    con.commit()
    print("Book Added")

def remove_book(book):
    b_id=book.get_b_id()
    sql="delete from book where book_id= :id"
    cur.execute(sql,{"id":b_id})
    con.commit()
    print("Book Removed")
   
def remove_Customer(c_id):
    sql="delete from customers where customer_id= :id"
    cur.execute(sql,{"id":c_id})
    con.commit()
    print("Customer Removed")

