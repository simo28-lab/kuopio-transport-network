# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 11:54:50 2025

@author: simon
"""



import numpy as np
import pandas as pd
import networkx as nx
import math as mt
import random
import time 
import os
from collections import Counter
import matplotlib.pyplot as plt


project_ = os.getcwd()
nodo = pd.read_csv("C:\\Users\\simon\\Downloads\\progetto python\\progetto\\kuopio\\network_nodes.csv", sep=';')
day = pd.read_csv("C:\\Users\\simon\\Downloads\\progetto python\\progetto\\kuopio\\network_temporal_day.csv", sep=';')
week = pd.read_csv("C:\\Users\\simon\\Downloads\\progetto python\\progetto\\kuopio\\network_temporal_week.csv",sep=';')

##############################################################################
################################# Question 1 #################################
##############################################################################

line=day 

line= pd.merge(line, nodo, left_on=("from_stop_I"), right_on=("stop_I")).drop("stop_I", axis=1) #.drop("stop_I", axis=1)


line = pd.merge(line, nodo, left_on=("to_stop_I"), right_on=("stop_I")).drop("stop_I", axis=1)


print(line.dtypes)


line["distance"] = ((line['lat_x']-line['lat_y'])**2 + (line['lon_x']-line['lon_y'])**2)**0.5
print(line.head())

somma = line.groupby(['route_I', 'trip_I'])['distance'].sum().reset_index() 



sommatop=somma['distance'].max() 
righe_max = somma[somma['distance']==sommatop]

riga=righe_max.iloc[0].tolist() 
print(type(riga[0]))
riga[0]=int(riga[0]) 
riga[1]=int(riga[1])
print(riga) #line that covers the greatest distance


# calculate the number of stops of the line that covers the greatest distance
print('Line ', riga[0])
line=line.sort_values(by='seq') 
for index, row in line.iterrows(): 
    if row['route_I']==riga[0] and row['trip_I']==riga[1]: 
        print(row['seq'],row['name_x']) #

        a=row['seq']
        b=row['name_y'] 
print(a+1,b) 



line_week=week #same for week


line_week= pd.merge(line_week, nodo, left_on=("from_stop_I"), right_on=("stop_I")).drop("stop_I", axis=1)
line_week = pd.merge(line_week, nodo, left_on=("to_stop_I"), right_on=("stop_I")).drop("stop_I", axis=1)

print(line_week.dtypes)


line_week["distance"] = ((line_week['lat_x']-line_week['lat_y'])**2 + (line_week['lon_x']-line_week['lon_y'])**2)**0.5
print(line_week.head())

somma = line_week.groupby(['route_I', 'trip_I'])['distance'].sum().reset_index()
sommatop=somma['distance'].max()
righe_max = somma[somma['distance']==sommatop]
riga=righe_max.iloc[0].tolist()

riga[0]=int(riga[0])
riga[1]=int(riga[1])
print(riga)

# calculate the number of stops of the line that covers the greatest distance
print('Line ', riga[0])
line_week = line_week.sort_values(by='seq')

prev_name = 'parola_random'  

for index, row in line_week.iterrows():
    if row['route_I']==riga[0] and row['trip_I']==riga[1]:
        if row['name_x'] == prev_name:
            continue  
        print(row['seq'],row['name_x'])
        prev_name = row['name_x']  
        a=row['seq']
        b=row['name_y']
print(a+1,b)



##############################################################################
################################# Question 2 #################################
##############################################################################

G_day = nx.DiGraph() #direct graph
diz_day={}
for _, row in nodo.iterrows():
    nodo_id = row['stop_I']
    valore = row['name']
    diz_day[nodo_id]=valore 
    G_day.add_node(nodo_id, name=valore) 
for _, row in day.iterrows():
    partenza=row['from_stop_I']
    arrivo=row['to_stop_I']
    if partenza in diz_day and arrivo in diz_day:
        G_day.add_edge(partenza,arrivo)
        
G_week = nx.Graph()
diz_week={}
for _, row in nodo.iterrows():
    nodo_id = row['stop_I']
    valore = row['name']
    diz_week[nodo_id]=valore
    G_week.add_node(nodo_id, nome=valore)        
    
for _, row in week.iterrows():
    partenza=row['from_stop_I']
    arrivo=row['to_stop_I']
    if partenza in diz_week and arrivo in diz_week:
        G_week.add_edge(partenza,arrivo)


diz_arrivi_day = {} 
for u, v in G_day.edges():
    
    diz_arrivi_day[v] = diz_arrivi_day.get(v, 0) + 1 

diz_arrivi_week = {} 
for u, v in G_week.edges():
   
    diz_arrivi_week[v] = diz_arrivi_week.get(v, 0) + 1


#print the top 10
print("Top 10 stops by number of arrivals (daily):")

top_10_day=sorted(diz_arrivi_day.items(), key=lambda x: x[1], reverse=True )[:10] 


print("Top 10 stops by number of arrivals (weekly):")

top_10_week=sorted(diz_arrivi_week.items(), key=lambda x: x[1], reverse=True )[:10]



for stop_id, count in top_10_day:
    stop_name = diz_day.get(stop_id, "") 
    print(f"ID: {stop_id} --> {stop_name}: # Arrivi, {count}") 

for stop_id, count in top_10_week:
    stop_name = diz_week.get(stop_id, "")
    print(f"ID: {stop_id} --> {stop_name}: # Arrivi, {count}")



##############################################################################
################################# Question 3 #################################
##############################################################################

#day
UG_day = nx.Graph(G_day) # UG_day undirected graph
diz_componenti_day = {}
cc_day=set()

for i in diz_day:
    if i not in diz_componenti_day:
        dfs_nodes_day = tuple(nx.dfs_preorder_nodes(UG_day, source=i))
        dfs_name_nodes_day = tuple(diz_day[n] for n in dfs_nodes_day)
        cc_day.add(dfs_nodes_day)
        for j in dfs_nodes_day:
            diz_componenti_day[j]=diz_day[j]

tupla_max_day = None
lunghezza_max_day = 0

for tupla in cc_day:
    if len(tupla) > lunghezza_max_day:
        tupla_max_day = tupla
        lunghezza_max_day = len(tupla)

remov_day={}
for i, j  in diz_componenti_day.items():
    if i not in tupla_max_day:
       remov_day[i]=j  

UG_day_connesso = UG_day.copy()
for i in remov_day:
    UG_day_connesso.remove_node(i)


#week
UG_week = nx.Graph(G_week) 

diz_componenti_week = {}
cc_week=set()

for i in diz_week:
    if i not in diz_componenti_week:
        dfs_nodes_week = tuple(nx.dfs_preorder_nodes(UG_week, source=i))
        dfs_name_nodes_week = tuple(diz_week[n] for n in dfs_nodes_week)
        cc_week.add(dfs_nodes_week)
        for j in dfs_nodes_week:
            diz_componenti_week[j]=diz_week[j]

tupla_max_week = None
lunghezza_max_week = 0

for tupla in cc_week:
    if len(tupla) > lunghezza_max_week:
        tupla_max_week = tupla
        lunghezza_max_week = len(tupla)

remov_week={}
for i, j  in diz_componenti_week.items():
    if i not in tupla_max_week:
       remov_week[i]=j  

UG_week_connesso = UG_week.copy()
for i in remov_week:
    UG_week_connesso.remove_node(i)



def approx_average_distance(G, k=100):
    nodes = list(G.nodes())
    total = 0
    count = 0

    for _ in range(k):
        u = random.sample(nodes, 1)[0]
        distances = nx.single_source_shortest_path_length(G, u)
        for v, d in distances.items():
            if u != v: 
                total += d 
                count += 1 
    return total / count if count > 0 else float('inf')




print("Estimated average distance daily:", approx_average_distance(UG_day_connesso))
print("Estimated average distance weekly:", approx_average_distance(UG_week_connesso))




def approx_closeness(G, k):
    """
    Approximate closeness centrality for each node in undirected, unweighted graph G
    using k random BFS samples and the given formula.
    """
    nodes = list(G.nodes())
    n = len(nodes)
    sample_nodes = random.sample(nodes, min(k, n))

    scores = {u: 0 for u in nodes}

    for u in nodes:
        total = 0
        for v in sample_nodes:
            if u == v:
                continue
            distances = nx.single_source_shortest_path_length(G, v)
            if u in distances:
                total += (n * distances[u]) / (n - 1)
        if total > 0:
            scores[u] = 1 / (total / k)  # formula corretta
        else:
            scores[u] = 0

    return scores

# Compute scores
closeness_scores_day = approx_closeness(UG_day_connesso, k=50)
closeness_scores_week = approx_closeness(UG_week_connesso, k=50)

# Get Top-10 nodes
top10_day = sorted(closeness_scores_day.items(), key=lambda x: x[1], reverse=True)[:10]
top10_week = sorted(closeness_scores_week.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTop 10 nodes by approximate closeness centrality (day):")
for node, score in top10_day:
    print(f"Stop {node} ({diz_day[node]}): {score:.4f}")


print("\nTop 10 nodes by approximate closeness centrality (week):")
for node, score in top10_week:
    print(f"Stop {node} ({diz_day[node]}): {score:.4f}")

##############################################################################
################################# Question 4 #################################
##############################################################################

#plot-day

day['dep_date_time'] = pd.to_datetime(day['dep_time_ut'], unit='s')
day['hour'] = day['dep_date_time'].dt.hour


departures_per_hour = day['hour'].value_counts().sort_index()


plt.figure(figsize=(12, 6))


plt.bar(departures_per_hour.index, departures_per_hour.values, color='lightgreen')

plt.title('Number of edges over time-day')
plt.xlabel('hours')
plt.ylabel('Number of departures')
plt.xticks(range(0, 24)) 
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.tight_layout() 
plt.show() 



#plot-week

week['dep_date_time'] = pd.to_datetime(week['dep_time_ut'], unit='s') 
week['hour'] = week['dep_date_time'].dt.hour

departures_per_hour = week['hour'].value_counts().sort_index()


plt.figure(figsize=(12, 6))


plt.bar(departures_per_hour.index, departures_per_hour.values, color='green')

plt.title('Number of edges over time-week')
plt.xlabel('hours')
plt.ylabel('Number of departures')
plt.xticks(range(0, 24)) 
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.tight_layout()
plt.show() 



#Calculation of the number of unique locations and direct connections (daily)

start_time_day = time.time()

all_stops = pd.concat([day['from_stop_I'], day['to_stop_I']]).drop_duplicates()
num_unique_locations = all_stops.nunique() 


groups_unique_edges = day.groupby(['from_stop_I', 'to_stop_I']).size()


num_unique_direct_connections = len(groups_unique_edges)

end_time_day = time.time()
execution_time_day = end_time_day - start_time_day
   
  
  
print('the number of unique locations daily is:', num_unique_locations)
print('the number of unique direct connections daily is:', num_unique_direct_connections)
print('the execution daily time is:', f'{execution_time_day:.16f}')

   

#Calculation of the number of unique locations and direct connections (weekly)


start_time_week = time.time()

all_stops = pd.concat([week['from_stop_I'], week['to_stop_I']]).drop_duplicates()
num_unique_locations = all_stops.nunique() 

  
groups_unique_edges = week.groupby(['from_stop_I', 'to_stop_I']).size()

    
num_unique_direct_connections = len(groups_unique_edges)

end_time_week = time.time()
execution_time_week = end_time_week - start_time_week
   
  
  
print('the number of unique locations weekly is:', num_unique_locations)
print('the number of unique direct connections weekly is:', num_unique_direct_connections)
print('the execution weekly time is:', f'{execution_time_week:.16f}')

   





