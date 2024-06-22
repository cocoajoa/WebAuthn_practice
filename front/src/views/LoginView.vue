<template>
  <div>
    <h1>Login</h1>
    <input v-model="username" placeholder="Username" />
    <button @click="login">Login</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/AuthService'

const authStore = useAuthStore()
const username = ref('')

const login = async () => {
  try {
    // 서버 DB에 저장된 옵션을 받아온다.
    const options = await authStore.loginBegin(username.value)
    // 가입되었던 경우에만 진행
    if (options) {
      const originChallenge = JSON.parse(options).challenge;
      const publicKey = await authStore.decodeLoginOptions(options)
      const credentials = await navigator.credentials.get({
        publicKey
      })
      // 자격 증명이 성공적으로 생성된 경우 서버에 완료 요청
      const encodedCredentials = await authStore.encodeLoginCredentials(credentials)
      authStore.loginComplete(username.value, encodedCredentials, originChallenge)
    } else {
      console.log('회원가입되지 않은 아이디입니다.');
    }
  } catch (err) {
    console.log(err)
  }
}

</script>