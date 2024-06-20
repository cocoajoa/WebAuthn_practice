import { defineStore } from 'pinia'
import axios from 'axios'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const API_URL = 'http://localhost:8000/api/v1/'

  const isLoggedin = ref(false)

  const registerBegin = (username) => {
    return axios({
      method: 'post',
      url: `${API_URL}register/begin/`,
      data: { username }
    })
      .then(res => {
        return res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const registerComplete = (username, attestationResponse) => {
    axios({
      method: 'post',
      url: `${API_URL}register/complete/`,
      data: { username, attestationResponse}
    })
      .then(res => {
        console.log(res)
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const loginBegin = (username) => {
    axios({
      method:'post',
      url:`${API_URL}login/begin/`,
      data: { username }
    })
      .then(res => {
        console.log(res)
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const loginComplete = (username, assertionResponse) => {
    axios({
      method:'post',
      url: `${API_URL}login/complete/`,
      data: { username, assertionResponse }
    })
      .then(res => {
        console.log(res)
        console.log(res.data)
        isLoggedin.value = true
      })
      .catch((err) => {
        console.log(`12312`,err)
      })
  }

  // Base64url을 ArrayBuffer로 변환하는 함수
  function base64urlToArrayBuffer(base64url) {
    // '-'를 '+'로, '_'를 '/'로 대체하고 패딩 문자 ('=')를 추가합니다.
    const base64 = base64url.replace(/-/g, '+').replace(/_/g, '/').replace(/\s/g, '').padEnd(base64url.length + (4 - base64url.length % 4) % 4, '=');

    const binaryString = atob(base64);
    const length = binaryString.length;
    const bytes = new Uint8Array(length);

    for (let i = 0; i < length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
    }

    return bytes.buffer; // ArrayBuffer 반환
  }

  const decodeThat = (options) => {
    const parsed = JSON.parse(options)
    let CredentialCreationOptions = {
        rp: parsed.rp,
        challenge: base64urlToArrayBuffer(parsed.challenge),
        user: {
          id: base64urlToArrayBuffer(parsed.user.id),
          name: parsed.user.name,
          displayName: parsed.user.displayName
        },
        pubKeyCredParams: parsed.pubKeyCredParams,
        timeout: parsed.timeout,
        excludeCredentials: parsed.excludeCredentials,
        attestation: parsed.attestation
      }

    return CredentialCreationOptions
  }


  return { registerBegin, registerComplete, loginBegin, loginComplete, decodeThat, isLoggedin }
})
