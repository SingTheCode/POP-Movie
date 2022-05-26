import axios from "axios";
import _ from "lodash";

import SERVER from "@/API/url";

export default {
  state: {
    currentMovie: {},
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
    SET_CURRENT_MOVIE(state, movie) {
      state.currentMovie = movie;
    },
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
    setCurrentMovie({commit}, movieIdx) {
      commit(
        "SET_CURRENT_MOVIE",
        this.state.movies.boxOffices[Number(movieIdx)]
      );
    },

    fetchCurrentIdx({commit, dispatch}, movieIdx) {
      commit("SET_CURRENTMOVIEIDX", movieIdx);
      dispatch("setCurrentMovie", movieIdx);
    },

    fetchBoxOffices({commit}) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.boxOffices,
        method: "get",
        headers: this.getters.authHeader,
      })
        .then((res) => {
          commit("SET_BOXOFFICES", res.data);
        })
        .catch((err) => console.error(err.res.data));
    },

    fetchMovieInDecade({commit}) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.movieDays,
        method: "get",
        headers: this.getters.authHeader,
      })
        .then((res) => commit("SET_MOVIEINDECADE", res.data))
        .catch((err) => console.error(err.res.data));
    },

    fetchMovieDetail({commit}, movieId) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.detail + movieId,
        method: "get",
        headers: this.getters.authHeader,
      })
        .then((res) => commit("FETCH_MOVIE_DETAIL", res.data))
        .catch((err) => console.error(err.res.data));
    },

    createComment(context, commentItem) {
      axios({
        url:
          SERVER.URL + SERVER.ROUTES.detail + commentItem.movieId + "/comments",
        method: "post",
        headers: this.getters.authHeader,
        data: {
          userId: this.getters.currentUser.username,
          content: commentItem.context,
        },
      })
        .then((res) => console.log(res.data))
        .catch((err) => console.error(err.res.data));
    },
  },
};
