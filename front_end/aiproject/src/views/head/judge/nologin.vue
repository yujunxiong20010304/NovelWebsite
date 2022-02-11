<template>
  <div id="nologin">
    <router-link to="/login" class="btn">登录</router-link>
    <router-link to="/register" class="btn">注册</router-link>
  </div>
</template>

<script>
export default {
  name: 'nologin'
}
</script>

<style scoped lang="less">
#nologin {
  display: flex;
  width: 80%;
  .btn {
    width: 50%;
    text-align: center;
  }
}
</style>
