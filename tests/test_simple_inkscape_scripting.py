from simple_inkscape_scripting import SimpleInkscapeScripting
from inkex.tester import ComparisonMixin, InkscapeExtensionTestMixin, TestCase
from inkex.tester.filters import CompareOrderIndependentStyle

class SimpInkScrTrivial(ComparisonMixin, InkscapeExtensionTestMixin, TestCase):
    effect_class = SimpleInkscapeScripting
    compare_filters = [CompareOrderIndependentStyle()]
    comparisons = [
        ('--program=circle((width/2, height/2), 50)',),
        ('--program=ellipse((width/2, height/2), (75, 50))',),
        ('--program=rect((width/2 - 50, height/2 - 30), (width/2 + 50, height/2 + 30))',),
        ('--program=line((width, 0), (0, height))',),
        ('--program=polyline([(0, 300), (150, 0), (300, 300), (150, 200)])',),
        ('--program=polygon([(0, 300), (150, 0), (300, 300), (150, 200)])',),
        ('--program=regular_polygon(5, (100, 100), 80)',),
        ('--program=star(5, (100, 100), (80, 30))',),
        ("--program=arc((width/2, height/2), 100, (pi/5, 9*pi/5), 'slice', fill='yellow', stroke_width=2)",),
        ("--program=path(['M', 226, 34, 'V', 237, 'L', 32, 185, 'C', 32, 185, 45, -9, 226, 34, 'Z'])",),
        ('''--program=
path([Move(226, 34),
      Vert(237),
      Line(32, 185),
      Curve(32, 185, 45, -9, 226, 34),
      ZoneClose()])
''',),
        ('''--program=
r = rect((50, 50), (100, 100))
c = circle((200, 200), 25)
connector(r, c, ctype='orthogonal', curve=15)
''',),
        ("--program=text('Simple Inkscape Scripting', (0, height), font_size='36pt')",),
        ('''--program=
text('Hello, ', (width/2, height/2), font_size='24pt', text_anchor='middle')
more_text('Inkscape', font_weight='bold', fill='#800000')
more_text('!!!')
''',),
        ("--program=image('https://media.inkscape.org/static/images/inkscape-logo.png', (0, 0), embed=False)",)
    ]
    compare_file = 'svg/default-inkscape-SVG.svg'
