#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

with BuildPart() as builder:
    Cylinder(radius=1, height=10)
    # Edges that are circles
    #edges1 = builder.edges().filter_by(GeomType.CIRCLE)[0:2]
    #print(edges1[0].show_topology())
    #print(edges1[1].show_topology())
    
    # Edge that is not a circle
    #edges2 = builder.edges().filter_by(GeomType.CIRCLE, reverse=True)
    #print(edges2[0].show_topology())
#show(builder, reset_camera=Camera.KEEP)
show_all(reset_camera=Camera.KEEP)

