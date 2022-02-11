<template>
  <!-- 信息修改 -->
  <div id="Informationmodification">

    <!-- 基础信息区域 -->
    <div class="subject">基本信息</div>
    <basic></basic>

    <!-- 修改登录头像 -->
    <div class="subject" style="margin-top: 20px;background-color: #FF3A55;">修改头像</div>
    <upimage></upimage>

    <!-- 人脸区域 -->
    <div class="subject" style="margin-top: 20px;background-color: #2D8DF0;">人脸录入</div>
    <getface></getface>
  </div>
</template>

<script>
/* 基础信息 */
import basic from '@/components/Informationmodification/basic'
/* 修改头像 */
import upimage from '@/components/Informationmodification/upimage'
/* 人脸数据录入 */
import getface from '@/components/Informationmodification/getface'
export default {
  name: 'Informationmodification',
  components: { basic, upimage, getface }
}
</script>

<style scoped lang="less">
#Informationmodification {
  width: 100%;
  margin: 25px 25px 0 25px;
  border-radius: 5px;
  .subject {
    width: 100%;
    height: 50px;
    background-color: lightseagreen;
    font-size: 18px;
    text-align: left;
    padding: 0 0 0 10px;
    line-height: 50px;
    border-radius: 5px;
    color: #fff;
  }
}
</style>
