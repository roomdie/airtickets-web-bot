<template>
    <v-spacer></v-spacer>
    <v-row class="justify-center">

      <v-col cols="6">
        <slot name="title"></slot>
      </v-col>

      <v-col cols="auto">
        <slot name="decrease_button"></slot>
      </v-col>

      <v-col cols="1">
        <slot name="count"></slot>
      </v-col>

      <v-col cols="auto">
        <slot name="increase_button"></slot>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>

</template>

<script>
export default {
  name: "PassengerCounterComponent",
  props: {

  },
  methods: {
  }
}
</script>

<style scoped>
</style>