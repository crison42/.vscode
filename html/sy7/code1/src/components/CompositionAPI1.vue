<!-- 组合式API-->
<template>
    <h1>{{ msg }}</h1>
    <h1>{{ count }}</h1>
    <button @click="addNumber">+1</button>
    <input type="text" v-model="val">
    <h1>{{ message }}</h1>
</template>
<!-- 相比于选项式API，组合式API是将组件中的数据、方法、计算属性、侦听器
    等代码全部组合在一起，写在setup()函数中。-->
<script>
import { ref, watch, computed }  from 'vue'
export default {
    setup() {
        const msg = ref('Hello Vue3.0!')
        const count = ref(0)
        const addNumber = () => {
            count.value++
        }
        const val = ref('')
        watch(val, () => {
            console.log('哈哈哈哈哈！')
        })
        const message = computed(() => {
            return val.value + "-----你好！"
        })
        return {msg,count,addNumber,val,message}
    }
}
</script>