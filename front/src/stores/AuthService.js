import { defineStore } from 'pinia'
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', () => {
  const API_URL = 'http://localhost:8000/api/v1/'

  const isLoggedin = ref(false)
  const router = useRouter()

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
  const registerComplete = (username, attestationResponse, originChallenge) => {
    axios({
      method: 'post',
      url: `${API_URL}register/complete/`,
      data: { username, attestationResponse, originChallenge}
    })
      .then(res => {
        console.log(res.data)
        router.push({ name: 'login' })
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
  // ArrayBuffer를 Base64url 문자열로 변환하는 함수
  function arrayBufferToBase64url(buffer) {
    const bytes = new Uint8Array(buffer);
    let binaryString = '';
    for (let i = 0; i < bytes.length; i++) {
      binaryString += String.fromCharCode(bytes[i]);
    }
    
    // Base64 인코딩
    let base64 = btoa(binaryString);
    
    // '-'를 '+', '_'를 '/'로 대체하고 패딩 문자를 제거합니다.
    const base64url = base64.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    
    return base64url;
  }

  const decodeOptions = (options) => {
    const parsedOptions = JSON.parse(options)
    const CredentialCreationOptions = {
        rp: parsedOptions.rp,
        challenge: base64urlToArrayBuffer(parsedOptions.challenge),
        user: {
          id: base64urlToArrayBuffer(parsedOptions.user.id),
          name: parsedOptions.user.name,
          displayName: parsedOptions.user.displayName
        },
        pubKeyCredParams: parsedOptions.pubKeyCredParams,
        timeout: parsedOptions.timeout,
        excludeCredentials: parsedOptions.excludeCredentials,
        attestation: parsedOptions.attestation
      }
    return CredentialCreationOptions
  }
  const encodeCredentials= (credentials) => {
    const encodedCredentials = {
      id: credentials.id,
      rawId: arrayBufferToBase64url(credentials.rawId),
      response: {
        attestationObject: arrayBufferToBase64url(credentials.response.attestationObject),
        clientDataJSON: arrayBufferToBase64url(credentials.response.clientDataJSON),
      },
      type: 'public-key'
    }
    return encodedCredentials
  }


  return { registerBegin, registerComplete, loginBegin, loginComplete, decodeOptions, encodeCredentials, isLoggedin }
})
