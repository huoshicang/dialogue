// vite.config.ts
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import {fileURLToPath, URL} from 'url'

// naiveui自动引入
import {NaiveUiResolver} from 'unplugin-vue-components/resolvers'

// arcoui自动引入
import {ArcoResolver} from 'unplugin-vue-components/resolvers';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      imports: [
        'vue',
        {
          'naive-ui': [
            'useDialog',
            'useMessage',
            'useNotification',
            'useLoadingBar'
          ]
        }
      ],
      resolvers: [ArcoResolver()],
    }),
    Components({
      resolvers: [
        NaiveUiResolver(),
        ArcoResolver({
          sideEffect: true
        })
      ]
    })
  ],

  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
