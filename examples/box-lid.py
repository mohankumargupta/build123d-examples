#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

#Parameters(mm)
length=155
width=45
bottom_thickness=2

#Radius and diameters(mm)
corner_radius = 4

with BuildPart() as builder:
    with BuildSketch(Plane.XY) as sketch1:
        RectangleRounded(length, width, radius=corner_radius)
    extrude(amount=bottom_thickness)

part = builder.part

#show(builder, reset_camera=Camera.KEEP)
show_all(reset_camera=Camera.KEEP)
print(part.volume)
