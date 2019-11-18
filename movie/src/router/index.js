import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    // name: 'home',
    // component: Home
    redirect:'/login'
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path:'/login',
    name:'login',
    component:() => import('../views/login/login.vue')
  },
  {
    path:'/index',
    name:'index',
    redirect:'/index/intelligent',
    component:() => import('../views/index/index.vue'),
    children:[
      {
        path:'intelligent',
        name:'intelligent',
        component:() =>import('../views/intelligent/intelligent.vue')
      },
      {
        path:'classify',
        name:'classify',
        component:() =>import('../views/classify/classify.vue')
      },
      {
        path:'ranking',
        name:'ranking',
        component:() =>import('../views/ranking/ranking.vue')
      },
      {
        path:"hot",
        name:'hot',
        component:() =>import('../views/hot/hot.vue')
      }
    ]

  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
