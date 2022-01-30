# Scott Pakin - Clear Inkscape Screen
# Public Domain - https://github.com/spakin/SimpInkScr/issues/29#issuecomment-1011882993
# -----------------------------------
for elt in svg_root.xpath('//*'):
    if not isinstance(elt, inkex.ShapeElement):
        continue
    if isinstance(elt, inkex.Layer):
        continue
    if isinstance(elt, inkex.Group) and len(elt) == 0:
        continue
    elt.getparent().remove(elt)
