```
const App = () => {
	const [count, setCount] = useState(50)
	const elements = [];
        const bufferSpace = 30

	useEffect(()=> {

          const onScroll = () => {
		if(window.innerHeight + window.scrollY >= window.document.body.offsetHeight  - bufferSpace) {
		  setCount(count + 50)
		}
	  }

	  window.addEventListener('scroll', onScroll);

          return () => window.removeEventListener('scroll', onScroll);
	},[count])

	for(let i =0; i < count; i++) {
		elements.push(<div key={i}>{i}</div>)
	}

	return <main>{elements}</main>
}
```
