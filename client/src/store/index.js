import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

import SERVER from "@/API/url";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentMovieIdx: 0,
    boxOffices: [],
    randomMovie: {},
    moviesInDecade: {},
  },
  getters: {},
  mutations: {
    SET_CURRENTMOVIEIDX(state, index) {
      state.currentMovieIdx = index;
    },
    SET_BOXOFFICES(state, boxOffices) {
      state.boxOffices = boxOffices;
    },
    SET_MOVIEDAYS(state, movieData) {
      state.randomMovie = movieData.randomMovie;
      Object.keys(movieData.moviesInDecade).forEach((key) => {
        state.moviesInDecade[key] = movieData.moviesInDecade[key];
      });
    },
  },
  actions: {
    fetchBoxOffices({ commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.boxOffices)
        .then((res) => commit("SET_BOXOFFICES", res.data))
        .catch((err) => console.error(err.res.data));
    },
    fetchMovieDays({ commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.movieDays)
        .then((res) => commit("SET_MOVIEDAYS", res.data))
        .catch((err) => console.error(err.res.data));
    },
  },
  modules: {},
});
