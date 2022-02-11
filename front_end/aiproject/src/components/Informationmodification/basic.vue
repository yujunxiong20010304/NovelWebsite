<template>
  <!-- 基本信息修改 -->
  <div id="basic">
      <div>
        <span>账&nbsp;&nbsp;&nbsp;&nbsp;号:</span>
        <a-input v-model="user_info['name']" :disabled="change" @blur="survey"/>
      </div>
      <div>
        <span>密&nbsp;&nbsp;&nbsp;&nbsp;码:</span>
        <a-input v-model="user_info['password']" :disabled="change"/>
      </div>
      <div>
        <span>邮&nbsp;&nbsp;&nbsp;&nbsp;箱:</span>
        <a-input v-model="user_info['mailbox']" :disabled="change"/>
      </div>
      <div style="justify-content: space-around;">
        <Button type="success" ghost @click="modify">修改</Button>
        <Button type="info" ghost @click="upload">提交</Button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'basic',
  data () {
    return {
      user: '',
      user_info: {
        name: '用户名',
        password: '密码',
        mailbox: '邮箱'
      },
      change: true,
      username_judge: true
    }
  },
  methods: {
    async exit_login () {
      const { data: res } = await this.$http.post('/sign_out')
      location.reload()
      console.log(res)
    },
    survey () {
      this.judge_user()
    },
    // 查看当前用户的用户名
    async trial () {
      let { data: res } = await this.$http.post('/trial')
      this.user = res.username
      // 初始化页面时请求用户的相关信息进行展示
      this.obtain_user()
    },
    upload () {
      if (this.username_judge) {
        this.preservation_user()
        this.exit_login()
      }
    },
    // 请求用户的相关信息
    async obtain_user () {
      let { data: res } = await this.$http.post('/obtain_user', { user: this.user })
      if (res.code === 200) {
        this.user_info = res.body
      } else {
        console.log(res.message)
      }
    },
    // 判断用户名是否重复
    async judge_user () {
      let { data: res } = await this.$http.post('/judge_register', { user: this.user_info.name })
      if (res.body === 'success') {
        this.$Message.warning('用户名重复')
        this.username_judge = false
      } else {
        this.username_judge = true
      }
    },
    // 保存用户修改后的信息
    async preservation_user () {
      let { data: res } = await this.$http.post('/preservation_user', { user_info: this.user_info, user: this.user })
      if (res.code === 400) {
        console.log(res.message)
      }
    },
    // 修改
    modify () {
      this.change = false
    }
  },
  created () {
    // 初始化请求当前用户的用户名
    this.trial()
  }
}
</script>

<style scoped lang="less">
#basic {
  width: 50%;
  div {
    margin-top: 20px;
    display: flex;
    align-items: center;
    span {
      width: 50px;
      margin-right: 10px;
    }
  }
}
</style>
