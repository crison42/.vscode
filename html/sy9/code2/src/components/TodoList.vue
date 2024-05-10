<template>
      <form class="form-inline" @submit.prevent="onFormSubmit"></form>
      <!-- 文本输入框 -->
      <input  type="text" class="form-control" placeholder="请填写任务信息" style="width: 356px" v-model.trim="taskname"/>
    <ul class="list-group">
        <li class="list-group-item d-flex justify-content-between align-items-center" v-for="item in list"
            :key="item.id">
            <!-- 复选框 -->
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" :id="item.id" v-model="item.done" />
                <label class="custom-control-label" :for="item.id" :class="item.done ?'delete' :''">{{item.task }}
</label>
            </div>
            <!-- badge 效果 -->
            <span class="badge badge-success badge-pill" v-if="item.done">完成</span>
            <span class="badge badge-warning badge-pill" v-else>未完成</span>
        </li>
    </ul>
</template>

<script setup>
const props = defineProps({
    // 表格的数据源
    list: {         //声明自定义属性
        type: Array,
        required: true,
        default: [],
    }
})   
import { ref } from 'vue'
const taskname = ref('')
const emit = defineEmits(['add'])    //自定义事件
// 表单提交的事件处理函数
const onFormSubmit = () => {
    // 1. 判断任务名称是否为空
    if (!taskname.value) return alert("任务名称不能为空！");
    // 2. 触发自定义的 add 事件，并向外界传递数据
    emit('add', taskname.value)
    // 3. 清空文本框
    taskname.value = ''
}     
</script>

<style scoped>
/* 为列表设置固定宽度 */
.list-group {
    width: 700px;
}

/* 删除效果 */
.delete {
    text-decoration: line-through;
}
</style>