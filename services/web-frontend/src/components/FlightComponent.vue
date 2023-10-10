<template>
  <v-container>
    <v-card
        color="var(--tg-theme-bg-color)"
        class="mx-auto"
    >
    <v-expand-transition>
      <div v-show="!show">
        <v-card-title>
          <v-row>
            <v-col cols="auto">
              <slot name="card-title"></slot>
            </v-col>

            <v-spacer></v-spacer>

            <v-col cols="auto">
              <slot name="status"></slot>
            </v-col>
          </v-row>
        </v-card-title>

        <slot name="info"></slot>

        <v-card-subtitle>
          <v-divider></v-divider>
        </v-card-subtitle>
      </div>
    </v-expand-transition>
      <v-card-actions>
        <v-row align="center">
          <v-col cols="6">
            <v-btn
              @click="redirectToPrePaymentPage()"
              color="green-lighten-1"
              variant="tonal"
              class="ml-5"
            >
              Buy · <slot name="price"></slot>
            </v-btn>
          </v-col>
          <v-spacer></v-spacer>
          <v-col cols="3">
            <v-btn

              color="var(--tg-theme-text-color)"
              :icon="show ? 'mdi-chevron-down' : 'mdi-chevron-up'"
              @click="show = !show"
            >

            </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>

      <v-expand-transition>
        <div v-show="show">
          <v-divider></v-divider>

          <v-card-text>
            More detailed information about the flight and transfers may be located here, but in your case the flight without transfers.
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
  </v-container>
</template>

<script>
import lscache from "lscache"

export default {
  name: "FlightComponent",
  data: () => ({
    show: false
  }),
  props: {
    ticket_index: {
      type: Number,
      required: true
    },
  },
  methods: {
    redirectToPrePaymentPage() {
      lscache.set("ticket_index", this.ticket_index, 5)
      this.$router.push({ path: '/prePayment'});
    }
  }
}
</script>

<style scoped>
.v-card-title {
  color: var(--tg-theme-text-color);
}

.v-card-text {
  color: var(--tg-theme-text-color);
}

.v-card-subtitle {
  color: var(--tg-theme-hint-color);
}
</style>