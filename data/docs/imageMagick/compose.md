[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

This page descibed the Image composition methods that is used to define how two images should be merged together in various image operations. For the Command Line API it is typically set using the [-compose](command-line-options.html#compose) setting option. 

The description of composition uses abstract terminology in order to allow the description to be more precise, while avoiding constant values which are specific to a particular build configuration. Each image pixel is represented by red, green, and blue levels (which are equal for a gray pixel). The build-dependent value QuantumRange is the maximum integral value which may be stored, per pixel, in the red, green, or blue channels of the image. Each image pixel may also optionally (if the image matte channel is enabled) have an associated level of opacity, ranging from opaque to transparent, which may be used to determine the influence of the pixel color when compositing the pixel with another image pixel. If the image matte channel is disabled, then all pixels in the image are treated as opaque. The color of an opaque pixel is fully visible while the color of a transparent pixel color is entirely absent (pixel color is ignored).

By definition, raster images have a rectangular shape. All image rows are of equal length, as are all image columns. By treating the alpha channel as a visual "mask" the rectangular image may be given a "shape" by treating the alpha channel as a cookie-cutter for the image. This is done by setting the pixels within the shape to be opaque, with pixels outside the shape set as transparent. Pixels on the boundary of the shape may be between opaque and transparent in order to provide antialiasing (visually smooth edges). The description of the composition operators use this concept of image "shape" in order to make the description of the operators easier to understand. While it is convenient to describe the operators in terms of "shapes" they are by no means limited to mask-style operations since they are based on continuous floating-point mathematics rather than simple boolean operations.

The following alpha blending (Duff-Porter) compose methods are available:

Method | Description  
---|---  
clear | Both the color and the alpha of the destination are cleared. Neither the source nor the destination are used (except for destinations size and other meta-data which is always preserved.  
src | The source is copied to the destination. The destination is not used as input, though it is cleared.  
dst | The destination is left untouched. The source image is completely ignored.  
src-over | The source is composited over the destination. this is the default alpha blending compose method, when neither the compose setting is set, nor is set in the image meta-data.  
dst-over | The destination is composited over the source and the result replaces the destination.  
src-in | The part of the source lying inside of the destination replaces the destination.  
dst-in | The part of the destination lying inside of the source replaces the destination. Areas not overlaid are cleared.  
src-out | The part of the source lying outside of the destination replaces the destination.  
dst-out | The part of the destination lying outside of the source replaces the destination.  
src-atop | The part of the source lying inside of the destination is composited onto the destination.  
dst-atop | The part of the destination lying inside of the source is composited over the source and replaces the destination. Areas not overlaid are cleared.   
xor | The part of the source that lies outside of the destination is combined with the part of the destination that lies outside of the source. Source or Destination, but not both.   
  
Any of the 'Src-*' methods can also be specified without the 'Src-' part. For example the default compose method can be specified as just 'Over'.

Many of these compose methods will clear the destination image which was not overlaid by the source image. This is to be expected as part of that specific composition methods defintion. You can disable this by setting the special [-define](command-line-options.html#define) 'compose:outside-overlay' to a value of 'false' will turn off this behavior. 

On top of the above 12 Duff-Porter Alpha Composition methods, one special related method '`Copy`' has been provided. This is equivalent to using the '`Src`' with the special [-define](command-line-options.html#define) option '`compose:outside-overlay`' set to '`false`', so as to only modify the overlaid area, without clearing the rest of the image outside the overlaid area. 

The following mathematical composition methods are also available. 

Method | Description  
---|---  
multiply | The source is multiplied by the destination and replaces the destination. The resultant color is always at least as dark as either of the two constituent colors. Multiplying any color with black produces black. Multiplying any color with white leaves the original color unchanged.  
screen | The source and destination are complemented and then multiplied and then replace the destination. The resultant color is always at least as light as either of the two constituent colors. Screening any color with white produces white. Screening any color with black leaves the original color unchanged.  
plus | The source is added to the destination and replaces the destination. This operator is useful for averaging or a controlled merger of two images, rather than a direct overlay.  
add | As per 'plus' but transparency data is treated as matte values. As such any transparent areas in either image remain transparent.   
minus | Subtract the colors in the source image from the destination image. When transparency is involved, opaque areas is subtracted from any destination opaque areas.   
subtract | Subtract the colors in the source image from the destination image. When transparency is involved transparent areas are subtracted, so only the opaque areas in the source remain opaque in the destination image.   
difference | Subtracts the darker of the two constituent colors from the lighter. Painting with white inverts the destination color. Painting with black produces no change.  
exclusion | Produces an effect similar to that of 'difference', but appears as lower contrast. Painting with white inverts the destination color. Painting with black produces no change.  
darken | Selects the darker of the destination and source colors. The destination is replaced with the source when the source is darker, otherwise it is left unchanged.  
lighten | Selects the lighter of the destination and source colors. The destination is replaced with the source when the source is lighter, otherwise it is left unchanged.   
  
Typically these use the default 'Over' alpha blending when transparencies are also involved, except for 'Plus' which uses a 'plus' alpha blending. This means the alpha channel of both images will only be used to ensure that any visible input remains visible even in parts not overlaid. It also means that any values are weighted by the alpha channel of the input and output images. This 'Over' alpha blending is also applied to the lighting composition methods below. 

As of IM v6.6.1-6, if the special '`Sync`' flag is not specified (enabled by default) with the [-channel](command-line-options.html#channel) setting, then the above mathematical compositions will nolonger synchronise its actions with the alpha channel. Instead the math composition will be applied on an individual channel basis as defined by the [-channel](command-line-options.html#channel). This includes the alpha channel. This special usage allows you to perform true mathematics of the image channels, without alpha composition effects, becoming involved. 

This special flag is not applied to the lighting composition methods (see below) even though they are closely related to mathematical composition methods.

The following lighting composition methods are also available. 

Method | Description  
---|---  
linear-dodge | This is equivalent to 'Plus' in that the color channels are simply added, however it does not 'Plus' the alpha channel, but uses the normal 'Over' alpha blending, which transparencies are involved. Produces a sort of additive multiply-like result. Added ImageMagick version 6.5.4-3.   
linear-burn | As 'Linear-Dodge', but also subtract one from the result. Sort of a additive 'Screen' of the images. Added ImageMagick version 6.5.4-3.   
color-dodge | Brightens the destination color to reflect the source color. Painting with black produces no change.  
color-burn | Darkens the destination color to reflect the source color. Painting with white produces no change. Fixed in ImageMagick version 6.5.4-3.   
overlay | Multiplies or screens the colors, dependent on the destination color. Source colors overlay the destination whilst preserving its highlights and shadows. The destination color is not replaced, but is mixed with the source color to reflect the lightness or darkness of the destination.  
hard-light | Multiplies or screens the colors, dependent on the source color value. If the source color is lighter than 0.5, the destination is lightened as if it were screened. If the source color is darker than 0.5, the destination is darkened, as if it were multiplied. The degree of lightening or darkening is proportional to the difference between the source color and 0.5. If it is equal to 0.5 the destination is unchanged. Painting with pure black or white produces black or white.  
linear-light | Like 'Hard-Light' but using linear-dodge and linear-burn instead. Increases contrast slightly with an impact on the foreground's tonal values.  
soft-light | Darkens or lightens the colors, dependent on the source color value. If the source color is lighter than 0.5, the destination is lightened. If the source color is darker than 0.5, the destination is darkened, as if it were burned in. The degree of darkening or lightening is proportional to the difference between the source color and 0.5. If it is equal to 0.5, the destination is unchanged. Painting with pure black or white produces a distinctly darker or lighter area, but does not result in pure black or white. Fixed in ImageMagick version 6.5.4-3.   
pegtop-light | Almost equivalent to 'Soft-Light', but using a continuous mathematical formula rather than two conditionally selected formulae. Added ImageMagick version 6.5.4-3.   
vivid-light | A modified 'Linear-Light' designed to preserve very stong primary and secondary colors in the image. Added ImageMagick version 6.5.4-3.   
pin-light | Similar to 'Hard-Light', but using sharp linear shadings, to simulate the effects of a strong 'pinhole' light source. Added ImageMagick version 6.5.4-3.   
  
Also included are these special purpose compose methods:

Method | Description  
---|---  
copy | This is equivalent to the Duff-Porter composition method '`Src,`' but without clearing the parts of the destination image that is not overlaid.   
copy-* | Copy the specified channel (Red, Green, Blue, Cyan, Magenta, Yellow, Black, or Opacity) in the source image to the same channel in the destination image. If the channel specified does not exist in the source image, (which can only happen for methods, '`copy-opacity`' or '`copy-black`') then it is assumed that the source image is a special grayscale channel image of the values that is to be copied.   
change-mask | Replace any destination pixel that is the similar to the source images pixel (as defined by the current [-fuzz](command-line-options.html#fuzz) factor), with transparency.   
  
On top of these composed methods are a few special ones that not only require the two images that are being merged or overlaid, but have some extra numerical arguments, which are tabled below. 

In the "`composite`" command these composition methods are selected using special options with the arguments needed. They are usually, but not always, the same name as the composite 'method' they use, and replaces the normal use of the [-compose](command-line-options.html#compose) setting in the "`composite`" command. For example... 
    
    
    composite ... -blend 50x50 ...
    

As of IM v6.5.3-4 the "`convert`" command can now also supply these extra arguments to its [-composite](command-line-options.html#composite) operator, using the special [-define](command-line-options.html#define) attribute of '`compose:args`'. This means you can now make use of these special augmented [-compose](command-line-options.html#compose) methods, those the argument and the method both need to be set separately. For example... 
    
    
    convert ... -compose blend  -define compose:args=50,50 -composite ...
    

The following is a table of these special 'argumented' compose methods, with a brief summary of what they do. For more details see the equivalent "composite" command option name. 

Method | Description  
---|---  
dissolve | Arguments: src_percent[xdst_percent]   
Equivalent to "`composite`" [-dissolve](command-line-options.html#dissolve)   
Dissolve the 'source' image by the percentage given before overlaying 'over' the 'destination' image. If src_percent is greater than 100, it starts dissolving the main image so it will become transparent at a value of '`200`'. If both percentages are given, each image are dissolved to the percentages given.   
blend | Arguments: src_percent[xdst_percent]   
Equivalent to "`composite`" [-blend](command-line-options.html#blend)   
Average the images together ('plus') according to the percentages given and each pixels transparency. If only a single percentage value is given it sets the weight of the composite or 'source' image, while the background image is weighted by the exact opposite amount. That is a `-blend 30` merges 30% of the 'source' image with 70% of the 'destination' image. Thus it is equivalent to `-blend 30x70`.   
mathematics | Arguments: A, B, C, D   
Not available in "`composite`" at this time.   
Merge the source and destination images according to the formula   
`A*Sc*Dc + B*Sc + C*Dc + D`   
Can be used to generate a custom composition method that would otherwise need to be implemented using the slow [-fx](command-line-options.html#fx) DIY image operator. Added to ImageMagick version 6.5.4-3.   
As of IM v6.6.1-6 this method will do per-channel math compositions if the 'Sync' flag is removed from [-channel](command-line-options.html#channel), just like all the other mathematical composition methods above.   
modulate | Arguments: brightness[xsaturation]   
Equivalent to "`composite`" [-watermark](command-line-options.html#watermark)   
Take a grayscale image (with alpha mask) and modify the destination image's brightness according to watermark image's grayscale value and the brightness percentage. The destinations color saturation attribute is just direct modified by the saturation percentage, which defaults to 100 percent (no color change).   
displace | Arguments: X-scale[xY-scale][!][%]   
Equivalent to "`composite`" [-displace](command-line-options.html#displace)   
With this option, the 'overlay' image, and optionally the 'mask' image, is used as a relative displacement map, which is used to displace the lookup of what part of the destination image is seen at each point of the overlaid area. Much like the displacement map is a 'lens' that distorts the original 'background' image behind it.   
  
The X-scale is modulated by the 'red' channel of the overlay image while the Y-scale is modulated by the green channel, (the mask image if given is rolled into green channel of the overlay image. This separation allows you to modulate the X and Y lookup displacement separately allowing you to do 2-dimensional displacements, rather than 1-dimensional vectored displacements (using grayscale image).   
  
If the overlay image contains transparency this is used as a mask of the resulting image to remove 'invalid' pixels.   
  
The '%' flag makes the displacement scale relative to the size of the overlay image (100% = half width/height of image). Using '!' switches percentage arguments to refer to the destination image size instead.   
  
Special flags were added Added to ImageMagick version 6.5.3-5.   
distort | Arguments: X-scale[xY-scale[+X-center+Y-center]][!][%]   
Not available in "`composite`" at this time.   
Exactly as per 'Displace' (above), but using absolute coordinates, relative to the center of the overlay (or that given). Basically allows you to generate absolute distortion maps where 'black' will look up the left/top edge, and 'white' looks up the bottom/right edge of the destination image, according to the scale given.   
  
The '!' flag not only switches percentage scaling, to use the destination image, but also the image the center offset of the lookup. This means the overlay can lookup a completely different region of the destination image.   
  
Added to ImageMagick version 6.5.3-5.   
blur | Arguments: Width[xHeight[+Angle][+Angle2]]   
Equivalent to "`composite`" [-blur](command-line-options.html#blur-composite)   
A Variable Blur Mapping Composition method, where each pixel in the overlaid region is replaced with an Elliptical Weighted Average (EWA), with an ellipse (typically a circle) of the given sigma size, scaled according to overlay (source image) grayscale mapping.   
  
As per 'Displace' and 'Distort', the red channel will modulate the width of the ellipse, while the green channel will modulate the height of the ellipse. If a single Angle value is given in the arguments, then the ellipse will then be rotated by the angle specified.   
  
Normally the blue channel of the mapping overlay image is ignored. However if a second ellipse angle is given, then it is assumed that the blue channel defines a variable angle for the ellipse ranging from the first angle to the second angle given. This allows to generate radial blurs, or a rough approximation for rotational blur. Or any mix of the two.   
  
Added to ImageMagick version 6.5.4-0.   
  
To print a complete list of all the available compose operators, use [-list compose](command-line-options.html#list).

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](compose.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
