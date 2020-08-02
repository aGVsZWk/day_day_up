import React from 'react'
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'
import Money from './workplace/Money'
import Getup from './workplace/Getup'


function Workplace() {
	return (
		<div>
			<div className="topNav">
				<ul>
					<li><Link to="/workplace/money">赚钱教程</Link></li>
					<li><Link to="/workplace/getup">早起攻略</Link></li>
				</ul>
			</div>
			<div className="videoContent">
				<div>
					<h3>职场软技能</h3>
				</div>
				<Route path="/workplace/money" component={Money}></Route>
				<Route path="/workplace/getup" component={Getup}></Route>
			</div>
		</div>
	)
}

export default Workplace
