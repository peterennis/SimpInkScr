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

r1 = rect((0, 0), (32, 512), stroke='none', fill='#ff0000', font_variation_settings='normal', display='inline', vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=0.70711, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000')
