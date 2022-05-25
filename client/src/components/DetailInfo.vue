<template>
  <div id="detail-info">
    <div id="item-title">{{ movieDetail.title }}</div>
    <div class="detail-box">
      <div class="info">
        <div id="base-info">{{ movieDetail.releaseDate }} {{ movieDetail.showTime }}</div>
        <div id="item-summary">{{ movieDetail.summary }}</div>
      </div>
      <div class="detail">
        <div id="item-people-name">출연 : {{ movieDetail.peopleName.join(', ') }}</div>
        <div id="item-genre-name">장르 : {{ movieDetail.genreName.join(', ') }}</div>
        <div id="item-gross">관람객 수 : {{ movieDetail.spectatorNum }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DetailInfo",
  computed: {
    movieDetail: function () {
      return this.$store.state.movieDetail;
    }
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

#item-summary {
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