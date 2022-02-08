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

# https://github.com/spakin/SimpInkScr/wiki/Effects#gradients

grad = linear_gradient((0, 0), (0, 1))
for i in range(5):
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    grad.add_stop(i/4.0, '#%02X%02X%02X' % (r, g, b))
ellipse((200, 150), (200, 150), fill=grad)
