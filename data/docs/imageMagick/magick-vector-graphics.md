[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[MVG Overview](http://nextgen.imagemagick.org/www/magick-vector-graphics.html#overview) • [Drawing Primitives](http://nextgen.imagemagick.org/www/magick-vector-graphics.html#primitives)

This specification defines the features and syntax for Magick Vector Graphics (MVG), a modularized language for describing two-dimensional vector and mixed vector/raster graphics in ImageMagick. You can use the language to draw from the command line, from an MVG file, from an [SVG -- Scalable Vector Graphics](http://www.w3.org/TR/SVG/) file or from one of the ImageMagick [program interfaces](http://nextgen.imagemagick.org/www/api.html). Use this command, for example, to render an arc:
    
    
    convert -size 100x60 canvas:skyblue -fill white -stroke black \
      -draw "path \'M 30,40  A 30,20  20  0,0 70,20 A 30,20  20  1,0 30,40 Z \'" \
      arc.png');
    

and here is the result:

[![arc](../images/arc.png)](../images/arc.png) 


When the drawing gets sufficiently complex, we recommend you assemble the graphic primitives into a MVG file. For our example, we use [piechart.mvg](../source/piechart.mvg):
    
    
    push graphic-context
      viewbox 0 0 624 369
      affine 0.283636 0 0 0.283846 -0 -0
      push graphic-context
        push graphic-context
          fill 'darkslateblue'
          stroke 'blue'
          stroke-width 1
          rectangle 1,1 2199,1299
        pop graphic-context
        push graphic-context
          font-size 40
          fill 'white'
          stroke-width 1
          text 600,1100 'Average: 20.0'
        pop graphic-context
        push graphic-context
          fill 'red'
          stroke 'black'
          stroke-width 5
          path 'M700.0,600.0 L340.0,600.0 A360.0,360.0 0 0,1 408.1452123287954,389.2376150414973 z'
        pop graphic-context
        push graphic-context
          font-size 40
          fill 'white'
          stroke-width 1
          text 1400,140 'MagickWand for PHP'
        pop graphic-context
        push graphic-context
          font-size 30
          fill 'white'
          stroke-width 1
          text 1800,140 '(10.0%)'
        pop graphic-context
        push graphic-context
          fill 'red'
          stroke 'black'
          stroke-width 4
          rectangle 1330,100 1370,140
        pop graphic-context
        push graphic-context
          fill 'yellow'
          stroke 'black'
          stroke-width 5
          path 'M700.0,600.0 L408.1452123287954,389.2376150414973 A360.0,360.0 0 0,1 976.5894480359858,369.56936567559273 z'
        pop graphic-context
        push graphic-context
          font-size 40
          fill 'white'
          stroke-width 1
          text 1400,220 'MagickCore'
        pop graphic-context
        push graphic-context
          font-size 30
          fill 'white'
          stroke-width 1
          text 1800,220 '(29.0%)'
        pop graphic-context
        push graphic-context
          fill 'yellow'
          stroke 'black'
          stroke-width 4
          rectangle 1330,180 1370,220
        pop graphic-context
        push graphic-context
          fill 'fuchsia'
          stroke 'black'
          stroke-width 5
          path 'M700.0,600.0 L976.5894480359858,369.56936567559273 A360.0,360.0 0 0,1 964.2680466142854,844.4634932636567 z'
        pop graphic-context
        push graphic-context
          font-size 40
          fill 'white'
          stroke-width 1
          text 1400,300 'MagickWand'
        pop graphic-context
        push graphic-context
          font-size 30
          fill 'white'
          stroke-width 1
          text 1800,300 '(22.9%)'
        pop graphic-context
        push graphic-context
          fill 'fuchsia'
          stroke 'black'
          stroke-width 4
          rectangle 1330,260 1370,300
        pop graphic-context
        push graphic-context
          fill 'blue'
          stroke 'black'
          stroke-width 5
          path 'M700.0,600.0 L964.2680466142854,844.4634932636567 A360.0,360.0 0 0,1 757.853099990584,955.3210081341651 z'
        pop graphic-context
        push graphic-context
          font-size 40
          fill 'white'
          stroke-width 1
          text 1400,380 'JMagick'
        pop graphic-context
        push graphic-context
          font-size 30
          fill 'white'
          stroke-width 1
          text 1800,380 '(10.6%)'
        pop graphic-context
        push graphic-context
          fill 'blue'
          stroke 'black'
          stroke-width 4
          rectangle 1330,340 1370,380
        pop graphic-context
        push graphic-context
          fill 'lime'
          stroke 'black'
          stroke-width 5
          path 'M700.0,600.0 L757.853099990584,955.3210081341651 A360.0,360.0 0 0,1 340.0,600.0 z'
        pop graphic-context
        push graphic-context
          font-size 40
          fill 'white'
          stroke-width 1
          text 1400,460 'Magick++'
        pop graphic-context
        push graphic-context
          font-size 30
          fill 'white'
          stroke-width 1
          text 1800,460 '(27.5%)'
        pop graphic-context
        push graphic-context
          fill 'lime'
          stroke 'black'
          stroke-width 4
          rectangle 1330,420 1370,460
        pop graphic-context
        push graphic-context
          font-size 100
          fill 'white'
          stroke-width 1
          text 100,150 'ImageMagick'
        pop graphic-context
        push graphic-context
          fill 'none'
          stroke 'black'
          stroke-width 5
          circle 700,600 700,960
        pop graphic-context
      pop graphic-context
    pop graphic-context
    

to render a pie chart with this command:
    
    
    convert piechart.mvg piechart.png
    

which produces this rendering:

[![piechart](../images/piechart.png)](../images/piechart.png) 


However, in general, MVG is sufficiently difficult to work with that you probably want to use a program to generate your graphics in the SVG format. ImageMagick automagically converts SVG to MVG and renders your image, for example, we render [piechart.svg](../source/piechart.svg) with this command:
    
    
    convert piechart.svg piechart.jpg
    

to produce the same pie chart we created with the MVG language.

Drawing is available from many of the ImageMagick [program interfaces](http://nextgen.imagemagick.org/www/api.html) as well. ImageMagick converts the drawing API calls to MVG and renders it. Here is example code written in the [MagickWand](http://nextgen.imagemagick.org/www/magick-wand.html) language: 
    
    
    (void) PushDrawingWand(draw_wand);
    {
      const PointInfo points[6] =
      {
        { 180,504 },
        { 282.7,578.6 },
        { 243.5,699.4 },
        { 116.5,699.4 },
        { 77.26,578.6 },
        { 180,504 }
      };
    
      DrawSetStrokeAntialias(draw_wand,True);
      DrawSetStrokeWidth(draw_wand,9);
      DrawSetStrokeLineCap(draw_wand,RoundCap);
      DrawSetStrokeLineJoin(draw_wand,RoundJoin);
      (void) DrawSetStrokeDashArray(draw_wand,0,(const double *)NULL);
      (void) PixelSetColor(color,"#4000c2");
      DrawSetStrokeColor(draw_wand,color);
      DrawSetFillRule(draw_wand,EvenOddRule);
      (void) PixelSetColor(color,"#800000");
      DrawSetFillColor(draw_wand,color);
      DrawPolygon(draw_wand,6,points);
    }
    (void) PopDrawingWand(draw_wand);
    

## MVG Overview

MVG ignores all white-space between commands. This allows multiple MVG commands per line. It is common convention to terminate each MVG command with a new line to make MVG easier to edit and read. This syntax description uses indentation in MVG sequences to aid with understanding. Indentation is supported but is not required.

Metafile wrapper syntax (to support stand-alone MVG files):
    
    
    push graphic-context
      viewbox 0 0 width height
      [ any other MVG commands ]
    pop graphic-context
    

Pattern syntax (saving and restoring context):
    
    
    push pattern id x,y width,height
     push graphic-context
      [ drawing commands ]
     pop graphic-context
    pop pattern
    

an example is (%s is a identifier string):
    
    
    push defs
     push pattern %s 10,10 20,20
      push graphic-context
       fill red
       rectangle 5,5 15,15
      pop graphic-context
      push graphic-context
       fill green
       rectangle 10,10 20,20
      pop graphic-context
     pop pattern
    pop defs
    

For image tiling use:
    
    
    push pattern id x,y width,height
     image Copy ...
    pop pattern
    

Note you can use the pattern for either the fill or stroke like:
    
    
    stroke url(#%s)
    

or
    
    
    fill url(#%s)
    

The clip path defines a clipping area, where only the contained area to be drawn upon. Areas outside of the clipping areare masked.
    
    
    push defs
     push clip-path %s
      push graphic-context
       rectangle 10,10 20,20
      pop graphic-context
     pop clip-path
    pop defs
    clip-path url(#%s)
    

## Drawing Primitives

Here is a complete description of the MVG drawing primitives:

Primitive | Description  
---|---  
affine sx,rx,ry,sy,tx,ty |   
arc x0,y0 x1,y1 a0,a1 |   
bezier x0,y0 ... xn,yn | `Bezier` (spline) requires three or more x,y coordinates to define its shape. The first and last points are the knots (preserved coordinates) and any intermediate coordinates are the control points. If two control points are specified, the line between each end knot and its sequentially respective control point determines the tangent direction of the curve at that end. If one control point is specified, the lines from the end knots to the one control point determines the tangent directions of the curve at each end. If more than two control points are specified, then the additional control points act in combination to determine the intermediate shape of the curve. In order to draw complex curves, it is highly recommended either to use the `Path` primitive or to draw multiple four-point bezier segments with the start and end knots of each successive segment repeated.   
border-color color |   
circle originx,originy perimeterx,perimetery |   
clip-path url(name) |   
clip-rule rule | Choose from these rule types: 
    
    
    evenodd
    nonzero  
  
clip-units units | Choose from these unit types: 
    
    
    userSpace
    userSpaceOnUse
    objectBoundingBox  
  
color x,y method | Choose from these method types: 
    
    
    point
    replace
    floodfill
    filltoborder
    reset  
  
decorate type | Choose from these types of decorations: 
    
    
    none
    line-through
    overline
    underline  
  
ellipse centerx,centery radiusx,radiusy arcstart,arcstop |   
fill color | Choose from any of these [colors](http://nextgen.imagemagick.org/www/color.html).  
fill-opacity opacity | The opacity ranges from 0.0 (fully transparent) to 1.0 (fully opaque) or as a percentage (e.g. 50%).  
fill-rule rule | Choose from these rule types: 
    
    
    evenodd
    nonzero  
  
font name |   
font-family family |   
font-size point-size |   
font-stretch type | Choose from these stretch types: 
    
    
    all
    normal
    ultra-condensed
    extra-condensed
    condensed
    semi-condensed
    semi-expanded
    expanded
    extra-expanded
    ultra-expanded  
  
font-style style | Choose from these styles: 
    
    
    all
    normal
    italic
    oblique  
  
font-weight weight | Choose from these weights: 
    
    
    all
    normal
    bold
    100
    200
    300
    400
    500
    600
    700
    800
    900  
  
gradient-units units | Choose from these units: 
    
    
    userSpace
    userSpaceOnUse
    objectBoundingBox  
  
gravity type | Choose from these gravity types: 
    
    
    NorthWest
    North
    NorthEast
    West
    Center
    East
    SouthWest
    South
    SouthEast  
  
image compose x,y width,height 'filename' | Choose from these compose operations:  | Method | Description  
---|---  
clear | Both the color and the alpha of the destination are cleared. Neither the source nor the destination are used as input.  
src | The source is copied to the destination. The destination is not used as input.  
dst | The destination is left untouched.  
**src-over** | The source is composited over the destination.  
dst-over | The destination is composited over the source and the result replaces the destination.  
src-in | The part of the source lying inside of the destination replaces the destination.  
dst-in | The part of the destination lying inside of the source replaces the destination.  
src-out | The part of the source lying outside of the destination replaces the destination.  
dst-out | The part of the destination lying outside of the source replaces the destination.  
src-atop | The part of the source lying inside of the destination is composited onto the destination.  
dst-atop | The part of the destination lying inside of the source is composited over the source and replaces the destination.  
multiply | The source is multiplied by the destination and replaces the destination. The resultant color is always at least as dark as either of the two constituent colors. Multiplying any color with black produces black. Multiplying any color with white leaves the original color unchanged.  
screen | The source and destination are complemented and then multiplied and then replace the destination. The resultant color is always at least as light as either of the two constituent colors. Screening any color with white produces white. Screening any color with black leaves the original color unchanged.  
overlay | Multiplies or screens the colors, dependent on the destination color. Source colors overlay the destination whilst preserving its highlights and shadows. The destination color is not replaced, but is mixed with the source color to reflect the lightness or darkness of the destination.  
darken | Selects the darker of the destination and source colors. The destination is replaced with the source when the source is darker, otherwise it is left unchanged.  
lighten | Selects the lighter of the destination and source colors. The destination is replaced with the source when the source is lighter, otherwise it is left unchanged.  
linear-light | Increase contrast slightly with an impact on the foreground's tonal values.  
color-dodge | Brightens the destination color to reflect the source color. Painting with black produces no change.  
color-burn | Darkens the destination color to reflect the source color. Painting with white produces no change.  
hard-light | Multiplies or screens the colors, dependent on the source color value. If the source color is lighter than 0.5, the destination is lightened as if it were screened. If the source color is darker than 0.5, the destination is darkened, as if it were multiplied. The degree of lightening or darkening is proportional to the difference between the source color and 0.5. If it is equal to 0.5 the destination is unchanged. Painting with pure black or white produces black or white.  
soft-light | Darkens or lightens the colors, dependent on the source color value. If the source color is lighter than 0.5, the destination is lightened. If the source color is darker than 0.5, the destination is darkened, as if it were burned in. The degree of darkening or lightening is proportional to the difference between the source color and 0.5. If it is equal to 0.5, the destination is unchanged. Painting with pure black or white produces a distinctly darker or lighter area, but does not result in pure black or white.  
plus | The source is added to the destination and replaces the destination. This operator is useful for animating a dissolve between two images.  
add | As per 'plus' but transparency data is treated as matte values. As such any transparent areas in either image remain transparent.   
minus | Subtract the colors in the source image from the destination image. When transparency is involved, Opaque areas will be subtracted from any destination opaque areas.   
subtract | Subtract the colors in the source image from the destination image. When transparency is involved transparent areas are subtracted, so only the opaque areas in the source remain opaque in the destination image.   
difference | Subtracts the darker of the two constituent colors from the lighter. Painting with white inverts the destination color. Painting with black produces no change.  
exclusion | Produces an effect similar to that of 'difference', but appears as lower contrast. Painting with white inverts the destination color. Painting with black produces no change.  
xor | The part of the source that lies outside of the destination is combined with the part of the destination that lies outside of the source.  
copy-* | Copy the specified channel in the source image to the same channel in the destination image. If the channel specified in the source image does not exist, (which can only happen for methods, '`copy-opacity`' or '`copy-black`') then it is assumed that the source image is a special grayscale channel image of the values to be copied.   
change-mask | Replace any destination pixel that is the similar to the source images pixel (as defined by the current [-fuzz](http://nextgen.imagemagick.org/www/magick-vector-graphics.html#fuzz) factor), with transparency.   
interline-spacing pixels |   
interword-spacing pixels |   
kerning pixels |   
line x,y x1,y1 |   
matte x,y method | Choose from these methods: 
    
    
    point
    replace
    floodfill
    filltoborder
    reset  
  
offset offset |   
opacity opacity | Use percent (e.g. 50%).  
path path |   
point x,y |   
polygon x,y x1,y1, ..., xn,yn |   
polyline x,y x1,y1, ..., xn,yn |   
pop clip-path |   
pop defs |   
pop gradient |   
pop graphic-context |   
pop pattern |   
push clip-path name |   
push defs |   
push gradient id linear x,y x1,y1 |   
push gradient id radial xc,cy xf,yf radius |   
push graphic-context |   
push pattern id radial x,y width,height |   
rectangle x,y x1,y1 |   
rotate angle |   
roundrectangle x,y x1,y1 width,height |   
scale x,y |   
skewX angle |   
skewX angle |   
stop-color color offset |   
stroke color |   
stroke-antialias 0 • 1 |   
stroke-dasharray none • numeric-list |   
stroke-dashoffset offset |   
stroke-linecap type | Choose from these cap types: 
    
    
    butt
    round
    square  
  
stroke-linejoin type | Choose from these join types: 
    
    
    bevel
    miter
    round  
  
stroke-miterlimit limit |   
stroke-opacity opacity | The opacity ranges from 0.0 (fully transparent) to 1.0 (fully opaque) or as a percentage (e.g. 50%).  
stroke-width width |   
text "text" |   
text-antialias 0 • 1 |   
text-undercolor color |   
translate x,y |   
viewbox x,y x1,y1 |   
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](magick-vector-graphics.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
