<template>
  <v-app id="app" class="wrapper">
    <Header/>
    <v-main class="">
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

import Header from "@/components/Header";

export default {
  name: 'App',
  components: {Header},
  mounted() {
    // this.$store.dispatch('refresh');
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

#nav a {
  font-weight: bold;
  color: blue;
}

main {
  min-height: 600px;
}

footer {
  font-size: 20pt;
}

footer .jumbotron {
  height: 160px;
}
</style>
