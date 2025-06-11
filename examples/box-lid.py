#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

#Parameters(mm)
length=155
width=45
bottom_thickness=2
thickness = 2

#Radius and diameters(mm)
corner_radius = 4

with BuildPart() as builder:
    with BuildSketch(Plane.XY) as sketch1:
        rr = RectangleRounded(length, width, radius=corner_radius)
    extrude(amount=bottom_thickness)
    with BuildSketch(Plane.XZ) as sketch2:
        with BuildLine() as line1:
            Polyline(
                (-(length/2+thickness), 0),
                (-(length/2+thickness), 30),
                (-length/2, 30),
                (-length/2, 31),
                (-(length/2 - 1), 31),
                (-(length/2 - 1), 27),
                (-length/2, 26),
                (-length/2, 0),
                close=True
            )
        make_face()
    sweep(path=rr.wire())

part = builder.part

show(builder, sketch2, reset_camera=Camera.KEEP)
#show_all(reset_camera=Camera.KEEP)
print(part.volume)
