组件code1-6.vue代码如下：
<!-- 绑定class属性,设置元素样式-->
<template>
    <h1 align="center">软工2213班常洪</h1>
    <h2 class="red bor">{{ msg }}</h2>
    <!-- 绑定字符串 -->
    <h2 :class="classval">{{ msg }}</h2>
    <!-- 绑定对象-->
    <h2 :class="{ red: isActive }" class="bb" @click="isActive = !isActive">{{ msg }}</h2>
    <!-- 在使用v-bind绑定class属性时，如果不想将对象类型的class属性值直接写在模板中， -->
    <!-- 可以将属性值定义成一个响应式对象或一个返回对象的计算属性 -->
    <h2 :class="classObj1">{{ msg }}</h2>
    <h2 :class="classObj2">{{ msg }}</h2>
    <!-- 绑定数组，数组中的每个元素为要绑定的类名 -->
    <h2 :class="['red', 'bor']">{{ msg }}</h2>
    <h2 :class="[classNam1, classNam2]">{{ msg }}</h2>
    <!-- 在数组中使用三元表达式 -->
    <h2 :class="['red', 'bor', flag ? 'italic' : '']">{{ msg }}</h2>
    <!-- 在数组中使用对象来代替三元表达式，提高代码的可读性 -->
    <h2 :class="['red', 'bor', { 'italic': flag }]">{{ msg }}</h2>
</template>

<script setup>
import { reactive, ref, computed } from 'vue'
const msg = "洛阳牡丹甲天下！"
const classval = 'red bor'
const isActive = ref(true)
const classObj1 = reactive({ red: true, bor: true })
const classObj2 = computed(() => ({
    red: isActive.value,
    italic: isActive.value
}))
const classNam1 = ref('red')
const classNam2 = ref('bor')
const flag = ref(true)
</script>

<style scoped>
.red {
    color: red;
}

.bor {
    width: 300px;
    border: 5px dashed yellow;
}

.italic {
    font-style: italic;
}
</style>