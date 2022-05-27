<template>
  <div id="login-view">

    <form @submit.prevent="login(credentials)">
      <div class="input-div">
        <label for="username">username</label>
        <input
            v-model="credentials.username"
            type="text"
            id="username"
            required
        />
      </div>

      <div class="input-div">
        <label for="password">password</label>
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 40rem
}

.input-div {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding-bottom: 1rem;
}

button {
  width: 5rem;
  height: 2rem;
  background-color: #b1fd00;
  color: black;
  font-size: 0.9rem;
  font-weight: 600;
  border-style: none;
  border-radius: 8px;
}


</style>
