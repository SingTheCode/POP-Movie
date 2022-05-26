import axios from "axios";
import SERVER from "@/API/url";

export default {
  state: {
    currentMovieIdx: 0,
    boxOffices: [],
    randomMovie: {},
    moviesInDecade: {},
    movieDetail: {},
    commentList: [],
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
    FETCH_MOVIE_DETAIL(state, movieDetail) {
      state.movieDetail = movieDetail;
      state.commentList = movieDetail.comments;
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
