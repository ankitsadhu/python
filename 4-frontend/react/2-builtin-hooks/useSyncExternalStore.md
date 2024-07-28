## useSyncExternalStore

Subscribe to external data sources like variables outside component, event listeners. Whenever external data changes, it triggers the re-render.

```js
sulet score = 0;
let emit = null;

function App() {
   function handleScoreIncrease() {
     score++;
     emit(); // notifies react to re-render
   }
   
   return (
	<div>
         <Score />
         <button onClick={handleScoreIncrease}>Increase Score</button>
	</div>
   )
}

function subscribe(notify) {
	emit = notify
}

function getSnapshot() {
	return score

	return function() {
	// cleanup function
	}
}

function Score() {
	const updatedScore = useSyncExternalStore(subscribe, getSnapshot())
	return <h1>{updatedScore}</h1>
}
```
