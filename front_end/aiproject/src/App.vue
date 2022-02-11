<template>
  <div id="app" :style="{height:screenHeight+'px'}">
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      screenWidth: '',
      screenHeight: ''
    }
  },
  mounted () {
    // noinspection JSSuspiciousNameCombination
    this.screenWidth = document.documentElement.clientHeight
    this.screenHeight = document.documentElement.clientHeight
    window.onresize = () => {
      return (() => {
        // noinspection JSSuspiciousNameCombination
        this.screenWidth = document.documentElement.clientHeight
        this.screenHeight = document.documentElement.clientHeight
      })()
    }
  }
}
</script>

<style lang="less">
* {
  padding: 0;
  margin: 0;
}
#app {
  width: 100%;
}
</style>
