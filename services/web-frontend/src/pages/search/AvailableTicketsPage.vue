<template>
  <v-container v-show="!available_tickets">
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
  <flight-component v-for="(ticket, index) in available_tickets" :key="index" :ticket_index="index">
    <template v-slot:card-title>
      {{ ticket.flight_details[0].from_country }} — {{ ticket.flight_details[0].to_country }}
    </template>

    <template v-slot:info>
      <flight-card-component v-for="(details, index) in ticket.flight_details" :key="index">
        <template v-slot:duration>
          {{ details.duration }}
        </template>

        <template v-slot:departure_time>
          {{ details.departure_time }}:00
        </template>

        <template v-slot:arrival_time>
          {{ details.arrival_time }}:00
        </template>

        <template v-slot:departure_airport>
          {{ details.departure_airport }}
        </template>

        <template v-slot:arrival_airport>
          {{ details.arrival_airport }}
        </template>

      </flight-card-component>
    </template>

    <template v-slot:price>
      {{ ticket.price.value }} {{ ticket.price.currency }}
    </template>

    <template v-slot:status>

      <v-btn v-if="ticket.status.name === 'default'"
          variant="text"
          rounded="xl"
      >
      </v-btn>

        <v-btn v-else
          variant="tonal"
          :color="ticket.status.color"
          rounded="xl"
      >
        {{ ticket.status.emoji }}
      </v-btn>
    </template>
  </flight-component>

</template>

<script>
import FlightComponent from "@/components/FlightComponent";
import axios from "axios";
import { VSkeletonLoader } from 'vuetify/labs/VSkeletonLoader'
import lscache from "lscache";
import FlightCardComponent from "@/components/FlightCardComponent";


export default {
  name: "TicketsPage",
  components: {FlightCardComponent, FlightComponent, VSkeletonLoader },

  data: () => ({
    loading: true,
    available_tickets: null || lscache.get('available_tickets'),
    ticket_statuses: ["default", "eco", "hot"]
  }),
  mounted() {
    window.Telegram.WebApp.enableClosingConfirmation()
    window.Telegram.WebApp.MainButton.hide();
    this.from_country = null

    if (!lscache.get('available_tickets')) {
        this.getSearchedFlights(lscache.get("flight_search_filter"))
    }
    lscache.flushExpired()
  },
  methods: {
    getSearchedFlights(data) {
      axios.post('api/getSearchedFlights', data)
      .then(response => {
        this.available_tickets = response.data
        lscache.set('available_tickets', response.data, 10);
      })
      .catch(error => {
        console.error(error);
      });
    },
  }
}
</script>

<style scoped>
html, body {
  overflow-y: visible !important;
  background-color: var(--tg-theme-bg-color);
}

div {
  background-color: var(--tg-theme-secondary-bg-color);
}
</style>