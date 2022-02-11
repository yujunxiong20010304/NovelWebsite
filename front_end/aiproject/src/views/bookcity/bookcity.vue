<template>
  <div id="bookcity">
    <keep-alive include="parallax">
      <parallax></parallax>
    </keep-alive>
    <BackTop><div class="iconfont" style="font-size:40px;color: deepskyblue;">&#xe7d9;</div></BackTop>
    <cityheader></cityheader>
    <heavyRecommendations></heavyRecommendations>
    <multiplexing :nickname="'one'" :bestseller="bestseller_data">
      <template v-slot:default>
        <div class="topic">畅销作品</div>
      </template>
    </multiplexing>

    <multiplexing :nickname="'two'" :bestseller="weekly_data">
      <template v-slot:default>
        <div class="topic">每周精品</div>
      </template>
    </multiplexing>

    <multiplexing :nickname="'three'" :bestseller="signAcontract_data">
      <template v-slot:default>
        <div class="topic">签约新作</div>
      </template>
    </multiplexing>

    <ranking></ranking>
    <ending></ending>
  </div>
</template>

<script>
import parallax from '@/components/bookcity/parallax'
import cityheader from '@/components/bookcity/cityheader'
import heavyRecommendations from '@/components/bookcity/heavyRecommendations'
import multiplexing from '@/components/bookcity/multiplexing'
import ranking from '@/components/bookcity/ranking'
export default {
  name: 'bookcity',
  data () {
    return {
      bestseller_data: '',
      weekly_data: '',
      signAcontract_data: '',
      user: ''// 当前用户
    }
  },
  components: {
    ranking,
    cityheader,
    parallax,
    heavyRecommendations,
    multiplexing
  },
  methods: {
    /* 畅销作品的数据展示 */
    async bestSeller () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游', '玄幻'], num: 5, amount: 10, breakdown: 5 }
      )
      if (res.code === 200) {
        this.bestseller_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    },
    /* 每周精品的数据展示 */
    async weekly () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游', '玄幻'], num: 5, amount: 20, breakdown: 5 }
      )
      if (res.code === 200) {
        this.weekly_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    },
    /* 签约新作的数据展示 */
    async signAcontract () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游', '玄幻'], num: 5, amount: 30, breakdown: 5 }
      )
      if (res.code === 200) {
        this.signAcontract_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    },
    /* 获取session */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
    }
  },
  created () {
    this.bestSeller()
    this.weekly()
    this.signAcontract()
    this.user = this.$store.state.session_name
  }
}
</script>
<style scoped lang="less">
#bookcity {
  width: 100%;
  height: 3200px;
}
@font-face {
  font-family: 'iconfont';  /* Project id 3006776 */
  src: url('//at.alicdn.com/t/font_3006776_u57eh6w9uz.woff2?t=1639278815228') format('woff2'),
       url('//at.alicdn.com/t/font_3006776_u57eh6w9uz.woff?t=1639278815228') format('woff'),
       url('//at.alicdn.com/t/font_3006776_u57eh6w9uz.ttf?t=1639278815228') format('truetype');
}
.iconfont{
  font-family:"iconfont" !important;
  font-size:16px;font-style:normal;
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: 0.2px;
  -moz-osx-font-smoothing: grayscale;
}
.topic {
  font-weight: bold;
  font-size: 24px;
  padding-left: 55px;
  padding-top: 35px;
}
</style>
