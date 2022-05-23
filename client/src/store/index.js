import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

import SERVER from "@/API/url";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentMovieIdx: 0,
    boxOffices: [],
    movieDecade: [],
  },
  getters: {},
  mutations: {
    SET_BOXOFFICES(state, boxOffices) {
      state.boxOffices = boxOffices;
    },
  },
  actions: {
    fetchBoxOffices({ commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.boxOffices)
        .then((res) => commit("SET_BOXOFFICES", res.data))
        .catch((err) => console.error(err.res.data));
    },
  },
  modules: {},
});
