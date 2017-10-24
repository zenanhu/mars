<template>
  <div>
    <div>
      <p v-for="word in words">{{ word.word }}: {{ word.value }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dict',
  data () {
    return {
      words: []
    }
  },
  methods: {
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
