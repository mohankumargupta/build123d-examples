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

class Tube(BasePartObject):
   def __init__(self, length: float):
      with BuildPart() as builder:
        Cylinder(tube_radius, length, rotation=(90, 0, 0))
        top_face = builder.faces().sort_by(Axis.Z).last
        fillet(top_face.edge(), tube_radius)
        split(bisect_by=Plane.XZ, keep=Keep.TOP)
        mirror(about=Plane.XZ)
        split(bisect_by=Plane.XY)      
      super().__init__(part=builder.part)

with BuildPart() as builder:
    with BuildSketch() as sketch1:
      Rectangle(width, height=length)
    extrude(amount=height)
    front_face = builder.faces().sort_by(Axis.Y).first
    with BuildSketch(front_face) as sketch2:
      Rectangle(notch_width, height)
    extrude(amount=-notch_depth, mode=Mode.SUBTRACT)
    split(bisect_by=Plane.XZ, keep=Keep.TOP)
    mirror(about=Plane.XZ)
    top_face = builder.faces().sort_by(Axis.Z).last
    with Locations(Plane(top_face) * Location((-long_x_offset,0,0))):
      Tube(long_tube_length)
    with Locations(Plane(top_face) * Location((-short_x_offset,0,0))):
      Tube(short_tube_length)
    split(bisect_by=Plane.YZ, keep=Keep.BOTTOM)
    mirror(about=Plane.YZ)


show_all(reset_camera=Camera.KEEP)
# export_stl(builder.part, "track.stl")
# export_step(builder.part, "track.step")

# %%
