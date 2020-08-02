# 安装 webpack
`npm install -g webpack webpack-cli`

`npm install webpack webpack-cli --save-dev`


# 命令行打包(demo1)
`webpack ./src/index.js`
## 开发环境
`webpack ./src/index.js -o ./dist/bundle.js --mode=development`
## 生产环境
`webpack ./src/index.js -o ./dist/bundle_production.js --mode=production`

## 默认处理
webpack 默认可以处理 js 文件、json 文件

生产环境下比开发环境多了压缩代码和代码混淆


# 使用配置文件打包(demo2)

编写好 webpack.config.js 后，直接敲 `webpack`


# 打包 css(demo3)

webpack 默认不支持 css，需要使用 loader (module 段中)

先安装 loader
`npm install style-loader css-loader --save-dev`
然后在 module 中配置 loader

最后 webpack 测试


# 用插件将 js 打包到 html 中(demo4)
这样操作，就不用自己在 html 中手写 script 引入 js 了

## 安装插件
`npm install html-webpack-plugin --save-dev`

## 配置插件



# 打包图片(demo5)

继续在 module 里面配置 loader 即可

`npm install url-loader html-loader --save-dev`

要增加选项，图片小于指定尺寸，做 base64 处理，减少请求数量，会使得体积更大

打包前，还要安装下 `file-loader`

`npm install file-loader --save-dev`

安装就好，不用配置


# 热更新(demo6)

安装 webpack-dev-server:
`npm install webpack-dev-server -g`

安装好之后，使用 `webpack-dev-server` 启动

`npm install webpack-dev-server --save-dev`

配置好 devServer 段即可，启动会暴露一堆依赖，全部安装即可。
