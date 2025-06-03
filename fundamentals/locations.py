#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

with BuildPart() as builder:
    Box(10,10,10)
    top_face = builder.faces().sort_by(Axis.Z).last
    with Locations(top_face):
        with Locations((3, 0)):
            Cylinder(radius=2, height=5, align=(Align.CENTER, Align.CENTER, Align.MIN))

    # print("---POLAR LOCATIONS---")
    # with Locations(Plane.XY):
    #     locs = PolarLocations(radius=20, count=4, start_angle=0)
    # for i in locs:
    #     print(i)
    # print("---MULTIPLE LOCATIONS---")
    # with Locations((10,10), (-20,-20)) as locs:    
    #     for i in locs:
    #         print(i)
    # print("---GRID LOCATIONS---")
    # with GridLocations(x_spacing=10, 
    #                    y_spacing=5, 
    #                    x_count=2, 
    #                    y_count=2, 
    #                    align=(
    #                        Align.CENTER, Align.CENTER,
    #                    )
    #                    ) as locs:
    #     for i in locs:
    #         print(i)
    # print("---HEX LOCATIONS---")
    # with HexLocations(radius=10, x_count=2, y_count=2) as locs:
    #     for i in locs:
    #         print(i)

#show(builder, reset_camera=Camera.KEEP)
show_all(reset_camera=Camera.KEEP)
