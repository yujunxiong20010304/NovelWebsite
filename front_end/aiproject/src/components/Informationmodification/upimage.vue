<template>
  <!-- 修改头像 -->
  <div id="upimage">
    <div style="width: 100%;display: flex;">
      <label for="real">
        <div class="upload" ref="frame">
          <a-icon type="plus" style="font-size: 32px; color: #999;line-height: 100px;"/>
        </div>
      </label>
      <input id="real" type="file" style="display: none" @change="show_new_img" accept="image/*"/>
      <div style="margin-left: 10px;">
        <div class="block" :style="{backgroundImage: 'url('+img+')'}"></div>
      </div>
    </div>
    <div id="choice">
      <Button type="info" ghost @click="upload">提交</Button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'upimage',
  data () {
    return {
      img: '',
      user: ''
    }
  },
  methods: {
    async trial () {
      let { data: res } = await this.$http.post('/trial')
      this.user = res.username
    },
    /* 在本次组件中并未使用 */
    show_img () {
      const file = document.querySelector('input[type=file]').files[0]
      const reader = new FileReader()
      reader.addEventListener(
        'load',
        () => {
          this.img = reader.result
        },
        false
      )
      if (file) {
        reader.readAsDataURL(file)
      }
    },
    /* 将上传的图片数据进行了压缩 */
    show_new_img () {
      const file = document.querySelector('input[type=file]').files[0] // 上传的文件对象
      const reader = new FileReader()
      reader.readAsDataURL(file)
      reader.addEventListener('load', (e) => {
        let image = new Image() // //新建一个img标签（还没嵌入DOM节点)
        image.src = e.target.result
        image.addEventListener('load', () => {
          let canvas = document.createElement('canvas')
          let context = canvas.getContext('2d')
          let imageWidth = image.width / 2 // 压缩后图片的大小
          let imageHeight = image.height / 2
          let data = ''
          canvas.width = imageWidth
          canvas.height = imageHeight
          context.drawImage(image, 0, 0, imageWidth, imageHeight)
          data = canvas.toDataURL('image/jpeg')
          // 压缩完成
          this.img = data
        })
      })
    },
    async submit_avatar () {
      const { data: res } = await this.$http.post('/submit_avatar', { user: this.user, img: this.img })
      if (res.code === 400) {
        console.log(res.message)
      }
    },
    upload () {
      this.submit_avatar()
      this.update_save_local()
      location.reload()
    },
    // 更新我保存在本地的头像数据
    update_save_local () {
      sessionStorage.setItem('head_portrait', this.img)
    }
  },
  created () {
    this.user = this.$store.state.session_name
  }

}
</script>

<style scoped lang="less">
#upimage{
  margin: 20px 0;
  width: 213px;
  height: 185px;
  .upload {
    width: 100px;
    height: 100px;
    border: 1px dashed #d9d9d9;
    text-align: center;
    background-color: #fafafa;
    border-radius: 5px;
    &:hover {
      border: 1px dashed #4CA7FF;
    }
  }
  .block {
    width: 100px;
    height: 100px;
    background-color: white;
    border-radius: 7px;
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
  }
  #choice {
    margin: 35px 0 0 0;
    text-align: center;
  }
}
</style>
