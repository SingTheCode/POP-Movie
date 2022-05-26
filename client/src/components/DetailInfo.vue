<template>
  <div id="detail-info">
    <div id="item-title">{{ movieDetail.original_title }}</div>
    <div class="detail-box">
      <div class="info">
        <div id="base-info">{{ movieDetail.release_date }}</div>
        <div id="item-overview">{{ movieDetail.overview }}</div>
      </div>
      <div class="detail">
        <img v-if="movieDetail.adult" src="@/assets/age-limit.png">
        <div id="item-average">평점 : {{ movieDetail.vote_average }}</div>
        <!--        <div id="item-people-name">출연 : {{ peopleName.join(', ') }}</div>-->
        <div id="item-genre-name">장르 : {{ genreNameList.join(', ') }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DetailInfo",
  computed: {
    movieDetail: function () {
      return this.$store.state.movies.movieDetail;
    },
    peopleName: function () {
      const peopleName = this.$store.state.movies.movieDetail.peopleName;
      return peopleName ? peopleName : '';
    },
    genreNameList: function () {
      const genreNameList = this.$store.state.movies.movieDetail.genre_ids.map(obj => obj.name);
      return genreNameList ? genreNameList : '';
    },

  }
}
</script>

<style scoped>
#detail-info {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  position: relative;
  top: 3rem;
  padding-top: 2rem;
}

#item-title {
  font-weight: 700;
  font-size: 48px;
}

.detail-box {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.info {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  width: 65%;
}

#item-overview {
  padding-top: 2rem;
  text-align: left;
}

.detail {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-left: 3rem;
  width: 30%;
}

.detail > div {
  padding-bottom: 1rem;
}

</style>