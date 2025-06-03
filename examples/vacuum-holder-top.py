#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

# Parameters(mm)
length = 160
width = 80
height = 6

small1_x = length/2 - 17
small1_y = 20

medium1_x = length/2 - 20
medium1_y = -7

large1_x = 0
large1_y = 8

# Radius and diameters(mm)
small_diameter = 6
small_radius = small_diameter / 2
medium_diameter = 31
medium_radius = medium_diameter / 2
large_diameter = 52
large_radius = large_diameter / 2

# Main Part
with BuildPart() as builder:
    with BuildSketch(Plane.XY) as sketch1:
        SlotOverall(length, width)
    extrude(amount=height)
    with Locations((-small1_x, small1_y)):
        Hole(small_radius)
    with Locations((-medium1_x, medium1_y)):
        Hole(medium_radius)
    split(bisect_by=Plane.YZ, keep=Keep.BOTTOM)
    mirror(about=Plane.YZ)
    with Locations((large1_x, large1_y)):
        Hole(large_radius)

#show(builder, reset_camera=Camera.KEEP)
show_all(reset_camera=Camera.KEEP)
print(builder.part.volume)
# target: 44952