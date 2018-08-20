__author__ = 'user'
import datetime
from abc import ABC,abstractmethod

class Customer():
    def set_first_name(self,fname):
        self.first_name = fname

    def set_last_name(self,lname):
        self.last_name = lname

    def set_customer_id(self,id):
        self.customer_id = id;

    def set_password(self,pwd):
        self.password = pwd

    def set_address(self,addr):
        self.addr = addr

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_customer_id(self):
        return self.customer_id

    def get_password(self):
        return self.password

    def get_address(self):
        return self.addr
class Book():

    def set_title(self,title):
        self.title = title
        
    def set_author(self,author):
        self.author = author
        
    def set_publish(self,publication):
        self.publication = publication
         
    def set_pub_year(self,pub_year):
        self.pub_year = pub_year
        
    def set_b_id(self,b_id):
        self.b_id = b_id
          
    def set_status(self,status):
        self.status = status
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_publish(self):
        return self.publication
    
    def get_pub_year(self):
        return self.pub_year
    
    def get_b_id(self):
        return self.b_id
    
    def get_status(self):
        return self.status
    
    


