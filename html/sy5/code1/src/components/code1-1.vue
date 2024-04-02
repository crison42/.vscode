<!-- 图片切换案例 -->
<template>
    <h1 align="center">软工2213班常洪</h1>
    <h1>洛阳牡丹甲天下,花开时节动京城</h1>
    <div id="box">
        <img :src="'../assets/images/mudan' + imgList + '.jpg'" alt="">
        <a href="javascript:;" @click="left" v-show="imgList > 1">
            <img class="imgl" src="../assets/images/left.png">
        </a>
        <a href="javascript:;" @click="right" v-show="imgList < 10">
            <img class="imgr" src="../assets/images/right.png">
        </a>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const imgList = ref(1)
const left = () => {
    imgList.value--
}
const right = () => {
    imgList.value++
}
</script>

<style scoped>
#box {
    width: 400px;
    margin: 0 auto;
    position: relative;
}

h1 {
    text-align: center;
}

#box>img {
    width: 100%;
    height: 300px;
    /*overflow: hidden;   消除误差*/
    display: block;
    /*消除误差*/
}

a>img {
    width: 30px;
    height: 50px;
    position: absolute;
}

a>.imgl {
    left: 0;
    top: 125px;
}

a>.imgr {
    right: 0;
    top: 125px;
}
</style>