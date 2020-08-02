
let path = require('path')
// 需要安装 html-webpack-plugin
let HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  // 入口文件
  entry: './src/index.js',
  output: {
    // 输出文件名称
    filename: 'bundle.js',
    // 输出的路径
    // 绝对路径
    path: path.resolve(__dirname, 'dist')
  },
  // 开发模式
  mode: 'development',
  // loader 配置
  module: {
    // 对某个格式的文件进行转换处理
    rules:[
      {
        test: /\.css$/,
        use:[
          // use 数组里 loader 的顺序，是从下到上，逆序执行
          // 将 js 的样式插入到 style 标签里
          "style-loader",
          // 将 css 文件转换为 js
          "css-loader"
        ]
      },
      {
        // 匹配图片文件
        test: /\.(jpg|png|gif)$/,
        loader: 'url-loader',
        // 图片小于 8kb， base64 处理，减少请求数量，会使得体积更大
        options: {
          limit: 8 * 1024,
          // url-loader 的 es6 模块化解析
          esModule: false,
          // [hash:10] 取图片 hash 的前10位
          // [ext] 取图片的扩展名
          name: '[hash:10].[ext]'
        }
      },
      {
        test: /\.html$/,
        loader: 'html-loader'
      }
    ]
  },
  // plugins 插件配置
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    })
  ],
  //
  devServer: {
    // 项目构建的路径
    contentBase: path.resolve(__dirname, 'dist'),
    // 启动 gzip 压缩
    compress: true,
    // 端口号
    port: 3000,
    // 自动打开浏览器
    open: true
  }
};
