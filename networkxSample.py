import matplotlib.pylab as plt
import networkx as nx

MG=nx.MultiDiGraph()

MG.add_node(1)
MG.add_node(2)
MG.add_node(3)
MG.add_node(4)
MG.add_edge(1,2)
MG.add_edge(1,3)
MG.add_edge(3,4)
MG.add_edge(1,4)
# MG.add_edge(3,2)
# MG.add_edge(2,3)

nx.draw_networkx(MG,pos=nx.spring_layout(MG),with_labels=True)
nx.draw
plt.show()