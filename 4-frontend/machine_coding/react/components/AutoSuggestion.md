# AutoSuggestion


```js
const LATENCY = 200;

function getRandomBool(n) {
   const threshold = 1000;
   if(n > threshold) n = threshold;
   return Math.floor(Math.random() * threshold) % n === 0;
}

function getSuggestion(text) {
   const pre = 'pre'
   const post = 'post'
   let results = []

   if(getRandomBool(2)) {
      results.push(text)
   }

   if(getRandomBool(2)) {
      results.push(text + post);
   }

   if(getRandomBool(2)) {
      results.push(pre + text + post)
   }

    return new Pormise((resolve, reject) => {
        const randomTimeout = Math.random() * LATENCY;
        setTimeout(()=> {
           if(getRandomBool(FAILURE_COUNT)) {
             reject()
	   } else {
             resolve(results)
	   }
	}, randomTimeout)
  
    })

}
```


```js
const App = () => {
  const inputRef = useRef();
  const suggestionAreaRef = useRef();
  const [searchQuery, setSearchQuery] = useState('')
  const [suggestionList, setSuggestionList] = useState([])
  const [IsSuggestionListVisible, setIsSuggestionListVisible] = useState(false);

  const handleChange = (e) => {
    const {value} = e.target;
    setSearchQuery(value);
    makeAPICall(value)
  }

  const makeAPIcall = async (query) => {
    try {
     let response = await getSuggestion(query);
     setSuggestionList(response)
    } catch (e) {
      setSuggestionList([)
      console.error("Error while getting suggestion")
    }
  }

   useEffect(()=> {
     window.addEventListener('click', e => {
          if(e.target !== inputRef.current && e.target !== suggestionAreaRef.current) {
           setIsSuggestionListVisible(false)
	}
     })
 
     return () => {
       window.removeEventListener('click', () => {});
     }
   })

  return (
     <main className="App">
	<input 
          type="text" 
          name="search" 
          placeholder="search"
          onFoucs={()=> setIsSuggestionListVisible(true)}
          // onBlur={()=> setIsSuggestionListVisible(false)} 
          onChange={handleChange}
          id="search"
          value={searchQuery}
          ref={inputRef}
	 />
  
        {IsSuggestionListVisible && 
	   <div id="suggestion-area" ref={suggestionRef}>
	    {suggestionList.map((e) => 
		<div onClick={()=> setSearchQuery(e)}>
		{e}
		</div>)
	     }
	   </div>
        }
       </main>
  )
}
```
