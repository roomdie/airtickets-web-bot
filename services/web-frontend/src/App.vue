<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import store from './store';

export default {
  store,
  data: () => ({
    isClickEventAttached: false
  }),
  mounted() {
    window.Telegram.WebApp.onEvent('backButtonClicked', () => {
      this.$router.push({ path: '/'});
    })

    window.Telegram.WebApp.onEvent('invoiceClosed', (data) => {
      window.Telegram.WebApp.BackButton.hide()
      window.Telegram.WebApp.MainButton.hide()
      if (data.status === "paid") {
        this.$router.push({ path: '/successfulPaid'});
      }
      else {
        this.$router.push({ path: '/failedPaid'});
      }
    });
  }
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&display=swap');

html, body {
  font-family: 'Inter', sans-serif;
  color: var(--tg-theme-text-color);
  background-color: var(--tg-theme-bg-color);
  overflow-y: hidden;
}

p {
  color: var(--tg-theme-hint-color);
}


</style>