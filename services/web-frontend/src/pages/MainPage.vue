<template>

  <v-container>
    <v-row class="justify-center text-center">
      <v-col cols="8">
          <v-img
           src="https://i.ibb.co/SPDqNMn/Animated-Emojies-256px-405.gif"
           alt="Описание изображения"></v-img>
      </v-col>
      <v-col cols="12">
        <h3>Telegram Airways</h3>
        <p>
          С другой стороны постоянное информационно-пропагандистское обеспечение нашей
          деятельности требуют от нас анализа направлений прогрессивного развития.
        </p>
      </v-col>
    </v-row>
  </v-container>
  <v-container>
    <v-row>
      <div class="v-col-6">

           <v-btn
               @click="redirectToTicketFindPage()"
              class="bg-light-blue-accent-3 text-center no-outline"
              :ripple="{ class: 'text-light-blue-darken-3'}"
              rounded="lg"
              variant="flat"
              block
              prepend-icon="mdi-magnify"
           >
           <template v-slot:prepend>
            <v-icon color="white" size="large"></v-icon>
           </template>
             FIND
           </v-btn>
      </div>
      <div class="v-col-6">
           <v-btn
              @click="redirectToTicketFindPage()"
              class="bg-light-blue-accent-3 text-center no-outline"
              :ripple="{ class: 'text-light-blue-darken-3'}"
              rounded="lg"
              variant="flat"
              block
              prepend-icon="mdi-qrcode-scan"
            >
             MY TICKETS
            <template v-slot:prepend>
            <v-icon color="white" size="medium"></v-icon>
           </template>
           </v-btn>
      </div>
    </v-row>
      <template>
        <v-icon icon="mdi-home" color="red" />
      </template>
  </v-container>
</template>

<script>
// import ButtonComponent from "@/components/ButtonComponent";

export default {
  name: "MainPage",
  props: {},
  mounted() {
    window.Telegram.WebApp.expand();
    window.Telegram.WebApp.BackButton.hide()
  },
  methods: {
    redirectToTicketFindPage() {
      this.$router.push({ path: '/TicketFindPage'});
    },
    redirectToUserTicketsPage() {
      this.$router.push({ path: '/UserTicketsPage'});
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@800&family=Roboto&display=swap');

v-btn {
  font-family: Roboto, sans-serif;
}
.no-outline:focus {
  outline: none;
}

</style>