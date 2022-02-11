<template>
  <!-- 二级导航 -->
  <div id="show">
    <router-link style="color: #525B6E;" to="/home/novelclassification/fantasy"><div @mouseover="switchs" @mouseout="recovery">玄幻小说</div></router-link>
    <router-link style="color: #525B6E;" to="/home/novelclassification/xiuzhen"><div @mouseover="switchs" @mouseout="recovery">修真小说</div></router-link>
    <router-link style="color: #525B6E;" to="/home/novelclassification/urban"><div @mouseover="switchs" @mouseout="recovery">都市小说</div></router-link>
    <router-link style="color: #525B6E;" to="/home/novelclassification/pass_through"><div @mouseover="switchs" @mouseout="recovery">穿越小说</div></router-link>
    <router-link style="color: #525B6E;" to="/home/novelclassification/online_games"><div @mouseover="switchs" @mouseout="recovery">网游小说</div></router-link>
    <router-link style="color: #525B6E;" to="/home/novelclassification/science_fiction"><div @mouseover="switchs" @mouseout="recovery">科幻小说</div></router-link>
  </div>
</template>

<script>
export default {
  name: 'cityheader',
  methods: {
    switchs (e) {
      e.target.style.backgroundColor = '#389EAD'
      e.target.style.color = 'white'
    },
    recovery (e) {
      e.target.style.background = 'white'
      e.target.style.color = '#525B6E'
    }
  }
}
</script>

<style scoped lang="less">
#show{
  width: 100%;
  height: 140px;
  display: flex;
  justify-content: center;
  background-color: #F8F9F9;
  align-items: center;
  div {
    width: 180px;
    height: 60px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin: 0 8px;
    line-height: 60px;
    background: #fff;
    border-radius: 5px;
    box-shadow:0 15px 35px rgba(0,0,0,0.01),0 3px 10px rgba(0,0,0,0.05);
    min-width: 180px;
  }
}
</style>
