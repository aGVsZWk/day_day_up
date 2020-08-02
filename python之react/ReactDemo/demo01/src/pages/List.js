import React, { Component } from 'react';
import {Redirect} from 'react-router-dom'


class List extends Component {
	constructor(props) {
		super(props);
		this.state = {
		}
	}

	componentDidMount() {
		console.log(this.props.match);
		let tempId = this.props.match.params.id
		this.setState({
			id: tempId
		})
	}

	render() {
		return (
			<div>
				<Redirect to="/home/" />
				<div>
					列表页----{this.state.id}
				</div>
			</div>
		)
	}
}

export default List;
