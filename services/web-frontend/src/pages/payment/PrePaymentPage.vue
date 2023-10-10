<template>
  <v-container>
    <v-card color="" variant="text">
      <v-card-title>Your payment card </v-card-title>
      <v-card-subtitle>Since this is a test payment, keep a test card.</v-card-subtitle>
      <v-card-subtitle>(PRESS TO COPY)</v-card-subtitle>
    </v-card>
    <br>
    <v-btn @click="copyURL" class="text-left" variant="tonal" color="blue" width="90%" height="180">
      <v-card width="100%" color="blue" variant="text">
        <v-card-subtitle class="text-white">Visa Classic</v-card-subtitle>

        <v-card-title>
          <v-icon size="x-large" icon="mdi-integrated-circuit-chip"></v-icon>
        </v-card-title>

        <v-card-title>
          4242 4242 4242 4242
        </v-card-title>
        <v-card-subtitle>
          P. Durov  09/29
        </v-card-subtitle>
      </v-card>
    </v-btn>
    <br>
    <br>
    <p>
      Other data such as date, CVC, country... choose whatever you want.
    </p>
    <br>
    <v-btn
        @click="redirectToPaymentPage()"
        size="large"
        width="100%"
        color="green"
        variant="tonal">
      PAY
    </v-btn>

  </v-container>
</template>

<script>
import axios from "axios";
import lscache from "lscache";

export default {
  name: "PrePaymentPage",
  data: () => ({
    purchase_ticket_index: null || lscache.get("ticket_index"),
    available_tickets: null || lscache.get("available_tickets")
  }),
  mounted() {
    window.Telegram.WebApp.enableClosingConfirmation()
    window.Telegram.WebApp.BackButton.hide()
    window.Telegram.WebApp.MainButton.hide()
  },
  methods: {
    createInvoiceLink(purchase_ticket, callback) {
      axios.post('api/createInvoiceLink', purchase_ticket)
          .then(response => {
            callback(response.data);
          })
          .catch(error => {
            console.error(error);
          });
    },
    redirectToPaymentPage() {
      this.createInvoiceLink(this.available_tickets[this.purchase_ticket_index], response => {
        window.Telegram.WebApp.openInvoice(response["invoice_link"]);
      });
    },
    async copyURL() {
      try {
        await navigator.clipboard.writeText("4242424242424242");
        alert('Copied');
      } catch ($e) {
        alert('Cannot copy');
      }
    }
  }
}

</script>

<style scoped>

</style>