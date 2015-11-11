import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cStringIO import StringIO

g = nx.dodecahedral_graph()
d = nx.to_pydot(g) # d is a pydot graph object, dot options can be easily set
# attributes get converted from networkx,
# use set methods to control dot attributes after creation

png_str = d.create_png()
sio = StringIO() # file-like string, appropriate for imread below
sio.write(png_str)
sio.seek(0)

img = mpimg.imread(sio)
imgplot = plt.imshow(img)
