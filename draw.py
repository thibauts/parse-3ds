import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
#import sys 

def importNodes(file, objects="all"):
    parsed = []
    with open(file, "r") as a_file:
        for line in a_file:
            parsed.append(line)
        for i in range(0, len(parsed)):
            parsed[i] = parsed[i].rstrip()
    
    nodes = {}
    for i in range(0, len(parsed)):
        if parsed[i][0] != " ":
            print("Found element "+parsed[i])
            coords = []
            for k in parsed[i+1:]:
                print("..."+k)
                if k[0] == " ":
                    print("This is a node ^.")
                    k = k.lstrip()
                    k = k.split(",")
                    for no in range(0,len(k)):
                        k[no] = float(k[no])
                    coords.append(k)
                else:
                    break
            nodes[parsed[i]] = coords[:]
            print("Finished analysing element "+parsed[i])
    print(nodes[0])
    
    
    
if __name__ == "__main__":
    importNodes("./vertices.txt")

'''
pts = np.array([[2,2], [6,5], [3,6]])
p = Polygon([[2,2],[6,5],[3,6]], closed=False)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,7)
ax.set_ylim(1,8)
plt.show()


'''
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