# %%

from build123d import *
from ocp_vscode import show_all, Camera

length = 67.85
width = 28.57
height = 1.72
notch_width = 9.14
notch_depth = 3

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
