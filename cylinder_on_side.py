# %%

from build123d import *
from ocp_vscode import show_all, Camera

# Parameters
height = 80

# Radius and diameters
radius = 20

# Part
with BuildPart() as builder:
    Cylinder(radius, height, rotation=(90, 0, 0))
    top_face = builder.faces().sort_by(Axis.Z).last
    fillet(top_face.edge(), radius)
    split(bisect_by=Plane.XZ)
    mirror(about=Plane.XZ)
    split(bisect_by=Plane.XY)
    
show_all(reset_camera=Camera.KEEP)


# %%
