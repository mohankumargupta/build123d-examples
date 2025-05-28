#%%

from build123d import *
from ocp_vscode import show_all, Camera

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# Parameters (all in mm)
height = 3
font = "Lexend"
font_size = 16
emboss_depth = 1.5

# Outer ring radius and diameters
outer_diameter = 250.4
inner_diameter = 217.6

outer_radius = outer_diameter / 2
inner_radius = inner_diameter / 2

with BuildPart() as outer_ring:
    with BuildSketch(Plane.XY) as sketch1:
        Circle(outer_radius)
        Circle(inner_radius, mode=Mode.SUBTRACT)
    extrude(amount=height)

# Middle ring radius and diameters
outer_diameter = 181.8
inner_diameter = 148.4

outer_radius = outer_diameter / 2
inner_radius = inner_diameter / 2

with BuildPart() as middle_ring:
    with BuildSketch(Plane.XY) as sketch2:
        Circle(outer_radius)
        Circle(inner_radius, mode=Mode.SUBTRACT)
    extrude(amount=height)

# Inner ring radius and diameters
outer_diameter = 112.4
inner_diameter = 79

outer_radius = outer_diameter / 2
inner_radius = inner_diameter / 2
text_path_radius = (outer_radius + inner_radius) / 2

with BuildPart() as inner_ring:
    with BuildSketch(Plane.XY) as sketch3:
        Circle(outer_radius)
        Circle(inner_radius, mode=Mode.SUBTRACT)
    extrude(amount=height)
    top_face = inner_ring.faces().sort_by(Axis.Z).last
    with BuildSketch(top_face, mode=Mode.PRIVATE) as text_path:
       Circle(text_path_radius) 
    with BuildSketch(top_face.rotate(Axis.X, 360)) as sketch4:
        text = Text(" MON ", font_size, 
                    path=text_path.wire(), 
                    position_on_path=0,
                    )
    extrude(amount=3, mode=Mode.ADD) 


# with BuildPart() as builder:
#     add(outer_ring)
#     add(middle_ring)
#     add(inner_ring)

show_all(reset_camera=Camera.KEEP)



