<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>

import store from './store';

export default {
  store
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&display=swap');

html, body {
  font-family: 'Inter', sans-serif;
  color: var(--tg-theme-text-color);
  background-color: var(--tg-theme-bg-color);
}

p {
  color: var(--tg-theme-hint-color);
}

.btn {
    background-color: var(--tg-theme-button-color);
    color: var(--tg-theme-button-text-color);
}

</style>