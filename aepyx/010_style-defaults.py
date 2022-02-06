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

# https://github.com/spakin/SimpInkScr/wiki/Changing-defaults/ff7589deeb37ccd10a4e64b18ec106ca012cf152#styles

circle((100, 100), 25)   # Thin, black stroke, no fill

push_defaults()
style(fill='#d7eef4')    # Faint cyan fill
#circle((200, 100), 25)

#push_defaults()
#style(stroke_width=5)    # Thick stroke
#circle((300, 100), 25)

#push_defaults()
#style(stroke='#216778')  # Dark cyan stroke
#circle((400, 100), 25)

#pop_defaults()           # Undo dark cyan stroke
#circle((500, 100), 25)

#pop_defaults()           # Undo thick stroke
#circle((600, 100), 25)

#pop_defaults()           # Undo faint cyan fill
#circle((700, 100), 25)
