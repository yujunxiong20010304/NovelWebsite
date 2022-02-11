# flask 函数
from flask import Flask, request, jsonify, session, make_response
from flask_cors import CORS
import processingFace
import os
from db_helper import MysqlOperation
import db_helper
from flask_session import Session
from sendMail import sendMail
import random

app = Flask(__name__)
app.config.from_pyfile('settings.py')
Session(app)
CORS(app, resources=r'/*')


# 解决session跨域问题
@app.after_request
def af_req(resp):  # 解决跨域session丢失
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    resp.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,OPTIONS'
    # resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    resp.headers[
        'Access-Control-Allow-Headers'] = 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'

    resp.headers['X-Powered-By'] = '3.2.1'
    resp.headers['Content-Type'] = 'application/json;charset=utf-8'
    return resp


# 判断当前用户是否登录
@app.route('/api/trial', methods=['POST'])
def trial():
    username = session.get('username')
    return jsonify(code=200, message='success', username=username)


# passwordlogin 密码登录
@app.route('/api/passwordlogin', methods=['POST'])
def passwordlogin():
    # 获取前端传送的数据
    username = request.json.get('username')
    password = request.json.get('password')
    # 判断参数是否齐全
    if not (username and password):
        return jsonify(code=400, message='Parameters are missing')
    # 查询数据库进行用户匹配
    result = MysqlOperation().matching(username, password)
    if not result:
        message = 'fail'
        code = 404
    else:
        message = 'success'
        session['username'] = username
        code = 200
    return jsonify(code=code, message=message)


# login 人脸登录
@app.route('/api/login', methods=['POST'])
def login():
    # 获取前端传送的数据
    img = request.json.get('img')
    print(img)
    if not img:
        return jsonify(code=404, message='Parameter cannot be empty')
    img = img.split(',')[1]
    # 图片格式转化
    picture = processingFace.obtainImg(img)
    # 提取特征点
    mask_csv = processingFace.singlePictureProcessing(picture)
    # 调用mysql数据库中的特征点来进行判断
    humanFace = MysqlOperation().login()
    features_name = humanFace[0]
    features = humanFace[1]
    # 欧式距离
    finale = processingFace.distance(features, mask_csv)
    if finale:
        for i in range(len(finale)):
            if finale[i] == min(finale) and min(finale) < 0.35:
                print(features_name[i])
                # 保存session信息
                session['username'] = features_name[i]
                return jsonify(code=200, message='success')
    return jsonify(code=404, message='fail')


# 某一类书本信息
@app.route('/api/novel', methods=['POST'])
def get_novel_data():
    test = MysqlOperation()
    # 数量
    amount = request.json.get('amount')
    # 类型
    types = request.json.get('type')
    # 个数
    num = request.json.get('num')
    # 翻页
    breakdown = request.json.get('breakdown')
    # 判断
    judge = request.json.get('judge')
    if not types:
        return jsonify(code=404, message='Incomplete parameters')
    parameters = (types, num)
    if amount:
        parameters = (types, num, amount)
    data = db_helper.data_clean(test.get_population(*parameters), breakdown)
    number = 0
    if judge:
        num = test.book_list_number(types[0])
        number = int(num / 20) + 1
    body = {
        'number': number,
        'data': data
    }
    return jsonify(code=200, message='success', body=body)


# 单个书本+章节信息
@app.route('/api/chapter', methods=['GET'])
def outgoing_book_chapter_data():
    types = request.args.get('type')
    name = request.args.get('name')
    if not (types and name):
        return jsonify(code=404, message='Incomplete parameters')
    result = MysqlOperation().second_level_book_data(types, name)
    return jsonify(code=200, message='success', body=result)


# 章节信息
@app.route('/api/content', methods=['GET'])
def output_chapter_data():
    types = request.args.get('type')
    name = request.args.get('name')
    page = request.args.get('page')
    if not (types and name and page):
        return jsonify(code=404, message='Incomplete parameters')
    data = MysqlOperation().chapter_content(types, name, page)
    return jsonify(code=200, message='success', body=data)


# 查询（按作者名和书名来查询）
@app.route('/api/query', methods=['GET'])
def query():
    search = request.args.get('search')
    data = MysqlOperation().query(search)
    if not search:
        return jsonify(code=404, message='Incomplete parameters')
    return jsonify(code=200, message='success', body=data)


# 添加进书架
@app.route('/api/addBookcase', methods=['POST'])
def addBookcase():
    user = request.json.get('user')
    book_name = request.json.get('book_name')
    book_type = request.json.get('book_type')
    book_author = request.json.get('book_author')
    book_new_chapter = request.json.get('book_new_chapter')
    book_old_chapter = request.json.get('book_old_chapter')
    updatetime = request.json.get('updatetime')
    if not (user and book_name and book_type and book_author and book_new_chapter and book_old_chapter and updatetime):
        return jsonify(code=404, message='Missing parameter')
    MysqlOperation().add_bookcase(user,
                                  book_name,
                                  book_type,
                                  book_author,
                                  book_new_chapter,
                                  book_old_chapter,
                                  updatetime)
    return jsonify(code=200, message='success')


