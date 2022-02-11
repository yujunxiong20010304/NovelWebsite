<template>
  <!-- 首页轮播图 -->
  <div id="parallax">
    <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../../assets/parallax/one.jpeg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../../assets/parallax/two.jpeg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../../assets/parallax/three.jpeg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../../assets/parallax/four.jpeg" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'parallax'
}
</script>

<style scoped>

</style>
