<template>
  <div class="home">
    <p v-if="isConnected">We're connected to the server!</p>
    <p>Message from server: "{{socketMessage}}"</p>
    <button @click="clickPublish()">Publish</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
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
    'param/param/param/test': function () {
      console.log('param/param/param/test');
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
  },

  methods: {
    clickPublish() {
      // Send the "pingServer" event to the server.
      this.$mqtt.publish('param/param/param/test', 'hello');
    },
  },
};
</script>
