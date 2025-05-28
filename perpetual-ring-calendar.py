#%%

from build123d import *
from ocp_vscode import show_all

# Parameters (all in mm)
height = 3

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

with BuildPart() as inner_ring:
    with BuildSketch(Plane.XY) as sketch3:
        Circle(outer_radius)
        Circle(inner_radius, mode=Mode.SUBTRACT)
    extrude(amount=height)

# with BuildPart() as builder:
#     add(outer_ring)
#     add(middle_ring)
#     add(inner_ring)

show_all()
