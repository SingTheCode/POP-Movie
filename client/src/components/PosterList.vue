<template>
  <div id="poster-list">
    <swiper ref="mySwiper" :options="swiperOption" @slideChange="slideChangeTransitionStart">
      <swiper-slide v-for="(src, index) in posterSrcList" :key="index"
      ><img :src="src" alt="poster"
      /></swiper-slide>
    </swiper>
  </div>
</template>

<script>
import {Swiper, SwiperSlide, directive} from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  data() {
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
      },
    };
  },
  methods: {
    slideChangeTransitionStart: function () {
      this.$store.commit('SET_CURRENTMOVIEIDX', this.swiper.activeIndex);
    },
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.$swiper;
    }
  },
  components: {
    Swiper,
    SwiperSlide,
  },
  directives: {
    swiper: directive,
  },
  props: {
    posterSrcList: Array,
  },
};
</script>

<style scoped>
#poster-list {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50vw;
  height: 70vh;
}

.swiper {
  width: 100%;
  height: 100%;
  padding-top: 50px;
  padding-bottom: 50px;
}

.swiper-slide {
  background-position: center;
  background-size: cover;
  width: 300px;
  height: 400px;
}

.swiper-slide img {
  display: block;
  width: 100%;
}
</style>
