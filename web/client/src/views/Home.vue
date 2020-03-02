<template>
  <div class="home">
    <p v-if="isConnected">We're connected to the server!</p>
    <p>Message from server: "{{socketMessage}}"</p>
    <button @click="clickPublish();">Publish</button>
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
      isConnected: false,
      socketMessage: '',
    };
  },

  mqtt: {
    'param/+/+/test': function () {
      console.log('param/+/+/test');
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

  mounted() {
    this.$mqtt.subscribe('param/param/param/test');

    axios({ method: 'get', url: 'json/messages.json' }).then((res) => {
      const root = protobuf.Root.fromJSON(res.data);
      this.person = root.lookupType('iot_processor.messages.Person');
    });
  },

  methods: {
    clickPublish() {
      const message = this.person.create({ id: 1234, name: 'sample name' });
      this.$mqtt.publish('param/param/param/test', this.person.encode(message).finish());
    },
  },
};
</script>
