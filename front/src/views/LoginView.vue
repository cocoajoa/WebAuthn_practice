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

    // WebAuthnAPI를 사용하여 자격 증명을 얻는다.
    const assertionResponse = await navigator.credentials.get({ publicKey: options })

    // 얻은 자격 증명을 사용하여 로그인 완료 요청을 보낸다.
    await authStore.loginComplete(username.value, assertionResponse)
  } catch (err) {
    console.log(err)
  }
}

</script>