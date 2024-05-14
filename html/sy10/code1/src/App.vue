<template>
  <button v-for="(item,index) in tabsName" :key="item" 
  :class="['tab-button',{active:current==index}]" @click="change(index)">
  {{item}}</button>
  <component :is="currentCom"></component>
</template>

<script setup>
import {ref, shallowRef,computed} from 'vue'
import MyHome from './components/MyHome.vue'
import MyPosts from './components/MyPosts.vue'
import MyActive from './components/MyActive.vue'
const current=ref(0)
const tabsName=['学校主页','校内新闻','大千世界']
const tabsComName=[MyHome,MyPosts,MyActive]
const currentCom=shallowRef(MyHome)
const change=(index)=>{
  currentCom.value=tabsComName[index]
  current.value=index
}
// 采用计算属性
// const change=(index)=>{
//   current.value=index
// }
// const currentCom=computed(()=>{
//   return tabsComName[current.value]
// })
</script>
<style scoped>
.tab-button{
  padding: 6px 10px;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
  border: 1px solid #ccc;
  cursor: pointer;
  background: #f0f0f0;
  margin-bottom: -1px;
  margin-right: -1px;
}
.tab-button:hover{
  background: #f5d1d1;
}
.tab-button.active{
  background: #e0e0e0;
}
.demo-tab
{border: 1px solid #ccc;
padding: 20px;
font-size: 30px;}
</style>