import { createApp } from 'vue'    
import './style.css'               
 import App from './App.vue'   
 //导入路由模块
import router from './router'
const app=createApp(App)
 //挂载路由模块
app.use(router)
app.mount('#app')  