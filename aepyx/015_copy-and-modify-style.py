# This Python script is intended to be run from Inkscape's Simple
# Inkscape Scripting extension.

# Respond to screen size.
svg_root.set('width', '100%')
svg_root.set('height', '100%')

def clear_svg():
    for elt in svg_root.xpath('//*'):
        if not isinstance(elt, inkex.ShapeElement):
            continue
        if isinstance(elt, inkex.Layer):
            continue
        if isinstance(elt, inkex.Group) and len(elt) == 0:
            continue
        elt.getparent().remove(elt)

clear_svg()

# https://github.com/spakin/SimpInkScr/wiki/Modifying-existing-objects#altering-a-shapes-style

# First object
down = -3*pi/2
a = arc((75, 75), 50, (down + pi/5, down - pi/5), arc_type='chord',
        stroke='#677821', fill='#abc837', stroke_width=3)

# Second object, which copies the first object's style but triples the
# stroke width
sty = a.style()
sty['stroke_width'] *= 3
path([Move(224, 112),
      Curve(176,64, 192,32, 256,32),
      Curve(320,32, 336,64, 288,112),
      ZoneClose()],
     **sty)

