const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    https: true,
    proxy: {
      "/api" : {
        target: "http://localhost:5000",
        ws: true,
        changeOrigin: true
      },
      '/socket.io': {
        target: 'http://localhost:5000',
        ws: true,
        changeOrigin: true,
        onProxyReq: (proxyReq) => {
          proxyReq.setHeader('Origin', 'http://localhost:5000');
        },
      },
    },
  }
})
