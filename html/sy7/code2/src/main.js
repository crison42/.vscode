import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'
import MyComA from './components/ComA.vue'
import MyComB from './components/ComB.vue'
const app = createApp(App)
app.component('my-com-a', MyComA)
app.component('my-com-b', MyComB)
app.mount('#app')