//按需导入对应的函数
import { createRouter, createWebHashHistory } from "vue-router"

//创建路由对象
const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: () => import('./components/MyLogin.vue') },
    {
      path: '/home', component: () => import('./components/Home.vue'), redirect: '/home/users',
      children: [
        {
          path: 'users',
          component: () => import('./components/subcomponents/MyUsers.vue')
        },
        {
          path: 'rights',
          component: () => import('./components/subcomponents/MyRights.vue')
        },
        {
          path: 'goods',
          component: () => import('./components/subcomponents/MyGoods.vue')
        },
        {
          path: 'orders',
          component: () => import('./components/subcomponents/MyOrders.vue')
        },
        {
          path: 'settings',
          component: () => import('./components/subcomponents/MySettings.vue')
        },
        {  //在用户管理组件单击详情匹配的路由规则
          path: 'users/:id',
          component: () => import('./components/user/MyUserDetail.vue'), props: true
        }
      ]
    }
  ]
})
//向外共享路由实例对象
export default router