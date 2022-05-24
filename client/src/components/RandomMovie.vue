<template>
  <div id="random-movie">
    <img :src="posterSrc" alt="random movie">
  </div>
</template>

<script>
export default {
  name: "RandomMovie",
  computed: {
    posterSrc: function () {
      return this.$store.state.randomMovie.posterSrc;
    },
    posterId: function () {
      return this.$store.state.randomMovie.id;
    }
  }
}
</script>

<style scoped>
#random-movie {
  position: relative;
  top: 3rem;
  width: 100vw;
  height: 45vh;
}

img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>