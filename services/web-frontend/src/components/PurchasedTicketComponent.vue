<template>
    <v-card
      class="m-0 p-0"
      width="100%"
      variant="tonal"
    >

      <v-sheet
        cover
        height="30"
        color="var(--tg-theme-button-color)"
        class="pt-1"
      >

        <v-card-subtitle>
          <v-row align="center">
            <v-col cols="auto">
              <v-icon icon="mdi-airplane-takeoff">
              </v-icon>
              <slot name="airline_company"></slot>
            </v-col>
            <v-spacer></v-spacer>

            <v-spacer></v-spacer>
            <v-col cols="auto">
              BOARDING PASS
            </v-col>
          </v-row>
        </v-card-subtitle>
      </v-sheet>

      <v-card-item>
        <v-row class="pb-0 mb-0">
            <v-col cols="4" class="pb-0">
              <v-card-subtitle>Passenger:</v-card-subtitle>
            </v-col>

            <v-col cols="4" class="pb-0">
              <v-card-subtitle>Flight №:</v-card-subtitle>
            </v-col>

            <v-col cols="4" class="pb-0" >
              <v-card-subtitle>Class:</v-card-subtitle>
            </v-col>
        </v-row>
        <v-row class="pt-0 mt-0">
          <v-col cols="4" class="pt-0">
            <v-card-subtitle>
              <slot name="passenger_name"></slot>
            </v-card-subtitle>
          </v-col>

          <v-col cols="4" class="pt-0">
            <v-card-subtitle>
              <slot name="flight_code"></slot>
            </v-card-subtitle>
          </v-col>

          <v-col cols="4" class="pt-0">
            <v-card-subtitle>
              <slot name="passenger_class"></slot>
            </v-card-subtitle>
          </v-col>
        </v-row>
      </v-card-item>

      <v-card-item>
      <v-row class="pb-0 mb-0">
        <v-col cols="4" class="pb-0">
          <v-card-subtitle>
            From: <slot name="from_country"></slot>
          </v-card-subtitle>
        </v-col>

        <v-col cols="4" class="pb-0">
          <v-card-subtitle>Date:</v-card-subtitle>
        </v-col>

        <v-col cols="3" class="pb-0">
          <v-card-subtitle>Seat:</v-card-subtitle>
        </v-col>
      </v-row>
      <v-row class="pt-0 mt-0">
        <v-col cols="4" class="pt-0">
          <v-card-subtitle>
            To: <slot name="to_country"></slot>
          </v-card-subtitle>
        </v-col>

        <v-col cols="4" class="pt-0">
          <v-card-subtitle>
            <slot name="departure_date"></slot>
          </v-card-subtitle>
        </v-col>

        <v-col cols="3" class="pt-0">
          <v-card-subtitle>
            <slot name="passenger_seat"></slot>
          </v-card-subtitle>
        </v-col>
      </v-row>
      </v-card-item>

      <v-divider></v-divider>
      <v-card-item class="pb-0">
      <v-row class="py-0 my-0">
        <v-col cols="1" class="py-0"></v-col>
        <v-col cols="4" class="py-0">
          <p>GATE:</p>
        </v-col>

        <v-col cols="6" class="py-0">
          <p>BOARDING TIME:</p>
        </v-col>
      </v-row>
      <v-row class="py-0 my-0">
        <v-col cols="1" class="py-0"></v-col>
        <v-col cols="4" class="py-0">
          <v-card-title>
            <slot name="gate"></slot>
          </v-card-title>
        </v-col>

        <v-col cols="6" class="py-0">
          <v-card-title>
            <slot name="departure_time"></slot>
          </v-card-title>
        </v-col>
      </v-row>
      </v-card-item>

      <v-btn
          @click="redirectToQrCodePage()"
          class="mt-3"
          width="100%"
          color="var(--tg-theme-button-color)"
          variant="flat"
      >
        Open
      </v-btn>
    </v-card>
  <br>
</template>

<script>
export default {
  name: "PurchasedTicketComponent",
  methods: {
    redirectToQrCodePage() {
      this.$router.push({ path: '/ticketQrCode'});
    }
  }
}
</script>

<style scoped>

</style>