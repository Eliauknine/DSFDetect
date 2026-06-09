[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireImageColormap](colormap.html#AcquireImageColormap) • [CycleColormap](colormap.html#CycleColormap)

## [AcquireImageColormap](http://www.imagemagick.org/api/MagickCore/colormap_8c.html)

AcquireImageColormap() allocates an image colormap and initializes it to a linear gray colorspace. If the image already has a colormap, it is replaced. AcquireImageColormap() returns MagickTrue if successful, otherwise MagickFalse if there is not enough memory.

The format of the AcquireImageColormap method is:
    
    
    MagickBooleanType AcquireImageColormap(Image *image,const size_t colors,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
colors
    the number of colors in the image colormap. 
    
exception
    return any errors or warnings in this structure. 
    

## [CycleColormap](http://www.imagemagick.org/api/MagickCore/colormap_8c.html)

CycleColormap() displaces an image's colormap by a given number of positions. If you cycle the colormap a number of times you can produce a psychodelic effect.

WARNING: this assumes an images colormap is in a well know and defined order. Currently Imagemagick has no way of setting that order.

The format of the CycleColormapImage method is:
    
    
    MagickBooleanType CycleColormapImage(Image *image,const ssize_t displace,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
displace
     displace the colormap this amount. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](colormap.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
