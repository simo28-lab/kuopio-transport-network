# Bus Transportation Network Analysis

This project analyzes daily and weekly bus transportation networks using Python and NetworkX. It constructs graphs from bus stops and routes, computes network metrics, and visualizes traffic patterns.

## Key Highlights

- **Longest Route**: Identified the bus route covering the maximum distance, along with its stops.  
- **Top-10 Most Frequent Stops**: Determined the busiest stops based on arrivals in daily and weekly networks.  
- **Largest Connected Component**: Extracted the largest undirected component to analyze the main network structure.  
- **Average Distance**: Approximated the average shortest-path distance between stops using random sampling and BFS.  
- **Closeness Centrality**: Computed approximate closeness for each stop, highlighting the top-10 most central stops.  
- **Traffic Patterns**: Visualized number of departures per hour for daily and weekly networks.

 ## Visualizations

![Daily Departures](daily_departures_kuopio.png)
![Weekly Departures](weekly_departures_kuopio.png) 


## Usage


1. **Place your CSV files** in the main project folder (same level as the Python script):

- `network_nodes.csv`  
- `network_temporal_day.csv`  
- `network_temporal_week.csv`  

2. **Install required Python packages**:

```bash
pip install pandas numpy networkx matplotlib
import os

print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())
python Project_Python.py
Key Highlights / Questions
Question 1: Longest Route

Objective: Find the bus line covering the greatest distance in daily and weekly schedules.

Methodology / Theory:

Merged the trip data with the stop coordinates (latitude and longitude).

Computed the Euclidean distance between consecutive stops for each trip:

𝑑
𝑖
𝑠
𝑡
𝑎
𝑛
𝑐
𝑒
=
(
𝑙
𝑎
𝑡
𝑓
𝑟
𝑜
𝑚
−
𝑙
𝑎
𝑡
𝑡
𝑜
)
2
+
(
𝑙
𝑜
𝑛
𝑓
𝑟
𝑜
𝑚
−
𝑙
𝑜
𝑛
𝑡
𝑜
)
2
distance=
(lat
from
	​

−lat
to
	​

)
2
+(lon
from
	​

−lon
to
	​

)
2
	​


Summed distances for each trip to get total route length.

Selected the trip with the maximum total distance.

Results:

Daily network:

Longest line: Route X, Trip Y

Number of stops: N

Last stop: Stop Name

Weekly network:

Longest line: Route X, Trip Y

Number of stops: N

Last stop: Stop Name

This identifies which bus lines cover the largest geographical span, useful for planning and analysis.

Question 2: Top-10 Most Frequent Stops

Objective: Identify the busiest stops based on the number of arrivals.

Methodology / Theory:

Built a directed graph for the daily network and an undirected graph for the weekly network using NetworkX.

Each node represents a bus stop; edges represent trips between stops.

Counted the number of incoming edges for each stop (arrivals).

Sorted stops by arrival count to get the top-10 busiest stops.

Results:

Top 10 stops (daily):

ID: 123 --> Stop Name: # Arrivals 45
ID: 124 --> Stop Name: # Arrivals 42
...


Top 10 stops (weekly):

ID: 123 --> Stop Name: # Arrivals 300
ID: 124 --> Stop Name: # Arrivals 290
...


Frequent stops indicate high traffic and are central for operational efficiency.

Question 3: Largest Connected Component & Centrality

Objective: Analyze network connectivity and identify central stops.

Methodology / Theory:

Largest Connected Component:

Converted graphs to undirected versions.

Applied Depth-First Search (DFS) to identify connected components.

Selected the largest connected component to focus on the main network structure.

Average Distance (approximation):

To measure typical path lengths, we used random sampling:

Selected k random nodes

Computed shortest-path distances from each sampled node to all others

Averaged the distances:

avg distance
≈
∑
𝑖
,
𝑗
𝑑
(
𝑖
,
𝑗
)
number of pairs
avg distance≈
number of pairs
∑
i,j
	​

d(i,j)
	​


This avoids expensive computation for very large networks.

Closeness Centrality (approximation):

Measures how close a stop is to all others in the network.

For each node u, used random BFS samples and the formula:

𝐶
(
𝑢
)
≈
𝑘
∑
𝑣
∈
𝑆
𝑑
(
𝑢
,
𝑣
)
C(u)≈
∑
v∈S
	​

d(u,v)
k
	​


where S is a set of k randomly sampled nodes.

Sorted nodes by centrality to identify top-10 most central stops.

Results:

Estimated average distance:

Daily: X.X

Weekly: Y.Y

Top 10 nodes by closeness centrality (daily/weekly):

Stop 123 (Stop Name): 0.1234
Stop 124 (Stop Name): 0.1201
...


Central nodes are critical for connectivity, efficiency, and passenger accessibility.

Question 4: Traffic Patterns & Unique Connections

Objective: Visualize network activity over time and quantify its structure.

Methodology / Theory:

Converted departure timestamps to hours of the day.

Counted number of edges (departures) per hour to visualize traffic patterns using bar charts.

Calculated unique stops and direct connections by removing duplicates from the daily and weekly data.

Results:

Daily departures: Bar chart shows peak hours.

Weekly departures: Bar chart shows trends across days.

Unique locations and connections:

Daily: X unique stops, Y unique direct connections

Weekly: X unique stops, Y unique direct connections

Plotting the frequency of edges helps identify peak traffic times and understand network load.

Visualizations

Daily Departures


Weekly Departures


Include actual plots generated by your script.

Usage

Place CSV files in the main project folder (same level as the Python script):

network_nodes.csv
network_temporal_day.csv
network_temporal_week.csv


Install required Python packages:

pip install pandas numpy networkx matplotlib


Run the Python script:

python Project_Python.py

Conclusions

The analysis identifies key routes, busiest stops, and central nodes, crucial for the efficiency of Kuopio’s bus network.

Daily and weekly traffic patterns reveal peak hours and high-demand stops, guiding operational decisions.

Approximate algorithms for distance and centrality allow fast estimation without computing all pairwise paths.

Future improvements could include:

Real-time traffic integration

Route optimization

Passenger flow analysis

This project provides a reproducible framework for analyzing urban bus networks and supports decision-making for network planning and management.
