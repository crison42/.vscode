<template>
    <input type="text" v-model.trim.number="n1">
    <select v-model="opt">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select>
    <input type="text" v-model.trim.number="n2">
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
            result.value = n1.value + n2.value;
            break;
        case '-':
            result.value = n1.value - n2.value;
            break;  
        case '*':
            result.value = n1.value * n2.value;
            break;
        case '/':
            result.value = n1.value / n2.value;
            break;
        default:
            result.value = 0;
            break;
    }
}
</script>