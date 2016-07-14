import falcon
import pymysql

HOST =     '127.0.0.1'
USER =     'user'
PASSWORD = 'password'

db = None

def open_connection(req, resp, resource, params):
    global db
    db = pymysql.connect(host=HOST,user=USER,passwd=PASSWORD,db="world")

def close_connection(req, resp, resource):
    db.close()
