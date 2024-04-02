<!-- 列表渲染指令v-for -->
<template>
    <h1 align="center">软工2213班常洪</h1>
    <h1>普通数组的遍历</h1>
    <ul>城市名称：
        <li v-for="(item, index) in arr">索引:{{ index }}-----数据:{{ item }}</li>
    </ul>
    <ul>
        <!-- 如果需要对一组元素进行循环，可以使用容器元素，在该元素上使用v-for -->
        <div v-for="(item, index) in arr">
            <span><img src="../assets/images/list.jpg" alt=""></span>
            <li>索引:{{ index }}-----数据:{{ item }}</li>
        </div>
    </ul>
    <hr>
    <h1>对象数组的遍历:学生信息</h1>
    <p v-for="(item, index) in stu" :title="'年龄:' + item.age">
        索引:{{ index }}-----姓名:{{ item.name }}----年龄:{{ item.age }}
    </p>
    <button type="button" @click="add">添加学生</button>
    <button type="button" @click="remove">删除学生</button>
    <button type="button" @click="change">改变学生</button>
    <button type="button" @click="length">改变数组长度</button>
    <button type="button" @click="agesort">按年龄排序</button>
    <hr>
    <h1>对象的遍历</h1>
    <p v-for="(val, key, i) in stuObject">
        索引:{{ i }}-----键:{{ key }}-----值:{{ val }}
    </p>
    <button type="button" @click="addAtr">对象添加属性</button>
    <button type="button" @click="addAtrs">对象添加多个属性</button>
    <hr>
    <h1>整数的遍历即循环操作</h1>
    <p v-for="count in 5">这是第{{ count }}次循环</p>
    <hr>
    <h1>输出九九乘法表</h1>
    <table>
        <tr v-for="n in 9">
            <td v-for="m in n">{{ m }}*{{ n }}={{ m * n }}</td>
        </tr>
    </table>
    <hr>
    <h1>字符串的遍历</h1>
    <p v-for="(ss, index) in str">{{ index }}-----{{ ss }}</p>
</template>

<script setup>
import { reactive, ref } from 'vue'
const arr = reactive(["北京", "上海", "深圳", "广州", "南京"])
const stu = reactive([
    { name: "张三", age: 19 },
    { name: "李四", age: 20 },
    { name: "王五", age: 21 },
    { name: "赵六", age: 18 }
])
const add = () => {
    stu.push({ name: "hhhh", age: 20 });
}
const remove = () => {
    stu.shift();  //将数组中的第一个元素从数组中删除
}
const change = () => {
    stu[2] = { name: "尤雨溪", age: 22 };
    stu[3].name = "娃哈哈"
}
const length = () => {
    // stu.length=0
    // stu.splice(0);   //从下标1开始删除
    stu.splice(2, 1);   //从下标2开始删除1个元素
}
const agesort = () => {   //按照年龄进行排序
    stu.sort(function (a, b) {
        return a.age - b.age; 升序排列
        // return b.age - a.age;   //降序排列
    });
}
const stuObject = reactive({ name: "zzzz", sex: "女", phone: "123456789999" })

const addAtr = () => {
    stuObject.address1 = "洛阳市洛龙区开元大道";
    stuObject.address2 = "洛阳市西工区唐宫路";
}
const addAtrs = () => {
    Object.assign(stuObject, {   // 如果你需要同时添加多个属性，可以使用Object.assign
        interest: "跑步",
        work: "教师"
    }) //将后面的属性合并到stuObject对象中
}
const str = ref('河南科技大学软件学院')
</script>

<style scoped>
li {
    list-style: none;
}

span {
    float: left;
}

table {
    border-collapse: collapse;

}

td {
    border: 1px solid red;
    padding: 3px;
    background-color: pink;
}
</style>