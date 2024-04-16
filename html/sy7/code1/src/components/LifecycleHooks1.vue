<!-- 生命周期函数 -->
<template>
    <div class="container">container</div>
</template>
<script setup>
import { onBeforeMount, onMounted } from 'vue'
onBeforeMount(() => {
    console.log('DOM元素渲染前', document.querySelector('.container'))
})
onMounted(() => {
    console.log('DOM元素渲染后', document.querySelector('.container'))
})
</script>