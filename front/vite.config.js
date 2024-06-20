import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
// import fs from 'fs'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  // 보안을 위해 원래 https가 권장된다.
  // server: {
  //   https: {
  //     key: fs.readFileSync('./server.key'),
  //     cert: fs.readFileSync('./server.cert'),
  //   }
  // },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
},)
