<!-- 计数器案例演示 -->
<template>
    <h6>2213 常洪</h6>
    <h1 align="center">软工XXX班XXX</h1>
        <button type="button" @click="sub">-</button>
        <span>{{ num }}</span>
        <button type="button" @click="add">+</button>
    </template>
    
    <script setup>
    import { ref } from 'vue';
    const num = ref(0);
    const sub = () => {
        if (num.value > -10) {
            num.value--
        }else
        alert("已经是最小值了！")
        }
    const add = () => {
        if (num.value < 10) {
            num.value++
        }else
        alert("已经是最大值了！")
    }
    </script>
    
    <style scoped>
    button {
        width: 70px;
        height: 40px;
        color: red;
        font-size: 30px;
        line-height: 30px;
        float: left;
    }
    
    span {
        display: block;
        width: 158px;
        height: 38px;
        border: 1px solid red;
        float: left;
        font-size: 40px;
        text-align: center;
        line-height: 38px;
    }
    </style>