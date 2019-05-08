<template>
  <div id="app">
    <Vheader></Vheader>
    <router-view></router-view>
  </div>
</template>

<script>
import $ from "jquery";
import Vheader from "./components/Vheader";
import "bootstrap/dist/css/bootstrap.min.css";

export default {
  name: "App",
  data() {
    return {};
  },
  components: {
    Vheader
  },
  mounted() {
    this.$store.dispatch("getAllList");
  }
};
</script>

<style>
</style>
