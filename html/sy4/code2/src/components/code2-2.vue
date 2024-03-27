<template>
    <h6>2213 常洪</h6>
    <h1 align="center">软工XXX班XXX</h1>
        <h1>{{ msg1 }}</h1>
        <button @click="add">{{ msg2 }}</button>
        <h2 @click="change">姓名：{{ obj.name }}--年龄：{{ obj.age }}--性别：{{ obj.sex }}</h2>
        <h3 @click="change2">姓名：{{ name }}--年龄：{{ age }}--性别：{{ obj.sex }}</h3>
        <h3>猫的名字：{{ cat.cname }}--猫的颜色：{{ cat.color }}--爱好：{{ cat.hobby }}</h3>
        <h3 @click="change3">猫的名字：{{ cname }}--猫的颜色：{{ color }}--爱好：{{ hobby }}</h3>
</template>

<script setup>
import { ref, reactive, toRef, toRefs } from 'vue';
// ref()函数用于将数据转换成响应式数据，其参数为数据，返回值为转换后的响应式数据
// ref()函数一般用于定义简单类型数据，它定义的数据在修改值或获取值时需要.value;在模版中式用时可以省略.value 
const msg1 = ref("洛阳牡丹甲天下！")
setTimeout(() => {
    msg1.value = "花开时节东京城！"
}, 3000)
const msg2 = ref(10)
const add = () => {
    msg2.value++
}

// reactive()函数用于创建一个响应式对象或数组,可以定义复杂数据类型
const obj = reactive({
    name: '张三',
    age: 20,
    sex: '男'
})
const change = () => {
    obj.name = "李四"
    obj.age = 40
}

// 当在模版中渲染数据时，不希望有前缀的时候可以使用toRef()函数
// toRef()函数用于将响应式对象中的单个属性转换为响应式数据，并且值是关联的。
const name = toRef(obj, 'name')
const age = toRef(obj, 'age')
const change2 = () => {
    name.value = "李四"
    age.value = 40
}
//toRefs()函数用于将响应式对象中的所有属性转换为单独的响应式数据，
// 通常用于reactive定义的对象，并且值是关联的
const cat = reactive({
    cname: '小花花',
    color: '黄色',
    hobby: '捉老鼠'
})
const { cname, color, hobby } = toRefs(cat)
const change3 = () => {
    cname.value = "小黄黄"
    color.value = '白色'
    hobby.value = '上窜下跳'
}
</script>

<style scoped>
h1,
h2,
h3 {
    background-color: pink;
}
</style>