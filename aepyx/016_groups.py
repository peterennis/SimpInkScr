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

# https://github.com/spakin/SimpInkScr/wiki/Object-collections#groups

rad = 25
evens = group()
odds = group()
fills = ['cyan', 'yellow']
for i in range(8):
    sides = i + 3
    p = regular_polygon(sides, (i*rad*3 + rad*2, 3*rad), rad, fill=fills[i%2])
    if sides%2 == 0:
        evens.add(p)
    else:
        odds.add(p)
