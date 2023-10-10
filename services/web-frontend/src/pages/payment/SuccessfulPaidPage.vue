<template>
  <v-container class="text-center">


    <br>
    <v-card class="text-center" color="green" variant="tonal">
      <v-card-title>
        Done!
      </v-card-title>

      <v-card-text>
        You have successfully purchased your ticket.
      </v-card-text>
    </v-card>
    <br>
    <v-img :width="300"
       class="mx-auto"
       src="./duck-like.webp"
    >
    </v-img>
    <br>
    <br>
    <v-btn
        @click="redirectToMainPage()"
        size="large"
        width="100%"
        prepend-icon="mdi-home"
        color="var(--tg-theme-button-color)"
        variant="tonal">
      Home
    </v-btn>

    <v-btn
        @click="redirectToPurchasedTicketsPage()"
        class="mt-2"
        size="large"
        width="100%"
        prepend-icon="mdi-qrcode-scan"
        color="var(--tg-theme-button-color)"
        variant="tonal">
      My Tickets
    </v-btn>
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
    redirectToPurchasedTicketsPage() {
      this.$router.push({ path: '/purchasedTickets'});
    },
    redirectToMainPage() {
      this.$router.push({ path: '/'});
    }
  }
}
</script>

<style scoped>

</style>