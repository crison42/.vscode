<!-- Vue 3支持选项式API和组合式API。其中，选项式API是从Vue 2开始使用的一种写法，而Vue 3新增了组合式API的写法。-->
<!-- 选项式API-->
<template>
    <h1>{{ msg }}</h1>
    <h1>{{ count }}</h1>
    <button @click="addNumber">+1</button>
    <input type="text" v-model="val">
    <h1>{{ message }}</h1>
</template>
<!-- 选项式API是一种通过包含多个选项的对象来描述组件逻辑的API，
    其常用的选项包括data、methods、computed、watch等。
 -->
<script>
export default {
    data() { // 定义数据
        return {
            msg: 'Hello Vue3.0!',
            count: 0,
            val: ''
        }
    },
    methods: {// 定义方法
        addNumber() {
            this.count++
        }
    },
    watch: {   //定义侦听器
        val: function(){
            console.log('哈哈哈哈哈！')
        }
    },
    computed: { // 定义计算属性
        message: function(){
            return this.val + "-----你好！"
        }
    }
}
</script>