<template>
  <div>
    <h1>Register</h1>
    <input v-model="username" />

    <button @click="register">Register</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/AuthService'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const username = ref('')

const register = async () => {
  try {
    // 사용자 이름을 가져와 서버에 등록 옵션 요청
    const options = await authStore.registerBegin(username.value)

    // 기존 이름이 없는 경우에만 진행
    if (options) {
      const originChallenge = JSON.parse(options).challenge;
      const publicKey = await authStore.decodeOptions(options)

      // navigator.credentials.create()를 사용하여 자격 증명을 생성
      const credentials = await navigator.credentials.create({
        publicKey
      })
      // 자격 증명이 성공적으로 생성된 경우 서버에 완료 요청
      const encodedCredentials = authStore.encodeCredentials(credentials)
      await authStore.registerComplete(username.value, encodedCredentials, originChallenge)
    } else {
      console.log('기존 등록된 이름이 있습니다.');
    }
  } catch (err) {
    console.error('Registration failed:', err);
  }
};



</script>