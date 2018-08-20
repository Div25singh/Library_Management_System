__author__ = 'user'

import database
from classes import Customer,Book
import login_menu
import admin_menu
import database_admin as db_admin

def sign_up():

    customer = Customer()
    first_name = input("Enter First Name\n")
    last_name = input("Enter Last Name\n")
    address = input("Enter Address\n")
    password = input("Enter password (min 8 char and max 20 char)\n")
    while len(password) < 8 or len(password) > 20:
        print("Please Enter password in given range\n")
        password = input();

    customer.set_first_name(first_name)
    customer.set_last_name(last_name)
    customer.set_password(password)
    customer.set_address(address)
    database.sign_up_customer(customer)

def sign_in():
    try:
        id = int(input("Enter Customer ID\n"))
    except:
        print("Invalid ID")
        return

    if db_admin.check_customer_exists(id) is True:
        customer = database.get_all_info_customer(id)
        password = input("Enter Password\n")
        res = database.login_customer(id,password)
        if res is True:
            print("Login Successful")
            ch = 1
            while ch != 0:
                print("\n--- Menu ---")
                print("1. Available Books")
                print("2. Issue Book")
                print("3. Return Book")
                print("4. Issued Books")
                print("5. Change Password")
                print("0. Logout")

                try:
                    ch = int(input())
                except:
                    print("Invalid Choice")
                    ch = 1
                    continue

                if ch == 1:
                    database.avail_book()
                elif ch == 2:
                    database.issuebook(id)
                elif ch == 3:
                    database.returnbook(id)
                elif ch == 4:
                    database.issued_books(id)
                elif ch == 5:
                    login_menu.change_password(id)
                elif ch == 0:
                    print("Logged Out Successfully")
                else:
                    print("Invalid Choice")
    else:
        print("Customer doesn't exist")


def admin_sign_in():
    try:
        id = input("\nEnter Admin ID : ")
    except:
        print("Invalid ID")
        return

    password = input("\nEnter Password : ")
    res = database.login_admin(id,password)

    while res == False:
        print("Wrong ID or Password")
        try:
            id = int(input("Enter Admin ID\n"))
        except:
            print("Invalid ID")
            return
        password = input("Enter Password\n")
        res = database.login_admin(id,password)

    if res == True:
        print("Login Successful")
        ch = 1
        while ch != 0:
            print("\n --- Menu --- ")
            print("1. All Books")
            print("2. Available Books")
            print("3. Add Book")
            print("4. Remove Book")
            print("5. All Customers")
            print("6. Remove Customer")
            print("7. Check Issue History")
            print("0. Admin Log Out")

            try:
                ch = int(input())
            except:
                print("Invalid Choice")
                ch = 1
                continue

            if ch == 1:
                database.all_books()
            elif ch == 2:
                database.avail_book()
            elif ch == 3:
                admin_menu.add_book()
            elif ch == 4:
                admin_menu.remove_book()
            elif ch == 5:
                admin_menu.all_customers()
            elif ch == 6:
                admin_menu.remove_customer()
            elif ch == 7:
                admin_menu.check_history()
            elif ch == 0:
                print("Logged Out Successfully")
            else:
                print("Invalid Choice")

    else:
        print("Sorry all Attempts Finished")




