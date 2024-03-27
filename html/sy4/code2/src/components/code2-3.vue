<template>
    <h6>2213 常洪</h6>
    <h1 align="center">软工XXX班XXX</h1>
    <p>河南科技大学{{ message }}</p>
    <p v-text="message"></p>
    <p v-html="message"></p>
    <h1 v-html="link"></h1>
    <h1 v-text="link"></h1>
    <p v-html="message + '--------'"></p>
</template>

<script setup>
const message = '<strong>千磨万击还坚劲，任尔东西南北风</strong>'
const link = '<a href="http://www.haust.edu.cn">河南科技大学</a>'
</script>

<style scoped>
p {
    font-size: 25px;
}
</style>