import React, {Component, Fragment} from 'react'
import './style.css'
import XiaojiejieItem from './XiaojiejieItem'
import axios from 'axios'


class Xiaojiejie extends Component {
	constructor(props) {
		super(props)
		this.deleteItem = this.deleteItem.bind(this)
		this.inputChange = this.inputChange.bind(this)
		this.addList = this.addList.bind(this)
		this.state = {
			inputValue: '',
			list: []
		}
	}

	componentDidMount() {
		axios.get('https://www.easy-mock.com/mock/5f219d31fa76424e9506a481/ReactDemo01/xiaojiejie')
			.then((res) => {
				console.log('axios 获取数据成功' + JSON.stringify(res))
				this.setState({
					list: res.data.data
				});
			})
			.catch((err)=>{console.log('axios 获取数据失败' + JSON.stringify(err))})
	}


	render() {
		return (
			<Fragment>
				<div>
					<label htmlFor="jspang">增加服务</label>
					<input
						id="jspang"
						className="input"
						type="text"
						value={this.state.inputValue}
						onChange={this.inputChange}
						ref={(input)=>{this.input=input}}
					/>
					<button onClick={this.addList}>增加服务</button>
				</div>
				<ul ref={(ul)=>{this.ul=ul}}>
					{
						this.state.list.map((item, index)=>{
							return (
								// <li
								// 	key={index+item}
								// 	onClick={this.deleteItem.bind(this, index)}
								// 	dangerouslySetInnerHTML={{__html:item}}
								// >
								// </li>
									<XiaojiejieItem
										// avname="Kaka"
										content={item}
										key={index+item}
										index={index}
										list={this.state.list}
										deleteItem={this.deleteItem.bind(this)}
         />
							)
						})
					}
				</ul>
			</Fragment>
		)
	}
	inputChange() {
		// console.log(e.target.value);
		// this.state.inputValue = e.target.value
		this.setState({
			inputValue: this.input.value,
		});
		// console.log(this);
	}

	addList() {
		this.setState({
			list: [...this.state.list, this.state.inputValue],
			inputValue: ''
		}, ()=>{
			console.log(this.ul.querySelectorAll('li').length);   // setState 完成的回调
		});
		console.log(this.ul.querySelectorAll('li').length);   // setState 异步
	}

	deleteItem(index) {
		let list = this.state.list
		list.splice(index, 1)
		this.setState({
			list: list
		});
	}
}

export default Xiaojiejie
