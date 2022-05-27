<template>
  <div id="box-office">
    <box-office-item :boxOfficeItem="boxOfficeItem"></box-office-item>
    <poster-list :posterSrcList="posterSrcList"></poster-list>
  </div>
</template>

<script>
import BoxOfficeItem from "@/components/BoxOfficeItem";
import PosterList from "@/components/PosterList";
import {IMAGE_BASE_URL} from "@/util/config";

export default {
  name: "BoxOffice",
  components: {
    BoxOfficeItem,
    PosterList,
  },
  mounted() {
    this.$store.dispatch('fetchBoxOffices');
  },
  computed: {
    posterSrcList: function () {
      return this.$store.state.movies.boxOffices.map(boxOffice => IMAGE_BASE_URL + boxOffice.poster_path);
    },
    boxOfficeItem: function () {
      const currentIdx = this.$store.state.movies.currentMovieIdx;
      return this.$store.state.movies.boxOffices[currentIdx];
    },
  },
};
</script>

<style scoped>
#box-office {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>