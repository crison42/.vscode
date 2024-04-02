<!-- 属性key的用法 -->
<template>
    <h1 align="center">软工2213班常洪</h1>
    ID:<input type="text" v-model="id">用户名:<input type="text" v-model="name">
    <input type="button" value="添加" @click="add">
    <p v-for="(item, index) in list" :key="item.idindex">
        <input type="checkbox">{{ item.idindex }}-----{{ item.username }}
    </p>
    <!--注意：key属性使用的时候，必须使用v-bind绑定属性的形式指定key的值 -->
    <!-- 在组件中，使用 v-for循环的时候，或者在一些特殊情况中，必须在使用v-for的同时，指定唯一的字符串/数字类型作为:key的值,如果没有可以让数据本身作为其值-->
</template>

<script setup>
import { reactive, ref } from 'vue'
const id = ref('')
const name = ref('')
const list = reactive([
    { idindex: 1, username: "zhang" },
    { idindex: 2, username: "zhao" },
    { idindex: 3, username: "huang" },
    { idindex: 4, username: "li" },
])
const add = () => {
    list.unshift({ idindex: id.value, username: name.value });  //在前面添加数据
    id.value = ''
    name.value = ''
}
</script>

<style scoped>
input {
    font-size: 20px;
}
</style>