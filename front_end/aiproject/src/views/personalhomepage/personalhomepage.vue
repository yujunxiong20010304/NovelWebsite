<template>
  <!-- 我的书架 -->
  <div id="mybookcity">
    <div id="navigation">
      <router-link to="/home/mybookcity/personalbookshelf"><div ref="mybookcity">我的书架</div></router-link>
      <router-link to="/home/mybookcity/Informationmodification"><div ref="personalbookshelf">个人信息</div></router-link>
      <div>退出登录</div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'mybookcity',
  watch: {
    $route: {
      handler (val) {
        this.$nextTick(() => {
          if (val.path === '/home/mybookcity/Informationmodification') {
            this.$refs.personalbookshelf.style.backgroundColor = 'lightseagreen'
            this.$refs.personalbookshelf.style.color = 'white'
            this.$refs.mybookcity.style.backgroundColor = 'white'
            this.$refs.mybookcity.style.color = '#333333'
          } else {
            this.$refs.mybookcity.style.backgroundColor = 'lightseagreen'
            this.$refs.mybookcity.style.color = 'white'
            this.$refs.personalbookshelf.style.backgroundColor = 'white'
            this.$refs.personalbookshelf.style.color = '#333333'
          }
        })
      },
      immediate: true
    }
  }
}
</script>

<style scoped lang="less">
#mybookcity {
  display: flex;
  width: 1280px;
  #navigation {
    min-width: 200px;
    width: 200px;
    height: 135px;
    border-radius: 5px;
    margin: 25px 0 0 25px;
    overflow: hidden;
    border: 1px solid #E8E8E8;
    div {
      width: 100%;
      width: 294px;
      height: 45px;
      text-align: left;
      line-height: 45px;
      padding-left: 15px;
      font-size: 14px;
      border-bottom: 1px solid #E8E8E8;
      color: #333333;
      &:hover {
        background-color: lightseagreen;
        color: white;
      }
    }
  }
}
</style>
