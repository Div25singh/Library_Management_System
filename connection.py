__author__ = 'user'

import cx_Oracle
"you must have Oracle database userId and password for connection from database."
con = cx_Oracle.connect("ani/mycycle.com")
cur = con.cursor()
