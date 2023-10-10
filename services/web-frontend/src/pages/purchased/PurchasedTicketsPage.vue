<template>
  <v-container v-show="!purchased_tickets">
    <v-row>
      <v-col cols="12" md="6" v-for="n in 5" :key="n.index">
        <v-skeleton-loader
          class="mx-auto border"
          width="100%"
          type="card"
        ></v-skeleton-loader>
      </v-col>
    </v-row>
  </v-container>
  <v-container>
    <purchased-ticket-component v-for="(ticket, index) in purchased_tickets" :key="index">
      <template v-slot:airline_company>
        {{ ticket.details.company }}
      </template>

      <template v-slot:passenger_name>
        {{ ticket.passenger_name }}
      </template>

      <template v-slot:flight_code>
        {{ ticket.flight_code }}
      </template>

      <template v-slot:from_country>
        {{ ticket.details.from_country }}
      </template>

      <template v-slot:to_country>
        {{ ticket.details.to_country }}
      </template>

      <template v-slot:departure_date>
        {{ ticket.details.departure_date }}
      </template>

      <template v-slot:passenger_class>
        {{ ticket.details.passenger_class }}
      </template>

      <template v-slot:passenger_seat>
        {{ ticket.details.passenger_seat }}
      </template>

      <template v-slot:gate>
        {{ ticket.details.gate }}
      </template>

      <template v-slot:departure_time>
        {{ ticket.details.departure_time }}:00
      </template>
    </purchased-ticket-component>
  </v-container>

</template>

<script>
import PurchasedTicketComponent from "@/components/PurchasedTicketComponent";
import axios from "axios";
import { VSkeletonLoader } from 'vuetify/labs/VSkeletonLoader'
import lscache from "lscache";

export default {
  name: "PurchasedTicketsPage",
  components: {PurchasedTicketComponent, VSkeletonLoader},
  data: () => ({
      purchased_tickets: null,
  }),
  mounted() {
    window.Telegram.WebApp.disableClosingConfirmation()
    window.Telegram.WebApp.BackButton.show()

    let user_id = lscache.get("user_id")
    this.getPurchasedTickets(user_id)
  },
  methods: {
    getPurchasedTickets(user_id) {
      axios.post('api/getPurchasedTickets ', {user_id: user_id})
        .then(response => {
          console.log(response.data)
          this.purchased_tickets = response.data
        })
        .catch(error => {
          console.error(error);
        });
    },
  }
}
</script>

<style scoped>
div {
  background-color: var(--tg-theme-bg-color);
}
</style>