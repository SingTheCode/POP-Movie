<template>
  <div id="box-office">
    <box-office-item :boxOfficeItem="boxOfficeItem"></box-office-item>
    <poster-list :posterSrcList="posterSrcList"></poster-list>
  </div>
</template>

<script>
import BoxOfficeItem from "@/components/BoxOfficeItem";
import PosterList from "@/components/PosterList";

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
      return this.$store.state.movies.boxOffices.map(boxOffice => boxOffice.posterSrc);
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