[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[GetImageHistogram](histogram.html#GetImageHistogram) • [IdentifyPaletteImage](histogram.html#IdentifyPaletteImage) • [IsHistogramImage](histogram.html#IsHistogramImage) • [IsPaletteImage](histogram.html#IsPaletteImage) • [MinMaxStretchImage](histogram.html#MinMaxStretchImage) • [GetNumberColors](histogram.html#GetNumberColors) • [UniqueImageColors](histogram.html#UniqueImageColors)

## [GetImageHistogram](http://www.imagemagick.org/api/MagickCore/histogram_8c.html)

GetImageHistogram() returns the unique colors in an image.

The format of the GetImageHistogram method is:
    
    
    size_t GetImageHistogram(const Image *image,
      size_t *number_colors,ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

file

Write a histogram of the color distribution to this file handle.

exception

return any errors or warnings in this structure.

## [IdentifyPaletteImage](http://www.imagemagick.org/api/MagickCore/histogram_8c.html)

IdentifyPaletteImage() returns MagickTrue if the image has 256 unique colors or less.

The format of the IdentifyPaletteImage method is:
    
    
    MagickBooleanType IdentifyPaletteImage(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

exception

return any errors or warnings in this structure.

## [IsHistogramImage](http://www.imagemagick.org/api/MagickCore/histogram_8c.html)

IsHistogramImage() returns MagickTrue if the image has 1024 unique colors or less.

The format of the IsHistogramImage method is:
    
    
    MagickBooleanType IsHistogramImage(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

exception

return any errors or warnings in this structure.

## [IsPaletteImage](http://www.imagemagick.org/api/MagickCore/histogram_8c.html)

IsPaletteImage() returns MagickTrue if the image is PseudoClass and has 256 unique colors or less.

The format of the IsPaletteImage method is:
    
    
    MagickBooleanType IsPaletteImage(const Image *image)
    

A description of each parameter follows.

image

the image.

## [MinMaxStretchImage](http://www.imagemagick.org/api/MagickCore/histogram_8c.html)

MinMaxStretchImage() uses the exact minimum and maximum values found in each of the channels given, as the BlackPoint and WhitePoint to linearly stretch the colors (and histogram) of the image. The stretch points are also moved further inward by the adjustment values given.

If the adjustment values are both zero this function is equivalent to a perfect normalization (or autolevel) of the image.

Each channel is stretched independantally of each other (producing color distortion) unless the special 'SyncChannels' flag is also provided in the channels setting. If this flag is present the minimum and maximum point will be extracted from all the given channels, and those channels will be stretched by exactly the same amount (preventing color distortion).

In the special case that only ONE value is found in a channel of the image that value is not stretched, that value is left as is.

The 'SyncChannels' is turned on in the 'DefaultChannels' setting by default.

The format of the MinMaxStretchImage method is:
    
    
    MagickBooleanType MinMaxStretchImage(Image *image,const double black,
      const double white,const double gamma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    The image to auto-level 
    
black, white
     move the black / white point inward from the minimum and maximum points by this color value. 
    
gamma
    the gamma. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetNumberColors](http://www.imagemagick.org/api/MagickCore/histogram_8c.html)

GetNumberColors() returns the number of unique colors in an image.

The format of the GetNumberColors method is:
    
    
    size_t GetNumberColors(const Image *image,FILE *file,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

file

Write a histogram of the color distribution to this file handle.

exception

return any errors or warnings in this structure.

## [UniqueImageColors](http://www.imagemagick.org/api/MagickCore/histogram_8c.html)

UniqueImageColors() returns the unique colors of an image.

The format of the UniqueImageColors method is:
    
    
    Image *UniqueImageColors(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

exception

return any errors or warnings in this structure.

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](histogram.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
