<template>
  <!-- 排行 -->
  <div id="ranking">
    <div id="nav"><span style="font-size:24px;font-weight:bold;color:black;line-height:30px;margin-left:55px;">排行</span>
      <span class="more" @mouseover="switchs" @mouseout="recovery">查看更多</span>
    </div>
    <div id="ranking_list">
      <rank :book="serial_data">
        <template #default>
          <div class="topic">
            <div>连载榜</div>
            <span>作品两日内有更新</span>
          </div>
        </template>
      </rank>

      <rank :book="potential_data">
        <template #default>
          <div class="topic">
            <div>潜力榜</div>
            <span>作品七日内有更新且字数在二万至十万之间，按周阅读时长排序</span>
          </div>
        </template>
      </rank>

      <rank :book="endbook_data">
        <template #default>
          <div class="topic">
            <div>完本榜</div>
            <span>八万字以上完本，按周阅读时长排序</span>
          </div>
        </template>
      </rank>

      <rank :book="recommend_data">
        <template #default>
          <div class="topic">
            <div>推荐榜</div>
            <span>按作品过去1个月所获得推荐票数排行</span>
          </div>
        </template>
      </rank>
    </div>
  </div>
</template>

<script>
import rank from '@/components/bookcity/rank'
export default {
  name: 'ranking',
  components: {
    rank
  },
  data () {
    return {
      serial_data: '',
      potential_data: '',
      endbook_data: '',
      recommend_data: ''
    }
  },
  methods: {
    switchs (e) {
      e.target.style.backgroundColor = '#389EAD'
      e.target.style.color = 'white'
    },
    recovery (e) {
      e.target.style.background = 'white'
      e.target.style.color = '#525B6E'
    },
    /* 连载榜 */
    async serial () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游'], num: 2, amount: 12 }
      )
      if (res.code === 200) {
        this.serial_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    },
    /* 潜力榜 */
    async potential () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游'], num: 2, amount: 4 }
      )
      if (res.code === 200) {
        this.potential_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    },
    /* 完本榜 */
    async endbook () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游'], num: 2, amount: 24 }
      )
      if (res.code === 200) {
        this.endbook_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    },
    /* 推荐榜 */
    async recommend () {
      const { data: res } = await this.$http.post(
        '/novel', { type: ['穿越', '修真', '都市', '科幻', '网游'], num: 2, amount: 34 }
      )
      if (res.code === 200) {
        this.recommend_data = res.body.data
      } else {
        console.log('参数不齐全')
      }
    }
  },
  created () {
    this.serial()
    this.potential()
    this.endbook()
    this.recommend()
  }
}
</script>

<style scoped lang="less">
#ranking {
  width: 100%;
  height: 707px;
  margin-top: 50px;
  #ranking_list {
    display: flex;
    justify-content: center;
    .topic {
      padding: 20px;
      margin-bottom: 10px;
      height: 84px;
      div{
        color: #bb996d;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        height: 22px;
        line-height: 22px;
      }
      span {
        color: #A6A6A6;
        font-size: 12px;
        font-weight: normal;
      }
    }
  }
  #nav {
    width: 100%;
    height: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    .more {
      width: 88px;
      height: 33px;
      background-color: #fff;
      text-align: center;
      line-height: 33px;
      border-radius: 5px;
      box-shadow:0 15px 35px rgba(0,0,0,0.01),0 3px 10px rgba(0,0,0,0.05);
      margin-right: 25px;
    }
  }
}
</style>
