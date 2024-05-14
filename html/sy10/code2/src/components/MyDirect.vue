<!-- 私有自定义指令的声明与使用 -->
<template>
  <div class="box1">
    <p>第二个input输入框自动获取焦点</p>
    <input type="text" placeholder="请输入内容" /><br /><br />
    <input type="text" v-focus placeholder="请输入内容" />
    <hr>
  </div>
</template>
<script setup>
// 在setup语法糖，任何以“v”开头的驼峰式命名的变量都可以被用作一个自定义指令
const vFocus = {
  mounted: (el) => { //当被绑定指令的元素挂载后，自动触发mounted函数
    el.focus();    //让被绑定的元素自动获取焦点
    el.value = "获取焦点";
  }
}
</script>
<style scoped>
.box1 {
  width: 500px;
  height: 280px;
  border: 1px solid #000;
  background-color: pink;
  float: left;
}
</style>