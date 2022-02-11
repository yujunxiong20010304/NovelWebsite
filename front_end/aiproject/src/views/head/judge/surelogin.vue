<template>
  <div id="surelogin" @mouseover="getout" @mouseout="comeback" ref="human" @click="exit_login">
    <div class="head_portrait" :style="{backgroundImage:'url('+this.img_old+')'}" v-if="this.img_old"></div>
    <div class="head_portrait" :style="{backgroundImage:'url('+this.img['image']+')'}" v-else-if="this.img['image']"></div>
    <!-- :style="{backgroundImage:'url('+this.img+')'}" -->
    <div class="head_portrait" v-else></div>
    <span style="font-size:14px;">{{user}}</span>
    <Icon type="ios-arrow-forward" style="font-size:25px;line-height:60px;" id="move" ref="yi"/>
  </div>
</template>

<script>
export default {
  name: 'surelogin',
  data () {
    return {
      user: '',
      img: '../../../assets/background/register.jpeg',
      img_old: ''
    }
  },
  methods: {
    async image () {
      const { data: res } = await this.$http.get('/image', { params: { user: this.user } })
      if (res.code === 200) {
        this.img = res.body
      } else {
        console.log(res.message)
      }
      this.local_storage()
      console.log(res)
    },
    exit_login () {
      this.signup()
      this.clear_storage()
      location.reload()
    },
    async signup () {
      const { data: res } = await this.$http.post('/sign_out')
      console.log(res)
      location.reload()
    },
    getout () {
      let move = document.querySelector('#move')
      move.style.transition = 'right .5s'
      move.style.right = '-28px'
      this.$refs.human.style.backgroundColor = '#DCDEE2'
    },
    comeback () {
      let move = document.querySelector('#move')
      move.style.right = '0'
      move.style.transition = 'all .5s'
      this.$refs.human.style.backgroundColor = 'white'
    },
    /* 获取session */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
    },
    /* 保存头像到本地 */
    local_storage () {
      sessionStorage.setItem('head_portrait', this.img.image)
    },
    /* 获取本地的头像 */
    get_storage () {
      this.img_old = sessionStorage.getItem('head_portrait')
    },
    /* 清除本地的头像 */
    clear_storage () {
      sessionStorage.removeItem('head_portrait')
    }
  },
  created () {
    this.user = this.$store.state.session_name
    this.get_storage()
    this.image()
  }
}
</script>

<style scoped lang="less">
#surelogin {
  min-width: 135px;
  max-width: 200px;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  .head_portrait {
    height: 45px;
    width: 45px;
    background-image: url("../../../assets/background/register.jpeg");
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    display: inline-block;
    border-radius: 5px;
  }
  #move{
    position: relative;
    right: 0;
  }
}
</style>
