<template>
  <div id="movie-trailer">
    <iframe :src="videoPath"
            title="YouTube video player" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
  </div>
</template>

<script>
import {YOUTUBE_VIDEO_URL} from "@/util/config";

export default {
  name: "MovieTrailer",
  computed: {
    videoPath() {
      return YOUTUBE_VIDEO_URL + this.$store.state.movies.movieDetail.video_key + '?controls=0';
    }
  }
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