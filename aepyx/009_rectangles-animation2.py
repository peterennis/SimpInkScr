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

linearGradient2983 = linear_gradient()
linearGradient2983.add_stop(0, '#ffffff', opacity=1)

r01 = rect((0, 0), (32, 0), stroke='#2b1100', fill='#ff0000', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r1 = rect((0, 0), (32, 1024), stroke='#2b1100', fill='#ff0000', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r01.animate([r1], duration='2s')

r02 = rect((1024, 32), (1024, 0), stroke='#2b1100', fill='#ff0000', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r2 = rect((0, 0), (1024, 32), stroke='#2b1100', fill='#ffff00', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r02.animate([r2], duration='2s', begin_time='2s')

r03 = rect((992, 1024), (1024, 1024), stroke='#2b1100', fill='#00ff00', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r3 = rect((992, 0), (1024, 1024), stroke='#2b1100', fill='#00ff00', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r03.animate([r3], duration='2s', begin_time='4s')

r04 = rect((0, 992), (0, 1024), stroke='#2b1100', fill='#00ffff', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r4 = rect((0, 992), (1024, 1024), stroke='#2b1100', fill='#00ffff', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r04.animate([r4], duration='2s', begin_time='6s')

r05 = rect((0, 496), (0, 528), stroke='#2b1100', fill='#800080', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r5 = rect((0, 496), (1024, 528), stroke='#2b1100', fill='#800080', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r05.animate([r5], duration='2s', begin_time='8s')

r06 = rect((496, 0), (528, 0), stroke='#2b1100', fill='#ff00ff', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r6 = rect((496, 0), (528, 1024), stroke='#2b1100', fill='#ff00ff', font_variation_settings='normal', opacity=1, vector_effect='none', fill_opacity=1, fill_rule='evenodd', stroke_width=1, stroke_linecap='butt', stroke_linejoin='miter', stroke_miterlimit=4, stroke_dasharray='none', stroke_dashoffset=0, stroke_opacity=1, _inkscape_stroke='none', stop_color='#000000', stop_opacity=1)
r06.animate([r6], duration='2s', begin_time='10s')
