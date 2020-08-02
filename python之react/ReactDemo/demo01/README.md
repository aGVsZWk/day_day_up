redux

## store 常用 api


```javascript
import {createStore} from 'redux'

const defaultState = {}
const reducer = (state=defaultState, action)=>{
	return state
}

store = createStore(reducer)
 
store.getState()


const action = {
	type: 'actionName',
	value: 'xxx'
}
store.dispatch(action)


store.subscribe(aaa)
function aaa() {
	setState(store.getState());
}

```
