import React, { useState, useEffect } from 'react'
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'



function Index(){
  useEffect(()=>{
    console.log('useEffect=>老弟，你来了！Index');    // Mount
    return ()=>{
      console.log("useEffect=>老弟，你走了！Index");   // Unmount
    };
  }, [])  // 控制什么时候解绑，传空为不使用这个组件的时候解绑
  return <h2>JSpange.com</h2>
}

function List(){
  useEffect(()=>{
    console.log('useEffect=>老弟，你来了！List');
  }, [])
  return <h2>List page</h2>
}


function Example() {
  const [count, setCount] = useState(0)  // 数组结构
  useEffect(() => {
    console.log(`useEffect=> you clicked ${count} times`);
    // return ()=>{
    //   console.log('==================');
    // };
  }, [count]) // 监听 count, 变化时, 第一个函数执行

  // let _useState = useState(0)
  // let count = _useState[0]
  // let setCount = _useState[1]
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={()=>{setCount(count+1)}}>点我</button>

      <Router>
        <ul>
          <li><Link to="/">首頁</Link></li>
          <li><Link to="/list">列表页</Link></li>
        </ul>
        <Route path='/' exact component={Index}></Route>
        <Route path='/list/' exact component={List}></Route>
      </Router>
    </div>
  )
}

export default Example
