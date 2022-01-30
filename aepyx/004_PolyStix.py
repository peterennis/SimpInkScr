####################################################
# Use Simple Inkscape Scripting to Draw Some Lines #
####################################################

# Force the image to a known size.
svg_root.set('width', 400)
svg_root.set('height', 300)
svg_root.set('viewBox', '0 0 400 300')

# Clear Screen
for elt in svg_root.xpath('//*'):
    if not isinstance(elt, inkex.ShapeElement):
        continue
    if isinstance(elt, inkex.Layer):
        continue
    if isinstance(elt, inkex.Group) and len(elt) == 0:
        continue
    elt.getparent().remove(elt)

#v = polyline([(0, 0), (2, 2), (0, 4)],
#             fill=None, stroke=None, stroke_linecap=None)

polyline([(10,25),(60,65)])
polyline([(20,25),(60,65)])
polyline([(30,25),(60,65)])
polyline([(40,25),(60,65)])
polyline([(50,25),(60,65)])
polyline([(60,25),(60,65)])
polyline([(70,25),(60,65)])
polyline([(80,25),(60,65)])
polyline([(90,25),(60,65)])
polyline([(100,25),(60,65)])

polyline([(180,65),(100,65),(40,100),(60,65)])
polyline([(190,65),(100,75),(50,110),(60,65)])
polyline([(200,65),(100,85),(60,120),(60,65)])

#polyline([(180,65),(100,90),(100,140),(60,65)])
#polyline([(190,65),(100,100),(100,150),(60,65)])
#polyline([(200,65),(100,110),(100,160),(60,65)])

#polyline([(180,65),(100,90),(120,140),(60,65)])
#polyline([(190,65),(100,100),(120,150),(60,65)])
#polyline([(200,65),(100,110),(120,160),(60,65)])
