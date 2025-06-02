#%%

from build123d import *
from ocp_vscode import show,show_all, Camera

large_radius = 80.0
inner_radius = 20.0
height = 10.0

with BuildPart() as builder:
    Cylinder(large_radius, height)
    top_face = builder.faces().sort_by(Axis.Z).last        
    with BuildSketch(top_face, mode=Mode.PRIVATE) as sketch1:
        Circle(inner_radius)
        Rectangle(10, 2*large_radius)
        Rectangle(2*large_radius, 10)
        
    cir_edges = sketch1.edges().sort_by(Edge.length)[4:8]
    print(len(cir_edges))
#show(builder, reset_camera=Camera.KEEP)
show_all(reset_camera=Camera.KEEP)
