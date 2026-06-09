[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[FloodfillPaintImage](paint.html#FloodfillPaintImage) • [OilPaintImage](paint.html#OilPaintImage) • [OpaquePaintImage](paint.html#OpaquePaintImage) • [TransparentPaintImage](paint.html#TransparentPaintImage) • [TransparentPaintImageChroma](paint.html#TransparentPaintImageChroma)

## [FloodfillPaintImage](http://www.imagemagick.org/api/MagickCore/paint_8c.html)

FloodfillPaintImage() changes the color value of any pixel that matches target and is an immediate neighbor. If the method FillToBorderMethod is specified, the color value is changed for any neighbor pixel that does not match the bordercolor member of image.

By default target must match a particular pixel color exactly. However, in many cases two colors may differ by a small amount. The fuzz member of image defines how much tolerance is acceptable to consider two colors as the same. For example, set fuzz to 10 and the color red at intensities of 100 and 102 respectively are now interpreted as the same color for the purposes of the floodfill.

The format of the FloodfillPaintImage method is:
    
    
    MagickBooleanType FloodfillPaintImage(Image *image,
      const DrawInfo *draw_info,const PixelInfo target,
      const ssize_t x_offset,const ssize_t y_offset,
      const MagickBooleanType invert,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
target
    the RGB value of the target color. 
    
x_offset,y_offset
    the starting location of the operation. 
    
invert
    paint any pixel that does not match the target color. 
    
exception
    return any errors or warnings in this structure. 
    

## [OilPaintImage](http://www.imagemagick.org/api/MagickCore/paint_8c.html)

OilPaintImage() applies a special effect filter that simulates an oil painting. Each pixel is replaced by the most frequent color occurring in a circular region defined by radius.

The format of the OilPaintImage method is:
    
    
    Image *OilPaintImage(const Image *image,const double radius,
      const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the circular neighborhood. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [OpaquePaintImage](http://www.imagemagick.org/api/MagickCore/paint_8c.html)

OpaquePaintImage() changes any pixel that matches color with the color defined by fill argument.

By default color must match a particular pixel color exactly. However, in many cases two colors may differ by a small amount. Fuzz defines how much tolerance is acceptable to consider two colors as the same. For example, set fuzz to 10 and the color red at intensities of 100 and 102 respectively are now interpreted as the same color.

The format of the OpaquePaintImage method is:
    
    
    MagickBooleanType OpaquePaintImage(Image *image,const PixelInfo *target,
      const PixelInfo *fill,const MagickBooleanType invert,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
target
    the RGB value of the target color. 
    
fill
    the replacement color. 
    
invert
    paint any pixel that does not match the target color. 
    
exception
    return any errors or warnings in this structure. 
    

## [TransparentPaintImage](http://www.imagemagick.org/api/MagickCore/paint_8c.html)

TransparentPaintImage() changes the opacity value associated with any pixel that matches color to the value defined by opacity.

By default color must match a particular pixel color exactly. However, in many cases two colors may differ by a small amount. Fuzz defines how much tolerance is acceptable to consider two colors as the same. For example, set fuzz to 10 and the color red at intensities of 100 and 102 respectively are now interpreted as the same color.

The format of the TransparentPaintImage method is:
    
    
    MagickBooleanType TransparentPaintImage(Image *image,
      const PixelInfo *target,const Quantum opacity,
      const MagickBooleanType invert,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
target
    the target color. 
    
opacity
    the replacement opacity value. 
    
invert
    paint any pixel that does not match the target color. 
    
exception
    return any errors or warnings in this structure. 
    

## [TransparentPaintImageChroma](http://www.imagemagick.org/api/MagickCore/paint_8c.html)

TransparentPaintImageChroma() changes the opacity value associated with any pixel that matches color to the value defined by opacity.

As there is one fuzz value for the all the channels, TransparentPaintImage() is not suitable for the operations like chroma, where the tolerance for similarity of two color component (RGB) can be different. Thus we define this method to take two target pixels (one low and one high) and all the pixels of an image which are lying between these two pixels are made transparent.

The format of the TransparentPaintImageChroma method is:
    
    
    MagickBooleanType TransparentPaintImageChroma(Image *image,
      const PixelInfo *low,const PixelInfo *high,const Quantum opacity,
      const MagickBooleanType invert,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
low
    the low target color. 
    
high
    the high target color. 
    
opacity
    the replacement opacity value. 
    
invert
    paint any pixel that does not match the target color. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](paint.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
