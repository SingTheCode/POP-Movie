<template>
  <div id="movie-trailer">
    <iframe src="https://www.youtube.com/embed/mI9oyFMUlfg?controls=0"
            title="YouTube video player" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
  </div>
</template>

<script>
export default {
  name: "MovieTrailer"
}
</script>

<style scoped>
#movie-trailer {
  position: relative;
  top: 3rem;
  padding-bottom: 56.25%;
}

iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>