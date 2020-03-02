module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "http://localshot:8000",
        changeOrigin: true,
        pathRewrite: {
          "^/api": ""
        }
      }
    }
  }
};
