# %%

from build123d import *
from ocp_vscode import show_all, show_object

# Parameters
height = 300
font_size = 40
emboss_depth = 5

# Radius/diameter

r2 = 100 
r1 = 80 

with BuildPart() as my_part:
    Cylinder(radius=r2, height=height, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    top_face = my_part.faces().sort_by(Axis.Z).last

    with BuildSketch(top_face, mode=Mode.PRIVATE) as circle:
       Circle(r1)

    with BuildSketch(top_face) as text_shape:
      Text(
        "around & around",
        font_size=font_size,
        path=circle.wire(),
        position_on_path=0.5,
        align=(Align.MIN, Align.MIN)
    )
    extrude(amount=emboss_depth)

show_all()
