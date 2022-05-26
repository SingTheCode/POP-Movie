<template>
  <!--  <div id="random-movie">-->
  <!--    <img :src="posterPath" alt="random movie"/>-->
  <!--  </div>-->
  <div
      @mouseover="mouseOverHandler"
      @mouseleave="mouseLeaveHandler"
      ref="iframe_box"
      id="random-movie"
  >
    <iframe
        :src="videoPath"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
    ></iframe>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import {IMAGE_BASE_URL, YOUTUBE_VIDEO_URL} from "@/util/config";

export default {
  name: "RandomMovie",
  computed: {
    ...mapGetters(["randomMovie"]),
    posterPath() {
      return IMAGE_BASE_URL + this.randomMovie.poster_path;
    },

    videoPath() {
      return YOUTUBE_VIDEO_URL + this.randomMovie.video_key + "?controls=0";
    },
  },
  methods: {
    mouseOverHandler() {
      console.log("hello");
      const iframeBox = this.$refs.iframe_box;
      iframeBox.classList.remove("mouseleave");
      iframeBox.classList.add("mouseover");
    },

    mouseLeaveHandler() {
      const iframeBox = this.$refs.iframe_box;
      iframeBox.classList.remove("mouseover");
      iframeBox.classList.add("mouseleave");
    },
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

iframe {
  width: 100%;
  height: 100%;
}

.mouseover {
  object-fit: cover;
  animation-duration: 1s;
  animation-name: coverall;
  animation-fill-mode: both;
}

.mouseleave {
  object-fit: cover;
  animation-duration: 1s;
  animation-name: reback;
  animation-fill-mode: both;
}

@keyframes coverall {
  from {
    height: 45vh;
  }

  to {
    height: 90vh;
  }
}

@keyframes reback {
  from {
    height: 90vh;
  }

  to {
    height: 45vh;
  }
}
</style>
