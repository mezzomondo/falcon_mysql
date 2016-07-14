## falcon_mysql
Using hooks to establish a per-connection connection to MySQL from Falcon in Python

## Instructions

Install prerequisites, namely the framework (falcon), pymysql, gunicorn, nose for tests and httpie because we are human:

```
$ pip install -r requirements.txt
```

Restore a copy of the database, I'm using the popular world database available [here](http://dev.mysql.com/doc/index-other.html). Maybe your credentials will differ...

```
$ mysql < world.sql
```

Edit credentials in mysql.py
