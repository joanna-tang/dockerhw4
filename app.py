"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
# import Redis and MySQL drivers
import redis
import MySQLdb
#from collections import Counter
from flask import Flask, redirect, url_for, render_template, request, session, flash
import os

# Redis server data
redis_host = os.environ.get('REDIS_HOST', "localhost")  
redis_port = int( os.environ.get('REDIS_PORT', 6379) )
# mysql server data
mysql_host = os.environ.get('MYSQL_HOST', "ms-surface")
mysql_port = int( os.environ.get('MYSQL_PORT', 3306) )
mysql_user = os.environ.get('MYSQL_USER', "hw4app")
mysql_pwd = os.environ.get('MYSQL_PASSWORD', "dockerhw4")
mysql_db = os.environ.get('MYSQL_DB', "hw4_db")
# initialize data
cachecnt = 0
sqlcnt = 0

# create instance connection
r = redis.StrictRedis(host=redis_host, port=redis_port)
db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_pwd, db=mysql_db,port=mysql_port)
#db.autocommit = True
c = db.cursor()
c.callproc('usp_getcount')
# get data
sqlcnt = int(c.fetchall()[0][0])
cachecnt = int(r.get('count'))
c.close()

app = Flask(__name__)
app.secret_key = "xxx"
#app.permanent_session_lifetime = timedelta(days=5)
#session.permanent = True

# Make the WSGI interface available at the top level so wfastcgi can get it.
# wsgi_app = app.wsgi_app

def savetoredis(username, email, password):
	#print ("inside cache: ", username, email, password)
	try:
		data = {username, email, password}
		r.set(email, str(data))
		r.incr('count')
		return int(r.get('count'))
	except redis.exceptions.ConnectionError as exc:
		flash(exc)

def savetosql(username, email, password):
	print ("inside sql: ", username, email, password)
	try:
		c = db.cursor()
		args = [username, email, password]
		print (args)
		result_args = c.callproc('usp_createlogin', args)
		c.callproc('usp_getcount')
		flash("Info is saved to mysql")
		return int(c.fetchall()[0][0])
	except db.Error as exsql:
		flash(exsql)
		return sqlcnt
	finally:
		c.close()

@app.route('/', methods=["POST", "GET"])
def index():
	global sqlcnt, cachecnt
	if request.method == "POST":
		username = request.form["username"]
		email = request.form["email"]
		password=request.form["pwd"]
		passwordHash = hash(password);
		print (username, email, password, passwordHash)
		if "sql" in request.form :
			sqlcnt = savetosql (username, email, str(passwordHash))
			
		if "cache" in request.form:
			cachecnt = savetoredis (username, email, str(passwordHash))
			flash("Info is saved to Redis")
	return render_template("index.html", sqlcount=sqlcnt, cachecount=cachecnt)

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', 5000))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT, debug=True)
