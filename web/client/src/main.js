import Vue from 'vue';
import VueMqtt from 'vue-mqtt';
import App from './App.vue';
import router from './router';

Vue.use(VueMqtt, 'ws://localhost:9001/ws', { clientId: 'WebClient-12123789123' });

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
