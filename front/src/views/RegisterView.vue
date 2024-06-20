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

const authStore = useAuthStore()
const username = ref('')

const register = async () => {
  try {
    // username을 서버에 전달하여 challenge가 포함된 등록 옵션을 받아온다.
    const options = await authStore.registerBegin(username)
    console.log(options)
    const publicKey = await authStore.decodeThat(options)
    console.log(publicKey)

    await navigator.credentials.create({ 
      publicKey
    })
      .then(credentials => {
        console.log(credentials)
      })
      .catch(err => {
        console.log(err)
      })

  } catch (err) {
    console.log(err)
  }
}



</script>