import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

# create a graph
G = nx.Graph()
# this graph has two connected components
G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('e', 'f')])
# draw this graph
draw(G, layout='circo')
print('this graph has ', nx.number_connected_components(G), 'connected components')
# print each connected components
for comp in nx.connected_components:
    print(comp)

