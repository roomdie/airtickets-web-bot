const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {

    https: false,
    proxy: {
      "/api" : {
        target: "http://localhost:5000",
        ws: true,
        changeOrigin: true

      },
    },
  }
})
