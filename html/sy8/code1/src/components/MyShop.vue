<template>
  <h1 style="text-align: center;">软工2213班常洪</h1>
  <table border="1" align="center" width="400px">
    <caption>
      <h2>购物车</h2>
    </caption>
    <tr align="center">
      <td>名称</td>
      <td>单价</td>
      <td>数量</td>
      <td>合计</td>
    </tr>
    <tr align="center" v-for="(item, index) in list" :key="item.id">
      <td>{{ item.name }}</td>
      <td>{{ item.price }}</td>
      <td>
        <button @click="sub(index)" :disabled="item.count == 0 ? true : false">-</button>
        {{ item.count }}
        <button @click="add(index)">+</button>
      </td>
      <td>{{ item.price * item.count }}</td>
    </tr>
    <tr align="center">
      <td>总价</td>
      <td colspan="3">{{ total }}</td>
    </tr>
  </table>
</template>

<script setup>
import { reactive, computed } from 'vue'
const list = reactive([
  { id: 1, name: '华为mate30', price: 4566, count: 2 },
  { id: 2, name: '华为mate40', price: 4166, count: 3 },
  { id: 3, name: '苹果X', price: 5200, count: 2 },
  { id: 4, name: 'OPPO', price: 2180, count: 4 }
])
const add = (index) => {
  list[index].count++
  total()
}
const sub = (index) => {
  list[index].count--
  total()
}
const total = computed(() => {
  let sum = 0
  list.forEach(item => {
    sum += item.price * item.count
  })
  return sum
})
</script>