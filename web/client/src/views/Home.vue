<template>
  <div class="home">
    <p>Broker Connectivity Status: {{brokerStatusMessage}}</p>
    <p>Server Connectivity Status: {{serverStatusMessage}}</p>
  </div>
</template>

<script>
import axios from 'axios';
// import { mapGetters, mapState } from 'vuex'

const protobuf = require('protobufjs');

export default {
  name: 'Home',
  data() {
    return {
      person: null,
      heartrate: null,
      isConnected: false,
      socketMessage: '',
      heartbeatDegradedModeTimeoutTimer: null,
      heartbeatNoConnectionTimeoutTimer: null,
      lastReceivedHeartbeat: null,
      brokerStatus: this.$mqtt.connected,
      serverStatus: -1,
    };
  },

  mqtt: {
    'server/heartbeat': function heartbeat(msg) {
      try {
        this.heartbeat.decode(msg);

        if (this.heartbeatTimeoutTimer) {
          clearTimeout(this.heartbeatTimeoutTimer);
          clearTimeout(this.heartbeatNoConnectionTimeoutTimer);
        }

        this.heartbeatTimeoutTimer = setTimeout(() => { this.updateStatus(1); }, 1500);
        this.heartbeatNoConnectionTimeoutTimer = setTimeout(() => { this.updateStatus(-1); }, 4000);

        this.updateStatus(0);
      } catch (error) {
        // console.error('Malformed Heartrate Message from Server', error);
      }
    },
    'param/param/param/test': function test(val) {
      try {
        this.person.decode(val);
        // console.log(`param/param/param/test ${p1.id} ${p1.name}`);
      } catch (error) {
        // console.error('Invalid message', error);
      }
    },
  },

  computed: {
    // ...mapState({
    //   checkoutStatus: state => state.cart.checkoutStatus
    // }),
    // ...mapGetters('cart', {
    //   products: 'cartProducts',
    //   total: 'cartTotalPrice'
    // }),
    serverStatusMessage() {
      switch (this.serverStatus) {
        case 0:
          return 'Connected';
        case 1:
          return 'Experiencing Connectivity Issues...';
        default:
          return 'Disconnected';
      }
    },
    brokerStatusMessage() {
      if (this.brokerStatus) return 'Connected';

      return 'Disconnected';
    },
  },

  mounted() {
    this.$mqtt.on('offline', () => {
      this.brokerStatus = this.$mqtt.connected;
    });

    this.$mqtt.on('connect', () => {
      this.brokerStatus = this.$mqtt.connected;
    });

    this.$mqtt.subscribe('server/heartbeat');
    this.$mqtt.subscribe('param/param/param/test');

    axios({ method: 'get', url: 'json/messages.json' }).then((res) => {
      const root = protobuf.Root.fromJSON(res.data);
      this.person = root.lookupType('iot_processor.messages.Person');
      this.heartbeat = root.lookupType('iot_processor.messages.Heartbeat');
    });
  },

  methods: {
    clickPublish() {
      const message = this.person.create({ id: 1234, name: 'sample name' });
      this.$mqtt.publish('param/param/param/test', this.person.encode(message).finish());
    },
    updateStatus(status) {
      this.serverStatus = status;
    },
    // checkout (products) {
    //   this.$store.dispatch('cart/checkout', products)
    // },
  },
};
</script>
