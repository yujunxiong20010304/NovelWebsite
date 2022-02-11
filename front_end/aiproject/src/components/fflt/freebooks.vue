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
          <router-link style="color:white;" :to="{path:'/home/read',query:{num:0,type:i.category,name:i.title,author:i.author,time:i.updateTime}}">
            免费阅读
          </router-link>
        </div>
        <div style="color:#ff3955;border: 1px solid #ff3955;" @click="addBookshelf(i.title,i.category,i.author,i.chapter,i.updateTime)">加入书架</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'freebooks',
  data () {
    return {
      book_data: '',
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
      if (res.code === 200) {
        console.log(res.message)
      } else {
        console.log(res.message)
      }
    },
    /* 获取当前用户的session */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
    },
    async free () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游', '玄幻'], num: 2, amount: 54 }
      )
      if (res.code === 200) {
        this.book_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    }
  },
  created () {
    this.free()
    this.trial()
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
</style>
