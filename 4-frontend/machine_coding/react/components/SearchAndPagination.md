**# Search & Pagination**


```
const URL = "https://api.punkapi.com/v2/beers"

export default function App() {
  const PER_PAGE = 25;
  const [beers, setBeers] = useState([])
  const [page, setpage] = useState(1);
  const [beerName, setBeerName] = useState();
  
  const makeAPICall = async (beerName, page, PER_PAGE) => {
    try {
      const beerNameSearch = beerName !== "" ? `beer_name=${beernName}` : ""
      let resp = await fetch(`${URL}?page=${page}&per_page=${PER_PAGE}${beerNameSearch}`);
      resp = await resp.json();
      setBeers(resp)
    } catch(e) {
      console.log("Error while calling api", e)
    }
  }

  useEffect(() => {
    makeApiCall(beerName, page, PER_PAGE);
  }, [page, beerName])

  return (
    <h1> Beer List </h1>
  
    <div>
     <input
      type="text"
      placeholder="Type Beer Name"
      onChange={e => setBeerName(e.target.value)}
      value={value}
      >
    </div>

    <div>
      <label htmlFor="page">Page</label>
      <select id="page" onChange={e => setpage(e.target.value)}>
        <option>1</option>
        <option>2</option>
        <option>3</option>
      </select>
    </div>

    {beers.map((e) => {
      <Beer key= {e.name} {...e} />
    })}
  )
}


const Beer = ({name, tagline, image_url}) => {
  return (
     <div class="beer">
	<div>
         <img src={image_url} alt={name}/>
	</div>
        <div>
          <h2>{name}</h2>
          <h2>{}</h2>
        </div>
     </div>
   )
}

```
