<template>
  <v-container class="text-center">
    <br>
    <v-card class="text-center" color="red" variant="tonal">
      <v-card-title>
        Failed!
      </v-card-title>

      <v-card-text>
        Oops, something went wrong.
      </v-card-text>
    </v-card>
    <br>
    <v-img :width="300"
       class="mx-auto"
       src="./duck-confusion.webp"
    >
    </v-img>
    <br>
    <br>
    <v-spacer></v-spacer>
    <v-btn
        @click="redirectToMainPage()"
        size="large"
        width="100%"
        prepend-icon="mdi-home"
        color="var(--tg-theme-button-color)"
        variant="tonal">
      Home
    </v-btn>
    <v-spacer></v-spacer>
  </v-container>

</template>

<script>
export default {
  name: "SuccessfulPaidPage",
  mounted() {
    window.Telegram.WebApp.BackButton.hide()
    window.Telegram.WebApp.MainButton.hide()
  },
  methods: {
    redirectToMainPage() {
      window.Telegram.WebApp.BackButton.hide()
      window.Telegram.WebApp.MainButton.hide()
      this.$router.push({ path: '/'});
    }
  }
}
</script>

<style scoped>

</style>