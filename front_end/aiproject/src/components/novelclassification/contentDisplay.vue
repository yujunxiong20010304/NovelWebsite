<template>
  <div>
    <div id="contentDisplay">
    <div class="book" v-for="i in book_list" :key="i.id">
      <router-link :to="{path:'/home/designatedBook',query:{type:i.category,name:i.title}}">
        <div class="image" :style="{backgroundImage:'url(' + i.chart + ')'}"></div>
      </router-link>
      <div class="content">
          <span style="color:#333;font-size: 16px;font-weight: bold;">
            <router-link style="color:initial;" :to="{path:'/home/designatedBook',query:{type:i.category,name:i.title}}">
              {{i.title}}
            </router-link>
          </span>
          <span style="color:#777;font-size: 12px;">{{i.author}}</span>
          <span class="introduce">{{i.briefIntroduction}}</span>
          <span class="category">{{i.category}}</span>
          <div class="choice" @click="addBookshelf(i.title,i.category,i.author,i.chapter,i.updateTime)">加入书架</div>
        </div>
      </div>
    </div>
    <div id="paging">
      <a-pagination :default-current="1" :total="num*10" v-model="current" @change="jump_page"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'contentDisplay',
  data () {
    return {
      current: 1, /* 当前所在页 */
      book_list: '', /* 每一页的书籍内容 */
      num: ''/* 总共的页数 */,
      routes: ''/* 当前的路由路径 */,
      /* 路由与请求参数的映射 */
      corresponding: {
        '/home/novelclassification/whole': ['全部'],
        '/home/novelclassification/fantasy': ['玄幻'],
        '/home/novelclassification/xiuzhen': ['修真'],
        '/home/novelclassification/urban': ['都市'],
        '/home/novelclassification/pass_through': ['穿越'],
        '/home/novelclassification/online_games': ['网游'],
        '/home/novelclassification/science_fiction': ['科幻']
      },
      user: ''
    }
  },
  methods: {
    addBookshelf (title, category, author, chapter, updateTime) {
      /* 加入书架前的两部操作 1。获取session判断是否登录，2。保存到书架 */
      if (this.user) {
        this.addBookcase(title, category, author, chapter, updateTime)
      } else {
        console.log('请登录')
      }
    },
    /* 保存到书架 */
    async addBookcase (title, category, author, chapter, updateTime) {
      const { data: res } = await this.$http.post(
        '/addBookcase',
        {
          user: this.user, // 用户名
          book_name: title, // 小说名
          book_type: category, // 小说类型
          book_author: author, // 小说作者
          book_new_chapter: chapter, // 小说最新章节
          book_old_chapter: '未读', // 当前阅读状态
          updatetime: updateTime
        })
      console.log(res)
    },
    /* 获取当前用户的session */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
    },
    async get_data_book () {
      const { data: res } = await this.$http.post('/novel', {
        type: this.corresponding[this.routes], num: 20, judge: 'quantity', amount: (this.current - 1) * 20
      })
      if (res.code === 200) {
        this.book_list = res.body.data
        this.num = res.body.number
      } else {
        console.log('参数不齐全')
      }
    },
    jump_page () {
      this.get_data_book()
    }
  },
  watch: {
    $route: {
      handler: function (val) {
        this.current = 1
        this.routes = val.path
        this.get_data_book()
      },
      immediate: true
    }
  },
  created () {
    this.user = this.$store.state.session_name
  }
}
</script>

<style scoped lang="less">
#paging {
  margin: 30px auto 0;
  width: 435px;
  height: 35px;
}
#contentDisplay {
  width: 1150px;
  background-color: #fff;
  margin: 20px auto 0;
  border-radius: 5px;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  .book {
    width: 520px;
    height: 146px;
    margin: 20px 24px;
    display: flex;
    border-bottom: 1px solid #e8e8e8;
    .content {
      display: flex;
      width: 428px;
      flex-wrap: wrap;
      margin-left: 12px;
      position: relative;
      height: 114px;
      span {
        width: 100%;
      }
      .choice {
        width: 100px;
        height: 30px;
        background-color: white;
        text-align: center;
        line-height: 30px;
        position: absolute;
        bottom: -15px;
        right: 0;
        box-shadow:0 15px 35px rgba(0,0,0,0.09),0 3px 10px rgba(0,0,0,0.09);
        border-radius: 5px;
        &:hover {
          background-color: lightseagreen;
          color: #fff;
        }
      }
      .category{
        height: 23px;
        width: 53px;
        background-color: lightseagreen;
        text-align: center;
        line-height: 23px;
        border-radius: 5px;
        font-size: 12px;
        color: white;
      }
      .introduce {
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        height: 42px;
        font-size: 13px;
      }
    }
    .image {
      min-width: 80px;
      min-height: 120px;
      max-height: 80px;
      max-height: 120px;
      border-radius: 7px;
      position: relative;
      background-image: url('https://www.xbiquge.la/files/article/image/90/90025/90025s.jpg');
      background-position: center;
      background-size: cover;
      background-repeat: no-repeat;
      border: 1px solid #333;
      box-shadow:0 15px 35px rgba(0,0,0,0.09),0 3px 10px rgba(0,0,0,0.09);
      &:after {
        content: ' ';
        background-image: url('../../assets/bookedge.png');
        width: 13px;
        height: 118px;
        display: block;
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
        position: absolute;
        right: -1px;
        border-radius: 7px;
      }
    }
  }
}
</style>
