<template>
  <div class="home">
    <p>Server Connectivity Status: {{serverStatusMessage}}</p>
  </div>
</template>

<script>
import axios from 'axios';

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
      serverStatus: -1,
    };
  },

  mqtt: {
    'server/heartbeat': function (msg) {
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
        console.error('Malformed Heartrate Message from Server', error);
      }
    },
    'param/#': function () {
      console.log('param/#');
    },
    'param/param/param/test': function (val) {
      console.log(val.length);
      try {
        const p1 = this.person.decode(val);
        console.log(`param/param/param/test ${p1.id} ${p1.name}`);
      } catch (error) {
        console.error('Invalid message', error);
      }
    },
    'template/+': function (data, topic) {
      if (topic.split('/').pop() === '12345') {
        console.log('topic:', 'template/12345');
      }
    },
    'template/+/param/param': function (data, topic) {
      if (topic.split('/')[1] === '12345') {
        console.log('topic:', 'template/12345/param/param');
      }
    },
  },

  computed: {
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
  },

  mounted() {
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
  },
};
</script>
