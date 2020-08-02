import React, { Component } from 'react';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'
import Index from './components/Index'
import Video from './components/Video'
import Workplace from './components/Workplace'
import './index.css'

// import Index from './pages/Index'
// import List from './pages/List'
// import Home from './pages/Home'


function AppRouter(){
	return (
		<Router>
			<div className="mainDiv">
				<div className="leftNav">
					<h3>一级导航</h3>
					<ul>
						<li><Link to="/">博客首页</Link></li>
						<li><Link to="/video">视频教程</Link></li>
						<li><Link to="/workplace">职场技能</Link></li>
					</ul>
				</div>
				<div className="rightMain">
					<Route path="/" exact component={Index}></Route>
					<Route path="/video" component={Video}></Route>
					<Route path="/workplace" component={Workplace}></Route>
				</div>
			</div>




			{/* <ul style={{display:'none'}}>
				<li><Link to="/">首页</Link></li>
				<li><Link to="/list/123">列表页</Link></li>
				</ul>
				<Route path='/xxx' exact component={Index}></Route>
				<Route path='/list/:id' component={List}></Route>
			<Route path='/home' component={Home}></Route> */}
		</Router>
	)
}

export default AppRouter
