from build123d import *
from ocp_vscode import show_all, show_object

# Parameters
height = 300 * MM
font_size = 40
emboss_depth = 5 * MM

# Radius/diameter

r2 = 100 * MM # Radius of the base cylinder
r1 = 80  * MM # Radius of the text path circle

with BuildPart() as my_part:
    Cylinder(radius=r2, height=height, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    top_face = my_part.faces().sort_by(Axis.Z)[-1]

    with BuildSketch(top_face, mode=Mode.PRIVATE) as circle:
       Circle(radius=r1)

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
#show_object()
#show_all(axes=False, axes0=False, black_edges=False)
