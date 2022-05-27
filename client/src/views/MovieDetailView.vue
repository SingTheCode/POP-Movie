<template>
  <div id="movie-detail">
    <MovieTrailer/>
    <DetailInfo/>
    <CommentBox/>
  </div>
</template>

<script>
import MovieTrailer from "@/components/MovieTrailer";
import DetailInfo from "@/components/DetailInfo";
import CommentBox from "@/components/CommentBox";

export default {
  name: "MovieDetailView",
  components: {
    MovieTrailer,
    DetailInfo,
    CommentBox,
  },
  created() {
    const movieId = this.$route.params.id;
    this.$store.dispatch("fetchMovieDetail", movieId);
  },
}
</script>

<style scoped>
#movie-detail {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  width: 60vw;
  height: 100%;
}
</style>