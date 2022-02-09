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

# https://github.com/spakin/SimpInkScr/wiki/Effects#live-path-effects

roughen = path_effect('rough_hatches',
                      do_bend=False,
                      fat_output=False,
                      dist_rdm=[0, 1])
e = ellipse((150, 100), (150, 100), stroke='#7f2aff', stroke_width=2)
p = e.to_path()
p.apply_path_effect(roughen)
