import React, { Component } from 'react';
import {Link} from 'react-router-dom'

class Index extends Component {
	constructor(props) {
		super(props);
		this.state = {
			list:[
				{cid: 123, title: '天生杀人狂'},
				{cid: 456, title: '天生杀人'},
				{cid: 4561, title: '天生杀'},
				{cid: 4561231, title: '天生'},
				{cid: 1234561, title: '天'},
			]
		}
	}
	render() {
		return (
			<div>
				<ul>
					{
						this.state.list.map((item, index)=>{
							return (
								<li key={index}>
									<Link to={'/list/'+item.cid}>
										技术博客-{index+1}
									</Link>
								</li>
							)
						})
					}
				</ul>
			</div>
		)
	}
}

export default Index;
