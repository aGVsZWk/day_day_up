let path = require('path')

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
      }
    ]
  }
};
