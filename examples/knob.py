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
    with BuildSketch(Plane.XZ.shift_origin((0,0, 10.4))) as sketch2:
        with BuildLine() as line2:
            l1 = Line((-9,0), (-9, -5.35))
            l2 = PolarLine(start=l1@1, length=20, angle=(90-18), length_mode=LengthMode.DIAGONAL, mode=Mode.PRIVATE)
            p1 = l2.find_intersection_points(Axis.X)[0]
            print(p1)
            l3 = Line(l1@1,(p1.X, 0))
            Line(l3@1, l1@0)
        make_face()
    
    r = revolve(axis=Axis(origin=(-9,0), direction=(0,0,1)), mode=Mode.SUBTRACT)
    with PolarLocations(radius=9, count=12) as locs:
        for loc in locs:
            print(loc)
    
        #IntersectingLine(l1@1, direction=(l2%1), other=l2)
        
#show(sketch1, show_sketch_local=True ,reset_camera=Camera.KEEP)
show(builder.part, reset_camera=Camera.KEEP)
#show(rim_face, show_parent=True)
#show_all(reset_camera=Camera.KEEP)

"""
#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

with BuildPart() as builder:
    # ------------------ 1. BASE PART (Unchanged) -------------------
    with BuildSketch(Plane.XZ) as sketch1:
        with BuildLine():
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

    # ------------------ 2. DEFINE A LOCAL CUTTER TEMPLATE -------------------
    # Create the cutting sketch once, defined locally around the origin (0,0).
    # This sketch is our "common sketch".
    with BuildSketch(Plane.XZ) as cutter_template:
        with BuildLine(mode=Mode.PRIVATE) as helper_line:
            # Geometry is shifted from x=-9 to x=0 to make it local
            start_pt = (0, 10.4 - 5.35)
            PolarLine(start_pt, length=20, angle=180 - (90-18)) # Angle points "inward"

        # Find intersection with the local top plane (z=10.4)
        top_plane = Plane.XY.offset(10.4)
        intersect_point = top_plane.intersect(helper_line.edges()[0])

        # Create the final triangular cutting face from local points
        Polyline(
            (0, 10.4),
            intersect_point,
            (0, 10.4 - 5.35),
            close=True
        )
        make_face()

    # ------------------ 3. PATTERN THE CUT -------------------
    # Use PolarLocations to define the 12 positions
    with PolarLocations(radius=9, count=12):
        # At each location, create a revolved part from the template and add it.
        # The mode=Mode.SUBTRACT on the revolve operation ensures it cuts away material.
        # The axis=Axis.Z is now LOCAL to each of the 12 positions.
        add(revolve(cutter_template.sketch, axis=Axis.Z, mode=Mode.SUBTRACT))


show(builder.part, reset_camera=Camera.KEEP)
"""    


#%%

from io import BytesIO
from build123d import Compound, ExportSVG, LineType

def write_svg(part, view_port_origin=(-100, 100, 150)):
    visible, hidden = part.project_to_viewport(view_port_origin)
    max_dimension = max(*Compound(children=visible + hidden).bounding_box().size)
    exporter = ExportSVG(scale=100 / max_dimension)
    exporter.add_layer("Visible", line_weight=0.2)
    exporter.add_layer("Hidden", line_color=(99, 99, 99), line_type=LineType.ISO_DOT)
    exporter.add_shape(visible, layer="Visible")
    exporter.add_shape(hidden, layer="Hidden")

    bytes = BytesIO()
    exporter.write(bytes)
    svg = bytes.getvalue().decode("utf-8")
    return svg


from IPython.display import HTML

svg_example1 = write_svg(builder.part)
HTML(svg_example1)


#%% [markdown]
"""
![knob1](https://cdn.jsdelivr.net/gh/mohankumargupta/build123d-examples/images/knob1.jpg)

![knob2](https://cdn.jsdelivr.net/gh/mohankumargupta/build123d-examples/images/knob2.jpg)

![knob3](https://cdn.jsdelivr.net/gh/mohankumargupta/build123d-examples/images/knob3.jpg)
"""



#%%

# from build123d import *
# from ocp_vscode import show, show_all, Camera

# with BuildPart() as test:
#     with BuildSketch(Plane.YZ) as two:
#         with Locations((0, 45)):
#             Circle(15)
#         with BuildLine() as bl:
#             c = Line((75 / 2, 0), (75 / 2, 60), mode=Mode.PRIVATE)
#             u = two.edge().find_tangent(75 / 2 + 90)[0]  # where is the slope 75/2?
#             print(two.edge().tangent_at(u))
#             l1 = IntersectingLine(
#                 two.edge().position_at(u), -two.edge().tangent_at(u), other=c
#             )
#             Line(l1 @ 0, (0, 45))
#             Polyline((0, 0), c @ 0, l1 @ 1)
#             mirror(about=Plane.YZ)
#         make_face()
#         # with Locations((0, 45)):
#         #     Circle(12 / 2, mode=Mode.SUBTRACT)
#     extrude(amount=-13)
# show(test.part,c,two, reset_camera=Camera.KEEP)
