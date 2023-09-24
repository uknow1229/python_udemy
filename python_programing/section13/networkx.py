# NetworkX
# ネットワーク図などそういったものを表示したい時に使われる！

import matplotlib.pyplot as pit
import networkx as nx


G = nx.Graph()
G.add_node(1)

G .add_nodes_from([2, 3])

G.add_edge(1, 2)
G.add_edge(2, 3)

nx.draw(G)
plt.show()

