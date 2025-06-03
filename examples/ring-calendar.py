#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

# def createText(items: list[str], space_around_words: int):
#   return ' ' * space_around_words + (' ' * space_around_words).join(items)

def calculate_position_on_path(index: int, total: int) -> float:
    """
    Calculates a normalized position (0.0 to 1.0) on a circular path.

    The path is defined in a Cartesian XY plane. Items are placed starting
    at 90 degrees (North) and proceed clockwise.
    The returned path position 't' maps to Cartesian angles as follows:
    - 0.0 corresponds to 0 degrees (East)
    - 0.25 corresponds to 270 degrees (South)
    - 0.5 corresponds to 180 degrees (West)
    - 0.75 corresponds to 90 degrees (North)
    """
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if not isinstance(total, int):
        raise TypeError("Total must be an integer.")
    if total <= 0:
        raise ValueError("Total must be a positive integer (total > 0).")

    start_position_t = 0.75
    increment_t_per_index = 1.0 / total
    position_t = start_position_t + (index * increment_t_per_index)
    normalized_position_t = position_t % 1.0

    return normalized_position_t

# Parameters(mm)

height = 3
emboss_depth = 1.5
font_size = 12
font = "Arial"
font_style = "Regular"

inner_ring_days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
#inner_ring_days = ["MON"]
#inner_ring_text = createText(inner_ring_days, 6)

middle_ring_days = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
#middle_ring_text = createText(middle_ring_days, 5)

outer_ring_days = [str(i+1) for i in range(31)]
#outer_ring_text = createText(outer_ring_days, 3)

# Radius and Diameters(mm)

## Inner ring
inner_ring_outer_diameter = 112.4
inner_ring_inner_diameter = 79
inner_ring_outer_radius = inner_ring_outer_diameter / 2
inner_ring_inner_radius = inner_ring_inner_diameter / 2

## Middle ring
middle_ring_outer_diameter = 181.8
middle_ring_inner_diameter = 148.4
middle_ring_outer_radius = middle_ring_outer_diameter / 2
middle_ring_inner_radius = middle_ring_inner_diameter / 2

## Outer ring
outer_ring_outer_diameter = 250.4
outer_ring_inner_diameter = 217.6
outer_ring_outer_radius = outer_ring_outer_diameter / 2
outer_ring_inner_radius = outer_ring_inner_diameter / 2

class Ring(BasePartObject):
  def __init__(self, outer_radius: float, inner_radius: float, items: list[str]):

    with BuildPart() as ring_builder:
      Cylinder(outer_radius, height)
      top_face = ring_builder.faces().sort_by(Axis.Z).last
      with BuildSketch(top_face, mode=Mode.PRIVATE) as sketch1:
        Circle(outer_radius)
        Circle((inner_radius+outer_radius)/2, mode=Mode.SUBTRACT)
      text_path = sketch1.face().inner_wires().first
      with BuildSketch(top_face) as sketch2:
        for i in range(len(items)):
            Text(
                items[i],
                font_size,
                font,
                font_style,
                path=text_path,
                position_on_path=calculate_position_on_path(i, len(items)),
            )
      extrude(amount=-emboss_depth, mode=Mode.SUBTRACT)
      Cylinder(inner_radius, height, mode=Mode.SUBTRACT)
    super().__init__(part=ring_builder.part)

with BuildPart() as builder:
  Ring(
    outer_radius=inner_ring_outer_radius,
    inner_radius=inner_ring_inner_radius,
    items=inner_ring_days,
  )
  Ring(
    outer_radius=middle_ring_outer_radius,
    inner_radius=middle_ring_inner_radius,
    items=middle_ring_days,
  )
  Ring(
    outer_radius=outer_ring_outer_radius,
    inner_radius=outer_ring_inner_radius,
    items=outer_ring_days,
  )    
  
show(builder.part, reset_camera=Camera.KEEP)  
#show_all( reset_camera=Camera.KEEP)
#show(builder, reset_camera=Camera.KEEP)

# export_stl(builder.part, file_path="ring-calendar.stl")
# export_step(builder.part, file_path="ring-calendar.step")