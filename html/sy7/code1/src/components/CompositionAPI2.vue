<!-- 组合式API—setup语法糖-->
<template>
    <h1>{{ msg }}</h1>
    <h1>{{ count }}</h1>
    <button @click="addNumber">+1</button>
    <input type="text" v-model="val">
    <h1>{{ message }}</h1>
</template>
<!-- Vue提供的选项式API和组合式API这两种写法可以覆盖大部分的应用场景，
    它们是同一底层系统所提供的两套不同的接口。选项式API是在组合式API的基础上实现的。
 -->
 <!-- Vue还提供了setup语法糖，用于简化组合式API的代码 -->
<script setup>
import { ref, watch, computed }  from 'vue'
        const msg = ref('Hello Vue3.0!')
        const count = ref(0)
        const addNumber = () => {
            count.value++
        }
        const val = ref('')
        watch(val, () => {
            console.log('哈哈哈哈哈！')
        })
        const message = computed(() => {
            return val.value + "-----你好！"
        })
</script>