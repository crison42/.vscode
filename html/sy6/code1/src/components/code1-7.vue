<!-- 绑定style属性,设置元素样式-->
<template>
    <h1 align="center">软工2213班常洪</h1>
    <h1 style="width:300px;color:red;">{{ msg }}</h1>
    <!-- 绑定对象，直接将样式写成对象,对象中的属性如果有连词符，必须加引号-->
    <h1 :style="{ 'width': '300px', 'color': '#fff', 'background-color': 'red' }">{{ msg }}</h1>
    <h1 :style="[{ 'width': '300px', 'color': '#fff' }, { backgroundColor: 'red' }]">{{ msg }}</h1>
    <h1 :style="{ 'color': activeCol, 'font-size': size + 'px' }">{{ msg }}</h1>
    <h1 :style="{ backgroundColor: isBlue ? 'blue' : 'black', width: '200px' }">{{ msg }}</h1>
    <h1 :style="styleObj1">{{ msg }}</h1>
    <h1 :style="[styleObj1, styleObj2]">{{ msg }}</h1>
    <h1 :style="[flag ? styleObj1 : styleObj2]">{{ msg }}</h1>
    <h1 :style="styleArr">{{ msg }}</h1>
</template>

<script setup>
import { reactive, ref, computed } from 'vue'
const msg = "花开时节东京城！"
const activeCol = ref('yellow')
const size = ref(50)
const isBlue = ref(true)
const styleObj1 = reactive({
    color: 'red',
    fontSize: '25px'
})
const styleObj2 = reactive({
    backgroundColor: 'pink'
})
const flag = ref(true)
const styleArr = reactive([styleObj1, styleObj2])
</script>
<style scoped></style>