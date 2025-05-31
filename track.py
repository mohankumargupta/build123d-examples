# %%

from build123d import *
from ocp_vscode import show_all, show_object, Camera

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
    

    # edges = builder.edges()
    # top_exterior_edge = top_face.outer_wire().edges()

    # bottom_edges = edges.group_by(Axis.Z)[0]
    # vertical_edges = edges.group_by(Axis.Z)[1]
    # #top_interior_edges = builder.edges().group_by(Axis.Z)[2].filter_by(Edge.is_interior)
    

    # fillet(bottom_edges, radius=0.2)
    # #fillet(vertical_edges, radius=0.0000001)

    # fillet(top_exterior_edge, radius=0.2)


    
  

show_all(reset_camera=Camera.KEEP)
#show_object(builder, reset_camera=Camera.KEEP)
# export_stl(builder.part, "track.stl")
# export_step(builder.part, "track.step")

# %%
