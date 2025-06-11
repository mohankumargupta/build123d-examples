#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

with BuildPart() as builder:
    Box(10,10,10)

"""
from build123d import *

# --- Potentially import an SVG ---
# This part is highly dependent on the SVG's structure and how build123d imports it.
# You might use import_svg_as_buildline_code and then construct the sketch from those lines.
# Or, if import_svg gives you a sketch directly:
#
# with BuildSketch() as wifi_symbol_2d:
#     # If your SVG is simple and directly usable as a sketch
#     add(import_svg("path/to/your/wifi_icon.svg"))
#
# For a more manual approach if the SVG is complex or needs cleanup:
# with BuildSketch() as wifi_symbol_2d:
    # Create the arcs and the base point of the wifi symbol
    # This is a simplified representation. You'd need to define
    # the precise geometry (radii, start/end angles, center points)
    # based on the wifi symbol's appearance.

    # Example of creating arcs (you'll need several, properly positioned and sized)
    # Arc((0, 0), radius_1, start_angle_1, end_angle_1)
    # Arc((0, 0), radius_2, start_angle_2, end_angle_2)
    # Arc((0, 0), radius_3, start_angle_3, end_angle_3)
    # Circle(radius_base, mode=Mode.ADD) # For the bottom dot

    # You would likely need to combine these primitive shapes using operations
    # or ensure they form a closed profile if not importing.
    # For instance, you might draw individual arcs and then combine them,
    # or draw sectors of circles.

# --- If you don't have an SVG or prefer to draw it manually ---
# Define the geometry of the Wi-Fi symbol using lines and arcs
# This requires knowing the dimensions and shapes of the symbol's parts.
# The Wi-Fi symbol typically consists of a small circle (or dot) at the bottom
# and a series of concentric arcs fanning out upwards.

base_point_radius = 1.0
arc_spacing = 1.5
arc_thickness = 0.8 # This will be controlled by offsetting if creating filled arcs
num_arcs = 3
arc_angle_degrees = 60 # Total angle of the arcs

with BuildPart() as wifi_3d:
    with BuildSketch() as wifi_symbol_2d:
        # Base dot
        Circle(base_point_radius)

        # Arcs
        current_radius = base_point_radius + arc_spacing
        for i in range(num_arcs):
            # To create filled arcs, you can make two arcs and connect them,
            # or create an offset shape. For simplicity, we'll sketch the centerline
            # and then thicken. Alternatively, create sectors.
            # This example shows creating sectors (pie slices) and then unioning.

            # Outer arc for the current band
            outer_arc_line = Arc(
                (0,0),
                current_radius + arc_thickness / 2,
                start_angle=-arc_angle_degrees / 2,
                end_angle=arc_angle_degrees / 2
            )
            # Inner arc for the current band
            inner_arc_line = Arc(
                (0,0),
                current_radius - arc_thickness / 2,
                start_angle=-arc_angle_degrees / 2,
                end_angle=arc_angle_degrees / 2
            )

            # Create a face from these arcs - this part needs careful construction
            # One way is to create a sector (pie slice)
            with BuildSketch() as arc_sector:
                pts = [
                    (0,0),
                    inner_arc_line @ 0, # Start point of inner arc
                ]
                pts.extend(inner_arc_line.points()) # Points along inner arc
                pts.append(inner_arc_line @ 1) # End point of inner arc
                pts.append(outer_arc_line @ 1) # End point of outer arc
                # Add outer arc points in reverse to close the shape
                outer_points = list(outer_arc_line.points())
                outer_points.reverse()
                pts.extend(outer_points)
                pts.append(outer_arc_line @ 0) # Start point of outer arc
                Polyline(*pts, close=True)
                MakeFace()
            add(arc_sector.sketch) # Add this arc segment to the main sketch

            current_radius += arc_spacing + arc_thickness

    extrude(amount=5) # Extrude the combined sketch

# To view the model (if using ocp_vscode or similar)
# show(wifi_3d)

# To export
# export_stl(wifi_3d.part, "wifi_symbol.stl")
"""

#show(builder, reset_camera=Camera.KEEP)
show_all(reset_camera=Camera.KEEP)
