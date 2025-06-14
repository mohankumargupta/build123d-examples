#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

with BuildPart() as builder:
    with BuildSketch(Plane.XZ) as sketch1:
        with BuildLine() as line1:
            Polyline((0,4.6), (0,10.4), (9, 10.4), (6,0),(2.8,0),(2.8, 4.6), close=True)
        make_face()
        with Locations((0, 10.4)):
            Circle(2, mode=Mode.SUBTRACT)
        with Locations((5, 10.4)):
            Circle(1, mode=Mode.SUBTRACT)
    revolve(axis=Axis.Z)
    rim_face = builder.faces().sort_by(Axis.Z)[-2]
    rim = rim_face.outer_wire().edge()
    chamfer(rim, 1)
#show(sketch1, show_sketch_local=True ,reset_camera=Camera.KEEP)
show(builder.part, reset_camera=Camera.KEEP)
#show(rim_face, show_parent=True)
#show_all(reset_camera=Camera.KEEP)

#%% [markdown]
"""
![knob1](https://cdn.jsdelivr.net/gh/mohankumargupta/build123d-examples/images/knob1.jpg)

![knob2](https://cdn.jsdelivr.net/gh/mohankumargupta/build123d-examples/images/knob2.jpg)

![knob3](https://cdn.jsdelivr.net/gh/mohankumargupta/build123d-examples/images/knob3.jpg)
"""



