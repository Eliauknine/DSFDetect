[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[SetImageColorspace](colorspace.html#SetImageColorspace) • [SetImageGray](colorspace.html#SetImageGray) • [SetImageMonochrome](colorspace.html#SetImageMonochrome) • [TransformImageColorspace](colorspace.html#TransformImageColorspace)

## [SetImageColorspace](http://www.imagemagick.org/api/MagickCore/colorspace_8c.html)

SetImageColorspace() sets the colorspace member of the Image structure.

The format of the SetImageColorspace method is:
    
    
    MagickBooleanType SetImageColorspace(Image *image,
      const ColorspaceType colorspace,ExceptiionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
colorspace
    the colorspace. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageGray](http://www.imagemagick.org/api/MagickCore/colorspace_8c.html)

SetImageGray() returns MagickTrue if all the pixels in the image have the same red, green, and blue intensities and changes the type of the image to bi-level or grayscale.

The format of the SetImageGray method is:
    
    
    MagickBooleanType SetImageGray(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageMonochrome](http://www.imagemagick.org/api/MagickCore/colorspace_8c.html)

SetImageMonochrome() returns MagickTrue if all the pixels in the image have the same red, green, and blue intensities and the intensity is either 0 or QuantumRange and changes the type of the image to bi-level.

The format of the SetImageMonochrome method is:
    
    
    MagickBooleanType SetImageMonochrome(Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [TransformImageColorspace](http://www.imagemagick.org/api/MagickCore/colorspace_8c.html)

TransformImageColorspace() transforms an image colorspace, changing the image data to reflect the new colorspace.

The format of the TransformImageColorspace method is:
    
    
    MagickBooleanType TransformImageColorspace(Image *image,
      const ColorspaceType colorspace,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
colorspace
    the colorspace. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](colorspace.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
