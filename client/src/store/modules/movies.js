import axios from "axios";
import _ from "lodash";

import SERVER from "@/API/url";

export default {
  state: {
    currentMovieIdx: 0,
    boxOffices: [],
    movieInDecade: {},
    movieDetail: {},
  },

  getters: {
    commentList: (state) => state.movieDetail.comments,
    randomMovie: (state) => _.sample(state.movieInDecade["2020s"]),
  },

  mutations: {
    SET_CURRENTMOVIEIDX(state, index) {
      state.currentMovieIdx = index;
    },
    SET_BOXOFFICES(state, boxOffices) {
      state.boxOffices = boxOffices;
    },
    SET_MOVIEINDECADE(state, movieData) {
      state.movieInDecade = movieData;
    },
    FETCH_MOVIE_DETAIL(state, movieDetail) {
      state.movieDetail = movieDetail;
    },
  },

  actions: {
    fetchBoxOffices({ commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.boxOffices)
        .then((res) => commit("SET_BOXOFFICES", res.data))
        .catch((err) => console.error(err.res.data));
    },
    fetchMovieInDecade({ commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.movieDays)
        .then((res) => commit("SET_MOVIEINDECADE", res.data))
        .catch((err) => console.error(err.res.data));
    },
    fetchMovieDetail({ commit }, movieId) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.detail + "/" + movieId)
        .then((res) => commit("FETCH_MOVIE_DETAIL", res.data))
        .catch((err) => console.error(err.res.data));
    },
    createComment(context, commentItem) {
      axios
        .post(
          SERVER.URL +
            SERVER.ROUTES.detail +
            "/" +
            commentItem.movieId +
            "/comments",
          {
            userId: commentItem.userId,
            context: commentItem.context,
          }
        )
        .then((res) => console.log(res.data))
        .catch((err) => console.error(err.res.data));
    },
  },
};
