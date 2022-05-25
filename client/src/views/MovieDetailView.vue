<template>
  <div id="movie-detail">
    <MovieTrailer/>
    <DetailInfo/>
  </div>
</template>

<script>
import MovieTrailer from "@/components/MovieTrailer";
import DetailInfo from "@/components/DetailInfo";

export default {
  name: "MovieDetailView",
  components: {
    MovieTrailer,
    DetailInfo,
  },
  created() {
    const movieId = this.$route.params.id;
    this.$store.dispatch("fetchMovieDetail", movieId);
  },
}
</script>

<style scoped>
#movie-detail {
  width: 60vw;
  height: 100vh;
}
</style>