<template>
  <!-- 图书数据的进一步展示 -->
  <div id="designatedbook">
    <!-- 书籍内容简介 -->
    <div id="designated" v-if="book[0]">
    <div id="works">
      <img :src="book[0].chart" alt="" />
      <div id="content">
        <h1>{{book[0].title}}</h1>
        <!-- 标签 -->
        <div id="label">
          <div style="margin-right: 10px;background-color: #1cb28a;">连载中</div>
          <div style="background-color: #d13153;">{{book[0].category}}</div>
        </div>
        <!-- 推荐指数 -->
        <div id="recommend">
          <span>字数</span>
          <i>29.2万</i>
          <span>总推荐</span>
          <i>3.9万</i>
          <span>总点击</span>
          <i>26.2万</i>
          <span>周推荐</span>
          <i>879</i>
        </div>
        <!-- 小说内容简介 -->
        <div id="brief_introduction">
          {{book[0].briefIntroduction}}
        </div>
        <!-- 最新信息 -->
        <div id="newest">
          <i>{{book[0].updateTime}}</i>
          <span>{{book[0].chapter}}</span>
        </div>
        <!-- 加入书架或者开始阅读 -->
        <div id="choice">
          <div style="background-color:#d13135;">
            <router-link
              :to="{path:'/home/read',query:{num:0,type:book[0].category,name:book[0].title,author:book[0].author,time:book[0].updateTime}}"
              style="text-decoration:none !important;color:#fff; ">
              开始阅读
            </router-link>
          </div>
          <div style="width:100px;color:#d13135;" @click="addBookshelf">加入书架</div>
        </div>
      </div>
    </div>

    <!-- 作者信息的面板 -->
    <div id="author">
      <!-- 作者信息 -->
      <div id="name">
        <!-- 头像 -->
        <div class="head_portrait" :style="{backgroundImage: 'url('+book[0].chart+')'}"></div>
        <span>签约作家</span>
        <h6>{{book[0].author}}</h6>
      </div>
      <!-- 作品信息 -->
      <div id="draft">
        <span>作品总数<i>1</i></span>
        <span style="border-left:1px solid #E6E6E6;border-right:1px solid #E6E6E6;">累计字数<i>29.2万</i></span>
        <span>本月更新<i>21天</i></span>
      </div>
      <!-- 作者自述 -->
      <div id="readme">
        <span>作者有话说</span>
        <p>我虽无意逐鹿，却知苍生疾苦</p>
      </div>
    </div>
  </div>
    <!-- 章节列表 -->
    <div id="chapter_list">
      <ul>
        <li v-for="(i,index) in chapter_list" :key="i.id">
          <router-link :to="{path:'/home/read',query:{num:index,type:book[0].category,name:book[0].title,author:book[0].author,time:book[0].updateTime}}">
          {{i.name}}
          </router-link>
        </li>
      </ul>
    </div>
    <ending></ending>
  </div>
</template>

<script>
export default {
  name: 'designatedBook',
  data () {
    return {
      name: '', // 小说名字
      type: '', // 小说类型
      chapter_list: '', // 章节列表
      book: '', // 这本书的所有信息
      first: '', // 感觉没卵用
      user: '' // 判断当前用户是否登录
    }
  },
  methods: {
    addBookshelf () {
      /* 加入书架前的两部操作 1。获取session判断是否登录，2。保存到书架 */
      if (this.user) {
        this.addBookcase()
      } else {
        console.log('请登录')
      }
    },
    /* 获取当前用户的session,无用 */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
    },
    /* 保存到书架 */
    async addBookcase () {
      const { data: res } = await this.$http.post(
        '/addBookcase',
        {
          user: this.user, // 用户名
          book_name: this.book[0].title, // 小说名
          book_type: this.book[0].category, // 小说类型
          book_author: this.book[0].author, // 小说作者
          book_new_chapter: this.book[0].chapter, // 小说最新章节
          book_old_chapter: '未读', // 当前阅读状态
          updatetime: this.book[0].updateTime // 当前更新的最新时间
        })
      if (res.code === 200) {
        console.log(res.message)
      } else {
        console.log(res.message)
      }
    },
    async get_data () {
      const { data: res } = await this.$http.get('/chapter', { params: { type: this.type, name: this.name } })
      console.log(res)
      if (res.code === 200) {
        this.chapter_list = res.body[1]
        this.book = res.body[0]
        this.first = res.body[1][0].sequence
      } else {
        console.log(res.message)
      }
    }
  },
  created () {
    this.type = this.$route.query.type
    this.name = this.$route.query.name
    this.user = this.$store.state.session_name
    this.get_data()
  }
}
</script>

