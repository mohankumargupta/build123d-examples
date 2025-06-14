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



