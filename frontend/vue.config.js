const { defineConfig } = require('@vue/cli-service')
const djangoStaticDir = '../messenger/static';
const templatePath = `templates/index.html`;

module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: djangoStaticDir,
  indexPath: templatePath,
  publicPath: '../static',
  assetsDir: '../static'
})
