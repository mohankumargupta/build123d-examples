# %%

from build123d import *
from ocp_vscode import show_all, Camera

# Parameters(mm)

## H base shape ##
length = 67.85
width = 28.57
height = 1.72
notch_width = 9.14
notch_depth = 3

## Tubes ##
tube_radius = 1
long_tube_length = 54.25
short_tube_length = 25.45
long_x_offset = tube_radius + (2.65 / 2)
short_x_offset = tube_radius + (19.17 / 2)

with BuildPart() as builder:
    with BuildSketch() as sketch1:
      Rectangle(width, height=length)
    extrude(amount=height)
    front_face = builder.faces().sort_by(Axis.Y).first
    with BuildSketch(front_face) as sketch2:
       Rectangle(notch_width, height)
    extrude(amount=-notch_depth, mode=Mode.SUBTRACT)
    split(bisect_by=Plane.XZ)
    mirror(about=Plane.XZ)

show_all(reset_camera=Camera.KEEP)


# %%
