# 数据库操作
from redis import *
import settings
import pymysql
import random
# 连接mysql数据库，获取数据库中存储的图书信息
class MysqlOperation(object):
    def __init__(self):
        self.conn = pymysql.connect(host=settings.Ip, port=settings.MysqlPort, user=settings.User,
                                    password=settings.Password,
                                    database=settings.Database_User, cursorclass=pymysql.cursors.DictCursor)


    # 保存注册信息,参数name:用户名，password:密码，face:人脸信息
    def register(self,name,password,face):
        # 创建游标对象
        cur = self.conn.cursor()
        # sql 语句
        sql = 'insert into user (name,password,face) values ("{}","{}","{}")'.format(name,password,str(list(face)))
        res = cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    # 登录
    def login(self):
        # 创建游标对象
        cur = self.conn.cursor()
        # sql 语句
        sql = 'select name,face from user'
        res = cur.execute(sql)
        data = cur.fetchall()
        name_list = []
        face_list = []
        for i in data:
            if i.get('face'):
                name_list.append(i['name'])
                face_list.append(eval(i['face']))
        return [name_list,face_list]




    # 参数：取的数据条数，取的数据是否有跳动，只获取图书表面信息
    def get_population(self,novel_list,*args):
        # 创建游标对象
        cur = self.conn.cursor()
        # 图书列表
        book_list = []
        for i in novel_list:
            if len(args)==1:
                if i=='全部':
                    sql = 'select * from book limit {}'.format(args[0])
                else:
                    sql = 'select * from book where category="{}" limit {}'.format(i, args[0])
            elif len(args)==2:
                if i=='全部':
                    sql = 'select * from book limit {} offset {} '.format(args[0], args[1])
                else:
                    sql = 'select * from book where category="{}" limit {} offset {} '.format(i, args[0], args[1])
            res = cur.execute(sql)
            data = cur.fetchall()
            book_list += data
        return book_list

    def book_list_number(self,type):
        cur = self.conn.cursor()
        if type == '全部':
            sql = 'select count(id) from book'
        else:
            sql = 'select count(id) from book where category="{}"'.format(type)
        res = cur.execute(sql)
        data = cur.fetchone()
        return data['count(id)']

    # 获取小说信息外以及小说章节信息,type:小说类型,name:小说的名字
    def second_level_book_data(self,type,name):
        cur = self.conn.cursor()
        sql_chapter = 'select id,name,sequence from chapter where title="{}"'.format(name)
        res = cur.execute(sql_chapter)
        chapter_data = cur.fetchall()
        chapter_data.sort(key=lambda chapter: chapter['sequence'])
        sql_book = 'select * from book where title="{}"'.format(name)
        res = cur.execute(sql_book)
        book_data = cur.fetchall()
        book_data = data_clean(book_data, [])
        return [book_data,chapter_data]

    # 获取指定小说的章节内容,type:小说类型，name：小说名字,page 是小说的序列号
    def chapter_content(self,type,name,page):
        cur = self.conn.cursor()
        sql = 'select content,sequence,title,name from chapter where title="{}" order by sequence limit 1 offset {}'.format(name,page)
        print(sql)
        res = cur.execute(sql)
        chapter_data = cur.fetchall()
        # 去除指定字符串 亲点击进去给个好评呗分数越高更新越快据说给新笔趣阁打满分的最后都找到了漂亮的老婆哦手机站全新改版升级地址：https:wapxbiqugela，数据和书签与电脑站同步，无广告清新阅读！
        return chapter_data
    # 查询小说,参数是查询的名字，可能是作者名可能是小说名
    def query(self,search):
        cur = self.conn.cursor()
        sql = 'select DISTINCT * from book where title like "%{}%" or author like "%{}%"'.format(search,search)
        print(sql)
        res = cur.execute(sql)
        data = cur.fetchall()
        return data
    # 匹配数据库中的用户名和密码
    def matching(self,username,password):
        cur = self.conn.cursor()
        sql = 'select name,password from user where name="{}" and password="{}"'.format(username,password)
        res = cur.execute(sql)
        result = cur.fetchone()
        return result
    # 添加书架
    # user 用户名
    # book_name 小说名字
    # book_type 小说类型
    # book_author 小说作者
    # book_new_chapter 小说最新章节
    # book_old_chapter 当前的阅读状态
    def add_bookcase(self,user,book_name,book_type,book_author,book_new_chapter,book_old_chapter,updatetime):
        cur = self.conn.cursor()
        # 首先需要知道当前用户的id
        sql_id = 'select id from user where name="{}"'.format(user)
        res = cur.execute(sql_id)
        result = cur.fetchone()
        sql = '''insert into bookshelf(book_name,book_type,book_author,book_new_chapter,book_old_chapter,user_id,updatetime)
                    values ("{}","{}","{}","{}","{}",{},"{}")'''.\
                    format(book_name,book_type,book_author,book_new_chapter,book_old_chapter,result['id'],updatetime)
        res = cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    # 查询书架中的对应信息
    # user 用户的名字,page当前的页码
    def getBookshelf(self,user,page):
        cur = self.conn.cursor()
        sql = 'select * from bookshelf where user_id=(select id from user where name="{}") limit 8 offset {}'.format(user,(page-1)*8)
        res = cur.execute(sql)
        result = cur.fetchall()
        sql_num = 'select count(*) from bookshelf where user_id=(select id from user where name="{}")'.format(user)
        res = cur.execute(sql_num)
        num = cur.fetchone()
        return [result,num]
    # 删除书架中的信息
    def delete(self,ids):
        cur = self.conn.cursor()
        for i in ids:
            sql = 'DELETE FROM bookshelf WHERE book_id={}'.format(i)
            res = cur.execute(sql)
            self.conn.commit()
    # 更新书架中的信息
    def update_history(self,num,chapter,user,name):
        cur = self.conn.cursor()
        sql = 'update bookshelf set num={},book_old_chapter="{}" where user_id=(select id from user where name="{}") and book_name="{}"'.format(num,chapter,user,name)
        res = cur.execute(sql)
        self.conn.commit()
        print(sql)

    # 判断这个用户名是否已被注册
    def judge_register(self,user):
        cur = self.conn.cursor()
        sql = 'select name from user where name="{}"'.format(user)
        res = cur.execute(sql)
        result = cur.fetchone()
        return result
    # 邮箱验证码的方式进行账号的注册
    def register_change(self,name,password,mailbox):
        cur = self.conn.cursor()
        sql = 'insert into user(name,password,mailbox) values ("{}","{}","{}")'.format(name,password,mailbox)
        res = cur.execute(sql)
        self.conn.commit()
    # 获取用户的相关信息进行展示
    def obtain_user(self,name):
        cur = self.conn.cursor()
        sql = 'select name,password,mailbox from user where name="{}"'.format(name)
        res = cur.execute(sql)
        result = cur.fetchone()
        print(result)
        return result
    # 对用户修改信息后进行一个保存
    def preservation_user(self,new_user,new_password,new_mailbox,old_user):
        cur = self.conn.cursor()
        sql = 'update user set name="{}",password="{}",mailbox="{}" where name="{}"'.format(new_user,new_password,new_mailbox,old_user)
        res = cur.execute(sql)
        self.conn.commit()
    # 保存用户头像进数据库
    def storage_image(self,name,image):
        cur = self.conn.cursor()
        sql = 'update user set image="{}" where name="{}"'.format(image,name)
        res = cur.execute(sql)
        self.conn.commit()
    # 获取用户头像
    def get_image(self,user):
        cur = self.conn.cursor()
        sql = 'select image from user where name="{}"'.format(user)
        res = cur.execute(sql)
        result = cur.fetchone()
        return result
    # 存储人脸的录入数据
    def get_face(self,username,judge):
        # 创建游标对象
        cur = self.conn.cursor()
        # sql 语句
        sql = 'update user set face="{}" where name="{}"'.format(str(list(judge)),username)
        res = cur.execute(sql)
        self.conn.commit()
        self.conn.close()
# 数据清洗，清洗作者名字，以及在小说简介中的空白行
def data_clean(data, breakdown):
    for i in data:
        i['author'] = i['author'].replace('\xa0', '')
        i['briefIntroduction'] = i['briefIntroduction'].replace(' ', '')
    random.shuffle(data)
    result = []
    lists = []
    if not breakdown:
        return data
    for i in data:
        lists.append(i)
        if len(lists) == breakdown:
            result.append(lists)
            lists = []
    return result



if __name__ == '__main__':
    test = MysqlOperation()
    test.login()
