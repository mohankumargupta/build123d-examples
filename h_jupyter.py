#%%

from build123d import *
from ocp_vscode import show_all, show_object, Camera

length = 100.0
width = 60
height = 10
notch_width = 30
notch_depth = 20

with BuildPart() as builder:
    with BuildSketch() as slab:
       Rectangle(width, height=length)
    extrude(amount=height)
    front_face = builder.faces().sort_by(Axis.Y).first
    with BuildSketch(front_face) as notch:
      Rectangle(notch_width, height)
    extrude(amount=-notch_depth, mode=Mode.SUBTRACT)
    split(bisect_by=Plane.XZ)
    mirror(about=Plane.XZ)

show_all()
#show_all(axes=True, axes)
#show_object(reset_camera=Camera.KEEP)


# %%
