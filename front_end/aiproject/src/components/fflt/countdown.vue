<template>
  <div id="countdown">
    <div class="introduce">
      <span style="font-size:30px;color:#fff;">VIP章节免费读</span>
      <span style="font-size:14px;color:#fff;">免费阅读全部收费章节</span>
    </div>
    <div class="time">
      <div class="details">
        <span style="font-size:30px;height:40px;line-height:40px;" ref="d">0</span>
        <span>天</span>
      </div>
      <div class="details">
        <span style="font-size:30px;height:40px;line-height:40px;" ref="h">00</span>
        <span>小时</span>
      </div>
      <div class="details">
        <span style="font-size:30px;height:40px;line-height:40px;" ref="m">00</span>
        <span>分钟</span>
      </div>
      <div class="details">
        <span style="font-size:30px;height:40px;line-height:40px;" ref="s">00</span>
        <span>秒</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'countdown',
  methods: {
    countdowntime () {
      /* 指定时间 */
      let end = 60 * 60 * 12 * 1000 + +new Date()
      let timer = setInterval(() => {
        let date = +new Date()
        let time = (end - date) / 1000
        let d = parseInt(time / 60 / 60 / 24)
        let h = parseInt(time / 60 / 60 % 24)
        let m = parseInt(time / 60 % 60)
        let s = parseInt(time % 60)
        h = h >= 10 ? h : '0' + h
        m = m >= 10 ? m : '0' + m
        s = s >= 10 ? s : '0' + s
        this.$refs.d.innerHTML = d
        this.$refs.h.innerHTML = h
        this.$refs.m.innerHTML = m
        this.$refs.s.innerHTML = s
      }, 1000)
      this.$once('hook:beforeDestroy', () => {
        clearInterval(timer)
        timer = null
      })
    }
  },
  mounted () {
    this.countdowntime()
  }
}
</script>

<style scoped lang="less">
#countdown {
  width: 100%;
  height: 160px;
  margin: 40px auto 0;
  background-image: url('../../assets/vip.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  border-radius: 5px;
  .introduce {
    display: flex;
    flex-wrap: wrap;
    width: 325px;
    align-content: center;
    span {
      width: 100%;
      padding-left: 50px;
    }
  }
  .time {
    width: 322px;
    display: flex;
    align-items: center;
    margin-left: 41px;
    div {
      width: 60px;
      height: 60px;
      margin-right: 16px;
      border-radius: 5px;
    }
    .details {
      display: flex;
      flex-wrap: wrap;
      color: #fff;
      text-align: center;
      span {
        width: 100%;
      }
      &:first-child {
        color:#fc3d59;
      }
    }
  }
}
</style>
