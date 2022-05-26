<template>
  <div id="movie-in-decade">
    <RandomMovie/>
    <MovieDaysList/>
  </div>
</template>

<script>
import RandomMovie from "@/components/RandomMovie";
import MovieDaysList from "@/components/MovieDaysList";

export default {
  name: "MovieInDecadeView",
  components: {
    RandomMovie,
    MovieDaysList
  },
  mounted() {
    this.$store.dispatch("fetchMovieInDecade");
  },
};
</script>

<style scoped>
#movie-in-decade {
  postion: relative;
  width: 100%;
  height: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
</style>
