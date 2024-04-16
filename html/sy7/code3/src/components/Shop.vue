<template>
    <h1>商品列表展示-软工2213班常洪</h1>
    <table>
        <thead>
            <tr>
                <th>序号</th>
                <th>商品名称</th>
                <th>商品单价</th>
                <th>购买数量</th>
                <th>操作</th>
                <th>
                    <input type="checkbox" id="checkBoxAll" @click="all" />全选/全不选
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in list" :key="item.id">
                <td>{{ index + 1 }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.price }}</td>
                <td>
                    <button class="btn" @click="sub(item.id)">-</button>
                    {{ item.count }}
                    <button class="btn" @click="add(item.id)">+</button>
                </td>
                <td>
                    <button class="btns" @click="del(item.id)">移除</button>
                </td>
                <td>
                    <input type="checkbox" name="list" @click="each" />
                </td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="6">总价：￥{{ totalPrice }}</td>
            </tr>
        </tfoot>
    </table>
</template>

<script setup>
import $ from 'jquery'
import { reactive, ref } from 'vue';
//计算总价
const totalPrice = ref(0)
const total = () => {
    var t = 0;
    list.forEach(function (item, index) {
        if ($("input[name='list']").eq(index).is(":checked"))
            t += item.price * item.count;
    })
    totalPrice.value = t;
}
const list = reactive([
    { id: 1, name: "iPhone 7", price: 6188, count: 1, },
    { id: 2, name: "iPad Pro", price: 5888, count: 1, },
    { id: 3, name: "MaxBook Pro", price: 21488, count: 1, },
    { id: 4, name: "SAMSUNG GalaxyS22", price: 3649, count: 1, },
    { id: 5, name: "HUAWEI P60", price: 4488, count: 1, }
])
const sub = (id) => {
    list.forEach((item) => {
        if (item.id === id) {
            if (item.count > 1) {
                item.count--;
            }
        }
    })
    total()
}
const add = (id) => {
    list.forEach((item) => {
        if (item.id === id) {
            item.count++;
        }
    })
    total()
}
const del = (id) => {
    list.forEach((item, index) => {
        if (item.id === id) {
            list.splice(index, 1)
        }
    })
    total()
}
const all = () => {
    const flag = $("#checkBoxAll").prop("checked");
    $("[name='list']").prop("checked", flag);
    total()
}
//下面复选框控制“全选/全不选” 复选框
const each = () => {
    if ($("[name='list']:checked").length == $("[name='list']").length)
        $("#checkBoxAll").prop("checked", true);
    else $("#checkBoxAll").prop("checked", false);
    total()
}
</script>

<style scoped>
h1 {
    text-align: center;
}

table {
    border: 1px solid #e9e9e9e9;
    border-collapse: collapse;
    border-spacing: 0;
    margin: 0 auto;
}

th,
td {
    padding: 8px 16px;
    border: 1px solid #e9e9e9e9;
}

th {
    background: #f7f7f7;
    color: #5c6c77;
    font-weight: 600;
    white-space: nowrap;
}

.btn {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 1px solid #cccccc;
    background: #ffffff;
    color: #778899;
}

.btns {
    width: 50px;
    height: 20px;
    border-radius: 5px;
    border: 1px solid #cccccc;
    background: #ffffff;
    color: #778899;
    line-height: 20px;
}
</style>