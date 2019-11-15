import Vue from 'vue';
import Router from 'vue-router';
import Books from '@/components/login.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Books',
      component: Books,
    },
  ],
  mode: 'history',
});
