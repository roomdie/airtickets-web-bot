<template>
  <v-container fill-height>
    <v-row>
      <v-col cols="12">
        <br>
      </v-col>

    </v-row>
    <v-card
        class="text-center"
        variant="text"
    >
      <v-img
          class="mx-auto"
          src="./airplane.webp"
          alt="Описание изображения"
          width="80%"
      >
      </v-img>
      <v-card-title>
        Airtickets Bot
      </v-card-title>

      <v-card-subtitle>
        Order air tickets directly via Telegram.
      </v-card-subtitle>


      <v-card-text>
        <v-icon
              color="var(--tg-theme-button-color)"
              size="small"
              icon="mdi-information-slab-circle-outline"
        >
        </v-icon>
        This bot was created for <a href="https://t.me/contest/326">Telegram Contest</a>.
        All purchases and actions are not real.
      </v-card-text>

      <v-card-actions>
        <v-row>
          <v-col cols="6">
               <v-btn
                   @click="redirectToTicketFindPage()"
                   color="var(--tg-theme-button-color)"
                   rounded="lg"
                   variant="tonal"
                   height="50px"
                   width="100%"
                   prepend-icon="mdi-magnify"
               >
                 <template v-slot:prepend>
                   <v-icon size="large"></v-icon>
                 </template>
                 SEARCH
               </v-btn>
          </v-col>

          <v-col cols="6">
               <v-btn
                   @click="redirectToPurchasedTicketsPage()"
                   color="var(--tg-theme-button-color)"
                   rounded="lg"
                   variant="tonal"
                   height="50px"
                   width="100%"
                   prepend-icon="mdi-qrcode-scan"
                >
                 MY TICKETS

                 <template v-slot:prepend>
                   <v-icon size="medium"></v-icon>
                 </template>
               </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
      <br>
      <v-card-subtitle>
        GitHub: <a target=”_blank” href="https://github.com/roomdie/">https://github.com/roomdie/</a>
      </v-card-subtitle>
    </v-card>
  </v-container>
</template>

<script>

import lscache from "lscache";
import axios from "axios";

export default {
  name: "MainPage",
  mounted() {
    lscache.flush()
    window.Telegram.WebApp.expand();
    window.Telegram.WebApp.disableClosingConfirmation()
    window.Telegram.WebApp.BackButton.hide()
    window.Telegram.WebApp.MainButton.hide()
    this.checkInitData({_auth: window.Telegram.WebApp.initData})
  },
  methods: {
    checkInitData(data) {
       axios.post('api/checkInitData ', data)
        .then(response => {
          lscache.set("user_id", response.data.user.id, "10")
        })
        .catch(error => {
          console.error(error);
        });
    },
    redirectToTicketFindPage() {
      this.$router.push({ path: '/ticketFind'});
    },
    redirectToPurchasedTicketsPage() {
      this.$router.push({ path: '/purchasedTickets'});
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@800&family=Roboto&display=swap');


a {
  color: var(--tg-theme-button-color);
  text-decoration: none;
}
v-btn {
  font-family: Roboto, sans-serif;
}
.no-outline:focus {
  outline: none;
}

</style>