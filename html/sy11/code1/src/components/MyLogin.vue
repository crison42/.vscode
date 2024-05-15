<template>
    <div class="login-container">
        <div class="login-box">
            <!-- 头像区域 -->
            <div class="avatar-box">
                <img class="avatar" src="../assets/logo.png" />
            </div>
            <!-- 表单区域 -->
            <div class="form-login">
                <!-- 登录名称 -->
                <div class="form-group">
                    <label for="username">登录名称：</label>
                    <input type="text" class="form-control" id="username" placeholder="请输入登录名称"  autocomplete="off"  v-model.trim="username" />
                </div>
                <!-- 登录密码 -->
                <div class="form-group">
                    <label for="password">登录密码：</label>
                    <input type="password" class="form-control" id="password" placeholder="请输入登录密码"  v-model.trim="password" />
                </div>
                <!-- 登录按钮 -->
                <div class="form-group">
                    <button type="button" class="btn" @click="onLogin">登录</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()  //创建全局路由实例
const username = ref('')   //存放用户名，利用v-model与页面输入框绑定
const password = ref('')   //存放密码，利用v-model与页面输入框绑定
// 登录按钮功能
const onLogin = () => {
    // //判断用户名与密码是否正确
    if (username.value === 'admin' && password.value === '123456') {
        //登录成功，跳转到后台首页(编程式导航)
        router.push('/home') 
        //模拟存储token的操作
        return localStorage.setItem('token', 'Bearer xxx')
    } else {
        alert('用户名或密码输入错误')
        //登录失败，清除token
        localStorage.removeItem('token')
    }
}
</script>

<style lang="less" scoped>
.login-container {
    background-color: #35495e;
    height: 100%;
}
.login-container .login-box {
    width: 400px;
    height: 250px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 6px rgba(255, 255, 255, 0.5);
}
.form-login {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    box-sizing: border-box;
    padding: 1.5rem !important;
}
.form-group {
    padding-top: 20px;
}
.btn {
    background-color: deepskyblue;
    color: #fff;
}

.form-control {
    flex: 1;
    padding: 0.5rem;
}

.avatar-box {
    position: absolute;
    width: 100%;
    top: -65px;
    left: 0;
}
.avatar {
    width: 120px;
    height: 120px;
    border-radius: 50% !important;
    box-shadow: 0 0 6px #efefef;
    background-color: #fff;
}
</style>