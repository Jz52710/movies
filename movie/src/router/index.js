import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    // name: 'home',
    // component: Home
    redirect:'/index'
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
    path:'/logon',
    name:'logon',
    component:() => import('../views/logon/logon.vue')
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
        redirect:'/index/classify/action',
        component:() =>import('../views/classify/classify.vue'),
        children: [
          {
            path:'action',
            name:'action',
            component:() =>import('../views/filmname/action.vue')
          },
            {
            path:'war',
            name:'war',
            component:() =>import('../views/filmname/war.vue')
          },
            {
            path:'science',
            name:'science',
            component:() =>import('../views/filmname/science.vue')
          },
            {
            path:'suspense',
            name:'suspense',
            component:() =>import('../views/filmname/suspense.vue')
          },
            {
            path:'comedy',
            name:'comedy',
            component:() =>import('../views/filmname/comedy.vue')
          },
            {
            path:'love',
            name:'love',
            component:() =>import('../views/filmname/love.vue')
          },
            {
            path:'inspiration',
            name:'inspiration',
            component:() =>import('../views/filmname/inspiration.vue')
          },
            {
            path:'animation',
            name:'animation',
            component:() =>import('../views/filmname/animation.vue')
          },
            {
            path:'thriller',
            name:'thriller',
            component:() =>import('../views/filmname/thriller.vue')
          },
            {
            path:'crime',
            name:'crime',
            component:() =>import('../views/filmname/crime.vue')
          },
            {
            path:'record',
            name:'record',
            component:() =>import('../views/filmname/record.vue')
          },
        ]
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

  },
  {
    path:'/channel',
    name:'channel',
    component:() => import('../views/channel/channel.vue'),
  },
  {
    path:'/middle',
    name:'middle',
    component:() => import('../views/middle/middle.vue'),
    children: [
          {
            path:'action',
            name:'action',
            component:() =>import('../views/filmname/action.vue')
          },
            {
            path:'war',
            name:'war',
            component:() =>import('../views/filmname/war.vue')
          },
            {
            path:'science',
            name:'science',
            component:() =>import('../views/filmname/science.vue')
          },
            {
            path:'suspense',
            name:'suspense',
            component:() =>import('../views/filmname/suspense.vue')
          },
            {
            path:'comedy',
            name:'comedy',
            component:() =>import('../views/filmname/comedy.vue')
          },
            {
            path:'love',
            name:'love',
            component:() =>import('../views/filmname/love.vue')
          },
            {
            path:'inspiration',
            name:'inspiration',
            component:() =>import('../views/filmname/inspiration.vue')
          },
            {
            path:'animation',
            name:'animation',
            component:() =>import('../views/filmname/animation.vue')
          },
            {
            path:'thriller',
            name:'thriller',
            component:() =>import('../views/filmname/thriller.vue')
          },
            {
            path:'crime',
            name:'crime',
            component:() =>import('../views/filmname/crime.vue')
          },
            {
            path:'record',
            name:'record',
            component:() =>import('../views/filmname/record.vue')
          },
        ]
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
