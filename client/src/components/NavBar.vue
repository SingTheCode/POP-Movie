<template>
  <div id="navbar">
    <ul>
      <div id="left-li">
        <li @click="selectPage">
          <RouterLink to="/" id="logo">POP Movie</RouterLink>
        </li>
        <li id="box-office" @click="selectPage">
          <RouterLink to="/" :class="{ selected: isBoxOfficeSelected }"
          >Box Office
          </RouterLink>
        </li>
        <li id="movie-days" @click="selectPage">
          <RouterLink
              to="/movieindecade"
              :class="{ selected: isMovieDaysSelected }"
          >Movie Days
          </RouterLink>
        </li>
      </div>
      <div class="log-box" v-if="isLoggedIn">
        <li id="username">{{ currentUser.username }}</li>
        <li id="logout" @click="logoutHandler">Sign out</li>
      </div>
      <div class="log-box" v-else>
        <li>
          <RouterLink to="/login">Sign in</RouterLink>
        </li>
        <li id="sign-up">
          <RouterLink to="/signup">Sign up</RouterLink>
        </li>
      </div>
    </ul>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty("--vh", `${vh}px`);
window.addEventListener("resize", () => {
  let vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty("--vh", `${vh}px`);
});

export default {
  name: "NavBar",
  data: function () {
    return {
      selected: "selected",
      isBoxOfficeSelected: true,
      isMovieDaysSelected: false,
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
  },
  methods: {
    selectPage() {
      const url = window.location.pathname;

      if (url === "/") {
        this.isBoxOfficeSelected = true;
        this.isMovieDaysSelected = false;
      }

      if (url === "/movieindecade") {
        this.isMovieDaysSelected = true;
        this.isBoxOfficeSelected = false;
      }
    },
    ...mapActions(["logout"]),
    logoutHandler() {
      console.log("check");
      if (this.isLoggedIn) {
        this.logout();
      } else {
        alert("잘못된 접근!");
      }
    },
  },
};
</script>

<style scoped>
#navbar {
  position: fixed;
  top: 0;
  padding: 0 2rem;
  width: 100vw;
  height: 3rem;
  background-color: #1a1b1e;
  color: white;
  z-index: 2;
}

ul {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0;
  height: 100%;
}

#left-li {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  width: 26rem;
}

.log-box {
  display: flex;
  justify-content: space-evenly;
  width: 13rem;
}

li {
  font-weight: 600;
  font-size: small;
  list-style-type: none;
}

li > a {
  color: white;
  text-decoration: none;
}

#logo {
  font-weight: 700;
  font-size: x-large;
}

#sign-up > a {
  color: #b1fd00;
}

.selected {
  color: #b1fd00;
}
</style>
