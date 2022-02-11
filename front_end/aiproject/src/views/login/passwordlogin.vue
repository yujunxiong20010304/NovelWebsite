<template>
  <div id="login">
      <div id="Input">
        <span>用户名<a-input placeholder="username" v-model="username"></a-input></span>
        <span>密&nbsp;&nbsp;&nbsp;&nbsp;码<a-input placeholder="password" v-model="password"></a-input></span>
      </div>
      <div id="Jump">
        <router-link to="/register" style="color:#fff;">找回密码</router-link>
        <router-link to="/register" style="color:#fff;">注册</router-link>
      </div>
      <div id="choiceInto">
        <Button type="success" ghost @click="login">登录</Button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'passwordlogin',
  data () {
    return {
      username: '',
      password: '',
      user: ''
    }
  },
  methods: {
    /* 登录按钮 */
    login () {
      this.LoginRequest()
    },
    /* 密码登录请求 */
    async LoginRequest () {
      const { data: res } = await this.$http.post('/passwordlogin', { username: this.username, password: this.password })
      console.log(res)
      /* 登录成功 */
      if (res.code === 200) {
        this.$router.push({ path: '/home/bookcity' })
      /* 登录失败 */
      } else {
        console.log('登录失败，请重新输入密码')
      }
    },
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
      if (this.user) {
        this.$router.push({ path: '/home/bookcity' })
      }
    }
  },
  created () {
    this.trial()
  }
}
</script>

<style scoped lang="less">
#login {
  width: 300px;
  margin: 30px auto 0;
  #Input {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    height: 140px;
    span {
      width: 100%;
      color: white;
    }
  }
  #choiceInto {
    display: flex;
    width: 80%;
    justify-content: space-around;
    margin: 20px auto 0;
  }
  button {
    width: 220px;
    height: 35px;
  }
  #Jump {
    display: flex;
    justify-content: space-between;
  }
}
</style>
