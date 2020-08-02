import React from 'react'
import ReactDOM from 'react-dom'
import Xiaojiejie from './Xiaojiejie'
import TodoList from './TodoList'
import FinishList from './FinishList'
import AppRouter from './AppRouter'
import Example from './Example'
import Example2 from './Example2'
import Example3 from './Example3'
import Example4 from './Example4'
import Example5 from './Example5'
import Example6 from './example6/Example6'
import Example7 from './Example7'
import Example8 from './Example8'
import {Provider} from 'react-redux'
import store from './store'


const App = (
	<Provider store={store}>
		<Example8 />
	</Provider>
)

// JSX  javascript and xml
ReactDOM.render(App, document.getElementById('root'))
