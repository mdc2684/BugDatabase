from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.ia8rqcv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bug", methods=["POST"])
def movie_post():
    title_receive = request.form['title_give']
    category_receive = request.form['category_give']
    content_receive = request.form['content_give']

    last_bug_id = db.auto_increment.find_one()['bug_id']
    db.auto_increment.update_one({'bug_id':last_bug_id}, {'$set':{'bug_id':last_bug_id+1}})

    doc = {
        'id':last_bug_id+1,
        'title':title_receive,
        'category':category_receive,
        'content':content_receive,
        'user_id':1,
        'user_nickname':'마태현(임시)'
    }
    db.bugs.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route("/bug_update", methods=["POST"])
def bug_update():
    title_receive = request.form['title_give']
    category_receive = request.form['category_give']
    content_receive = request.form['content_give']
    bug_id_receive = int(request.form['bug_id_give'])

    doc = {
        'id':bug_id_receive,
        'title':title_receive,
        'category':category_receive,
        'content':content_receive,
        'user_id':1,
        'user_nickname':'마태현(임시)'
    }
    db.bugs.update_one({'id':bug_id_receive}, {'$set':doc})

    return jsonify({'msg':'수정 완료!'})



@app.route("/bug", methods=["GET"])
def movie_get():
    all_bugs = list(db.bugs.find({},{'_id':False}))
    return jsonify({'result':all_bugs})

@app.route('/modify', methods=["POST"])
def modify_bug():
    bug_id_receive = request.form['bug_id_give']
    print(bug_id_receive)
    target_bug = db.bugs.find_one({'id':int(bug_id_receive)}, {'_id':False})
    # target_bug = {'id':bug_id_receive, 'title':'몰라'}
    return jsonify({'result':target_bug})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)