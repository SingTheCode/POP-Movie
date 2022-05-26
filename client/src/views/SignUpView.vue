<template>
  <div id="sign-up">
    <form @submit.prevent="signup(credentials)">
      <div class="signup-box">
        <label for="username">Username</label>
        <input v-model="credentials.username" type="text" id="username" required/>
      </div>
      <div class="signup-box">
        <label for="password1">Password</label>
        <input v-model="credentials.password1" type="password" id="password1" required/>
      </div>
      <div class="signup-box">
        <label for="password2">Confirm Password</label>
        <input v-model="credentials.password2" type="password" id="password2" required/>
      </div>
      <button>Signup</button>
    </form>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "SignUpView",
  components: {},
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {},
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style scoped>
#sign-up {
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

.signup-box {
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