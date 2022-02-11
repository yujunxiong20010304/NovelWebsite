<template>
  <!-- 侧边导航栏 -->
    <Affix :offset-top="108" style="position: absolute;left: 112px;">
      <div id="sidenavigation">
        <div class="option">
          <i class="iconfont">&#xe62b;</i>
          <span>目录</span>
        </div>
        <div class="option">
          <i class="iconfont">&#xe610;</i>
          <span>书架</span>
        </div>
        <div id="set_up" class="option" @click="open">
          <i class="iconfont">&#xe654;</i>
          <span>设置</span>
          <!-- 设置项 -->
          <div id="set_item" ref="sidenav">
            <!-- 标题 -->
            <div class="targets" id="title">
              <span>设置</span>
              <!-- .stop阻止事件冒泡 -->
              <i @click.stop="close">&#xe605;</i>
            </div>
            <!-- 需要设置的内容 -->
            <div>
              <!-- 背景设置 -->
              <div class="targets" id="backcolor" @click="replace_backcolor">
                <span>阅读背景</span>
                <div style="background-color: #FAEED7;color: #D9CDB6;"></div>
                <div style="background-color: #E9EFF5;color: #B9C1C9;"></div>
                <div style="background-color: #E7F0E1;color: #C4CCC1;"></div>
                <div style="background-color: #F2E4E9;color: #D4C7CC;"></div>
                <div style="background-color: #F7F7F7;color: #CCCCCC;"></div>
                <div style="background-color: #F9F5E2;color: #D6D5C1;"></div>
                <div style="background-color: #E5E4E0;color: #B8B8B8;"></div>
                <div style="background-color: #343434;color: #222222;"></div>
              </div>
              <!-- 字体大小设置 -->
              <div class="targets" id="fontsize">
                <span>字体大小</span>
                <div @click="plus">A+</div>
                <div ref="sizes">{{characterSize}}</div>
                <div @click="reduce">A-</div>
              </div>
              <!-- 选择保存或者恢复默认设置 -->
              <div class="targets" id="result">
                <div style="background-color:#D32F2F;color:#fff;" @click.stop="preservation">保存设置</div>
                <div style="background-color:#fff;color:black;border: 1px solid #d6d6d6;" @click.stop="recovery">恢复默认</div>
              </div>
            </div>
          </div>
        </div>
        <div class="option">
          <BackTop>
            <i class="iconfont" style="padding-bottom: 0;color: #333;">&#xe64a;</i>
            <span>顶部</span>
          </BackTop>
        </div>
      </div>
    </Affix>
</template>

<script>
export default {
  name: 'sidenavigation',
  props: ['info'],
  data () {
    return {
      behindColor: this.info.behindColor,
      backcolor: this.info.backcolor,
      characterSize: this.info.characterSize
    }
  },
  methods: {
    close () {
      this.$refs.sidenav.style.display = 'none'
      this.info.behindColor = this.behindColor
      this.info.backcolor = this.backcolor
      this.info.characterSize = this.characterSize
      console.log('关闭')
      /* location.reload() */
    },
    open () {
      this.$refs.sidenav.style.display = 'block'
      console.log('打开')
    },
    replace_backcolor (e) {
      this.info.backcolor = e.target.style.backgroundColor
      this.info.behindColor = e.target.style.color
    },
    plus () {
      this.info.characterSize *= 1
      if (this.info.characterSize < 20) {
        this.info.characterSize += 1
        this.$refs.sizes.innerHTML = this.info.characterSize
      }
    },
    reduce () {
      this.info.characterSize *= 1
      if (this.info.characterSize > 14) {
        this.info.characterSize -= 1
        this.$refs.sizes.innerHTML = this.info.characterSize
      }
    },
    /* 保存设置 */
    preservation () {
      window.sessionStorage.setItem('present', [this.info.behindColor, this.info.backcolor, this.info.characterSize])
      this.$refs.sidenav.style.display = 'none'
    },
    /* 恢复默认设置 */
    recovery () {
      window.sessionStorage.removeItem('present')
      this.$refs.sidenav.style.display = 'none'
      location.reload()
    }
  }
}
</script>

<style scoped lang="less">
#sidenavigation {
  width: 60px;
  height: 246px;
  #set_up {
    position: relative;
    #set_item {
      border-radius: 5px;
      top: -126px;
      left: 75px;
      position: absolute;
      padding: 0 35px;
      width: 570px;
      height: 275px;
      display: none;
      background-color: #fafaf9;
      /* 标题样式 */
      #title {
        width: 100%;
        height: 50px;
        text-align: left;
        line-height: 50px;
        font-size: 16px;
        color: #333;
        font-weight: 700;
        border-bottom: 1px solid #e6e6e6;
        margin-bottom: 20px;
        justify-content: space-between;
        i {
          text-align: center;
          line-height: 50px;
          font-family:"iconfont" !important;
          font-size:16px;font-style:normal;
          -webkit-font-smoothing: antialiased;
          -webkit-text-stroke-width: 0.2px;
          -moz-osx-font-smoothing: grayscale;
          padding-top: 0;
          width: 50px;
        }
      }
      /* 每一个设置项的共同样式 */
      .targets {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        font-size: 14px;
        color: #666;
        letter-spacing: .72px;
        font-weight: 500;
      }
      /* 背景设置样式 */
      #backcolor {
        height: 50px;
        line-height: 50px;
        margin-bottom: 20px;
        span {
          margin-right: 10px;
        }
        div {
          height: 38px;
          width: 38px;
          border: 1px solid #999;
          border-radius: 50%;
          margin-left: 13px;
        }
      }
      /* 设置字体大小 */
      #fontsize {
        height: 36px;
        line-height: 36px;
        margin-bottom: 20px;
        span {
          margin-right: 23px;
        }
        div {
          border: 1px solid #e6e6e6;
          height: 36px;
          width: 63px;
          font-size: 20px;
        }
      }
      /* 保存设置或者恢复默认设置 */
      #result {
        margin-top: 12px;
        height: 36px;
        width: 100%;
        justify-content: center;
        line-height: 36px;
        text-align: center;
        div {
          width: 128px;
          height: 34px;
          margin: 0 30px;
          border-radius: 3px;
        }
      }
    }
  }
  .option {
    width: 100%;
    height: 60px;
    margin-top: 2px;
    text-align: center;
    border: 1px solid #FFFFFF;
    color: #999;
    &:hover {
      color: crimson;
      border: 1px solid crimson;
    }
    span {
      display: inline-block;
      width: 60px;
    }
    i {
      padding-top: 13px;
      display: inline-block;
    }
  }
  @font-face {
  font-family: 'iconfont';  /* Project id 3006776 */
  src: url('//at.alicdn.com/t/font_3006776_l7rw0sbuca.woff2?t=1640181318005') format('woff2'),
       url('//at.alicdn.com/t/font_3006776_l7rw0sbuca.woff?t=1640181318005') format('woff'),
       url('//at.alicdn.com/t/font_3006776_l7rw0sbuca.ttf?t=1640181318005') format('truetype');
  }
  .iconfont{
    font-family:"iconfont" !important;
    font-size:16px;font-style:normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
  }
  /deep/ .ivu-back-top {
    display: block;
    position: static;
  }
}
</style>
