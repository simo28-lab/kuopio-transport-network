# Bus Transportation Network Analysis

This project analyzes daily and weekly bus transportation networks using Python and NetworkX. It constructs graphs from bus stops and routes, computes network metrics, and visualizes traffic patterns.

## Key Highlights

- **Longest Route**: Identified the bus route covering the maximum distance, along with its stops.  
- **Top-10 Most Frequent Stops**: Determined the busiest stops based on arrivals in daily and weekly networks.  
- **Largest Connected Component**: Extracted the largest undirected component to analyze the main network structure.  
- **Average Distance**: Approximated the average shortest-path distance between stops using random sampling and BFS.  
- **Closeness Centrality**: Computed approximate closeness for each stop, highlighting the top-10 most central stops.  
- **Traffic Patterns**: Visualized number of departures per hour for daily and weekly networks.


## Theoretical Appendix: Key Concepts in Network Analysis

This section provides an overview of the theoretical concepts underlying the transportation network analysis.

---

### 1. Longest Route

#### Concept: Geographical Distance and Path Aggregation

Identifying the **longest route** requires calculating the approximate distance of each bus segment and aggregating it for an entire trip.

* **Euclidean Distance:** The distance between consecutive stops (using latitude and longitude) is approximated using the Euclidean distance formula in a 2D space. While an approximation of the actual road distance, it provides a consistent metric for comparison:
    $$d = \sqrt{(\text{lat}_1 - \text{lat}_2)^2 + (\text{lon}_1 - \text{lon}_2)^2}$$
* **Route Length:** The total length of a specific route (identified by `route_I` and `trip_I`) is the sum of these Euclidean distances for all segments the bus travels.

---

### 2. Top-10 Most Frequent Stops

#### Concept: Node Degree (In-degree)

This analysis models the transit system as a **Directed Graph ($\mathbf{G}$)**, where nodes are stops and edges are direct bus connections.

* **In-degree:** To find the busiest arrival stops, we calculate the **In-degree** of each node ($v$). The $\text{in-degree}(v)$ is the number of edges pointing *into* the stop $v$.
    $$\text{in-degree}(v) = \text{Number of arrivals at stop } v$$
* **Interpretation:** Stops with the highest in-degree are the **major attractors** or **arrival hubs** in the network, indicating high incoming traffic volume.

---

### 3. Core Network Structure (Largest Connected Component)

#### Concept: Connectedness and Efficiency

Before calculating path-based metrics, the network is viewed as an **Undirected Graph ($\mathbf{UG}$)**.

* **Connected Component:** A connected component is a subgraph where a path exists between any two nodes within it.
* **Largest Connected Component (LCC):** The LCC is the component containing the maximum number of nodes. It represents the **main, interconnected backbone** of the transit system. All calculated distance metrics are performed *only* on the LCC, as paths cannot be calculated to stops outside this core network.

#### 3.1 Average Shortest-Path Distance

#### Concept: Global Network Efficiency

The average shortest-path distance is a measure of the overall **efficiency** and **compactness** of the LCC.

* **Shortest Path ($\mathbf{d(u,v)}$):** The minimum number of transfers (segments) required to travel between any two stops $u$ and $v$ in the LCC, calculated using **Breadth-First Search (BFS)**.
* **Average Distance ($\mathbf{\bar{d}}$):** The average of all shortest paths between all distinct pairs of nodes. A low $\bar{d}$ suggests an efficient network where most stops are quickly reachable from others.
* **Approximation:** For large networks, calculating all shortest paths is computationally intensive. The analysis uses **random sampling ($\mathbf{k}$)**, calculating shortest paths from a small subset of randomly chosen nodes to all others, providing a statistically sound estimate much faster.

#### 3.2 Closeness Centrality

#### Concept: Accessibility and Speed of Access

Closeness centrality identifies which stops are best positioned to quickly reach *the entire network* and be reached by it.

* **Definition:** The **Closeness Centrality** $C_c(v)$ of a stop $v$ is the **inverse of the sum of its shortest-path distances** to all other nodes ($u \neq v$) in the LCC.
    $$C_c(v) = \frac{N-1}{\sum_{u \neq v} d(v,u)}$$
    where $N$ is the number of nodes in the LCC.
* **Interpretation:** Stops with high $C_c(v)$ are the most **central** in terms of **travel time (number of steps)**, acting as ideal transit points to minimize transfers for reaching any part of the core network.
* **Approximation:** Similar to average distance, **approximate closeness** uses a random sample of nodes ($\mathbf{k}$) to estimate the total distance sum, allowing for fast calculation of this metric across all nodes.

---

### 4. Traffic Patterns (Departures per Hour)

#### Concept: Temporal Dynamics and Peak Load

This analysis focuses on the temporal dimension of the network.

* **Time Series Analysis:** The total number of bus departures (edges) is aggregated by the hour of the day.
* **Distribution:** The resulting bar chart shows the distribution of the system's workload over 24 hours.
* **Peak Hours:** High bars indicate **peak hours** (rush hours), which are critical for service planning and resource allocation. Comparing the daily and weekly distributions helps distinguish between typical weekday commuting patterns and weekend/off-peak usage.





 ## Visualizations

![Daily Departures](daily_departures_kuopio.png)
![Weekly Departures](weekly_departures_kuopio.png) 


## Usage


1. **Place CSV files**:

- `network_nodes.csv`  
- `network_temporal_day.csv`  
- `network_temporal_week.csv`  

2. **Install required Python packages

```bash
pip install pandas numpy networkx matplotlib
Run the script:

Bash

python Progetto_Python.py






