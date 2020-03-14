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


### react创建虚拟DOM对象
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


## JSX语法详细

#### 渲染

注释: `{/*要注释的内容*/}`

多行元素: 必须有父标签把它包裹起来
```jsx
let myDom = <div>
    <div>我是第一个内容</div>
    <div>我是第二个内容</div>
</div>
ReactDOM.render(myDom, document.getElementById('demoReact'))
```


jsx 使用表达式，要将其放在 `{}`中

```jsx
let text="你好"
let myDom=<div>{text}</div>
ReactDOM.render(myDom, document.getElementById('reactDom'))
```

计算的话，直接写在`{}`中
```jsx
let num = 9527
let myDom = <div>{num+1}</div>
ReactDOM.render(myDom, document.getElementById('reactDom'))
```

直接调用函数，也写在`{}`中

```jsx
function fun(obj) {
    // return "姓名：" + obj.name + "---年龄：" + obj.age
    return `姓名是${obj.name}，年龄是${obj.age}`
}
let user = {
    name: "小明",
    age: 18
}
let myDom = <div>{fun(user)}</div>
```

直接使用三元运算符，pass

渲染数组
```jsx
let arr = [
    <p>新闻列表1</p>,
    <p>新闻列表2</p>,
    <p>新闻列表3</p>,
    <p>新闻列表4</p>,
    <p>新闻列表5</p>,
    <p>新闻列表6</p>
]
let myDom = <div>{arr}</div>
ReactDOM.render(myDom, document.getElementById('reactDom'))
```

#### 设置属性
```jsx
let text = "点我去百度"
let linkUrl = "http://www.baidu.com"
let myDom = <a href={linkUrl}>{text}</a>
ReactDOM.render(myDom, document.getElementById('reactDom'))
```

动态设置类时，不能使用 `class`，要使用 `className`，样式名不加大括号，要加双引号引起来
```jsx
<style>
    .part {
        background-color: pink;
    }
</style>
<script type="text/babel">
    let myDom = <p className="part">样式</p>
    ReactDOM.render(myDom, document.getElementById('reactDom'))
</script>
```

#### 设置样式
```jsx
let modStyle = {color: "red", backgroundColor: "pink"}
let myDom = <p style={modStyle}>样式</p>
ReactDOM.render(myDom, document.getElementById('reactDom'))

```

#### 列表
```jsx
let arr = ["吃饭", "睡觉"]
let myDom = arr.map((item, index) => {
    // return <p key={index}>{item}</p>
    // 加圆括号解决换行问题
    return (
        <p key={index}>{item}</p>
    )
})
ReactDOM.render(myDom, document.getElementById('reactDom'))
```

另一种写法：
```jsx
let arr = ["吃饭", "睡觉"]
function fun() {
    let newarr = []
    for (let index in arr) {
        newarr.push(<p key={index}>{arr[index]}</p>)
    }
    return newarr
}
ReactDOM.render(fun(), document.getElementById('reactDom'))
```

#### 对象列表
```jsx
let objArr = [
    {name: "zhangsan", age: 18},
    {name: 'lisi', age: 16}
]
let myDom = objArr.map((item, index) => {
    return <p key={index}>{item.name} ------- {item.age}</p>
})
ReactDOM.render(myDom, document.getElementById('reactDom'))
```


### 面向组件

1. 构建方式
2. 组建的属性
3. 生命周期

react 组件分为 3 个部分:
1. 属性 props
2. 状态 state
3. 生命周期

#### 无状态组件

```jsx
// 无状态组件创建方式
function MyDom() {
    return (
        <div>我是一个无状态组件</div>
    )
}
// 调用组件(也可使用双标签)
// let com = <MyDom/>
// let com = <div><MyDom></MyDom><MyDom></MyDom></div>
let com = <div><MyDom/><MyDom/></div>
ReactDOM.render(com, document.getElementById('reactDom'))
```

父子组件

```jsx
function MyComA() {
    return (
        <div>我是组件A</div>
    )
}
function MyComB() {
    return (
        <div>我是组件B</div>
    )
}
function MyComC() {
    return (
        <div>我是组件C</div>
    )
}
function MyComD() {
    return (
        <div>我是组件D</div>
    )
}
function Com() {
    return (
        <div>
        <MyComA></MyComA>
        <MyComB></MyComB>
        <MyComC></MyComC>
        <MyComD></MyComD>
        </div>
    )
}
ReactDOM.render(<Com></Com>, document.getElementById('reactDom'))
```

#### 类组件

```jsx
class MyCom extends React.Component{
    render() {
        return (
           <div>类组件</div>
        )
   }
}
ReactDOM.render(<MyCom></MyCom>, document.getElementById('reactDom'))
```

#### props 数据传递
```jsx
function Com(props) {
    return (
        <div>我是一个无状态组件，外部传递的数据是----{props.text}-----{props.num}</div>
    )
}
// ReactDOM.render(<Com text="aaa"></Com>, document.getElementById('reactDom'))
let data = "aaa"
ReactDOM.render(<Com text={data} num="bbb"></Com>, document.getElementById('reactDom'))
```

