import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '@/views/login/login.vue'
import register from '@/views/register/register'
import home from '@/views/head/home.vue'
import faceslogin from '@/views/login/faceslogin'
import passwordlogin from '@/views/login/passwordlogin'
import fflt from '@/views/fflt/fflt'
import mybookcity from '@/views/personalhomepage/personalhomepage'
import novelclassification from '@/views/novelclassification/novelclassification'
import bookcity from '@/views/bookcity/bookcity'
import contentDisplay from '@/components/novelclassification/contentDisplay'
import designatedBook from '@/views/designatedBook/designatedBook'
import read from '@/views/read/read'
import query from '@/views/query/query'
import personalbookshelf from '@/views/personalhomepage/personalbookshelf'
import Informationmodification from '@/views/personalhomepage/Informationmodification'
import registerModify from '@/views/register/register_modify'
import store from '@/store/index'

import Antd from 'ant-design-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import * as bootstrap from 'bootstrap'
import 'ant-design-vue/dist/antd.css'
import ViewUI from 'view-design'
import 'view-design/dist/styles/iview.css'

Vue.use(ViewUI)
Vue.use(Antd)
Vue.use(VueRouter)
Vue.use(bootstrap)

const routes = [
  { path: '/', redirect: '/login' },
  {
    path: '/login',
    component: login,
    redirect: '/login/passwordlogin',
    children: [
      { path: 'faceslogin', component: faceslogin },
      { path: 'passwordlogin', component: passwordlogin }
    ]
  },
  { path: '/register', component: register },
  { path: '/register_modify', component: registerModify },
  {
    path: '/home',
    component: home,
    redirect: '/home/bookcity',
    children: [
      { path: 'query', component: query },
      { path: 'read', component: read },
      { path: 'designatedBook', component: designatedBook },
      { path: 'bookcity', component: bookcity },
      { path: 'fflt', component: fflt },
      {
        path: 'mybookcity',
        component: mybookcity,
        redirect: '/home/mybookcity/personalbookshelf',
        children: [
          { path: 'personalbookshelf', component: personalbookshelf },
          { path: 'Informationmodification', component: Informationmodification }
        ]
      },
      {
        path: 'novelclassification',
        component: novelclassification,
        redirect: '/home/novelclassification/whole',
        children: [
          { path: 'whole', component: contentDisplay },
          { path: 'fantasy', component: contentDisplay },
          { path: 'xiuzhen', component: contentDisplay },
          { path: 'urban', component: contentDisplay },
          { path: 'pass_through', component: contentDisplay },
          { path: 'online_games', component: contentDisplay },
          { path: 'science_fiction', component: contentDisplay }
        ]
      }
    ]
  }

]

const router = new VueRouter({
  routes
})
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}
/* 针对与session的可持久化存储把相关证明保存在vuex中可通过获取 */
router.beforeEach((to, from, next) => {
  const path = ['/home/mybookcity/personalbookshelf', '/home/mybookcity/Informationmodification']
  if (path.indexOf(to.path) !== -1) {
    if (store.state.session_name) {
      next()
    } else {
      next('/login')
    }
  } else {
    next()
  }
})
export default router
