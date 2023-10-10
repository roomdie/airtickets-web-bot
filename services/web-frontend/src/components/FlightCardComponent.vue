<template>
    <v-card-subtitle class="mt-1">
      <v-row class="pl-3">
        <v-col cols="auto" class="px-1">
          <v-icon size="small" icon="mdi-clock-time-eight-outline"></v-icon>
        </v-col>

        <v-col cols="auto" class="px-1">
          <slot name="duration"></slot> hours
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-card-subtitle>

    <v-card-text class="py-0">
      <v-card-text>
        <v-row align="center">
          <v-col cols="auto">
            <slot name="departure_time"></slot>
          </v-col>

          <v-spacer class="text-center">------------------></v-spacer>

          <v-col cols="auto">
            <slot name="arrival_time"></slot>
          </v-col>
        </v-row>
        <v-row class="my-0 p-0">
          <v-col cols="auto" class="my-0 pt-1 pb-0">
            <p>10 OCT, THU</p>
          </v-col>

          <v-spacer></v-spacer>

          <v-col cols="auto" class="my-0 pt-1 pb-0">
            <p>10 OCT, THU</p>
          </v-col>
        </v-row>

        <v-row class="my-0 p-0">
          <v-col cols="auto" class="my-0 py-0">
            <p><slot name="country_from"></slot> (<slot name="departure_airport"></slot>)</p>
          </v-col>

          <v-spacer></v-spacer>

          <v-col cols="auto" class="my-0 py-0">
            <p><slot name="country_to"></slot> (<slot name="arrival_airport"></slot>)</p>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card-text>

    <v-card-subtitle>
      <v-divider></v-divider>
    </v-card-subtitle>
</template>

<script>
export default {
  name: "FlightCardComponent"
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