from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.gya4p0t.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    userid_receive = request.form['userid_give']
    usernickname_receive = request.form['usernickname_give']
    userpwd_receive = request.form['userpwd_give']
    useremail1_receive = request.form['useremail1_give']
    useremail2_receive = request.form['useremail2_give']
    

    doc = {
        'userid':userid_receive,
        'usernickname': usernickname_receive,
        'userpwd': userpwd_receive,
        'useremail1':useremail1_receive,
        'useremail2':useremail2_receive
    }
    db.bug.insert_one(doc)
    return jsonify({'msg': '회원가입 완료!'})

@app.route("/register", methods=["GET"])
def register_form():
   return render_template('register.html')

@app.route("/login", methods=["GET"])
def login_form():
   return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
   return jsonify({'msg': '로그인 완료!'})





@app.route('/update/<int:num>', methods=['POST'])
def update_post():
    seq = request.form['seq']
    num_receive = request.form['num_give']
    db.board.update_one({'num': int(num_receive)})
    return jsonify({'msg': '수정 완료'})

@app.route("/update", methods = ['GET'])
def board_updateform():
   
   return render_template('update.html')


@app.route("/modify", methods=["GET"])
def modify_form():
   return render_template('modify.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)