<template>
    <div id="box">
        <h1 style="text-align: center;">水果商店—软工2213班常洪 </h1>
        <table class="table table-bordered table-hover">
            <thead>
            <tbody>
                <tr v-for="item in fruitlist" :key="item.id">
                    <td><input type="checkbox" v-model="item.state"></td>
                    <td>{{ item.fruit }}</td>
                    <td><img :src="item.pic" alt="" style="width: 50px;height: 50px;border-radius: 50%;"></td>
                    <td>${{ item.price }}</td>
                    <td>
                        <button type="button" @click="onSubClick(item.id)">-</button>
                        <span>{{ item.count }}</span>
                        <button type="button" @click="onAddClick(item.id)">+</button>
                    </td>
                </tr>
            <tfoot>
                <tr style="font-weight: bolder;">
                    <td colspan="2"><span>总数量:{{ total }}</span></td>
                    <td colspan="2"><span>总金额:${{ totalPrice }}元</span></td>
                    <td style="text-align: center;">
                        <button type="button" class="btn btn-primary" :disabled="isDisabled">结算</button>
                    </td>
                </tr>
            </tfoot>
            </tbody>
            <tr>
                <th>操作</th>
                <th>水果名称</th>
                <th>水果图片</th>
                <th>单价(斤)</th>
                <th>数量</th>
            </tr>
            </thead>
        </table>
    </div>
</template>

<script setup>
const onSubClick = (id) => {
    const findResult = fruitlist.find(x => x.id === id)
    if (findResult.count && findResult > 1) {
        findResult.count--
    }
}
const onAddClick = (id) => {
    const findResult = fruitlist.find(findResult => findResult.id === id)
    if (findResult.count) {
        findResult.count++
    }
}
import { reactive, computed } from 'vue';
const total = computed(() => {
    let t = 0;
    fruitlist.forEach(x => {
        if (x.state) {
            t += x.count;
        }
    })
    return t;
})
const totalPrice = computed(() => {
    let t = 0;
    fruitlist.forEach(x => {
        if (x.state) {
            t += x.count * x.price;
        }
    })
    return t;
})
const isDisabled = computed(() => {
    var flag = true;
    fruitlist.forEach(x => {
        if (x.state) {
            flag = false;
        }
    })
    return flag;
})
const fruitlist = reactive([
    { id: 1, fruit: '香橼', pic: './src/components/images/1.jpg', price: 5, count: 1, state: true },
    { id: 2, fruit: '柚子', pic: './src/components/images/2.jpg', price: 4.5, count: 1, state: false },
    { id: 3, fruit: '橘子', pic: './src/components/images/3.jpg', price: 3, count: 1, state: false },
    { id: 4, fruit: '橙子', pic: './src/components/images/4.jpg', price: 6, count: 1, state: false },
    { id: 5, fruit: '粑粑柑', pic: './src/components/images/5.jpg', price: 6.5, count: 1, state: false },
    { id: 6, fruit: '柠檬', pic: './src/components/images/6.jpg', price: 4, count: 1, state: false },
    { id: 7, fruit: '青柠', pic: './src/components/images/7.jpg', price: 5.2, count: 1, state: false },
])
</script>
<style scoped></style>