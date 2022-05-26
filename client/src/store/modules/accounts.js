import axios from "axios";
// import _ from "lodash";

import SERVER from "@/API/url";
import router from "@/router";

export default {
  state: {
    token: localStorage.getItem("token") || "",
    currentUser: {},
    profile: {},
    authError: null,
  },

  getters: {
    isLoggedIn: (state) => !!state.token,
    currentUser: (state) => state.currentUser,
    profile: (state) => state.profile,
    authError: (state) => state.authError,
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),
  },

  mutations: {
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, profile) => (state.profile = profile),
    SET_AUTH_ERROR: (state, error) => (state.authError = error),
  },

  actions: {
    saveToken({ commit }, token) {
      commit("SET_TOKEN", token);
      localStorage.setItem("token", token);
    },

    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.removeItem("token");
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.signin,
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          router.push({ name: "BoxOffice" });
        })
        .catch((err) => {
          console.error(err.response.data);
          commit("SET_AUTH_ERROR", err.response.data);
        });
    },

    logout({ getters, dispatch }) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.signout,
        method: "post",
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch("removeToken");
          alert("성공적으로 logout");
          router.push({ name: "login" });
        })
        .catch((err) => {
          console.error(err.response);
        });
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.signup,
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          router.push({ name: "BoxOffice" });
        })
        .catch((err) => {
          console.error(err.response.data);
          commit("SET_AUTH_ERROR", err.response.data);
        });
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.user,
          method: "get",
          headers: getters.authHeader,
        })
          .then((res) => commit("SET_CURRENT_USER", res.data))
          .catch((err) => {
            if (err.response.status === 401) {
              dispatch("removeToken");
              router.push({ name: "login" });
            }
            console.error(err.response);
          });
      }
    },
  },
};
