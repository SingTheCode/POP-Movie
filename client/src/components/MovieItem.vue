<template>
  <div id="movie-item">
    <RouterLink :to="goToMovieDetail"><img :src="posterPath"/></RouterLink>
  </div>
</template>

<script>
import {IMAGE_BASE_URL} from "@/util/config.js";

export default {
  name: "MovieItem",
  props: {
    movie: Object,
  },
  computed: {
    posterPath() {
      return IMAGE_BASE_URL + this.movie.poster_path;
    },

    goToMovieDetail() {
      return `/movie/${this.movie.id}`;
    }
  }
};
</script>

<style scoped>
#movie-item {
  display: block;
  width: 200px;
}

img {
  width: 15rem;
  height: 20rem;
  object-fit: contain;
}
</style>
