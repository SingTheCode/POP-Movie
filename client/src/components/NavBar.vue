<template>
  <div id="navbar">
    <ul>
      <div id="left-li">
        <li @click="selectPage">
          <RouterLink to="/" id="logo">POP Movie</RouterLink>
        </li>
        <li id="box-office" @click="selectPage">
          <RouterLink to="/" :class="{selected: isBoxOfficeSelected}">Box Office</RouterLink>
        </li>
        <li id="movie-days" @click="selectPage">
          <RouterLink to="/movieindecade" :class="{selected: isMovieDaysSelected}">Movie Days</RouterLink>
        </li>
      </div>
      <div id="right-li">
        <li>Sign in</li>
        <li id="sign-up">Sign up</li>
      </div>
    </ul>

  </div>
</template>

<script>
let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`)
window.addEventListener('resize', () => {
  let vh = window.innerHeight * 0.01
  document.documentElement.style.setProperty('--vh', `${vh}px`)
})

export default {
  name: "NavBar",
  data: function () {
    return {
      selected: 'selected',
      isBoxOfficeSelected: true,
      isMovieDaysSelected: false,
    }
  },
  methods: {
    selectPage: function () {
      const url = window.location.pathname;

      if (url === "/") {
        this.isBoxOfficeSelected = true;
        this.isMovieDaysSelected = false;
      }

      if (url === "/moviedays") {
        this.isMovieDaysSelected = true;
        this.isBoxOfficeSelected = false;
      }
    }
  }
}
</script>

<style scoped>
#navbar {
  position: fixed;
  top: 0;
  padding: 0 2rem;
  width: 100vw;
  height: 3rem;
  background-color: #1A1B1E;
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

#right-li {
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

#sign-up {
  color: #B1FD00;
}

.selected {
  color: #B1FD00;
}
</style>