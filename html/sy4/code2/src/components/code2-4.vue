<template>
    <h6>2213 常洪</h6>
    <h1 align="center">软工XXX班XXX</h1>
    <h1 v-on:click="showinfo">咬定青山不放松，立根原在破岩中</h1>
    <h1 v-on:click="add" v-text="num"></h1>
    <h1 @click="change" v-text="msg"></h1>
</template>

<script setup>
import { ref } from 'vue'
const showinfo = () => {
    alert("欢迎学习Vue.js！")
}
const num = ref(10)
function add() {
    num.value++
}
const msg = ref('好雨知时节，当春乃发生')
const change = () => {
    msg.value = '随风潜入夜，润物细无声'
}
</script>

<style scoped></style>