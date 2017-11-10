<template>
  <div>
    <div>
      <p>BMI calculator</p>
      <v-layout row>
        <v-flex xs-4>
          <v-text-field id="weight" name="weight" label="Weight (kg)" v-model="weight"></v-text-field>
        </v-flex>
        <v-flex xs-4 offset-xs-5>
          <v-text-field id="height" name="height" label="Height (m)" v-model="height"></v-text-field>
        </v-flex>
      </v-layout>
      <p>{{ bmi }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Bmi',
  data () {
    return {
      weight: 0,
      height: 0,
      result: 0
    }
  },
  methods: {
    cal () {

    }
  },
  computed: {
    bmi () {
      if (this.height === 0 || this.height === undefined) {
        return 0
      } else {
        return this.weight / this.height / this.height
      }
    }
  },
  mounted () {
  }
}
</script>

<style scoped>
</style>
