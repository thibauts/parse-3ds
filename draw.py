import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import json

def matchNodesFaces(nodes,faces):
    triangles = []
    for i in range(0, len(faces)):
        for k in range(0, len(faces[i])):
            faces[i][k] = nodes[faces[i][k]]
    triangles = faces
    return triangles

def getTriangles(model, target="all"):
    if target == "all":
        triangles = {}
        for i in range(0, len(model)):
            triangles[model[i]["name"]] = matchNodesFaces(nodes, faces)
        return triangles
    else:
        triangles = []
        for i in range(0, len(model)):
            if model[i]["name"] == target:
                nodes = model[i]["vertices"]
                faces = model[i]["faces"]
                triangles = matchNodesFaces(nodes, faces)
        return triangles
        
def make2D(triangles):
    newTrigs = []
    for i in range(0, len(triangles)):
        trig2D = []

        for k in [0,1,2]:
            newVertex = [triangles[i][k][0],triangles[i][k][2]]
            trig2D.append(newVertex)
        newTrigs.append(trig2D)

    return newTrigs
           
if __name__ == "__main__":
    highlightedges = False
    
    model = json.load(open("./everything.json","r"))

    # DEMO MODE
    for k in range(1, len(model)):
        if model[k]["noFaces"] != 0:
            print("Drawing "+model[k]["name"])
            triangles = getTriangles(model,model[k]["name"])
            triangles = make2D(triangles)
            for i in triangles:
                pts = i
                if highlightedges == True:
                    highlighter="b"
                else:
                    highlighter="k"
                 
                p = Polygon(pts, closed=False,facecolor="k", edgecolor=highlighter)
                ax = plt.gca()
                ax.add_patch(p)
        else:
            print("Skipping "+model[k]["name"]+" because it's got no faces.")
            
    ax.set_xlim(-2000,11000)
    ax.set_ylim(-2000,11000)
    plt.show()

