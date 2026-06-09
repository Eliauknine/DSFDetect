[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AdaptiveResizeImage](resize.html#AdaptiveResizeImage) • [InterpolativeResizeImage](resize.html#InterpolativeResizeImage) • [LiquidRescaleImage](resize.html#LiquidRescaleImage) • [MagnifyImage](resize.html#MagnifyImage) • [MinifyImage](resize.html#MinifyImage) • [ResampleImage](resize.html#ResampleImage) • [ResizeImage](resize.html#ResizeImage) • [SampleImage](resize.html#SampleImage) • [ScaleImage](resize.html#ScaleImage) • [ThumbnailImage](resize.html#ThumbnailImage)

## [AdaptiveResizeImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

AdaptiveResizeImage() adaptively resize image with pixel resampling.

This is shortcut function for a fast interpolative resize using mesh interpolation. It works well for small resizes of less than +/- 50 of the original image size. For larger resizing on images a full filtered and slower resize function should be used instead.

The format of the AdaptiveResizeImage method is:
    
    
    Image *AdaptiveResizeImage(const Image *image,const size_t columns,
      const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the resized image. 
    
rows
    the number of rows in the resized image. 
    
exception
    return any errors or warnings in this structure. 
    

## [InterpolativeResizeImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

InterpolativeResizeImage() resizes an image using the specified interpolation method.

The format of the InterpolativeResizeImage method is:
    
    
    Image *InterpolativeResizeImage(const Image *image,const size_t columns,
      const size_t rows,const PixelInterpolateMethod method,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the resized image. 
    
rows
    the number of rows in the resized image. 
    
method
    the pixel interpolation method. 
    
exception
    return any errors or warnings in this structure. 
    

## [LiquidRescaleImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

LiquidRescaleImage() rescales image with seam carving.

The format of the LiquidRescaleImage method is:
    
    
    Image *LiquidRescaleImage(const Image *image,const size_t columns,
      const size_t rows,const double delta_x,const double rigidity,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the rescaled image. 
    
rows
    the number of rows in the rescaled image. 
    
delta_x
    maximum seam transversal step (0 means straight seams). 
    
rigidity
    introduce a bias for non-straight seams (typically 0). 
    
exception
    return any errors or warnings in this structure. 
    

## [MagnifyImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

MagnifyImage() doubles the size of the image with a pixel art scaling algorithm.

The format of the MagnifyImage method is:
    
    
    Image *MagnifyImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [MinifyImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

MinifyImage() is a convenience method that scales an image proportionally to half its size.

The format of the MinifyImage method is:
    
    
    Image *MinifyImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [ResampleImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

ResampleImage() resize image in terms of its pixel size, so that when displayed at the given resolution it will be the same size in terms of real world units as the original image at the original resolution.

The format of the ResampleImage method is:
    
    
    Image *ResampleImage(Image *image,const double x_resolution,
      const double y_resolution,const FilterType filter,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image to be resized to fit the given resolution. 
    
x_resolution
    the new image x resolution. 
    
y_resolution
    the new image y resolution. 
    
filter
    Image filter to use. 
    
exception
    return any errors or warnings in this structure. 
    

## [ResizeImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

ResizeImage() scales an image to the desired dimensions, using the given filter (see AcquireFilterInfo()).

If an undefined filter is given the filter defaults to Mitchell for a colormapped image, a image with a matte channel, or if the image is enlarged. Otherwise the filter defaults to a Lanczos.

ResizeImage() was inspired by Paul Heckbert's "zoom" program.

The format of the ResizeImage method is:
    
    
    Image *ResizeImage(Image *image,const size_t columns,const size_t rows,
      const FilterType filter,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the scaled image. 
    
rows
    the number of rows in the scaled image. 
    
filter
    Image filter to use. 
    
exception
    return any errors or warnings in this structure. 
    

## [SampleImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

SampleImage() scales an image to the desired dimensions with pixel sampling. Unlike other scaling methods, this method does not introduce any additional color into the scaled image.

The format of the SampleImage method is:
    
    
    Image *SampleImage(const Image *image,const size_t columns,
      const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the sampled image. 
    
rows
    the number of rows in the sampled image. 
    
exception
    return any errors or warnings in this structure. 
    

## [ScaleImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

ScaleImage() changes the size of an image to the given dimensions.

The format of the ScaleImage method is:
    
    
    Image *ScaleImage(const Image *image,const size_t columns,
      const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the scaled image. 
    
rows
    the number of rows in the scaled image. 
    
exception
    return any errors or warnings in this structure. 
    

## [ThumbnailImage](http://www.imagemagick.org/api/MagickCore/resize_8c.html)

ThumbnailImage() changes the size of an image to the given dimensions and removes any associated profiles. The goal is to produce small low cost thumbnail images suited for display on the Web.

The format of the ThumbnailImage method is:
    
    
    Image *ThumbnailImage(const Image *image,const size_t columns,
      const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the scaled image. 
    
rows
    the number of rows in the scaled image. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](resize.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
