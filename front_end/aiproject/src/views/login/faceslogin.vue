<template>
  <div id="login">
    <div id="texiao">
    </div>
    <canvas id='canvas' width='400' height='300' style="display:none" ref="canvas"></canvas>
    <div id="circular">
      <video id="video" width="200px" height="200px" ref="video"></video>
    </div>
  </div>
</template>

<script>
export default {
  name: 'faceslogin',
  data () {
    return {
      mediaStreamTrack: '',
      timer: null
    }
  },
  watch: {
    $route: {
      handler (val, oldVal) {
        this.$nextTick(() => {
          this.openvideo()
        })
      },
      immediate: true
    }
  },
  methods: {
    openvideo () {
      navigator.getMedia = navigator.getUserMedia ||
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia ||
                         navigator.msGetUserMedia

      navigator.getMedia({
        video: true, // 打开video
        audio: false
      },
      (strem) => {
        this.$refs.video.srcObject = strem
        this.mediaStreamTrack = strem
        this.$refs.video.onloadedmetadata = (e) => {
          this.$refs.video.play()
        }
      }, (error) => {
        console.log(error)
      })
      this.timer = setInterval(() => {
        this.$refs.canvas.getContext('2d').drawImage(this.$refs.video, 0, 0, 400, 300)
        this.transmitData()
      }, 1000)
      this.$once('hook:beforeDestroy', () => {
        clearInterval(this.timer)
        this.timer = null
      })
    },
    async transmitData () {
      let { data: res } = await this.$http.post('/login', { img: this.$refs.canvas.toDataURL('image/png') })
      console.log(res)
      if (res.code === 200) {
        clearInterval(this.timer)
        this.timer = null
        this.$router.push({ path: '/home/bookcity' })
      }
    }

  },
  beforeDestroy () {
    try {
      this.mediaStreamTrack.getTracks()[0].stop()
      this.mediaStreamTrack.getTracks()[1].stop()
    } catch (e) {

    }
  }

}
</script>

<style scoped lang="less">
#login {
  width: 100%;
  height: 100%;
  position: relative;
  text-align:center;
}
#texiao {
    width: 150px;
    height:150px;
    background-color: black;
    position: absolute;
    z-index: 3;
    left: 50%;
    border-radius: 50%;
    transform: translate(-50%, 0);
    top: 20px;
    background:
      linear-gradient(springgreen, springgreen),
      linear-gradient(90deg, #ffffff33 1px,transparent 0,transparent 19px),
      linear-gradient( #ffffff33 1px,transparent 0,transparent 19px),
      linear-gradient(transparent, springgreen);
      background-size:100% 1.5%, 10% 100%,100% 8%, 100% 100%;
      background-repeat:no-repeat, repeat, repeat, no-repeat;
      background-position: 0 0, 0 0, 0 0, 0 0;
      /* 初始位置 */
      clip-path: polygon(0% 0%, 100% 0%, 100% 1.5%, 0% 1.5%);
      /* 添加动画效果 */
      animation: move 2s infinite linear;
}
@keyframes move{
  to{
    background-position: 0 100%,0 0, 0 0, 0 0;
        /* 终止位置 */
        clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
    }
}
#circular {
  width: 150px;
  height: 150px;
  background-size: cover;
  background-position: center;
  border-radius: 50%;
  position: relative;
  overflow:hidden;
  left: 50%;
  transform: translate(-50%, 0);
  top: 20px;
  box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.7);
  #video {
    position: absolute;
    top: -25px;
    left: 50%;
    transform: translate(-50%, 0);
  }
}
</style>
