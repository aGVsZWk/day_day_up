import React, { Component } from 'react'

class Example3 extends Component {
  constructor(props) {
    super(props)
    this.addCount = this.addCount.bind(this)
    this.state = {
      count: 0
    }
  }
  componentDidMount() {
    console.log(`componentDidMount => you clicked ${this.state.count} times`);
  }

  componentDidUpdate(prevProps, prevState) {
    console.log(`componentDidUpdate => you clicked ${this.state.count} times`);
  }

  render() {
    return (
      <div>
        <p>You clicked {this.state.count} times</p>
        <button onClick={this.addCount}>点我</button>
      </div>
    )
  }
  addCount(){
    this.setState({
      count: this.state.count+1
    })
  }
}

export default Example3
