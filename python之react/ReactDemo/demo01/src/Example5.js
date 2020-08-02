import React, {useReducer} from 'react'

function ReducerDemo() {
  const [count, dispatch] = useReducer((state, action)=>{
    switch(action){
      case 'add':
        return state + 1
      case 'sub':
        return state - 1
      default:
        return state
    }
  }, 0)  // 初始值
  return (
    <div>
      <h2>现在的分数是{count}</h2>
      <button onClick={()=>{dispatch('add')}}>Inc</button>
      <button onClick={()=>{dispatch('sub')}}>Dec</button>
    </div>
  )
}


// function countReducer(state, action) {
//   switch(action.type){
//     case 'add':
//       return state + 1
//     case 'sub':
//       return state - 1
//     default:
//       return state
//   }
// }



export default ReducerDemo
