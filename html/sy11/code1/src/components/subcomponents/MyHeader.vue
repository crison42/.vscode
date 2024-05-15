<template>
    <div class="layout-header-container">
        <!-- 左侧 logo 和 标题区域 -->
        <div class="layout-header-left">
            <!-- logo -->
            <img class="layout-header-left-img" src="../../assets/logo.png" alt="">
            <!-- 标题 -->
            <h4 class="layout-header-left-title ml-3">商城后台管理系统</h4>
        </div>
        <!-- 右侧按钮区域 -->
        <div class="layout-header-right">
            <button type="button" class="btn btn-light" @click="onLogout">退出登录</button>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
// 单击“退出登录”按钮功能
const onLogout = () => {
    // 清除缓存信息
    localStorage.removeItem('token')
    // 跳转到登录组件
    router.push('/login')
}
</script>

<style scoped>
.layout-header-container {
    height: 60px;
    border-bottom: 1px solid #eaeaea;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 0.5rem;
    background-color: #5f9ea0
}

.layout-header-left {
    display: flex;
    align-items: center;
    color: #fff;
}

.layout-header-left-img {
    height: 50px;
}

.btn {
    background-color: #5f9ea0;
    color: #fff;
}

.btn:hover {
    color: #999;
    opacity: 0.5;
    background-color: #fff;
}
</style>