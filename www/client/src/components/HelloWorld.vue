<template>
  <div class="hello">
    <h5>{{ msg }}</h5>
    <div>
      <p v-for="message in messages">{{ message.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome',
      messages: []
    }
  },
  methods: {
    fetchMessages () {
      var self = this
      this.axios.get('/messages')
        .then(function (response) {
          var data = response.data
          self.messages = self.messages.concat(data.messages)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  mounted () {
    this.fetchMessages()
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
