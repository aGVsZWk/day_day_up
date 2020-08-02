npm init -y

npm install --save-dev babel-cli
npm install --save-dev babel-preset-es2015

在根目录下新建 .babelrc 文件，写入下面代码
```js
{
	"presets": [
		"es2015"
	],
	"plugins": []
}
```


babel ./src/index.js -o ./dist/index.js


将 build 改到 package.json 的 scripts 里，删掉 test
