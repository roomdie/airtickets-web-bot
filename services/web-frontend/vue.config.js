const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {

    https: true,
    proxy: {
      "/api" : {
        target: "http://web-backend:5000",
        ws: true,
        changeOrigin: true

      },
    },
  }
})
