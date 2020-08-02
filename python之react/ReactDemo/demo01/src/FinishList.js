import React, { Component } from 'react';
import {connect} from 'react-redux'
import * as actionCreators from './store/actionCreators'

const FinishList = (props) => {
	let {inputValue, inputChange, clickBtn, list} = props
	return (
		<div>
			<div>
				<input type="text"
					value={inputValue}
					onChange={inputChange}
				/>
				<button onClick={clickBtn}>提交</button>
			</div>
			<ul>
				{
					list.map((item, index)=>{
						return (<li key={index}>{item}</li>);
					})
				}
			</ul>
		</div>
	)
}

const stateToProps = (state)=>{
	return {
		inputValue: state.inputValue,
		list: state.list
	}
}

const dispatchToProps = (dispatch) => {
	return {
		inputChange(e){
			let action = actionCreators.changeInputAction(e.target.value)
			dispatch(action)
		},
		clickBtn(){
			let action = actionCreators.addItemAction()
			dispatch(action)
		}
	}
}

export default connect(stateToProps, dispatchToProps)(FinishList);
