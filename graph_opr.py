import networkx as nx
import matplotlib.pyplot as plt

# create a graph
G = nx.Graph()
# this graph has two connected components
G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('e', 'f')])
# draw this graph
nx.draw(G)
print('this graph has ', nx.number_connected_components(G), 'connected components')
# print each connected components
for comp in nx.connected_components(G):
    print(comp)
plt.show()
