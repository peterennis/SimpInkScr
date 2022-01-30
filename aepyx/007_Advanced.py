# Scott Pakin - Wiki Animation Example
# https://github.com/spakin/SimpInkScr/wiki/Advanced-usage
# --------------------------------------------------------

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

# set the page size to A5 paper and hide the grid
svg_root.set('width', '148mm')
svg_root.set('height', '210mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')

# using Inkscape's inkex API
c = inkex.Circle(cx="200", cy="200", r="50")
inkex_object(c)

# using Simple Inkscape Scripting's shape API
p1 = path('M 61 196 C 125 132 128 263 192 196 253 132 263 263 320 200 384 128 384 256 448 195 515 131 512 256 576 192',
          stroke='purple', stroke_width=4)
p2 = duplicate(p1, stroke='magenta')
obj = p2.get_inkex_object()
obj.set('d', obj.path.rotate(15, inkex.Vector2d(61, 196)))
