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
    name_receive = request.form['name_give']
    pwd_receive = request.form['pwd_give']
    email_receive = request.form['email_give']
    tel_receive = request.form['tel_give']
    

    doc = {
        'userid':userid_receive,
        'name':name_receive,
        'pwd':pwd_receive,
        'email':email_receive,
        'tel':tel_receive
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




@app.route("/write", methods=["POST"])
def board_write():
   
   count = list(db.board.find({}, {'_id': False}))
   seq = len(count) + 1

   title_receive = request.form['title_give']
   userid_receive = request.form['userid_give']
   comment_receive = request.form['comment_give']



   doc = {
        'seq' : seq,
        'title':title_receive,
        'userid':userid_receive,
        'comment':comment_receive
        
   }
   
   db.board.insert_one(doc)
   return jsonify({'msg': '게시글 작성 완료!'})


@app.route("/write", methods=["GET"])
def write_form():
   return render_template('write.html')

@app.route('/board')
def board():
   boards = list(db.board.find({},{'_id':False}))
   return jsonify({'result': boards})





@app.route("/delete", methods=["POST"])
def board_deletevalue():
   seq = request.form['seq']
   
   db.board.delete_one({'seq':int(seq)})
   return jsonify({'msg': '삭제 완료!'})




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