__author__ = 'user'

import database
from classes import Customer,Book
import database_admin as db_admin

def change_password(id):
    addr=input("ENTER NEW PASSWORD")
    database.change_password(id,addr)





