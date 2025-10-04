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

1. Place your CSV files (`network_nodes.csv`, `network_temporal_day.csv`, `network_temporal_week.csv`) in the project folder.  
2. Install dependencies:

```bash
pip install pandas numpy networkx matplotlib

## Run the python script

python bus_network_analysis.py

Outputs you will get:

- Top-10 most central stops for daily and weekly networks

- Average path length of the largest connected component

- Longest bus route and its stops

- Bar plots showing departures per hour for day and week networks

## Takeaways

-Understand network structure and efficiency
-Identify key hubs and high-traffic stops
-Visualize daily and weekly activity patterns


This project demonstrates practical graph analysis and network science applied to real-world transport data.
