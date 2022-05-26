<template>
  <div id="box-office-item">
    <div id="rank">{{ movieIndex + 1 }}</div>
    <div id="title">{{ boxOfficeItem.original_title }}</div>
    <div id="detail">
      <div id="release-date">
        <div>RELEASE DATE</div>
        <div>{{ boxOfficeItem.release_date }}</div>
      </div>
      <div id="max-theather">
        <div>MAX THEATHER</div>
        <div>{{ boxOfficeItem.vote_average }}</div>
      </div>
      <div id="genre">
        <div>GENRE</div>
        <div>{{ genre }}</div>
      </div>
    </div>
    <button @click="goToMovieDetail">Details</button>
  </div>
</template>

<script>
export default {
  name: "BoxOfficeItem",
  props: {
    boxOfficeItem: {
      // rank: Number,
      original_title: String,
      release_date: String,
      vote_average: String,
      genre_ids: Object,
    },
  },
  methods: {
    goToMovieDetail: function () {
      this.$router.push({
        name: "MovieDetail",
        params: {id: String(this.$store.state.movies.currentMovie.id)},
      });
    },
  },

  computed: {
    movieIndex() {
      return this.$store.state.movies.currentMovieIdx;
    },

    genre() {
      let result = this.boxOfficeItem.genre_ids.map(obj => obj.name);
      return result.join(', ');
    }
  }
};
</script>

<style scoped>
#box-office-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  height: 75vh;
  max-height: 10rem;
  padding: 0 3rem;
}

#rank {
  display: flex;
  padding-bottom: 8rem;
  color: #b1fd00;
  font-size: 5rem;
}

#title {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  font-size: 6rem;
}

#detail {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 38vw;
  max-width: 34rem;
  padding: 3rem 0;
  color: #acacac;
}

#detail > div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 3rem;
}

#genre {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

button {
  width: 7rem;
  height: 3.5rem;
  background-color: #b1fd00;
  color: black;
  font-size: 0.9rem;
  font-weight: 600;
  border-style: none;
  border-radius: 20px;
}
</style>
