<template>
    <button @click="goBack">后退</button>
    <h4>用户{{ id }}的详情页面</h4>
</template>

<script setup>
import { useRouter } from 'vue-router'
//用自定义属性接受参数
const props = defineProps({
    id: String
})
const router = useRouter()
//编程式导航实现后退功能
const goBack = () => {
    router.back()
}
</script>

<style scoped>
button {
    background-color: #409eff;
    color: #fff;
}
</style>