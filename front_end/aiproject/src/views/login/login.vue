<template>
  <!-- 登录页面 -->
  <div id="home">
    <div id="content">
      <div id="choice">
          <router-link to="/login/passwordlogin"><div @mouseover="openMoon" @mouseout="closeMoon" ref="password" id="ss">密码登录</div></router-link>
          <router-link to="/login/faceslogin"><div @mouseover="openMoon" @mouseout="closeMoon" ref="faces">人脸登录</div></router-link>
      </div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  methods: {
    openMoon (e) {
      e.target.style.color = '#11884D'
      e.target.style.boxShadow = '0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.7)'
    },
    closeMoon (e) {
      e.target.style.color = ''
      e.target.style.boxShadow = ''
    },
    switchcolor () {
      this.$nextTick(() => {
        if (this.$route.path === '/login/passwordlogin') {
          this.$refs.password.style.backgroundColor = 'white'
          this.$refs.faces.style.backgroundColor = ''
        } else if (this.$route.path === '/login/faceslogin') {
          this.$refs.faces.style.backgroundColor = 'white'
          this.$refs.password.style.backgroundColor = ''
        }
      })
    }
  },
  watch: {
    $route: {
      handler () {
        this.switchcolor()
      },
      immediate: true
    }
  }
}
</script>

<style scoped lang="less">
#home {
  background-image: url('../../assets/background/login.jpg');
  width: 100%;
  height: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  overflow: hidden;
  #content {
    width: 400px;
    background-color: rgba(255,255,255,.2);
    height: 345px;
    margin: 100px auto 0;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    border-radius: 10px;
    box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.5);
    #choice {
      width: 100%;
      height: 55px;
      font-size: 18px;
      line-height: 55px;
      display: flex;
      background-color: rgba(255,255,255,.5);
      font-weight: 800;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      border-bottom: 1px solid #C1C1C1;
      text-align: center;
      border-top-right-radius: 5px;
      border-top-left-radius: 5px;
      overflow: hidden;
      box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.07);
      a {
        width: 100%;
        color: #57839E;
        div {
          width: 100%;
          height: 100%;
        }
      }
    }
  }
}
</style>
