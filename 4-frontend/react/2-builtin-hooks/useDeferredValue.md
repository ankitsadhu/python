**## useDeferredValue**

`kind of debounce`, once entire text is written then only setText is render, dont use array or object as refrence is change on render. Only updates when browser is free

useDeferredValue vs useMemo: no need to specify time incase of useDeferred (only runs whenever browser is free)

```js
function debounce(cb) {
  let timeoutId = '';

  return function() {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(function(){
     callback(...args)
    }, 200) 
  }
}


function App() {
  const [text, setText] = useState("")
  const deferredText = useDeferredValue(text)
  
  function handleSearch(e) {
    const value = e.target.value
    setText(value);
  }

  const debouncedMakkeAPICall = useMemo(()=> {debounce(makeApiCall)}, []) # we are caching the debounce so that new instance of debounce fun is created on every render
  function makeApiCall(data) {
    console.log("calling api")
  }

  return (
   <div>
    <input onInput={handleSearch} placeholder="Search"/>
    ([...new Array(100)].map((_, i) => {
      return <MemorizedSearchText key={i} text=deferredText} />
     }})))))
   )
}

function SearchText({text}}) {
 let i =0;
 while(i < 10e) { // to add some delay or show high computation
  i++
 }
 return <h3>{text} </h3>
}

const MemorizedSearchText = memo(SearchText);
```
