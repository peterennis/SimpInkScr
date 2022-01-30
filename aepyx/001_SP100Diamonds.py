# Scott Pakin - Generate 100 Diamonds
# https://github.com/spakin/SimpInkScr
# ------------------------------------
for i in range(100):
    x, y = uniform(0, width), uniform(0, height)
    rect((-5, -5), (5, 5),
         transform='translate(%g, %g) scale(0.75, 1) rotate(45)' % (x, y),
         fill='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256)))
