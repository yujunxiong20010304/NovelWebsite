<template>
  <!-- 小说分类 -->
  <div id="novelclassification">
    <div id="navigation">
      <div id="one">
        <span>频道</span>
        <ul>
          <li>出版</li>
          <li>男频</li>
          <li>女频</li>
        </ul>
      </div>
      <div class="divisions">
        <a-divider class="division"/>
      </div>
      <div id="two">
        <span>类型</span>
        <ul id="main">
          <li><router-link to="/home/novelclassification/whole" style="color:#fff;">全部</router-link></li>
          <li><router-link to="/home/novelclassification/fantasy" style="color:#fff;">玄幻</router-link></li>
          <li><router-link to="/home/novelclassification/xiuzhen" style="color:#fff;">修真</router-link></li>
          <li><router-link to="/home/novelclassification/urban" style="color:#fff;">都市</router-link></li>
          <li><router-link to="/home/novelclassification/pass_through" style="color:#fff;">穿越</router-link></li>
          <li><router-link to="/home/novelclassification/online_games" style="color:#fff;">网游</router-link></li>
          <li><router-link to="/home/novelclassification/science_fiction" style="color:#fff;">科幻</router-link></li>
        </ul>
      </div>
      <div class="divisions">
        <a-divider class="division"/>
      </div>
      <div id="three">
        <span>其他</span>
        <ul>
          <li>全部</li>
          <li>免费</li>
          <li>特价</li>
          <li>Vip</li>
        </ul>
      </div>
    </div>

    <router-view></router-view>
    <ending></ending>
  </div>
</template>

<script>
export default {
  name: 'novelclassification',
  components: {
  },
  data () {
    return {
      current: 1,
      pathList: {
        '/home/novelclassification/whole': 0,
        '/home/novelclassification/fantasy': 1,
        '/home/novelclassification/xiuzhen': 2,
        '/home/novelclassification/urban': 3,
        '/home/novelclassification/pass_through': 4,
        '/home/novelclassification/online_games': 5,
        '/home/novelclassification/science_fiction': 6
      }
    }
  },
  methods: {
    switchs () {
      this.$nextTick(() => {
        let liList = document.getElementById('main').querySelectorAll('li')
        for (let i of liList) {
          i.style.backgroundColor = '#9e9e9e'
        }
        liList[this.pathList[this.$route.path]].style.backgroundColor = '#389EAC'
      })
    }
  },
  created () {
    this.switchs()
  },
  watch: {
    $route: {
      handler (val, oldVal) {
        this.switchs()
      },
      immediate: true
    }
  }
}
</script>

<style scoped lang="less">
#novelclassification {
  background-color: #f0f0f0;
  overflow: hidden;
}
#navigation {
  width: 1150px;
  height: 188px;
  background: #fff;
  margin: 35px auto 0;
  display: flex;
  list-style-type:none;
  flex-wrap: wrap;
  padding: 27px 46px;
  border-radius: 15px;
  box-shadow:0 15px 35px rgba(0,0,0,0.01),0 3px 10px rgba(0,0,0,0.05);
  #one,#two,#three{
    display: flex;
    width: 100%;
    align-items: center;
    span {
      color: #ccc;
    }
    ul {
      list-style-type:none;
      display: flex;
      color: #9e9e9e;
      font-weight: normal;
      margin-left: 48px;
      align-items: center;
      li {
        width: 44px;
        height: 22px;
        background-color: #9e9e9e;
        margin-right: 20px;
        text-align: center;
        line-height: 22px;
        border-radius: 22px;
        color: #fff;
        &:hover {
          background-color: #389EAC;
        }
      }
    }
  }
  .divisions{
    width: 100%;
    height: 10px;
    margin-left: 68px;
    margin-top: 15px;
    .division {
      margin: 0;
    }
  }
}
</style>
