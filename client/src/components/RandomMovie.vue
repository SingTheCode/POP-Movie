<template>
  <div id="random-movie">
    <img :src="randomMovie.posterSrc" alt="random movie"/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "RandomMovie",
  computed: {
    ...mapGetters(["randomMovie"]),
  },
};
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
