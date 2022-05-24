<template>
  <div id="movie-days">
    <RandomMovie/>
    <MovieDaysList/>
  </div>
</template>

<script>
import RandomMovie from "@/components/RandomMovie";
import MovieDaysList from "@/components/MovieDaysList";

export default {
  name: "MovieDaysView",
  components: {
    RandomMovie,
    MovieDaysList
  },
  mounted() {
    this.$store.dispatch("fetchMovieDays");
  },
};
</script>

<style scoped>
#movie-days {
  postion: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
</style>
