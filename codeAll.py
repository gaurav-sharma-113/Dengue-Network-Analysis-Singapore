from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv
import codecs
import networkx as nx
'''m = Basemap(projection='merc', lat_0=1.3, lon_0=103.8,
    area_thresh = 0.01, llcrnrlon=103.52,llcrnrlat=1.12,urcrnrlon=104.16,urcrnrlat=1.56,lat_ts=20,resolution='f')
'''

def evalGraph(f, m, g):
	#opening files for reading and writing
	f1 = csv.reader(open('sample2_' + f + '.csv', 'rb'))

	#skipping first row
	next(f1)

	#doing the calculations for latitudes and longitudes
	labeldict = {}
	pos={}
	list = [0,1,2,3,4,5]
	for row in f1:
		row[6] = float(row[6])
		g.add_edge(row[2], row[5], weight = 1000.0/row[6])
		for i in list :
			if (i == 2 or i == 5):
				continue
			else:
				row[i] = float(row[i])
				i = i+1
		lats = [row[0], row[3]]
		lons = [row[1], row[4]]
		
		mx, my = m(lons, lats)
		pos[row[2]] = (mx[0], my[0])
		pos[row[5]] = (mx[1], my[1])
		labeldict[row[2]] = row[2]
		labeldict[row[5]] = row[5]
	edgewidth = [ d['weight'] for (u,v,d) in g.edges(data=True)]

	#defining the parameters of the graph
	nx.draw_networkx(g, pos, labels = labeldict, with_labels = False, node_size = 25, edge_color = edgewidth, width = 1)
	m.arcgisimage(service='World_Imagery', xpixels = 2500, dpi = 192, verbose= True)
	#m.bluemarble(scale = 2.0)
	#m.shadedrelief()
	#m.etopo()
	plt.savefig('singa' + f + '.pdf', format='pdf', dpi=1800)
	
	#clustering coefficient of each node and the average clustering coefficient
	clusteringdata = nx.clustering(g)
	writeToFile(f, g, clusteringdata)
	
	#plotting the whole network
	plt.show()

def writeToFile(f, g, clusteringdata):
	f2 = csv.writer(open('results_' + f + '.csv','wb'))
	#network parameters - generating edgelist and writing them into the file
	for line in nx.generate_edgelist(g):
    	line.replace('  ','    ')
    	#codecs.encode(line)
    	data1 = line.split("   ")
    	f2.writerow(data1)

	#writing and printing the edges and rows, and their numbers in the file
	edgesnum = ["Number of Edges in the network", g.number_of_edges()]
	f2.writerow([])
	f2.writerow (edgesnum)
	nodesnum = ["Number of Nodes in the network", g.number_of_nodes()]
	f2.writerow([])
	f2.writerow(nodesnum)
	f2.writerow([])
	heading1 = ("Node","Clustering Coefficient of the Node")
	f2.writerow(heading1)
	for key, value in clusteringdata.items():
    	f2.writerow([key, value])
	avg_cluster = ["Average clustering of the network", nx.average_clustering(g)]
	f2.writerow([])
	f2.writerow(avg_cluster)
	#shortest path of each node
	shortestpath = nx.shortest_path_length(g, weight = 'edgewidth')
	f2.writerow([])
	heading2 = ("Shortest Path from Node","Shortest Path to Node")
	f2.writerow (heading2)
	for key, value in shortestpath.items():
    	f2.writerow([key, value])

	#average shortest path length of the subgraphs in the whole graph
	count = 0
	f2.writerow([])
	heading3 = ("Average Shortest Path Length of the subgraph","Edges of the subgraph")
	f2.writerow(heading3)
	for G in nx.connected_component_subgraphs(g):
    	subgraph = [nx.average_shortest_path_length(G, weight = 'edgewidth'), G.edges()]
    	f2.writerow(subgraph)
    	count = count + 1
	number_of_subgraph = ["Number of subgraphs", count]
	f2.writerow(number_of_subgraph)
	f2.writerow([])
	degrees = g.degree()
	heading4 = ("Node", "Degree of the Node")
	f2.writerow(heading4)
	for key, value in degrees.items():
    	f2.writerow([key,value])

def executeGraph():
	# Specifying coordinates of Singapore and mapping it
	m = Basemap(lat_0=1.3, lon_0=103.8,
    	area_thresh = 0.01, llcrnrlon=103.52,llcrnrlat=1.12,urcrnrlon=104.16,urcrnrlat=1.56,lat_ts=20,resolution='f', epsg=3414)
	g = nx.Graph()
	listOfFiles = ["150", "200", "500", "750", "1000", "1250", "1500", "2000", "3000", "5000", "10000", "20000"]
	for f in listOfFiles:
		evalGraph(f, m, g)

if __name__ == "__main__":
	executeGraph()

