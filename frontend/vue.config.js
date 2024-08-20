const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        pathRewrite: { "^/api": "" },
      },
    },
  },
  configureWebpack: {
    resolve: {
      fallback: {
        crypto: require.resolve("crypto-browserify"),
        stream: require.resolve("stream-browserify"),
        util: require.resolve("util"),
        vm: require.resolve("vm-browserify"),
        process: require.resolve("process/browser"),
      },
    },
  },
});
