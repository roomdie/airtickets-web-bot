<template>
  <v-container max-height="100%">
    <v-card class="text-center mx-auto" max-height="100%" variant="text">
      <v-sheet
          rounded class="mx-auto align-end"
          color="var(--tg-theme-bg-color)"
          width="260" height="260">
        <v-img
            class="bg-transparent"
            src="./qrcode.webp"
        />

      </v-sheet>
      <v-card-text>
        Scan this QR code of the ticket if necessary and have a good flight!
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "TicketQrCodePage",
  mounted() {
    window.Telegram.WebApp.disableClosingConfirmation()
    window.Telegram.WebApp.BackButton.show()
  }
}
</script>

<style scoped>

html, body, div {
  font-family: 'Inter', sans-serif;
  color: var(--tg-theme-text-color);
  background-color: var(--tg-theme-secondary-bg-color);
  overflow-y: hidden;
  color-scheme: var(--tg-color-scheme);
}
</style>