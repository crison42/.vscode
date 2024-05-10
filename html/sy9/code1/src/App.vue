<template>
  <div class="vote-wrapper">
    <h1>请为您最喜欢的人投票</h1>
    <ul>
      <li v-for="item in list" v-bind:key="item.id">
        <div class="img">
          <img v-bind:src="item.avatar" v-bind:alt="item.name">
        </div>
        <greeting v-bind:to="item.name" @toupiao="onClick"></greeting>
      </li>
    </ul>
    <p v-for="(item, index) in appList" v-bind:key="index">
      {{ item.time }} - {{ item.name }} - {{ item.count }}票
    </p>
  </div>
</template>

<script setup>
import Greeting from './components/greeting.vue'
import { reactive } from 'vue'
const list = [
  { id: 1, avatar: '/src/assets/images/jane.png', name: 'Jane' },
  { id: 2, avatar: '/src/assets/images/mike.png', name: 'Mike' },
  { id: 3, avatar: '/src/assets/images/kate.png', name: 'Kate' },
  { id: 4, avatar: '/src/assets/images/tom.png', name: 'Tom' }
]
const appList = reactive([])   //存储投票信息
const onClick = (name, count) => {    //接收子组件传递过来的数据
  console.log(name, count)
  appList.push({ time: new Date().toLocaleTimeString(), name, count });
}
</script>

<style scoped>
.vote-wrapper {
  border: 1px solid #999;
  border-radius: 10px;
  width: 600px;
  margin: auto;
}

.vote-wrapper h1 {
  text-align: center;
}

ul {
  display: flex;
  justify-content: space-around;
  padding: 25px;
  border-top: 1px solid #999;
  margin: 0;
}

li {
  list-style: none;
  text-align: center;
}

li .img {
  width: 110px;
  border: 1px solid #999;
  border-radius: 10px;
  margin-bottom: 20px;
}

li .img img {
  width: 100%;
}

p {
  text-align: center;
}
</style>