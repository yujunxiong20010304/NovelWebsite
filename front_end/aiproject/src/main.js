import Vue from 'vue'
import App from './App.vue'
import ending from '@/components/ending'
import router from './router'
import axios from 'axios'
import store from '@/store/index'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8' // 编码
axios.defaults.baseURL = '/api'
Vue.prototype.$http = axios
// axios.defaults.baseURL = 'http://localhost:5000'
axios.defaults.withCredentials = true
Vue.config.productionTip = false
Vue.component('ending', ending)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
