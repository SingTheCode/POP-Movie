<template>
  <div id="movie-item-list">
    <div id="decade">{{ decade }}</div>
    <div id="movie-list">
      <swiper ref="mySwiper" :options="swiperOption">
        <swiper-slide
            v-for="movie in movieInDecade"
            :key="movie.id"
        >
          <movie-item
              :movie="movie"
          />
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script>
import {Swiper, SwiperSlide, directive} from "vue-awesome-swiper";
import "swiper/css/swiper.css";

import MovieItem from "@/components/MovieItem";

export default {
  name: "MoviesItemList",
  data() {
    return {
      swiperOption: {
        grabCursor: true,
        centeredSlides: false,
        slidesPerView: "8",
        pagination: {
          clickable: true,
        },
        breakpoints: {
          769: {
            slidesPerView: 7,
            slidesPerGroup: 3,
          },
        },
        scrollbar: true,
        navigation: true,
      },
    };
  },
  props: {
    movieInDecade: Array,
    decade: String,
  },
  components: {
    MovieItem,
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive,
  },
};
</script>

<style scoped>
#movie-item-list {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 2rem 0;
}

#decade {
  padding-left: 3rem;
  padding-bottom: 1rem;
}

#movie-list {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 100vw;
  overflow: hidden;
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

</style>
