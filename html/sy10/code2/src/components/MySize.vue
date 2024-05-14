<!-- 私有自定义指令的声明与使用 -->
<template>
    <div id="mydiv">
        <label for="">选择文字大小：</label>
        <select name="" id="" v-model="size">
            <option value="20px">20px</option>
            <option value="30px">30px</option>
            <option value="40px">40px</option>
            <option value="50px">50px</option>
            <option value="60px">60px</option>
        </select>
        <p v-font-size="size">天生我才必有用</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const size = ref("50px")
const vFontSize = {
    mounted: (el, binding) => {  //当被绑定指令的元素挂载后，自动触发mounted函数
        el.style.fontSize = binding.value
    },
    updated: (el, binding) => { //被绑定指令的元素数据更新前更新后调用(可以调用多次)
        el.style.fontSize = binding.value
    }
}
</script>

<style scoped>
#mydiv {
    width: 500px;
    height: 300px;
    background-color: yellow;
    float: left;
}
</style>