<template>
  <div id="login-view">
    <h1>Login</h1>

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input
            v-model="credentials.username"
            type="text"
            id="username"
            required
        />
      </div>

      <div>
        <label for="password">password: </label>
        <input
            v-model="credentials.password"
            type="password"
            id="password"
            required
        />
      </div>

      <button>Login</button>
    </form>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "LoginView",
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  computed: {},
  methods: {
    ...mapActions(["login"]),
  },
};
</script>

<style scoped>
#login-view {
  width: 100vw;
  height: 100vh;
}
</style>
