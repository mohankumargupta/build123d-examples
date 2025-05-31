#%%

from build123d import *
from ocp_vscode import show, show_all, Camera

def createText(items: list[str], space_around_words: int):
  return ' ' * space_around_words + (' ' * space_around_words).join(items)

# Parameters(mm)

height = 3
emboss_depth = 1.5
font_size = 12
font = "Arial"

inner_ring_days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
inner_ring_text = createText(inner_ring_days, 5)

middle_ring_days = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
middle_ring_text = createText(middle_ring_days, 5)

outer_ring_days = [str(i+1) for i in range(31)]
outer_ring_text = createText(outer_ring_days, 3)

# Radius and Diameters(mm)
(250.4,217.6),(181.8,148.4),(112.4,79)
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
  def __init__(self, outer_radius: float, inner_radius: float, text: str):

    with BuildPart() as ring_builder:
      Cylinder(outer_radius, height)
      top_face = ring_builder.faces().sort_by(Axis.Z).last
      with BuildSketch(top_face, mode=Mode.PRIVATE) as sketch1:
        Circle(outer_radius)
        Circle((inner_radius+outer_radius)/2, mode=Mode.SUBTRACT)
      text_path = sketch1.face().inner_wires().first
      with BuildSketch(top_face) as sketch2:
        Text(
            text,
            font_size,
            path=text_path,
          )
      extrude(amount=-emboss_depth, mode=Mode.SUBTRACT)
      Cylinder(inner_radius, height, mode=Mode.SUBTRACT)
    super().__init__(part=ring_builder.part)

with BuildPart() as builder:
  Ring(
    outer_radius=inner_ring_outer_radius,
    inner_radius=inner_ring_inner_radius,
    text=inner_ring_text,
  )
  Ring(
    outer_radius=middle_ring_outer_radius,
    inner_radius=middle_ring_inner_radius,
    text=middle_ring_text,
  )
  Ring(
    outer_radius=outer_ring_outer_radius,
    inner_radius=outer_ring_inner_radius,
    text=outer_ring_text,
  )    
  
show_all( reset_camera=Camera.KEEP)
#show(builder, reset_camera=Camera.KEEP)

