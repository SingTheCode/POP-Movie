import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentMovieIdx: 0,
    boxOffices: [
      {
        rank: 1,
        title: "Movie Title",
        releaseDate: "April 8, 2022",
        maxTheather: 4258,
        gross: 145829424,
        posterSrc: "slkfjasiofj.jpg",
      },
      {
        rank: 2,
        title: "Movie Title",
        releaseDate: "April 8, 2022",
        maxTheather: 4258,
        gross: 145829424,
        posterSrc: "slkfjasiofj.jpg",
      },
    ],
  },
  getters: {},
  mutations: {},
  actions: {},
  modules: {},
});
