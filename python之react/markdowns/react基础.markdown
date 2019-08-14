# 基础概念
react包
react: 必备
react-dom: 操作虚拟DOM，有引入之后才能用`ReactDOM`
babel: 将ES6转化为ES5。(举例：let转化为var).



## 虚拟DOM
ReactDOM.render使用:

将虚拟DOM对象转换为真实DOM对象. `ReactDOM.render(虚拟DOM对象, 真实DOM对象)`
html中:
```html
<div id="container"></div>
```
js中:
```javascript
<script type='text/babel'>    // 必须用text/babel
    let element = <h1>Hello World</h1>;
    console.log(ReactDOM);
    ReactDOM.render(element, document.getElementById('container'));
</script>
```

1. 虚拟DOM是个特别的js对象， 常用方法:render, createElement等等
createElement方法如何使用：
```js
var element = React.createElement('h1', {'id': 'myTitle'}, 'hello');
let element = <h1>Hello react</h1>
```
2. 虚拟DOM对象最终都会被React转换为真实的DOM
3. 我们编码时只需要操作react的虚拟DOM相关数据，react会转换为真实DOM变化而更新界面

## JSX
1. 全称: javascript XML
2. react定义的一种类似于XML的JS扩展语法：XML+JS
3. 作用：用来创建react虚拟DOM(元素)对象。
举例：
```jsx
var msg = 'Hello JSX!';
var ele = <h1>{msg}</h1>
```
标签里直接加个大括号。
它不是字符串，也不是XML标签，最终产生的就是个js对象.

4. 标签名任意: HTML或其他标签
5. 标签属性任意：HTML标签属性或其它
6. 基本语法规则:
    1. 遇到`<`开头的代码，以标签的语法解析：html同名标签转换为html同名元素，其它标签需要特别解析。
    2. 遇到以`{`开头的代码，以js的语法解析：标签中的js代码必须用`{}`包含。
7. babel.js：浏览器的js引擎无法解析JSX语法，需要用babel将其转换为纯js代码。只要用了JSX，都要加上**type=text/babel**，声明需要babel来处理。


### react创建虚拟DOM对象·
```js
let element1 = React.createElement('h1', {id: 'box1', className: 'box1'}, 'React.createElement创建的虚拟DOM对象');
ReactDOM.render(element1, document.getElementById('example1'));
```

### JSX创建虚拟DOM对象·
```js
let element2 = <h3>JSX创建的虚拟DOM对象</h3>;
ReactDOM.render(element2, document.getElementById('example2'));
```

多用JSX语法，react基本不用。

## 库引入
js的库引入有先后顺序，依赖关系，比如必须先jquery，后bootstrap；先react后react-dom。
