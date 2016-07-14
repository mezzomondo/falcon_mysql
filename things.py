import falcon
#import datetime
import json
import pymysql
import mysql

class Things(object):
    
    @falcon.before(mysql.open_connection)
    @falcon.after(mysql.close_connection)
    def on_get(self, req, resp):
        #resp.body = json.dumps({'pippo': 'pluto'})
        cursor = mysql.db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Country")
        catalog = cursor.fetchall()
        cursor.close()
        #dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.date) else None
        resp.body = json.dumps(catalog)
        resp.status = falcon.HTTP_200