<style scoped lang="less">
#designated {
  width: 1200px;
  height: 300px;
  border-bottom: 1px dashed skyblue;
  display: flex;
  margin: 15px auto 0;
  justify-content: space-between;
  #works {
    width: 923px;
    height: 292px;
    display: flex;
    justify-content: space-between;
    img {
      width: 200px;
      height: 264px;
      border-radius: 5px;
    }
    #content {
      width: 697px;
      height: 262px;
      /* 小说标签 */
      h1 {
        font-size: 24px;
        color: #333;
        font-weight: 700;
      }
      #label {
        width: 100%;
        height: 20px;
        margin-top: 5px;
        div {
          display: inline-block;
          background-color: snow;
          border-radius: 2px;
          width: 66px;
          text-align: center;
          color: white;
          line-height: 20px;
          height: 20px;
        }
      }
      /* 推荐指数 */
      #recommend {
        width: 100%;
        height: 22px;
        margin-top: 5px;
        span {
          color: #999;
          font-size: 12px;
          line-height: 22px;
          margin-right: 5px;
        }
        i {
          font-style:normal;
          font-size: 16px;
          font-weight: 400;
          color: #333;
          line-height: 22px;
          margin-right: 20px;
        }
      }
      /* 小说内容简介 */
      #brief_introduction {
        width: 100%;
        height: 80px;
        font-size: 14px;
        color: #333;
        margin-top: 5px;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp:4;
        -webkit-box-orient: vertical;
      }
      /* 最新数据 */
      #newest {
        width: 100%;
        height: 25px;
        margin-top: 20px;
        i {
          margin-right: 15px;
          font-style: normal;
          line-height: 25px;
        }
      }
      /* 阅读还是加入书架 */
      #choice {
        width: 100%;
        height: 36px;
        margin-top: 17px;
        div {
          width: 180px;
          height: 36px;
          margin-right: 10px;
          display: inline-block;
          text-align: center;
          line-height: 36px;
          border-radius: 3px;
          border: 1px solid #d13135;
          color: #fff;
        }
      }
    }
  }
  #author {
    width: 225px;
    height: 282px;
    background-color: #f5f5f5;
    #name {
      width: 100%;
      height: 95px;
      position: relative;
      .head_portrait {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        margin: 15px auto 0;
        background-image: url('http://static.zongheng.com/upload/cover/0b/fb/0bfbdc4a009c6a2c0f8359fdf99b0457.jpeg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
      }
      span {
        background-color: #fa7423;
        border-radius: 3px;
        color: #fff;
        display: block;
        width: 60px;
        height: 20px;
        font-size: 12px;
        font-weight: 400;
        text-align: center;
        line-height: 20px;
        position: absolute;
        left: 50%;
        transform: translate(-50%, -50%);
      }
      h6 {
        text-align: center;
        margin-top: 20px;
        color: #333;
        font-size: 14px;
        font-weight: 700;
      }
    }
    #draft {
      text-align: center;
      margin-top: 10px;
      span {
        display: inline-block;
        width: 74px;
        height: 40px;
        text-align: center;
        font-size: 12px;
        color: #999;
        padding: 0 12px;
        i {
          font-style: normal;
          color: #666;
          font-size: 14px;
          font-weight: 400;
        }
      }
    }
    #readme {
      width: 195px;
      margin: 15px auto 0;
      span {
        font-size: 12px;
        color: #999;
        font-weight: 400;
      }
      p {
        color: #333;
        font-size: 12px;
      }
    }
  }
}
#chapter_list {
  margin: 20px auto 0;
  width: 1200px;
  background-color: #f5f5f5;
  border-radius: 5px;
  padding: 20px;
  ul {
    display: flex;
    list-style: none;
    flex-wrap: wrap;
    justify-content: flex-start;
    li {
      width: 305px;
      height: 40px;
      line-height: 40px;
      text-align: left;
      border-bottom: 1px dashed #ddd;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin: 0 40px;
    }
  }
}
</style>
