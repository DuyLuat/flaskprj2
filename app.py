from flask import Flask, url_for, request, json, jsonify, render_template
import pymysql
 
db = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='test',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor) 
app = Flask(__name__)


@app.route("/")
def index():
   return render_template('base.html')
 
@app.route('/signUp')
def signUp():
   return render_template('signUp.html')
 
@app.route('/process', methods=['POST', 'GET'])
def process():
   
   msg = ''
   username = request.form['username']
   password = request.form['password']
   name = request.form['name']
   email = request.form['email']
 
   if name and email and username and password:
      cur = db.cursor()
      cur.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s)', (name, username, password, email)) 
      db.commit()
      msg = 'You have successfully registered!'
      return jsonify({'name' : msg})
   return jsonify({'error' : 'Missing data!'})
