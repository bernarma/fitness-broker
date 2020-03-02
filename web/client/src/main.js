import Vue from 'vue';
import VueMqtt from 'vue-mqtt';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.use(VueMqtt, 'ws://localhost:9001/ws');

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
