# Studying disease spread patterns (Dengue) in Singapore

This is the code of part of a project that aims to study the spread of dengue in Singapore on spatial and temporal basis using network analysis. The data for number of cases reported from all locations in Singapore over the last 10 years was provided and it was visualised by varying different parameters to obtain spreading pattern of the disease over the island on spatial and temporal basis by modeling it as Small world network and Scale free network. The study enabled us to identify hubs of breeding and transmission of Dengue virus which need to be tackled by the government to minimize the spreado of Dengue as humans are the major carrier of the virus. This is because mosquito responsible for spreading the virus (*Ades aegypti*) cannot fly beyond 200-400 meter raidus from the point. of it's birth.  

The data for this study has not been uploaded here in the Repo due to confidentiality.

The data is visualised using python 3.7 and NetworkX 1.1 along with ArcGIS platform and Basemap module for HD map of Singapore. 
As for the data engineering, for Spatial component distance between distinct nodes has been calculated and a new dataset has been created based on inter-nodal distance. This varies from 150 meters to 20,000 meters. Temporally, the data has been organised over a certain time period (20 days timeframe by taking into consideration 14 days of incubation time of virus and 6-7 days to recover from the fever) and then properties of small world and scale free network have been observed. The distance has been calculated using Haversine formula. 

![image](https://user-images.githubusercontent.com/71308636/128586584-85778458-cbb0-4651-bc44-3b564143d891.png)

All the visualisations have been done using "World Imagery" background as shown above.

![image](https://user-images.githubusercontent.com/71308636/128587086-34a8cde9-0b3f-48ed-bab9-c97a10d69a27.png)

![image](https://user-images.githubusercontent.com/71308636/128587092-2c6d39f0-2a0d-45da-a4ef-31057eea71f5.png)

The figures above are for inter-nodal distance of 1000 meters.

For different settings, temporal and spatial case, values calculated are: Number of nodes, Number of Edges, Average Clustering Coefficient and Number of Sub-graphs. Degree of every node was calculated too and a plot of Degree vs Number of nodes was plotted which obeyed the flat tailed distribution (with high clustering coefficient) which is the essence of small-world and scale-free networks. Visually, the trend of the plots follow power-law distribution (pending mathematical verification) and can allow us to conclude that there are few nodes which have a larger degree meaning those nodes with higher degree are strategic nodes which are connected to the ones with smaller degrees. So these nodes need to be targeted for effective dengue prevention. 

![image](https://user-images.githubusercontent.com/71308636/128587273-0573f371-84fe-40a4-b6a3-fdcff4ce1cf5.png)

The Mass Rapid Transit (MRT) system was also analysed to see if the observations correlate with the acutal environment. It seems that the nodes with higher degrees are in the areas where density of trains is maximum, thereby higher probability of human-human transmission. The following image of the MRT map with the area encircled is the location with the nodes that have very high degree.  

![image](https://user-images.githubusercontent.com/71308636/128587214-2325961a-da51-48c0-8cbb-d609cf32434b.png)

Based on this study and different other factors, such as weather, proximity to Malaysia, traffic, industrial area, population density, public transport, etc. the areas encircled above have been observed to be the hotspots for Dengue spreading. 
