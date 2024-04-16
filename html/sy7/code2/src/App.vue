<template>
  <h1>根组件App.vue</h1>
  <hr>
  <my-com-a></my-com-a>
  <hr>
  <my-com-b></my-com-b>
  <hr>
  <my-com-c></my-com-c>
</template>

<script setup>
import MyComC from './components/ComC.vue'
</script>

<style scoped>
h1{
  background-color: cadetblue;
}
</style>