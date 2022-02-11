<template>
  <!-- 更改后的注册页面 -->
  <div id="registers">
    <div id="head">
      <h4>注册账号</h4>
      <div id="table_area">

        <div class="content">
          <span class="iconfont" ref="userhead">&#xe697;</span>
          <input type="text" placeholder="请输入账号" @blur="standard_user" v-model="user" ref="user"/>
        </div>
        <div class="tips" ref="username">规范用户名长度为6-12个任意字符</div>

        <div class="content">
          <span class="iconfont" ref="passwd">&#xe621;</span>
          <input type="text" placeholder="请输入密码" v-model="password" @blur="standard_password" ref="password"/>
        </div>
        <div class="tips" ref="pass">规范密码长度为6-12个任意字符</div>

        <div class="content">
          <span class="iconfont" ref="mailhead">&#xe908;</span>
          <input type="text" placeholder="请输QQ入邮箱" v-model="mail" @blur="standard_mail" ref="mailcontent"/>
        </div>
        <div class="tips" ref="mailtip">邮箱不能为空</div>

        <div class="content">
          <span class="iconfont">&#xe63c;</span>
          <input type="text" placeholder="请输入验证码" class="verification" v-model="code"/>
          <input type="button" class="sure" value="邮箱验证" @click="verified" ref="verified"/>
        </div>
        <div class="tips" style="text-align: right;"></div>

        <Button type="success" long style="margin-top: 18px;" @click="register">注册</Button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'register_modify',
  data () {
    return {
      // 用户名
      user: '',
      // 密码
      password: '',
      // 邮箱
      mail: '',
      // 验证码
      verificationCode: '',
      user_judge: false,
      passwd_judge: false,
      mail_judge: false,
      code: ''
    }
  },
  methods: {
    /* 判断用户名规范 */
    standard_user () {
      this.judge()
    },
    /* 用与请求邮箱验证码 */
    verified () {
      if (this.mail_judge) {
        // 加一个倒计时
        this.count_down()
        this.verification()
      } else {
        this.$Message.warning('请正确输入邮箱内容')
      }
    },
    /* 判断密码规范 */
    standard_password () {
      if (this.password.length < 6 || this.password.length > 12) {
        this.$refs.pass.style.opacity = 1
        this.$refs.passwd.style.color = 'red'
        this.$refs.passwd.style.borderBottom = '2px solid red'
        this.$refs.password.style.color = 'red'
        this.$refs.password.style.borderBottom = '2px solid red'
        this.passwd_judge = false
      } else {
        this.$refs.pass.style.opacity = 0
        this.$refs.passwd.style.color = '#fff'
        this.$refs.passwd.style.borderBottom = '2px solid #fff'
        this.$refs.password.style.color = '#fff'
        this.$refs.password.style.borderBottom = '2px solid #fff'
        this.passwd_judge = true
      }
    },
    /* 判断邮箱规范 */
    standard_mail () {
      if (this.mail === '' || this.mail === null) {
        this.$refs.mailtip.style.opacity = 1
        this.$refs.mailcontent.style.color = 'red'
        this.$refs.mailcontent.style.borderBottom = '2px solid red'
        this.$refs.mailhead.style.color = 'red'
        this.$refs.mailhead.style.borderBottom = '2px solid red'
        this.$refs.mailtip.innerHTML = '邮箱不能为空'
        this.mail_judge = false
      } else {
        let mailreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/
        if (!mailreg.test(this.mail)) {
          this.$refs.mailtip.style.opacity = 1
          this.$refs.mailcontent.style.color = 'red'
          this.$refs.mailcontent.style.borderBottom = '2px solid red'
          this.$refs.mailhead.style.color = 'red'
          this.$refs.mailhead.style.borderBottom = '2px solid red'
          this.$refs.mailtip.innerHTML = '请输入正确的邮箱格式'
          this.mail_judge = false
        } else {
          this.$refs.mailtip.style.opacity = 0
          this.$refs.mailcontent.style.color = '#fff'
          this.$refs.mailcontent.style.borderBottom = '2px solid #fff'
          this.$refs.mailhead.style.color = '#fff'
          this.$refs.mailhead.style.borderBottom = '2px solid #fff'
          this.mail_judge = true
        }
      }
    },
    /* 判断当前用户是否注册 */
    async judge () {
      let { data: res } = await this.$http.post('/judge_register', { user: this.user })
      if (res.body !== 'fail') {
        this.$refs.username.innerHTML = '用户名已注册请重新输入'
        this.$refs.username.style.opacity = 1
        this.$refs.user.style.color = 'red'
        this.$refs.user.style.borderBottom = '2px solid red'
        this.$refs.userhead.style.color = 'red'
        this.$refs.userhead.style.borderBottom = '2px solid red'
      } else {
        this.$refs.username.innerHTML = '规范用户名长度为6-12个任意字符'
        if (this.user.length < 6 || this.user.length > 12) {
          this.$refs.username.style.opacity = 1
          this.$refs.user.style.color = 'red'
          this.$refs.user.style.borderBottom = '2px solid red'
          this.$refs.userhead.style.color = 'red'
          this.$refs.userhead.style.borderBottom = '2px solid red'
          this.user_judge = false
        } else {
          this.$refs.username.style.opacity = 0
          this.$refs.user.style.color = '#fff'
          this.$refs.user.style.borderBottom = '2px solid #fff'
          this.$refs.userhead.style.color = '#fff'
          this.$refs.userhead.style.borderBottom = '2px solid #fff'
          this.user_judge = true
        }
      }
    },
    /* 发起邮箱验证 */
    async verification () {
      let { data: res } = await this.$http.post('/sendmail', { mail: this.mail })
      if (res.code === 200) {
        this.verificationCode = res.body
      } else {
        console.log(res.message)
      }
    },
    /* 注册成功,存储进数据库 */
    async uploads () {
      let { data: res } = await this.$http.post('/register_change', { user: this.user, password: this.password, mail: this.mail })
      if (res.code === 400) {
        console.log(res.message)
      }
    },
    register () {
      if (this.user_judge && this.passwd_judge && this.mail_judge) {
        if (this.code !== this.verificationCode) {
          this.$Message.warning('邮箱验证码错误')
        } else {
          this.uploads()
        }
      }
    },
    // 发起邮箱之后进入倒计时，60s内不可点击
    count_down () {
      // 基于当前时间加六十秒
      let end = 60 * 1000 + +new Date()
      let timer = setInterval(() => {
        let date = +new Date()
        let time = (end - date) / 1000
        let s = parseInt(time % 60)
        s = s >= 10 ? s : '0' + s
        this.$refs.verified.value = s
        this.$refs.verified.disabled = true
        if (s === '00') {
          clearInterval(timer)
          this.$refs.verified.value = '邮箱验证'
          this.$refs.verified.disabled = false
        }
      }, 1000)
      this.$once('hook:beforeDestroy', () => {
        clearInterval(timer)
        timer = null
      })
    }
  }
}
</script>

