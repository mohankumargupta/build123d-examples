#%%

from build123d import *
from ocp_vscode import show_all, Camera # Assuming ocp_vscode is used for visualization

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
outer_diameter = 181.8 # Re-defined for middle ring
inner_diameter = 148.4 # Re-defined for middle ring

outer_radius = outer_diameter / 2
inner_radius = inner_diameter / 2

with BuildPart() as middle_ring:
    with BuildSketch(Plane.XY) as sketch2:
        Circle(outer_radius)
        Circle(inner_radius, mode=Mode.SUBTRACT)
    extrude(amount=height)

# Inner ring radius and diameters
outer_diameter = 112.4 # Re-defined for inner ring
inner_diameter = 79    # Re-defined for inner ring

outer_radius = outer_diameter / 2
inner_radius = inner_diameter / 2
text_path_radius = (outer_radius + inner_radius) / 2

with BuildPart() as inner_ring_builder: # Changed context name to avoid confusion with inner_ring part itself
    with BuildSketch(Plane.XY) as sketch3:
        Circle(outer_radius)
        Circle(inner_radius, mode=Mode.SUBTRACT)
    extrude(amount=height)
    
    # Operations are now on the 'inner_ring_builder.part'
    top_face = inner_ring_builder.part.faces().sort_by(Axis.Z).last
    
    # Create the circular path for the text on the top_face
    with BuildSketch(top_face, mode=Mode.PRIVATE) as text_path_on_face_sketch:
       Circle(text_path_radius) 
    text_path_wire = text_path_on_face_sketch.wire() # This is the path

    num_days = len(days)

    for i, day_str in enumerate(days):
        # Calculate position_on_path:
        # 0.25 aligns the start (MON) to 12 o'clock (positive Y axis for a path on XY plane)
        # i / num_days distributes items CCW around the circle.
        pos_on_path = (0.25 + i / num_days) % 1.0

        # Create sketch for each text item on the top_face
        # This sketch is then extruded and added to 'inner_ring_builder.part'
        with BuildSketch(top_face) as day_text_sketch:
            Text(
                f" {day_str} ",  # Using f-string for consistency, same as " " + day_str + " "
                font_size=font_size,
                font=font,
                path=text_path_wire,
                position_on_path=pos_on_path,
                # Align.CENTER for horizontal: centers the text string on the path point.
                # Align.MAX for vertical: places text top (ascender) on path. Characters extend
                # to the "right" of the path tangent. For a CCW circle, "right" is radially outward.
                align=(Align.CENTER, Align.MAX) 
            )
        extrude(amount=emboss_depth, mode=Mode.ADD) # Extrudes from day_text_sketch and adds to current part


# Retrieve the final part from the builder
inner_ring = inner_ring_builder.part

# with BuildPart() as builder:
#     add(outer_ring.part)
#     add(middle_ring.part)
#     add(inner_ring) # inner_ring is now a Part, not a builder

show_all(reset_camera=Camera.KEEP)
