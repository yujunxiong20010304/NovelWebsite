<template>
  <!-- 精品推荐 -->
  <div id="fflt">
    <countdown></countdown>
    <freebooks></freebooks>
    <ending></ending>
  </div>
</template>

<script>
import countdown from '@/components/fflt/countdown'
import freebooks from '@/components/fflt/freebooks'

export default {
  name: 'fflt',
  components: {
    countdown,
    freebooks
  }
}
</script>

<style scoped lang="less">
#fflt {
  width: 1020px;
  margin: 0 auto;
  overflow: hidden;
  box-shadow:0 15px 35px rgba(0,0,0,0.08),0 3px 10px rgba(0,0,0,0.005);
}
</style>
