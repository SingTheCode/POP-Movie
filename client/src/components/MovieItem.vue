<template>
  <div id="movie-item">
    <img :src="movie.posterSrc"/>
  </div>
</template>

<script>
export default {
  name: "MovieItem",
  props: {
    movie: Object,
  },
  mounted() {
    console.log(this.movie)
  }
};
</script>

<style scoped>
#movie-item {
  display: block;
  width: 100%;
}
</style>
