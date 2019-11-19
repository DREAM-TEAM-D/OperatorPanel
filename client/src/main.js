import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from '../store/index';
import vuetify from './plugins/vuetify';

Vue.prototype.$http = axios;

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://localhost:5000';

Vue.use(BootstrapVue);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');
