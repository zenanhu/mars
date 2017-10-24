import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Dict from '@/components/Dict'
import About from '@/components/About'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: HelloWorld
    },
    {
      path: '/dict',
      name: 'Dict',
      component: Dict
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    { path: '*', redirect: '/' }
  ]
})
