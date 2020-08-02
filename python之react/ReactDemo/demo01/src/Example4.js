import React, { useState, createContext, useContext } from 'react'
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'

const CountContext = createContext()    // 1. 创建上下文

function Counter() {
  let count = useContext(CountContext)    // 3. 用 useContext 接收
  return (<h2>{count}</h2>);
}

function Example4() {
  const [count, setCount] = useState(0)  // 数组结构

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={()=>{setCount(count+1)}}>点我</button>
      <CountContext.Provider value={count}>   {/* 2. 用 Provider 传入想共享的东西 */}
        <Counter />
      </CountContext.Provider>
    </div>
  )
}

export default Example4
