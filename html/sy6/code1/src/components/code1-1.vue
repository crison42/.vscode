<template>
    <h1 align="center">软工2213班常洪</h1>
    <div id="box">
        <p>
            <input type="text" placeholder="猜数游戏" v-model="val" v-on:input="guessed" />
        </p>
        <p>{{ result }}</p>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const val = ref('')
const result = ref('请猜一个1~100之间的整数')
const key = Math.round(Math.random() * 100)
const guessed = () => {
    const num = parseInt(val.value);
    if (isNaN(num))
        result.value = "请猜一个1~100之间的整数";
    if (num > key)
        result.value = "太大了，往小一点猜!";
    if (num < key)
        result.value = "太小了，往大一点猜!";
    if (num === key) {
        result.value = "祝贺你，你猜对了!";
    }
}
</script>

<style scoped>
div#box {
    width: 300px;
    margin: 30px auto;
    border: 1px solid #666;
    border-radius: 10px;
    padding: 10px;
}

input {
    font-size: 20px;
}

p {
    font-size: 20px;
    text-align: center;
}
</style>