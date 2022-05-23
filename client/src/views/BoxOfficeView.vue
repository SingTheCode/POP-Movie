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
  computed: {
    posterSrcList: function () {
      return this.$store.state.boxOffices.posterSrc;
    },
    boxOfficeItem: function () {
      const currentIdx = this.$store.state.currentMovieIdx;
      return this.$store.state.boxOffices[currentIdx];
    },
  },
};
</script>

<style scoped>
#box-office {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>