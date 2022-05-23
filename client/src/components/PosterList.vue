<template>
  <div id="poster-list">
    <swiper ref="mySwiper" :options="swiperOption">
      <swiper-slide><img
        src="https://swiperjs.com/demos/images/nature-1.jpg" alt="poster"/></swiper-slide>
      <swiper-slide><img
          src="https://swiperjs.com/demos/images/nature-1.jpg" alt="poster"/></swiper-slide>
      <swiper-slide><img
          src="https://swiperjs.com/demos/images/nature-1.jpg" alt="poster"/></swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  data () {
    return {
      swiperOption: {
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: "auto",
        coverflowEffect: {
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows: true,
        },
        pagination: true,
      }
    }
  },
  components: {
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  }
}
</script>

<style scoped>
  #poster-list {
    width: 50vw;
  }

  .swiper {
    width: 100%;
    padding-top: 50px;
    padding-bottom: 50px;
  }

  .swiper-slide {
    background-position: center;
    background-size: cover;
    width: 300px;
    height: 300px;
  }

  .swiper-slide img {
    display: block;
    width: 100%;
  }
</style>