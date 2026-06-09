[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

An image gradient creates a gradual blend between two colors formed into a shape that is linear, circular, or ellipical.

For a linear gradient, the operator is either:
    
    
    gradient:
    gradient:color1-color2
    

The for a radial gradient, the operator is either:
    
    
    radial-gradient:
    radial-gradient:color1-color2
    

In the above, color1 is the fromColor and color2 is the toColor, as described in more detail below. The default is white for color1 and black for color2, i.e., white-black.

The default for a linear gradient has color1 at the top of the image and color2 at the bottom of the image. Similarly, the default for a radial gradient has color1 at the center of the image and color2 at the boundary of the image.

Gradient colors may be any valid color defined per <http://www.imagemagick.org/www/color.html>. The named colors of black/white/grayXX are non-linear gray gradients; whereas gray(XX[%]) is a linear gray gradient. For Unix systems, enclose rgb(a) and hex colors in quotes. Use double quotes, if using variables for the values.

Here is an example linear gradient:
    
    
    convert -size 256x256 gradient: linear_gradient.png
    convert -size 256x256 gradient:white-black linear_gradient.png
    

![](http://nextgen.imagemagick.org/images/gradients/linear_gradient.png)

If you want a radial gradient, try:
    
    
    convert -size 256x256 radial-gradient: radial_gradient.png
    convert -size 256x256 radial-gradient:white-black radial_gradient.png
    

![](http://nextgen.imagemagick.org/images/gradients/radial_gradient.png)

As of IM 6.9.2.5, gradients have been enhanced through the use of several -defines.

`-define gradient:vector=x1,y1, x2,y2` ` | Specifies the direction of the linear gradient going from vector1 (x1,y1) to vector2 (x2,y2). Color1 (fromColor) will be located at vector position x1,y1 and color2 (toColor) will be located at vector position x2,y2.  
---|---  
`-define gradient:center=x,y` | Specifies the coordinates of the center point for the radial gradient. The default is the center of the image.  
`-define gradient:radii=x,y` | Specifies the x and y radii of the gradient. If the x radius and the y radius are equal, the shape of the radial gradient will be a circle. If they differ, then the shape will be an ellipse. The default values are the maximum of the half width and half height of the image.  
`-define gradient:angle=angle in degrees` | For a linear gradient, this specifies the direction of the gradient going from color1 to color2 in a clockwise positive manner relative to north (up). For a radial gradient, this specifies the rotation of the gradient in a clockwise positive manner from its normal X-Y orientation.  
`-define gradient:bounding-box=widthxheight+x+y` | Limits the gradient to a larger or smaller region than the image dimensions. If the region defined by the bounding box is smaller than the image, then color1 will be the color of the background.  
  
We also support two convenience defines for setting the linear gradient direction and the radial gradient shape.

`-define gradient:direction=_{NorthWest, North, Northeast, West, East, SouthWest, South, SouthEast}_` | Specifies the direction of the linear gradient towards the top/bottom/left/right or diagonal corners.  
---|---  
`-define gradient:extent=_{Circle, Diagonal, Ellipse, Maximum, Minimum}` | Specifies the shape of an image centered radial gradient. Circle and Maximum draw a circular radial gradient even for rectangular shaped images of radius equal to the larger of the half-width and half-height of the image. The Circle and Maximum options are both equivalent to the default radial gradient. The Minimum option draws a circular radial gradient even for rectangular shaped images of radius equal to the smaller of the half-width and half-height of the image. The Diagonal option draws a circular radial gradient even for rectangular shaped images of radius equal to the half-diagonal of the image. The Ellipse options draws an elliptical radial gradient for rectangular shaped images of radii equal to half the width and half the height of the image.  
  
Examples

The default linear gradient may also be generated in any of the following ways (or by reversing the direction and swapping color1 and color2):
    
    
    convert -size 256x128 -define gradient:direction=north gradient:black-white linear_gradient_default.png
    convert -size 256x128 -define gradient:angle=0 gradient:black-white linear_gradient_default.png
    

![](http://nextgen.imagemagick.org/images/gradients/linear_gradient_default.png)

The equivalent of 
    
    
    convert -size 128x256 gradient: -rotate 90 linear_gradient_east.png
    

can be generate by either of the following (or by reversing the direction and swapping color1 and color2):
    
    
    convert -size 256x128 -define gradient:direction=east gradient:black-white linear_gradient_east.png
    convert -size 256x128 -define gradient:angle=90 gradient:black-white linear_gradient_east.png
    

![](http://nextgen.imagemagick.org/images/gradients/linear_gradient_east.png)

Examples of radial gradients going from black in the center to white at the boundary for the cases of "maximum/circle/default", "minimum", "diagonal", "ellipse" and 45 degree rotated ellipse, respectively, follow below.
    
    
    convert -size 256x128 radial-gradient:black-white radial_gradient_maximum.png
    convert -size 256x128 -define gradient:radii=128,128 radial-gradient:black-white radial_gradient_maximum.png
    

![](http://nextgen.imagemagick.org/images/gradients/radial_gradient_maximum.png)
    
    
    convert -size 256x128 -define gradient:extent=minimum radial-gradient:black-white radial_gradient_minimum.png
    convert -size 256x128 -define gradient:radii=64,64 radial-gradient:black-white radial_gradient_minimum.png
    

![](http://nextgen.imagemagick.org/images/gradients/radial_gradient_minimum.png)
    
    
    convert -size 256x128 -define gradient:extent=diagonal radial-gradient:black-white radial_gradient_diagonal.png
    

![](http://nextgen.imagemagick.org/images/gradients/radial_gradient_diagonal.png)
    
    
    convert -size 256x128 -define gradient:extent=ellipse radial-gradient:black-white radial_gradient_ellipse.png
    convert -size 256x128 -define gradient:radii=128,64 radial-gradient:black-white radial_gradient_ellipse.png
    

![](http://nextgen.imagemagick.org/images/gradients/radial_gradient_ellipse.png)
    
    
    convert -size 256x256 -define gradient:radii=128,64 -define gradient:angle=45 radial-gradient:black-white radial_gradient_ellipse_angle45.png
    

![](http://nextgen.imagemagick.org/images/gradients/radial_gradient_ellipse_angle45.png)

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](gradient.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
