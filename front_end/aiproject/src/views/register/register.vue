<template>
  <!-- 注册 -->
  <div id="header">
    <div id="register">
      <div id="title">通行证</div>
      <div id="videoContent">
        <div id="texiao" ref="texiao"></div>
        <div id="img" ref="img"></div>
        <!-- 进度环 -->
        <a-progress
          type="circle"
          :percent="speed_progress"
          id="progress_bar"
          :width="150"
          strokeColor="#01041C"
          :strokeWidth="5"/>

        <canvas id='canvas' width='400' height='300' style="display:none" ref="canvas"></canvas>
        <div id="circular">
          <video id="video" width="200px" height="200px" ref="video"></video>
        </div>
        <div>
          <div style="text-align: center;">
            <div id="inputcontent">
                <Input
                  clearable
                  @on-blur="user"
                  v-model= "username"
                  prefix="md-contact"
                  style="width:270px;
                  box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.2);"
                  placeholder="用户名"
                  size="large"
                  type="text">
                </Input>
                <Input
                  password
                  clearable
                  @on-blur="secrecy"
                  v-model="password"
                  size="large"
                  prefix="ios-key"
                  style="width:270px;
                  box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.2);"
                  placeholder="密码"
                  type="password">
                </Input>
            </div>
            <Button type="default"
                    ghost style="height: 40px;
                    width: 185px;
                    margin-top: 25px;
                    box-shadow:0 15px 35px rgba(0,0,0,0.2),0 3px 10px rgba(0,0,0,0.2);"
                    @click="openvideo">提交并录入人脸信息</Button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'register',
  data () {
    return {
      username: '',
      password: '',
      mediaStreamTrack: '', // 摄像头
      speed_progress: 0, // 当前录入的进度
      timer: null
    }
  },
  methods: {
    // 向数据库发起请求判断用户名是否存在
    testing () {

    },
    user () {
      console.log('用户')
    },
    secrecy () {
      console.log('密码')
    },
    // 打开摄像头，一切事件的启动
    openvideo () {
      if (this.username.length < 5 || this.password.length < 5) {
        alert('请输入密码用户名长度大于5')
      } else {
        this.$refs.img.style.display = 'none'
        let progressbar = document.getElementById('progress_bar')
        progressbar.style.display = 'block'
        this.Controlcamera()
      }
    },
    // 操作摄像头
    Controlcamera () {
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
        this.register()
      }, 500)
      this.$once('hook:beforeDestroy', () => {
        clearInterval(this.timer)
        this.timer = null
      })
    },
    async register () {
      let { data: res } = await this.$http.post(
        'register', { username: this.username, password: this.password, img: this.$refs.canvas.toDataURL('image/png') }
      )
      if (res === 'break') {
        clearInterval(this.timer)
        this.timer = null
        this.$router.push({ path: '/home/bookcity' })
      } else {
        this.speed_progress = res.len * 4
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
#header {
  background-image: url('../../assets/background/register.jpeg');
  width: 100%;
  height: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  overflow: hidden;
  #register {
    width: 445px;
    height: 435px;
    border-radius: 10px;
    background:
      radial-gradient(circle at 50% 0,
        rgba(255,0,0,.5),
        rgba(255,0,0,0) 70.71%),
      radial-gradient(circle at 26.7% 75%,
        rgba(0,0,255,.5),
        rgba(0,0,255,0) 70.71%),
      radial-gradient(circle at 93.3% 75%,
        rgba(98,0,171,.5),
        rgba(101,8,109,0.7) 90.71%) beige;
    box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,7);
    margin: 100px auto 0;
    #title {
      text-align: center;
      width: 100%;
      height: 50px;
      font-size: 20px;
      line-height: 50px;
      border-bottom: 1px solid #65086D;
      color: white;
      box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.7);
      border-bottom-left-radius: 40px;
      border-bottom-right-radius: 40px;
    }
    #videoContent {
      width: 100%;
      height: 160px;
      position: relative;
      margin-top: 23px;
      #texiao {
        width: 130px;
        height:130px;
        border-radius: 100px;
        background-color: black;
        position: absolute;
        z-index: 3;
        left: 50%;
        transform: translate(-50%, 0);
        background:
          linear-gradient(green, green),
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
      #circular {
        text-align:left;
        width: 130px;
        height:130px;
        border-radius: 100px;
        overflow:hidden;
        position: relative;
        margin: 0 auto;
        box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.2);
        background-repeat:no-repeat;
        background-position: center;
        background-size: cover;
        #video {
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translate(-50%, 0);
        }
      }
      @keyframes move{
        to{
          background-position: 0 100%,0 0, 0 0, 0 0;
            /* 终止位置 */
            clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
        }
      }
    }
  }
  #inputcontent {
    display: flex;
    width: 300px;
    height: 95px;
    flex-wrap: wrap;
    margin: 25px auto 0;
    justify-content: center;
    align-content: space-between;
  }
  #progress_bar {
    position: absolute;
    top: -10px;
    left: 148px;
    display: none;
  }
  #img {
    width: 130px;
    height:130px;
    border-radius: 100px;
    background-color: black;
    position: absolute;
    z-index: 3;
    left: 50%;
    transform: translate(-50%, 0);
    background-image: url('../../assets/face.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    box-shadow:0 15px 35px rgba(0,0,0,0.5),0 3px 10px rgba(0,0,0,0.5);
  }
}

</style>