# 查询对应用户书架中的内容
@app.route('/api/getBookshelf', methods=['GET'])
def getBookshelf():
    user = request.args.get('user')
    page = request.args.get('page')
    if not (user and page):
        return jsonify(code=404, message='Missing parameter')
    data = MysqlOperation().getBookshelf(user, int(page))
    return jsonify(code=200, message='success', body=data)


# 删除书架收藏书籍
@app.route('/api/delete', methods=['GET'])
def delete():
    book_id = request.args.get('id')
    # book_id = request.args.get('id')  # get 请求使用
    # book_id = request.form.get('id')  # 表单使用
    if not book_id:
        return jsonify(code=400, message='Missing parameter')
    MysqlOperation().delete(book_id)
    return jsonify(code=200, message='success')


# 更新书架的历史记录
@app.route('/api/update_history', methods=['GET'])
def update_history():
    num = request.args.get('num')
    chapter = request.args.get('chapter')
    user = request.args.get('user')
    name = request.args.get('name')
    if not (num and chapter and user and name):
        return jsonify(code=400, message='Missing parameter')
    MysqlOperation().update_history(num, chapter, user, name)
    return jsonify(code=200, message='success')


# 退出登录
@app.route('/api/sign_out', methods=['POST'])
def sign_out():
    return session.pop('username')


# 判断当前用户是否注册
@app.route('/api/judge_register', methods=['POST'])
def judge_register():
    user = request.json.get('user')
    if not user:
        return jsonify(code=400, message='Missing parameter')
    result = MysqlOperation().judge_register(user)
    data = 'fail' if not result else 'success'
    return jsonify(code=200, message='success', body=data)


# 发送邮箱验证码
@app.route('/api/sendmail', methods=['POST'])
def sendmail():
    mail = request.json.get('mail')
    if not mail:
        return jsonify(code=400, message='Missing parameter')
    code_string = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    codes = list(code_string)
    data = "".join(random.sample(codes, 6))
    test = sendMail(mail, data)
    test.send_out_email()
    # 返回生成的验证码
    return jsonify(code=200, message='success', body=data)


# 邮箱方式注册账号
@app.route('/api/register_change', methods=['POST'])
def register_change():
    user = request.json.get('user')
    password = request.json.get('password')
    mail = request.json.get('mail')
    if not (user and password and mail):
        return jsonify(code=400, message='Missing parameter')
    MysqlOperation().register_change(user, password, mail)
    return jsonify(code=200, message='success')


# 获取用户的相关信息进行展示
@app.route('/api/obtain_user', methods=['POST'])
def obtain_user():
    user = request.json.get('user')
    if not user:
        return jsonify(code=400, message='Missing parameter')
    data = MysqlOperation().obtain_user(user)
    return jsonify(code=200, message='success', body=data)


# 对用户修改信息后进行一个保存
@app.route('/api/preservation_user', methods=['POST'])
def preservation_user():
    name = request.json.get('user_info').get('name')
    password = request.json.get('user_info').get('password')
    mailbox = request.json.get('user_info').get('mailbox')
    user = request.json.get('user')
    if not (name and password and mailbox and user):
        return jsonify(code=400, message='Missing parameter')
    MysqlOperation().preservation_user(name,
                                       password,
                                       mailbox,
                                       user
                                       )
    return jsonify(code=200, message='success')


# 保存用户的头像进数据库
@app.route('/api/submit_avatar', methods=['POST'])
def submit_avatar():
    img = request.json.get('img')
    user = request.json.get('user')
    if not (img and user):
        return jsonify(code=400, message='Missing parameter')
    MysqlOperation().storage_image(user, str(img))
    return jsonify(code=200, message='success')


# 获取用户的头像
@app.route('/api/image', methods=['GET'])
def image():
    user = request.args.get('user')
    if not user:
        return jsonify(code=400, message='Missing parameter')
    result = MysqlOperation().get_image(user)
    return jsonify(code=200, body=result, message='success')


# 人脸数据的录入
@app.route('/api/get_face', methods=['POST'])
def get_face():
    # 用户名
    username = request.json.get('user')
    # 图片
    result = request.json.get('img').split(',')[1]
    if not (username and result):
        return jsonify(code=400, message='Missing parameter')
    # 图片格式转化
    img = processingFace.obtainImg(result)
    # 提取特征点
    mask_csv = processingFace.singlePictureProcessing(img)
    processingFace.storageCsv(username, mask_csv)
    judge = processingFace.judge(username)  # 获取的数据有两种可能1。当前录入数据条数，2。最终得到的结果
    # 录入没有完成，应该返回对应的进度数
    if not (type(judge) != dict):
        return jsonify(code=202, body=judge, message='continue')
    # 录取完成
    # 存储进mysql数据库
    MysqlOperation().get_face(username, judge)
    # 删除掉存储的所有特征(有点问题)
    os.remove('./face/' + username + '.csv')
    return jsonify(code=200, message='success')


if __name__ == '__main__':
    # 创建数据库
    app.run(host='0.0.0.0',port=5000)

