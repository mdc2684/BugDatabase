from flask import Flask, render_template, request, jsonify, session, flash, redirect, url_for
import certifi, hashlib
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'secret_key'
ca = certifi.where()


client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.ia8rqcv.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

#client = MongoClient('mongodb+srv://sparta:test@cluster0.ia8rqcv.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
#client = MongoClient('mongodb+srv://sparta:test@cluster0.gya4p0t.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

@app.route('/')
def home():
   return render_template('index.html', session=session)

db = client.dbsparta

offset = 10 # 한 페이지에 들어갈 데이터 수
page_num = 5 # 페이징 버튼에 들어갈 버튼 수
page = 1 # 현재 페이지

# create bug data
@app.route("/bug", methods=["POST"])
def insert_bug():
    title_receive = request.form['title_give']
    category_receive = request.form['category_give']
    content_receive = request.form['content_give'].replace('\n', '<br>')  # 줄바꿈 문자를 HTML 태그로 변환
    user_id_receive = request.form['user_id_give']
    user_nickname_receive = request.form['user_nickname_give']

    last_bug_id = db.auto_increment.find_one()['bug_id']
    db.auto_increment.update_one({'bug_id':last_bug_id}, {'$set':{'bug_id':last_bug_id+1}})

    doc = {
        'id':last_bug_id+1,
        'title':title_receive,
        'category':category_receive,
        'content':content_receive,
        'user_id':user_id_receive,
        'user_nickname':user_nickname_receive
    }
    db.bugs.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

# read bug data
@app.route("/get_bug", methods=["POST"])
def bug_get():
    page = int(request.form['page_give'])
    bug_count = db.bugs.estimated_document_count()
    subdata = {'bug_count':bug_count}
    all_bugs = list(db.bugs.find({},{'_id':False}).sort('id',-1).skip((page-1)*offset).limit(offset))
    return jsonify({'result':all_bugs, 'subdata':subdata})
    
# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      userid_receive = request.form['userid']
      userpwd_receive = request.form['userpwd']
      userpwd_hash = hashlib.sha256(userpwd_receive.encode('utf-8')).hexdigest()
      user = db.user.find_one({'userid': userid_receive, 'userpwd': userpwd_hash})

      if user:
         session['userid'] = userid_receive
         session['user_index'] = user['user_index']
         session['user_nickname'] = user['usernickname']
         return render_template('index.html')
      else:
         flash('회원 정보가 일치하지 않습니다.')
         return render_template('login.html')
   else:
      return render_template('login.html')
     
# 로그아웃
@app.route("/logout")
def logout():
    session.clear()
    return render_template('index.html')


# update bug data
@app.route("/bug_update", methods=["POST"])
def update_bug():
    bug_id_receive = int(request.form['bug_id_give'])
    title_receive = request.form['title_give']
    category_receive = request.form['category_give']
    content_receive = request.form['content_give'].replace('<br>', '')  # <br> 태그 제거
    user_id_receive = request.form['user_id_give']
    user_nickname_receive = request.form['user_nickname_give']

    doc = {
        'id':bug_id_receive,
        'title':title_receive,
        'category':category_receive,
        'content':content_receive,
        'user_id':user_id_receive,
        'user_nickname':user_nickname_receive
    }
    db.bugs.update_one({'id':bug_id_receive}, {'$set':doc})

    return jsonify({'msg':'수정 완료!'})

# delete bug data
@app.route("/bug_delete", methods=["POST"])
def delete_bug():
    bug_id_receive = int(request.form['bug_id_give'])
    db.bugs.delete_one({'id':bug_id_receive})
    return jsonify({'msg':'삭제 완료!'})

# read one data for update bug data
@app.route('/modify', methods=["POST"])
def modify_bug():
    bug_id_receive = request.form['bug_id_give']
    print(bug_id_receive)
    target_bug = db.bugs.find_one({'id':int(bug_id_receive)}, {'_id':False})
    return jsonify({'result':target_bug})

# search bug data
@app.route("/bug_search", methods=["POST"])
def bug_search():
    query_receive = request.form['query_give']
    category_receive = request.form['category_give']
    query_type_receive = request.form['query_type_give']
    page = int(request.form['page_give'])

    doc = {}
    # 내용, 제목, 작성자 별로 검색할 수 있음.
    if query_type_receive == '내용' :
        doc['content'] = {'$regex':query_receive}
    elif query_type_receive == '제목' :
        doc['title'] = {'$regex':query_receive}
    elif query_type_receive == '작성자' :
        doc['user_nickname'] = {'$regex':query_receive}
    elif query_type_receive == '내용+제목' :
        doc['content'] = {'$regex':query_receive}
        doc['title'] = {'$regex':query_receive}
    elif query_type_receive == '내용+제목+작성자' :
        doc['content'] = {'$regex':query_receive}
        doc['title'] = {'$regex':query_receive}
        doc['user_nickname'] = {'$regex':query_receive}

    if (category_receive != '카테고리'):
        doc['category'] = category_receive

    all_bugs = list(db.bugs.find(doc,{'_id':False}).sort(id,-1).skip((page-1)*offset).limit(offset))
    bug_count = len(all_bugs)
    subdata = {'bug_count':bug_count}
    return jsonify({'result':all_bugs, 'subdata':subdata})

@app.route("/register", methods=["POST"])
def register():
    
    userid_receive = request.form['userid_give']
    usernickname_receive = request.form['usernickname_give']
    userpwd_receive = request.form['userpwd_give']
    useremail1_receive = request.form['useremail1_give']
    useremail2_receive = request.form['useremail2_give']

    id_exist = bool(db.user.find_one({"userid": userid_receive}))
    print(id_exist)
    if id_exist:
        return jsonify({'msg': '중복입니다!'})


    id_exist = bool(db.user.find_one({"userid": userid_receive}))
    print(id_exist)
    if id_exist:
        
        return jsonify({'msg': '중복입니다!'})
    

    userpwd_hash = hashlib.sha256(userpwd_receive.encode('utf-8')).hexdigest()

    userindex = db.auto_increment.find_one()['user_index']
    db.auto_increment.update_one({'user_index':userindex}, {'$set':{'user_index':userindex+1}})

    doc = {
        'user_index':userindex+1,
        'userid':userid_receive,
        'usernickname': usernickname_receive,
        'userpwd': userpwd_hash,
        'useremail1':useremail1_receive,
        'useremail2':useremail2_receive
    }
    db.user.insert_one(doc)
    return jsonify({'msg': '회원가입 완료!'})

@app.route("/register", methods=["GET"])
def register_form():
   return render_template('register.html')

# paging read와 search에 넣기
def paging():
    bug_count = db.bugs.count_documents()
    total_page_num = bug_count / offset + 1
    return 0
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)
