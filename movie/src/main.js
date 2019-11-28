import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from './store'

Vue.use(VueAxios, axios);

Vue.prototype.$axios = axios;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

axios.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  config.headers["AUTHENTICATION"]=localStorage.token;
  return config;
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error);
});


Vue.config.productionTip = false;
Vue.use(ElementUI);


//全局路由守卫
router.beforeEach((to, from, next)=>{
  if(to.matched.length>0){
    // 路由地址正确
    //判断是否需要登录才能进入   路由对象中 requeredsAuth true
    // for(let i of to.matched){
    //     console.log(i.meta.requiresAuth)
    // }
    // alert(to.matched.length)

    if(to.matched.some(obj=>{
      if(obj.meta.requiresAuth){
        // alert(obj.meta.requiresAuth)
        return true
      }
    })){
      if(localStorage.token){
        // alert(localStorage.token)
        next()
      }else{
        next({path:'/login'})
      }
    }else{
      next()
    }

  }else{
    // 路由地址不正确
    next({path:'/login'})
  }
})


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
