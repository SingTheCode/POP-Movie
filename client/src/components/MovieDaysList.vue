<template>
  <div id="movie-days-list">
    <movies-in-decade
        v-for="(decade, index) in decades"
        :moviesInDecade="movieList[decade]"
        :decade="decades[index]"
        :key="index"
    ></movies-in-decade>
  </div>
</template>

<script>
import MoviesInDecade from "@/components/MovieItemList";

export default {
  name: "MovieDaysList",
  components: {
    MoviesInDecade,
  },
  computed: {
    movieList: function () {
      return this.$store.state.movies.moviesInDecade;
    },
    decades: function () {
      return Object.keys(this.$store.state.movies.moviesInDecade);
    },
  },
};
</script>

<style scoped>
#movie-days-list {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 8rem;
  width: 100%;
  font-weight: 600;
  font-size: 28px;
}
</style>
