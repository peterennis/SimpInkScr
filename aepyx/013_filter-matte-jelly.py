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

# https://github.com/spakin/SimpInkScr/wiki/Effects#filters

# Reproduce Inkscape's Matte Jelly filter.
jelly = filter_effect(name='Matte Jelly',
                      pt1=(-0.098, -0.147),
                      pt2=(1.098, 1.147),
                      color_interpolation_filters='sRGB')
color = jelly.add('ColorMatrix',
                  src1='SourceGraphic',
                  values=[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0.85, 0])
blur = jelly.add('GaussianBlur',
                 src1='SourceAlpha',
                 stdDeviation=7)
specular = jelly.add('SpecularLighting',
                     src1=blur,
                     specularExponent=25,
                     specularConstant=0.9,
                     surfaceScale=5,
                     lighting_color='white')
specular.add('DistantLight',
             elevation=60,
             azimuth=225)
composite = jelly.add('Composite',
                      src1=specular,
                      src2='SourceGraphic',
                      k2=1,
                      k3=1,
                      operator='arithmetic')
jelly.add('Composite',
          src1=composite,
          src2=color,
          operator='atop')

# Apply Matte Jelly to a rectangle with a hole in it.
path([Move(0, 0), Line(0, 128), Line(192, 128), Line(192, 0), Line(0, 0), ZoneClose(),
      Move(32, 32), Line(160, 32), Line(160, 96), Line(32, 96), Line(32, 32), ZoneClose()],
     stroke='#004455',
     fill='#0088aa',
     stroke_width=4,
     filter=jelly)
