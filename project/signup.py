import mysql.connector
from Database import Mysql_Connector
from tkinter import *
class Sign_Up():
    def __init__(self):
        db_obj = Mysql_Connector(host="localhost", user='root', passwd='password', db='hcl')
