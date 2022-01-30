# Scott Pakin - Wiki Animation Example
# https://github.com/spakin/SimpInkScr/wiki/Animation
# ---------------------------------------------------

# Force the animation to respond to screen size.
svg_root.set('width', '100%')
svg_root.set('height', '100%')

# Clear Screen
for elt in svg_root.xpath('//*'):
    if not isinstance(elt, inkex.ShapeElement):
        continue
    if isinstance(elt, inkex.Layer):
        continue
    if isinstance(elt, inkex.Group) and len(elt) == 0:
        continue
    elt.getparent().remove(elt)

def make_rect(center, fill, edge=100):
    return rect(inkex.Vector2d(-edge/2, -edge/2) + center,
                inkex.Vector2d(edge/2, edge/2) + center,
                fill=fill)

r1 = make_rect((50, 50), '#aade87')
r4 = make_rect((0, 0), '#5599ff')

r4.transform = 'translate(%.5f, %.5f) rotate(200) scale(2)' % (width/2, height/2)
r1.animate(r4, duration='3s')