<style scoped lang="less">
#registers {
  background-image: url('../../assets/background/registe.png');
  width: 100%;
  height: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  overflow: hidden;
  position: relative;
  #head {
    width: 500px;
    height: 500px;
    background-color: rgba(28,23,54,0.5);
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    border-radius: 5px;
    box-shadow:0 15px 35px rgba(0,0,0,0.7),0 3px 10px rgba(0,0,0,0.7);
    h4 {
      text-align: center;
      padding-top: 45px;
      color: #fff;
    }
    /* 表单区域 */
    #table_area {
      width: 59%;
      height: 350px;
      margin: 20px auto 0;
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-end;
      align-content: flex-start;
      .tips {
        width: 100%;
        height: 20px;
        margin-top: 5px;
        opacity: 0;
        color: #fff;
        font-size: 12px;
        line-height: 20px;
        color: red;
      }
      .content {
        display: flex;
        color: black;
        margin-top: 15px;
        span {
          border-bottom: 2px solid #fff;
          height: 30px;
          line-height: 30px;
        }
        .sure {
          width: 50px;
          text-align: center;
          line-height: 30px;
          padding: 0;
          font-size: 12px;
          &:hover {
            color: #18BE6B;
          }
        }
        .verification {
          width: 115px;
        }
      }
      input{
        background:none;
        outline:none;
        border-bottom:2px solid #fff;
        border-top: 0;
        border-left: 0;
        border-right: 0;
        height: 30px;
        width: 275px;
        padding-left: 10px;
        color: #fff;
        font-size: 16px;
      }
      input::-webkit-input-placeholder {
        color: #fff;
        font-size: 14px;
      }
    }
  }
}
@font-face {
  font-family: 'iconfont';  /* Project id 3006776 */
  src: url('//at.alicdn.com/t/font_3006776_oc7ukqyk8ym.woff2?t=1640689181193') format('woff2'),
       url('//at.alicdn.com/t/font_3006776_oc7ukqyk8ym.woff?t=1640689181193') format('woff'),
       url('//at.alicdn.com/t/font_3006776_oc7ukqyk8ym.ttf?t=1640689181193') format('truetype');
}
.iconfont{
    font-family:"iconfont" !important;
    font-size:16px;
    font-style:normal;
    font-weight: 500;
    color:#fff;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
}
</style>
