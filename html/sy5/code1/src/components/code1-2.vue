<!-- 简单计算器案例 -->
<template>
    <h1 align="center">软工2213班常洪</h1>
    <input type="text" v-model="n1">
    <select v-model="opt">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select>
    <input type="text" v-model="n2">
    <input type="button" value="=" @click="cal">
    <input type="text" :value="result">
</template>

<script setup>

import { ref } from 'vue';

let n1 = ref(0);
let n2 = ref(0);
let opt = ref('+');
let result = ref(0);

function cal() {
    switch (opt.value) {
        case '+':
            result.value = parseFloat(n1.value) + parseFloat(n2.value);
            break;
        case '-':
            result.value = parseFloat(n1.value) - parseFloat(n2.value);
            break;
        case '*':
            result.value = parseFloat(n1.value) * parseFloat(n2.value);
            break;
        case '/':
            result.value = parseFloat(n1.value) / parseFloat(n2.value);
            break;
        default:
            result.value = 0;
            break;
    }
}

</script>

<style scoped>
input,
select {
    font-size: 30px;
}

input[type=button] {
    margin-left: 10px;
    margin-right: 10px;
}
</style>