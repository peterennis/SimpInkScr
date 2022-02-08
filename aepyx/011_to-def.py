# This Python script is intended to be run from Inkscape's Simple
# Inkscape Scripting extension.

# Force the animation to respond to screen size.
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

# https://github.com/spakin/SimpInkScr/wiki/Copying-objects#clones

tmpl = rect((-50, -50), (50, 50), fill='#0088aa').to_def()
rot = 0.0
for y in range(5):
    for x in range(5):
        tr = inkex.Transform()
        tr.add_translate(x*200 + 100, y*200 + 100)
        tr.add_rotate(rot)
        clone(tmpl, transform=tr)
        rot -= 360/25
