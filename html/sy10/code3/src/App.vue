<template>
  <h1 style="text-align:center">商品列表展示-软工2213班常洪</h1>
  <MyShop :data="goodsList"> <!-- 使用My-Shop组件 -->
    <template v-slot:header>
      <th>序号</th>
      <th>商品名称</th>
      <th>价格</th>
      <th>标签</th>
      <th>操作</th>
    </template>
    <template #body="{ row, index }">
      <td>{{ index + 1 }}</td>
      <td>{{ row.goods_name }}</td>
      <td>￥{{ row.goods_price }}</td>
      <td>
        <!-- 基于当前行的 inputVisible，来控制 input 和 button 的按需展示-->
        <input type="text" class="form-control form-control-sm form-ipt" v-if="row.inputVisible"
          v-model.trim="row.inputValue" v-focus @blur="hide(row)" @keyup.enter="onInputConfirm(row)"
          @keyup.esc="row.inputValue = ''" />
        <button type="button" class="btn btn-primary btn-sm" v-else @click="row.inputVisible = true">+Tag</button>
        <span class="badge badge-warning" v-for="val in row.tags" :key="val">{{ val }}</span>
      </td>
      <td>
        <button type="button" class="btn btn-danger btn-sm" @click="onRemove(row.id)">删除</button>
      </td>
    </template>

  </MyShop>
</template>

<script setup>
import MyShop from './components/MyShop.vue'     //导入并注册组件My-Shop
import { ref } from 'vue'
const goodsList = ref([
  { id: 1, goods_name: "Teenmix/天美意夏季专柜同款金色布女鞋6YF18BBT6", goods_price: 298, tags: ['舒适', '透气'], inputVisible: false, inputValue: "" },
  { id: 2, goods_name: "奥休斯（all shoes）冬季保暖女士休闲雪地靴，舒适加绒防水短靴，防滑棉鞋子", goods_price: 89, tags: ['保暖', '防滑'], inputVisible: false, inputValue: "" },
  { id: 3, goods_name: "初语秋冬新款毛衣女套头宽松针织衫简约插肩袖上衣", goods_price: 199, tags: ['秋冬', '毛衣'], inputVisible: false, inputValue: "" },
  { id: 4, goods_name: "佐露丝蕾丝衫女2020春秋装新款大码女装衬衫上衣雪纺衫韩版打底衫长袖", goods_price: 19, tags: ['雪纺衫', '打底'], inputVisible: false, inputValue: "" },
  { id: 5, goods_name: "熙世界中长款长袖圆领毛衣2022秋装新款假两件连衣裙107SL170", goods_price: 178, tags: ['圆领', '连衣裙'], inputVisible: false, inputValue: "" },
  { id: 6, goods_name: "烟花烫2021秋季装新品女装简约修身显瘦七分袖欧根纱连衣裙花央", goods_price: 282, tags: ['秋季新品', '显瘦'], inputVisible: false, inputValue: "" },
  { id: 7, goods_name: "韩都衣舍2021韩版女装秋装宽松显瘦纯色系带长袖衬NG8201", goods_price: 180, tags: ['韩都衣舍', '长袖衬衫'], inputVisible: false, inputValue: "" },
  { id: 8, goods_name: "预售纤莉大码女装胖妹妹秋装2020新款圆领百搭绣花胖mm休闲套头卫衣", goods_price: 128, tags: ['预售', '卫衣'], inputVisible: false, inputValue: "" },
  { id: 9, goods_name: "沙密2022夏改良旗袍裙连衣裙修身复古时尚日常短款礼服旗袍", goods_price: 128, tags: ['沙密', '礼服'], inputVisible: false, inputValue: "" },
  { id: 10, goods_name: "南极人秋冬韩版七彩棉加绒加厚一体保暖打底裤", goods_price: 128, tags: ['南极人', '打底裤'], inputVisible: false, inputValue: "" }
])
const onRemove = id => {
  goodsList.value = goodsList.value.filter(item => item.id != id)
}
const vFocus = el => { el.focus() }  //定义自定义指令
const onInputConfirm = (itemA) => {
  // 1. 把用户在文本框中输入的值，预先转存到常量 val 中
  const val = itemA.inputValue;
  // 2. 清空文本框的值
  itemA.inputValue = "";
  // 3. 隐藏文本框
  itemA.inputVisible = false;
  // 1.1 判断 val 的值是否为空，如果为空，则不进行添加
  // 1.2 判断 val 的值是否已存在于 tags 数组中，防止重复添加
  if (!val || itemA.tags.indexOf(val) !== -1) return
  //2. 将用户输入的内容，作为新标签 push 到当前行的 tags 数组中
  itemA.tags.push(val)
}
</script>

<style scoped>
span {
  background-color: yellow;
  color: #000;
  margin: 0 4px;
}

input.form-ipt {
  width: 80px;
  display: inline;
}
</style>