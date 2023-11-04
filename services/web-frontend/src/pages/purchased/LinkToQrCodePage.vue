<template>
  <v-container>
    <v-card color="green" class="text-center" variant="tonal">
      <v-card-title>
        The ticket is active.
      </v-card-title>
    </v-card>
    <br>
    <v-card class="pl-2" variant="text">
      Details:
      <v-card-subtitle>
        Flight Number: ...
      </v-card-subtitle>
      <v-card-subtitle>
        From: ...
      </v-card-subtitle>
      <v-card-subtitle>
        To: ...
      </v-card-subtitle>

      <v-card-subtitle>
        Company: ...
      </v-card-subtitle>
      <v-card-subtitle>
        Price: ...
      </v-card-subtitle>
    </v-card>

    <v-card-text class="text-center">
      Unfortunately, I wanted to link the flight number to the QR code,
      but I had little time left and decided to remove this function.

      I hope you liked my app idea ❤️
    </v-card-text>
  </v-container>
</template>

<script>
export default {
  name: "QrLinkPage",
  mounted() {
  }
}
</script>

<style scoped>

</style>