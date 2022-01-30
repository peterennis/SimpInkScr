# Scott Pakin - Wiki Animation Example
# https://github.com/spakin/SimpInkScr/wiki/Animation
# ---------------------------------------------------

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

def make_rect(center, fill, edge=100):
    return rect(inkex.Vector2d(-edge/2, -edge/2) + center,
                inkex.Vector2d(edge/2, edge/2) + center,
                fill=fill)

r1 = make_rect((50, 50), '#aade87')
r2 = make_rect((width/2, height/2), '#9955ff')
r3 = make_rect((width - 50, height - 50), '#d35f5f')

r1.animate([r2, r3], duration='3s')

# reverse the animation
r1.animate([r3, r2], duration='3s', begin_time='3s', at_end=True)

# render changes in discrete jumps
r1.animate([r2, r3], duration='3s', begin_time='6s', interpolation='discrete')

# specifiy key times
r1.animate([r2, r3], duration='3s',  begin_time='9s', key_times=[0, 0.75, 1])

# use repeat count
r1.animate([r2, r3], duration='3s', begin_time='12s', repeat_count=3)

# repeat count and repeat time support repeating the animation sequence indefinitely
#r1.animate([r2, r3, r2, r1], duration='3s', begin_time='15s', repeat_count='indefinite')

# invoke animate repeatedly on a target object
# and show example use of attribute filter
r1.animate(r2, duration='2s', begin_time='21s', attr_filter=lambda a: a in ['x', 'y'])
r1.animate(r3, duration='4s', begin_time='23s', attr_filter=lambda a: a not in ['x', 'y'])
