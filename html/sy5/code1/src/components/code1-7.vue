<template>
    <h1 align="center">软工2213班常洪</h1>
    <button class="btn" @click="add">添加景点</button>
    <table>
        <tr>
            <th>序号</th>
            <th>省份</th>
            <th>省会</th>
            <th>旅游景点</th>
            <th>操作</th>
        </tr>
        <tr v-for="(item, index) in list">
            <td>{{ index + 1 }}</td>
            <td>{{ item.province }}</td>
            <td>{{ item.city }}</td>
            <td>{{ item.spot }}</td>
            <td><button @click="del(index)">删除</button></td>
        </tr>
    </table>
</template>

<script setup>
import { reactive } from 'vue'
const list = reactive([
    { province: "河南省", city: "郑州市", spot: "少林寺" },
    { province: "河南省", city: "洛阳市", spot: "龙门石窟" },
    { province: "湖北省", city: "长沙市", spot: "橘子洲头" },
    { province: "湖南省", city: "武汉市", spot: "黄鹤楼" },
])

function add() {
    const newItem = { province: "山东省", city: "青岛市", spot: "日照" }
    list.push(newItem)
}

function del(index) {
    list.splice(index, 1)
}
</script>

<style scoped>
button.btn {
    margin-bottom: 20px;
}

table {
    border: 3px solid red;
    border-collapse: collapse;
}

td,
th {
    border: 1px solid red;
}
</style>