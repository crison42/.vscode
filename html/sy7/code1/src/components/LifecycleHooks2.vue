<!-- 生命周期函数 -->
<template>
  请输入书籍关键字：
  <input type="text" v-model="state.mytext" />
  <p></p>
  查询结果：
  <ul>
    <li v-for="(item, index) in computedList"  :key="index">
      {{ item }}
    </li>
  </ul>
</template>

<script setup>
import { reactive, onMounted,computed } from 'vue'
const state = reactive({
  mytext: '',
  list: []
})
onMounted(() => {   //生命周期函数onMounted,经常在该函数中获取组件所需要的数据
  fetch('/src/assets/test.json')   //利用fetch从test.json中异步获取数据
    .then(res => res.json())
    .then(res => {
      state.list = res.list    //res.list即获取到的数据
      console.log(state.list)  //可以在控制台下查看获取的数据
    })
})
const computedList = computed(() => {   //根据关键字，计算查询结果
  const newlist = state.list.filter(item => item.includes(state.mytext))
  return newlist
})
</script>