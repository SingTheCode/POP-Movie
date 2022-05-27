<template>
  <div id="movie-days-list">
    <movie-item-list
        v-for="(decade, index) in decades"
        :movieInDecade="movieList[decade]"
        :decade="decades[index]"
        :key="index"
    ></movie-item-list>
  </div>
</template>

<script>
import MovieItemList from "@/components/MovieItemList";

export default {
  name: "MovieDaysList",
  components: {
    MovieItemList,
  },
  computed: {
    movieList: function () {
      return this.$store.state.movies.movieInDecade;
    },
    decades: function () {
      return Object.keys(this.$store.state.movies.movieInDecade);
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
