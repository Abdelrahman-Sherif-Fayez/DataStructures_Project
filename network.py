from phase2 import getlist, users_dictionary
import networkx as nx
import matplotlib.pyplot as plt
def network(filepath):
	ourdict = users_dictionary(getlist(filepath))
	alist = []
	for i in ourdict:
		for j in ourdict[i]:
			alist.append((i, j))
	G = nx.DiGraph()
	G.add_edges_from(alist)

	plt.figure(figsize=(9, 9))
	nx.draw_networkx(G, node_color='green')
	plt.show()