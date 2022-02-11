<template>
<!-- 可复用轮播图 -->
  <div id="bestSellingWorks">
    <slot name="default"></slot>
    <div :id="nickname" style="overflow: hidden;" class="carousel carousel-dark slide" data-bs-ride="false" @mouseover="exhibition" @mouseout="hides"  data-bs-interval="60000">
      <div class="carousel-inner">

        <div :class="[index===1? 'active':'','carousel-item']" v-for="(i,index) in bestseller" :key="index">
          <!-- 占位 -->
          <div class="seize"></div>
          <div class="carousel-caption d-md-block">
            <!-- 内容 -->
            <div class="content">
              <div class="book" v-for="x in i" :key="x.id">
                <router-link :to="{path:'/home/designatedBook',query:{type:x.category,name:x.title}}">
                  <img :src="x.chart" alt="" />
                </router-link>
                <span class="alias"><router-link style="color:initial;" :to="{path:'/home/designatedBook',query:{type:x.category,name:x.title}}">{{ x.title }}</router-link></span>
                <span class="author">{{x.author}}</span>
                <span class="introduce">{{ x.briefIntroduction }}</span>
                <span class="author">{{ x.updateTime }}</span>
              </div>
            </div>
          </div>
        </div>

      </div>
      <button ref = "right"
              id="rightbtn"
              class="carousel-control-prev iconfont"
              type="button"
              :data-bs-target="'#'+nickname"
              data-bs-slide="prev">
        &#xeb0a;
        <span class="visually-hidden">Previous</span>
      </button>

      <button ref="left"
              id="leftbtn"
              class="carousel-control-next iconfont"
              type="button"
              :data-bs-target="'#'+nickname"
              data-bs-slide="next">
        &#xeb09;
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'bestSellingWorks',
  props: ['nickname', 'bestseller'],
  data () {
    return {
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
    }
  }
}
</script>

<style scoped lang="less">
#bestSellingWorks {
  background-color: #F8F9F9;
  min-width: 1280px;
  height: 485px;
  width: 100%;
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
    .book {
      width: 192px;
      height: 334px;
      margin: 40px 20px 0;
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;
      align-content: flex-start;
      img {
        width: 120px;
        height: 180px;
        border-radius: 5px;
      }
      span {
        text-align: left;
        width: 192px;
      }
      .alias {
        flex: 0 1 auto;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        font-size: 16px;
        font-weight: bold;
      }
      .author {
        color: #777;
        font-size: 12px;
        margin-bottom: 5px;
      }
      .introduce {
        font-size: 13px;
        color: #333;
        overflow: hidden;
        text-overflow: ellipsis;
        display:-webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        margin-bottom: 5px;
      }
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
}
</style>
