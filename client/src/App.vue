<template>
  <div id="app">
    <NavBar></NavBar>
    <RouterView></RouterView>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";

export default {
  name: "App",
  components: {
    NavBar,
  },
  computed: {},
};
</script>

<style>
#app {
  width: 100vw;
  height: 100%; /* 혹시나 Custom Property 지원 안하는 브라우저를 위한 복귀점(Fallback) */
  color: white;
  background-color: #1a1b1e;
  font-family: "Open Sans", sans-serif;
  font-weight: 600;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
