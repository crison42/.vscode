<!-- 跑马灯案例演示 -->
<template>
    <h6>2213 常洪</h6>
    <button type="button" @click="dong">跑起来</button>
    <button type="button" @click="stop">停止</button>
    <h1>{{ msg }}</h1>
</template>

<script setup>
import { ref } from 'vue';
const msg = ref('古之立大事者，不惟有超世之才，亦必有坚忍不拔之志。——苏轼' + '\t')
const intervalId = null;
const dong = () => {
    if (intervalId != null)
        return;
    intervalId = setInterval(() => {
        var start = msg.value.substring(0, 1);
        var end = msg.value.substring(1);
        msg.value = end + start;
    }, 1000);
}
const stop = () => {
    clearInterval(intervalId);
    intervalId = null;
}
</script>

<style scoped></style>