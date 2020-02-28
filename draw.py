import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

pts = np.array([[2,2], [6,5], [3,6]])
p = Polygon([[2,2],[6,5],[3,6]], closed=False)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,7)
ax.set_ylim(1,8)
plt.show()

'''
Theory:

Name the nodes and assign locations (per object dictionary?)
Delete respective depth dimension (depends on angle)

0 -> (x,y,z)
1 -> (x,y,z)
2 -> (x,y,z)

Once the dictionary is created, acknowledge the faces:

face 1: node 0, 1, 2
face 1: (x,y,z), (x1,y1,z1), (x2,y2,z2)
p = Polygon(((x,y,z), (x1,y1,z1), (x2,y2,z2)), closed=False);
ax = plot.gca()

...
'''