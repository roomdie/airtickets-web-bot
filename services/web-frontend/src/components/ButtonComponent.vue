<template>
  <v-btn
      class="bg-light-blue-accent-3 text-center no-outline"
      :ripple="{ class: 'text-light-blue-darken-3'}"
      rounded="lg"
      variant="flat"
      block

  >{{ text }}</v-btn>
</template>

<script>
export default {
  name: "ButtonComponent",
  props: {
    text: {
      type: String,
      required: true
    }
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@700&family=Roboto&display=swap');

.no-outline:focus {
  outline: none;
}

</style>