<template>
  <div>
    <div>
      <v-layout row>
        <v-flex xs4>
          <v-text-field id="word" name="word" label="Input a word" v-model="word"></v-text-field>
        </v-flex>
        <v-flex xs4>
          <v-btn color="primary" dark id="button" type="button" @click="searchWord()">Search</v-btn>
        </v-flex>
      </v-layout>
      <p v-if="result">Search result: {{ result }}</p>

      <p v-for="word in words">{{ word.word }}: {{ word.value }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dict',
  data () {
    return {
      word: '',
      result: '',
      words: []
    }
  },
  methods: {
    searchWord () {
      var self = this
      this.axios.get('/dict/word/' + self.word)
        .then(function (response) {
          var data = response.data
          self.result = data.word
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    fetchWords () {
      var self = this
      this.axios.get('/words')
        .then(function (response) {
          var data = response.data
          self.words = self.words.concat(data.words)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  mounted () {
    this.fetchWords()
  }
}
</script>

<style scoped>
</style>
