const CHART_DATA = [
    {
        id: "dep-1", 
        name: "Legal", 
        ticketCount: 32, 
        colour: '#3F888F'
    }
]

export default CHART_DATA;

// Animate transition from 0 to full height
// No of tickets(Y-axis) vs Depts (X-axis)

// Approach 2: SVG
// Approach 3: HTML Canvas



export function App() {
    const [showChart, setShowChart] = useState(false);
    return (
        <main className="container">
            <button
                onClick={()=> setShowChart(pre => !prev)}>
                    Toggle Chart
            </button>
            {showChart ?
                <BarChart data={CHART_DATA}/> : null
            }
        </main>
    )
}

const Bar = ({
    name,
    color,
    height,
    ticketCount
}) => {
    return (
        <div 
            className="bar"
            style={{
                height: `${height}%`,
                backgroundColor: color
            }}
        >
        <div className="tooltip">{name} - {ticketCount}</div>            
        </div>
    )
}

const BarChart = ({data}) => {
    const maxTicketCount = useMemo(()=> {
        return Math.max(...data.map(Item => Item.ticketCount))
    }, [])

    return (
        <div className="chart-container">
            <div className="chart">
                {
                    data.map(item => {
                        return <Bar
                            key={item.id}
                            height={(item.ticketCount /maxTicketCount) * 100}
                            {...item}/>
                    })
                }
            </div>
            <div className="y-axis-label">No of tickets</div>
            <div className="x-axis-label">Deptt</div>
        </div>
    )
}


