<template>
    <table class="table table-bordered table-striped">
        <!-- 表格的标题区域 -->
        <thead>
            <tr>
                <slot name="header"></slot>
            </tr>
        </thead>
        <!-- 表格的主体区域 -->
        <tbody>
            <!-- 使用 v-for 指令，循环渲染表格的数据行 -->
            <tr v-for="(item, index) in data" :key="item.id">
                <slot name="body" :row="item" :index="index"></slot>
            </tr>
        </tbody>
    </table>
</template>
<script setup>
const props = defineProps({
    // 表格的数据源
    data: {         //声明自定义属性接受App.vue提供的数据
        type: Array,
        required: true,
        default: [],
    }
})
</script>