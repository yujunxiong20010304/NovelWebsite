<template>
  <div id="read" :style="{backgroundColor:info.behindColor}">
    <!-- 侧边导航 -->
    <sidenavigation :info="info" v-if="content[0]"></sidenavigation>
    <!-- 展示小说内容 -->
    <div id="exhibition" :style="{backgroundColor:info.backcolor}" v-if="content[0]">
      <!-- 章节标题内容 -->
      <div id="topic_conversation">
        <h3>{{content[0]['name']}}</h3>
        <span>{{this.author}}</span>
        <span style="border-left:1px solid #999;border-right: 1px solid #999;">字数：2022</span>
        <span>{{this.time}}</span>
      </div>
      <!-- 小说内容 -->
      <div id="content" :style="{fontSize: info.characterSize+'px'}">
        {{ content[0]['content'] }}
      </div>
      <!-- 选择是下一章还是上一章 -->
      <div id="direction">
        <div style="width:144px;">目录</div>
        <router-link :to="{path:'/home/read/',query:{num:this.serial_number,type:this.type,name:this.name,author:this.author,time:this.time}}" replace>
          <div style="width:144px;" @click=reduce>上一章</div>
        </router-link>
        <router-link :to="{path:'/home/read',query:{num:this.serial_number,type:this.type,name:this.name,author:this.author,time:this.time}}" replace>
          <div style="width:292px;" @click=plus>下一章</div>
        </router-link>
        <!--<div style="width:144px;" @click=reduce>上一章</div>
        <div style="width:292px;" @click=plus>下一章</div>-->
      </div>
    </div>
  </div>
</template>

<script>
import sidenavigation from '@/components/read/sidenavigation'
export default {
  name: 'read',
  data () {
    return {
      /* 小说类型 */
      type: '',
      /* 小说名字 */
      name: '',
      /* 作者的名字 */
      author: '',
      /* 最后更新的时间 */
      time: '',
      /* 小说展示内容 */
      content: '',
      info: { behindColor: '#D9CDB6', backcolor: '#FAEED7', characterSize: 14 },
      first: ['#D9CDB6', '#FAEED7', 14],
      /* 当前小说的序列号 */
      serial_number: '',
      user: ''
    }
  },
  components: {
    sidenavigation
  },
  methods: {
    /* 获取当前用户的session，并需要做判断是否登录 */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
    }, /* 更新书架中的历史数据 */
    async updateHistory () {
      let { data: res } = await this.$http.get('/update_history', { params: { num: this.serial_number, chapter: this.content[0].name, user: this.user, name: this.name } })
      if (res.code === 400) {
        console.log(res.message)
      }
    },
    async switch_page () {
      const { data: res } = await this.$http.get('/content', { params: { type: this.type, name: this.name, page: this.serial_number } })
      if (res.code === 200) {
        this.content = res.body
      }
      if (!res.body[0]) {
        this.$router.back()
      }
    },
    plus () {
      this.serial_number++
      this.switch_page()
      window.scrollTo(0, 0)
      if (this.user) {
        this.updateHistory()
      } else {
        console.log('请登录')
      }
    },
    reduce () {
      this.serial_number--
      this.switch_page()
      window.scrollTo(0, 0)
      if (this.user) {
        this.updateHistory()
      } else {
        console.log('请登录')
      }
    },
    setting () {
      /* 保存历史背景和字体进入本地存储 */
      window.sessionStorage.setItem('initial', this.first)
      /* 如果存在最新值 */
      let newVal = window.sessionStorage.getItem('present')
      if (newVal) {
        let list = newVal.split(',')
        if (newVal.indexOf('#') !== -1) {
          this.info.behindColor = list[0]
          this.info.backcolor = list[1]
          this.info.characterSize = list[2] + ''
        } else {
          this.info.behindColor = list[0] + list[1] + list[2]
          this.info.backcolor = list[3] + list[4] + list[5]
          this.info.characterSize = list[6] + ''
        }
      } else {
        this.info.behindColor = this.first[0]
        this.info.backcolor = this.first[1]
        this.info.characterSize = this.first[2]
      }
    }
  },
  created () {
    this.type = this.$route.query.type
    this.name = this.$route.query.name
    this.author = this.$route.query.author
    this.time = this.$route.query.time
    this.serial_number = this.$route.query.num
    this.switch_page()
    this.setting()
    this.user = this.$store.state.session_name
  }
}
</script>

<style scoped lang="less">
#read {
  overflow: hidden;
}
#exhibition {
  width: 900px;
  border: 1px solid #ccc;
  margin: 50px auto 50px;
  #direction {
    width: 100%;
    height: 50px;
    display: flex;
    justify-content: center;
    margin: 50px 0;
    div {
      height: 50px;
      line-height: 50px;
      text-align: center;
      border:1px solid #CCCCCC;
      margin-right: 10px;
      &:hover {
        color: crimson;
        border:1px solid crimson;
      }
    }
  }
  #topic_conversation {
    width: 80%;
    text-align: center;
    height: 100px;
    border-bottom: 1px dashed #ccc;
    margin: 50px auto 0;
    h3 {
      font-size: 28px;
      color: #333;
      font-weight: 700;
    }
    span {
      display: inline-block;
      margin-top: 10px;
      color: #999;
      padding: 0 10px;
      height: 13px;
      line-height: 13px;
    }
  }
  #content {
    width: 80%;
    margin: 45px auto 0;
  }
}
</style>
