import React, { useState } from 'react'
let showSex = true

function Example() {
  const [age, setAge] = useState(18)
  const [work, setWork] = useState('前端程序员')
  const [sex, setSex] = useState('男')


  return (
    <div>
      <p>JSPange今年：{age}岁</p>
      <p>JSPange性别：{sex}岁</p>
      <p>JSPange工作：{work}岁</p>
    </div>
  )
}

export default Example
