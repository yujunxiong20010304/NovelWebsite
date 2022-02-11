<template>
  <div id="freebooks">
    <div class="book" v-for="i in book_data" :key="i.id">
      <router-link :to="{path:'/home/designatedBook',query:{type:i.category,name:i.title}}">
        <img :src="i.chart" alt=""/>
      </router-link>
      <div id="content">
        <span style="font-size:20px;font-weight: bold;">
          <router-link style="color:initial;" :to="{path:'/home/designatedBook',query:{type:i.category,name:i.title}}">
            {{i.title}}
          </router-link>
        </span>
        <span style="font-size:12px;color:#B4B4B4;"><span>{{i.author}}</span> | <span>{{i.category}}</span></span>
        <span class = "limit" style="font-size:12px;margin-top:10px;">
          {{i.briefIntroduction}}
        </span>
        <div class="lately">
          <span style="font-size:12px;color:#B4B4B4;">{{i.updateTime}}</span>
          <span style="font-size:12px;margin-left: 25px;color:#2972cc;">{{i.chapter}}</span>
        </div>
      </div>
      <div class="choice">
        <div style="background-color: #ff3955;color: #fff;">
          <router-link
              :to="{path:'/home/read',query:{num:0,type:i.category,name:i.title,author:i.author,time:i.updateTime}}"
              style="text-decoration:none !important;color:#fff; ">
          免费阅读
          </router-link>
        </div>
        <div style="color:#ff3955;border: 1px solid #ff3955;" @click="addBookshelf(i.title,i.category,i.author,i.chapter,i.updateTime)">加入书架</div>
      </div>
    </div>
    <BackTop><div class="iconfont" style="font-size:40px;color: deepskyblue;">&#xe7d9;</div></BackTop>
  </div>
</template>

<script>
export default {
  name: 'query',
  data () {
    return {
      book_data: '',
      query: '',
      user: '' // 当前用户
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
    /* 获取当前用户的session */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
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
      if (res.code === 200) {
        console.log(res.message)
      } else {
        console.log(res.message)
      }
    },
    async search () {
      const { data: res } = await this.$http.get('/query', { params: { search: this.query } })
      if (res.code === 200) {
        this.book_data = res.body
      } else {
        console.log(res.message)
      }
    }
  },
  created () {
    this.query = this.$route.query.search
    this.search()
    this.user = this.$store.state.session_name
  },
  watch: {
    $route: {
      handler (val, oldVal) {
        this.query = this.$route.query.search
        this.search()
      },
      immediate: true
    }
  }
}
</script>

<style scoped lang="less">
#freebooks {
  width: 100%;
  background-color: #fff;
  height: 100%;
  overflow: hidden;
  .book {
    width: 980px;
    height: 158px;
    margin: 20px auto 0;
    padding-bottom: 22px;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    .choice {
      width: 98px;
      margin-left: 65px;
      div {
        width: 98px;
        height: 32px;
        border-radius: 32px;
        text-align: center;
        line-height: 32px;
        margin-top: 20px;
      }
    }
    #content {
      margin-left: 20px;
      display: flex;
      flex-wrap: wrap;
      width: 686px;
      .lately {
        width: 100%;
        margin-top: 20px;
      }
      .limit {
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2;
        height: 39px;
      }
      span {
        width: 100%;
      }
    }
    img {
      width: 102px;
      height: 136px;
    }

  }
}
.iconfont{
  font-family:"iconfont" !important;
  font-size:16px;font-style:normal;
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: 0.2px;
  -moz-osx-font-smoothing: grayscale;
}
.topic {
  font-weight: bold;
  font-size: 24px;
  padding-left: 55px;
  padding-top: 35px;
}
</style>
