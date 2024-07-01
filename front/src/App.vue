<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>
    <nav>
      <router-link :to="{ name: 'home' }">home</router-link> |
      <router-link :to="{ name: 'register' }">register</router-link> |
      <router-link :to="{ name: 'login' }">login</router-link> |
    </nav>
  </div>
  <RouterView />
</template>

<style scoped>

</style>
