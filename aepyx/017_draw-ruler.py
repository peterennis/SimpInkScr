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

# https://github.com/spakin/SimpInkScr/wiki/Other-features#unit-conversions

# Define various parameters for rendering a ruler.
ruler_ht = 2.5*cm
short_ht = 4*mm
tall_ht = 7*mm
margin = 5*mm
font_size = 10*pt
n_ticks = (width - 2*margin)/mm
n_ticks = int(n_ticks/10)*10 + 1

# Draw a ruler with labeled tick marks.
rect((0, 0), (width, ruler_ht), stroke_width=2, fill='#fff6d5')
for i in range(0, n_ticks):
    pos = i*mm + margin
    if i%5 == 0:
        line((pos, 0), (pos, tall_ht))
    else:
        line((pos, 0), (pos, short_ht))
    if i%10 == 0:
        text(str(i//10), (pos, tall_ht + font_size),
             font_family='DejaVu Sans, Calibri, sans-serif',
             font_height=font_size, text_anchor='middle')
