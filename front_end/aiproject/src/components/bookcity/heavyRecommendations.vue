<template>
  <!-- 重磅推荐轮播图 -->
  <div id="hR">
    <div class="topic">
      <div>
        重磅推荐
      </div>
    </div>
    <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="false" @mouseover="exhibition" @mouseout="hides"  data-bs-interval="60000">
      <div class="carousel-inner">

        <div :class="[index===1? 'active':'','carousel-item']" v-for="(i,index) in book_data" :key="index">
          <!-- 占位 -->
          <div class="seize"></div>
          <div class="carousel-caption d-md-block">
            <!-- 内容 -->
            <div class="content">
              <div class="book" v-for="x in i" :key="x.id">
                <router-link :to="{path:'/home/designatedBook',query:{type:x.category,name:x.title}}"><img :src="x.chart" alt=""/></router-link>
                <div class="text">
                  <span style="font-size:20px;color: #333;font-weight: bold;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"><router-link style="font-size:20px;color: #333;font-weight: bold;" :to="{path:'/home/designatedBook',query:{type:x.category,name:x.title}}">{{ x.title }}</router-link></span>
                  <span style="font-size:12px;color:#777;">{{x.author}}</span>
                  <span style="font-size: 14px;color:#333;" class="brief_introduction">
                    {{ x.briefIntroduction }}
                  </span>
                  <span style="color:#fff;background-color:deepskyblue;width:50px;height:20px;text-align:center;border-radius:5px;">{{ x.category }}</span>
                  <span style="color:#777;height:25px;line-height:25px;">{{ x.updateTime }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
      <button ref = "right"
              id="rightbtn"
              class="carousel-control-prev iconfont"
              type="button"
              data-bs-target="#carouselExampleDark"
              data-bs-slide="prev">
        &#xeb0a;
        <span class="visually-hidden">Previous</span>
      </button>

      <button ref="left"
              id="leftbtn"
              class="carousel-control-next iconfont"
              type="button"
              data-bs-target="#carouselExampleDark"
              data-bs-slide="next">
        &#xeb09;
        <span class="visually-hidden">Next</span>
      </button>
    </div>

  </div>
</template>

<script>
export default {
  name: 'heavyRecommendations',
  data () {
    return {
      book_data: ''
    }
  },
  methods: {
    exhibition (e) {
      this.$refs.right.style.left = '25px'
      this.$refs.left.style.right = '25px'
      this.$refs.right.style.transition = 'all .5s'
      this.$refs.left.style.transition = 'all .5s'
      this.$refs.left.style.opacity = '1'
      this.$refs.right.style.opacity = '1'
      if (e.target.id === 'leftbtn') {
        this.$refs.left.style.backgroundColor = '#389EAD'
        this.$refs.left.style.color = '#fff'
      } else if (e.target.id === 'rightbtn') {
        this.$refs.right.style.backgroundColor = '#389EAD'
        this.$refs.right.style.color = '#fff'
      }
    },
    hides (e) {
      this.$refs.right.style.left = '-25px'
      this.$refs.left.style.right = '-25px'
      this.$refs.right.style.transition = 'all .5s'
      this.$refs.left.style.transition = 'all .5s'
      this.$refs.left.style.opacity = '0'
      this.$refs.right.style.opacity = '0'
      if (e.target.id === 'leftbtn') {
        this.$refs.left.style.backgroundColor = '#fff'
        this.$refs.left.style.color = '#525B6E'
      } else if (e.target.id === 'rightbtn') {
        this.$refs.right.style.backgroundColor = '#fff'
        this.$refs.right.style.color = '#525B6E'
      }
    },
    /* 请求数据 */
    async rotationChart () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游', '玄幻'], num: 2, breakdown: 4 }
      )
      if (res.code === 200) {
        this.book_data = res.body.data
      } else {
        console.log(res.message)
      }
    }
  },
  created () {
    this.rotationChart()
  }
}
</script>

<style scoped lang="less">
#hR {
  width: 1280px;
  height: 500px;
  background-color: #fff;
  .seize {
    width: 1280px;
    height: 410px;
  }
  .content {
    margin: 0 auto;
    width: 1160px;
    height: 410px;
    color: black;
    display: flex;
    flex-wrap: wrap;
    .book {
      width: 50%;
      height: 50%;
      color: white;
      display: flex;
      align-content: space-between;
    }
    .text {
      display: flex;
      flex-wrap: wrap;
      width: 415px;
      height: 165px;
      .brief_introduction {
        height: 55px;
        position: relative;
        padding: 10px;
        overflow: hidden;
        text-overflow: ellipsis;
        display:-webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        &:before {
          top: 0;
          left: 0;
          position: absolute;
          width: 5px;
          height: 10px;
          border-top: 1px solid #A6A6A6;
          border-left: 1px solid #A6A6A6;
          content: '';
        }
        &:after{
          bottom: 0;
          right: 0;
          position: absolute;
          width: 5px;
          height: 10px;
          border-bottom: 1px solid #A6A6A6;
          border-right: 1px solid #A6A6A6;
          content: '';
        }
      }
      span {
        width: 100%;
        text-align: left;
      }
    }
    img {
      width: 110px;
      height: 165px;
      border-radius: 5px;
      margin-right: 20px;
    }
  }
  /deep/ .carousel-caption {
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
    padding-top: 0;
    padding-bottom: 0;
    color: #fff;
    text-align: center;
  }
  #rightbtn,#leftbtn{
    background-color: #FFFFFF;
    width: 40px;
    height: 40px;
    position: absolute;
    top: 50%;
    transform: translate(0, -100%);
    text-align: center;
    border-radius: 50%;
    z-index: 10;
    box-shadow:0 15px 35px rgba(0,0,0,0.01),0 3px 10px rgba(0,0,0,0.5);
  }
  /deep/ .carousel-control-prev {
    left: -135px;
  }
  /deep/ .carousel-control-next {
    right: -135px;
  }
  /deep/ #carouselExampleDark {
    overflow: hidden;
  }
  @font-face {
  font-family: 'iconfont';  /* Project id 3006776 */
  src: url('//at.alicdn.com/t/font_3006776_93yzmtwrnmp.woff2?t=1639663060737') format('woff2'),
       url('//at.alicdn.com/t/font_3006776_93yzmtwrnmp.woff?t=1639663060737') format('woff'),
       url('//at.alicdn.com/t/font_3006776_93yzmtwrnmp.ttf?t=1639663060737') format('truetype');
  }
  .iconfont{
    font-family:"iconfont" !important;
    font-size:16px;font-style:normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
    color: #525B6E;
  }
  .topic {
    width:100%;
    height: 50px;
    background: #fff;
    div {
      height: 34px;
      width: 96px;
      background-color: #BB996D;
      text-align: center;
      font-size: 14px;
      border-radius: 5px;
      color: #fff;
      line-height: 34px;
      margin-left: 55px;
    }
  }
}
</style>
