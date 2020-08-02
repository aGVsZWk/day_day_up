import React, {Component} from 'react'

// 自定义的组件，首字母必须大写
class App extends Component {
  render(){
    return (
      <ul className="my-list">
        <li>Jspang.com</li>
        <li>L Love React</li>
        <li>{true?'JSPang':'技术胖'}</li>
      </ul>
    )

    var child1 = React.createElement('li', null, 'JSPang.com')
    var child2 = React.createElement('li', null, 'I Love React')
    var root = React.createElement('ul', {className: 'my-list'}, child1, child2)
    console.log(root);
  }
}

export default App
