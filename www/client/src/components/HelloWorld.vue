<template>
  <v-container fluid class="hello">
    <h5>{{ msg }}</h5>
    <v-layout row>
      <v-flex xs4>
        <v-text-field id="message" name="message" label="Leave a message" v-model="message"></v-text-field>
      </v-flex>
      <v-flex xs4>
        <v-btn color="primary" dark id="button" type="button" @click="sendMessage()">Send</v-btn>
      </v-flex>
    </v-layout>
    <div>
      <p v-for="message in messages">{{ message.content }}</p>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome',
      message: '',
      messages: []
    }
  },
  methods: {
    sendMessage () {
      var self = this
      this.axios.post('/message', {message: self.message})
        .then(function (response) {
          var data = response.data
          self.messages.push(data.message)
          self.message = ''
        })
        .catch(function (error) {
          console.log(error)
        })
    },
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
