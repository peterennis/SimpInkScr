def make_smiley(fill_color='yellow'):
    'Return a smiley face of a given color.'
    head = circle((0, 0), 25, stroke='black', fill=fill_color)
    r_eye = circle((-9.2, -9.8), 5.4)
    l_eye = circle((9.2, -9.8), 5.4)
    mouth = path([Move(16.2, 4.2),
                  Curve(17.6, 10.3, 9.0, 19.4, 0.2, 19.4),
                  Curve(-9.0, 19.4, -17.8, 10.2, -16.2, 4.2),
                  Curve(-8.7, 9.4, 6.3, 9.4, 16.2, 4.2),
                  ZoneClose()])
    smiley = group([head, r_eye, l_eye, mouth])
    return smiley

# Draw a grid of slightly different smiley faces.
style(stroke='none', fill='black')
for y in range(30, int(height) - 30, 60):
    for x in range(30, int(width) - 30, 60):
        smiley = make_smiley('#%02x%02x00' % (randint(225, 255), randint(225, 255)))
        xform = inkex.Transform()
        xform.add_translate(x, y)
        xform.add_scale(uniform(0.8, 1.1))
        xform.add_rotate(uniform(-10, 10))
        smiley.transform = xform
        