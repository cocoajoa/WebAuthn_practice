<template>
  <div>
    <h1>메인 화면</h1>
    <p v-if="isLoggedIn">로그인 완료</p>
    <p v-else>로그인 필요</p>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/AuthService'
const authStore = useAuthStore()
const isLoggedIn = authStore.isLoggedIn

</script>

<style lang="scss" scoped>

</style>