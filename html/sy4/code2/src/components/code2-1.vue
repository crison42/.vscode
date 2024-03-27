<template>
    <h6>2213 常洪</h6>
    <h1>河南科技大学软件学院</h1>
    <h2>{{ msg }}</h2>
    <h2>{{ num1 + num2 }}</h2>
    <h2>{{ num1 > num2 }}</h2>
    <h2>{{ flag ? 'YES' : 'NO' }}</h2>
    <h2>{{ arr[3] }}</h2>
    <h2>{{ obj.name }}</h2>
    <div>
        欢迎学习Vue3.0
    </div>
</template>
<script setup>
var msg = 'Hello Vue3.0'
setTimeout(() => {
    msg = '锲而不舍，金石可镂'
}, 2000)
const num1 = 10
const num2 = 20
const flag = 1
const arr = [11, 22, 33, 44]
const obj = { name: '张三', age: 20, sex: "男" }
</script>
<style scoped>
h1 {
    color: red;
    background-color: aqua;
}

div {
    width: 300px;
    height: 200px;
    background-color: bisque;
    font-style: 30px;
}
</style>