使用 ES6 扩展运算符方式传递多个参数
```jsx
function Com(props) {
    return (
        <div>我是一个无状态组件，外部传递的数据是----{props.text}-----{props.num}</div>
    )
}
// ReactDOM.render(<Com text="aaa"></Com>, document.getElementById('reactDom'))
let obj = {
    text: "text数据",
    num: "num数据"
}
ReactDOM.render(<Com {...obj}></Com>, document.getElementById('reactDom'))
```

类组件
```jsx
class MyCom extends React.Component{
    render() {
        return (
            <div>类组件---{this.props.text}---{this.props.num}</div>
        )
    }
}
let obj = {
    text: "text数据",
    num: "num数据"
}
ReactDOM.render(<MyCom {...obj}></MyCom>, document.getElementById('reactDom'))
```

使用 `组件名.defaultProps`设置默认值

```jsx
class MyCom extends React.Component{
           render() {
               return (
                   <div>类组件---{this.props.text}---{this.props.num}</div>
               )
           }
       }
MyCom.defaultProps = {
   text: "text数据",
   num: "num数据"
}
ReactDOM.render(<MyCom num="666"></MyCom>, document.getElementById('reactDom'))
```

可使用`组件名.propTypes` 进行数据验证，要安装`prop-types` 包，pass


#### state

必须使用类组件来写 state, state 改变 ReactDOM 自动更新，state 可读可写，使用setState进行修改，props 只读。

```jsx
class MyCom extends React.Component{
    // ES6 子类不管写不写 constructor 在 new 实例的时候都会带上 constructor
    // state 在 constructor 中定义
    constructor(props) {
        super(props)
        this.state = {
            name: "嘻嘻",
            newHtml: "<p>我是传奇</p>"
        }
    }
    fun = () => {
        this.setState({
            name:"哈哈"
        }, ()=>{
            console.log(this.state.name);
        })
    }
    render() {
        return (
            <div>
                <button onClick={()=>{this.setState({name:"嘻嘻"})}}>改变</button>
                <button onClick={this.fun}>改变</button>
                <div>state 中数据：----{this.state.name}</div>
                <div dangerouslySetInnerHTML={{__html:this.state.newHtml}}></div>
            </div>
        )
    }
}

ReactDOM.render(<MyCom></MyCom>, document.getElementById('reactDom'))
```

### 转发 refs

react 当中提供了一个 ref 数据（不能在无状态组件当中来进行使用），它会返回绑定当前属性的元素。

总结：类似 DOM 操作，标识组件内部的元素，方便我们的查找。

我们有 3 种方式进行 ref 的使用
1. 字符串的方式
2. 回调函数（推荐）
3. React.CreateRef()

```jsx
class MyCom extends React.Component{
    fun = () => {
        // 得到 ref 使用 refs 获取；第一种方式
        // console.log(this.refs.demoInput.value);
        console.log(this.textinput.value);

    }
    render() {
        return (
            <div>
                {/* 直接绑 ref 上 */}
                {/*<input type="text" placeholder="请输入" ref="demoInput"/>*/}
                {/* 回调函数 */}
                <input type="text" placeholder="请输入" ref={(input)=>(this.textinput=input)}/>
                <button onClick={this.fun}>获取input值</button>
            </div>
        )
    }
}

ReactDOM.render(<MyCom></MyCom>, document.getElementById('reactDom'))
```

第三种不再演示


### 事件

react 绑定事件使用小驼峰命名法，绑定函数时不能加() ----> 函数会立即执行


写在类型中，通过箭头函数定义函数，直接在花括号中指定；如果使用 function 定义函数，则要用 bind 绑定 this.

如果传参的话，采用箭头函数调用的方式传参

1. 修改 this 指向
2. bind 方式原地绑定
3. 函数通过箭头函数进行创建
4. constructor 中提前绑定
5. 把事件调用写成箭头函数调用的调用方式

举例第 3 种和第 5 种
```jsx
class MyCom extends React.Component{
    fun = (a) => {
        console.log(a);

    }
    render() {
        return (
            <div>
                <button onClick={()=>{this.fun(1)}}>掉用</button>
            </div>
        )
    }
}
```


### 条件渲染

1. if 语句，jsx 中不允许有if，在 return jsx 之前用 if 判断 state 中的值
2. 三元运算符：和 if 一样

```jsx
class MyCom extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            bool: true
        }
    }

    fun = () => {
        this.setState({
            bool: !this.state.bool
        })
    }
    render() {
        let text
        if (this.state.bool) {
            text = "你好"
        } else {
            text = "你坏"
        }
        return (
            <div>
                <button onClick={()=>{this.fun()}}>点我</button>
                <div>{text}</div>
                <div>{this.state.bool?"呵呵":"哈哈"}</div>
            </div>
        )
    }
}
ReactDOM.render(<MyCom></MyCom>, document.getElementById('reactDom'))
```
