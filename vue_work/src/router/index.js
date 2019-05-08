import Vue from 'vue'
import Router from 'vue-router'
import Vmain from '@/components/Vmain'
import Vnote from '@/components/Vnote'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', component: Vmain },
    { path: '/note', component: Vnote },
  ]
})
