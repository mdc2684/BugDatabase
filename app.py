from flask import Flask, render_template, request, jsonify, session, flash, redirect, url_for
import certifi
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = 'secret_key'


ca = certifi.where()
client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.jzm1gqj.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

db = client['dbbugdatabase']

@app.route('/')
def home():
   return render_template('index.html')

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      userid_receive = request.form['userid']
      userpw_receive = request.form['userpw']
      
      user = db.bugdatabase.find_one({'userid': userid_receive})
      if user and user['userpw'] == userpw_receive:
         session['userid'] = userid_receive
         return redirect(url_for('index'))
      else:
         flash('Invalid')
         return redirect(url_for('login'))
   else:
      return render_template('login.html')


if __name__ == '__main__':
   app.run('0.0.0.0', port=5040, debug=True)