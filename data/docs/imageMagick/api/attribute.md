[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[GetImageDepth](attribute.html#GetImageDepth) • [GetImageQuantumDepth](attribute.html#GetImageQuantumDepth) • [GetImageType](attribute.html#GetImageType) • [IdentifyImageGray](attribute.html#IdentifyImageGray) • [IdentifyImageMonochrome](attribute.html#IdentifyImageMonochrome) • [IdentifyImageType](attribute.html#IdentifyImageType) • [IsImageGray](attribute.html#IsImageGray) • [IsImageMonochrome](attribute.html#IsImageMonochrome) • [IsImageOpaque](attribute.html#IsImageOpaque) • [SetImageDepth](attribute.html#SetImageDepth) • [SetImageType](attribute.html#SetImageType)

## [GetImageDepth](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

GetImageDepth() returns the depth of a particular image channel.

The format of the GetImageDepth method is:
    
    
    size_t GetImageDepth(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageQuantumDepth](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

GetImageQuantumDepth() returns the depth of the image rounded to a legal quantum depth: 8, 16, or 32.

The format of the GetImageQuantumDepth method is:
    
    
    size_t GetImageQuantumDepth(const Image *image,
      const MagickBooleanType constrain)
    

A description of each parameter follows:

    
    

image
    the image. 
    
constrain
    A value other than MagickFalse, constrains the depth to a maximum of MAGICKCORE_QUANTUM_DEPTH. 
    

## [GetImageType](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

GetImageType() returns the type of image:

Bilevel Grayscale GrayscaleMatte Palette PaletteMatte TrueColor TrueColorMatte ColorSeparation ColorSeparationMatte

The format of the GetImageType method is:
    
    
    ImageType GetImageType(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [IdentifyImageGray](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

IdentifyImageGray() returns grayscale if all the pixels in the image have the same red, green, and blue intensities, and bi-level is the intensity is either 0 or QuantumRange. Otherwise undefined is returned.

The format of the IdentifyImageGray method is:
    
    
    ImageType IdentifyImageGray(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [IdentifyImageMonochrome](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

IdentifyImageMonochrome() returns MagickTrue if all the pixels in the image have the same red, green, and blue intensities and the intensity is either 0 or QuantumRange.

The format of the IdentifyImageMonochrome method is:
    
    
    MagickBooleanType IdentifyImageMonochrome(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [IdentifyImageType](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

IdentifyImageType() returns the potential type of image:

Bilevel Grayscale GrayscaleMatte Palette PaletteMatte TrueColor TrueColorMatte ColorSeparation ColorSeparationMatte

To ensure the image type matches its potential, use SetImageType():
    
    
        (void) SetImageType(image,IdentifyImageType(image,exception),exception);
    

The format of the IdentifyImageType method is:
    
    
    ImageType IdentifyImageType(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [IsImageGray](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

IsImageGray() returns MagickTrue if the type of the image is grayscale or bi-level.

The format of the IsImageGray method is:
    
    
    MagickBooleanType IsImageGray(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [IsImageMonochrome](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

IsImageMonochrome() returns MagickTrue if type of the image is bi-level.

The format of the IsImageMonochrome method is:
    
    
    MagickBooleanType IsImageMonochrome(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [IsImageOpaque](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

IsImageOpaque() returns MagickTrue if none of the pixels in the image have an alpha value other than OpaqueAlpha (QuantumRange).

Will return true immediatally is alpha channel is not available.

The format of the IsImageOpaque method is:
    
    
    MagickBooleanType IsImageOpaque(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageDepth](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

SetImageDepth() sets the depth of the image.

The format of the SetImageDepth method is:
    
    
    MagickBooleanType SetImageDepth(Image *image,const size_t depth,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
channel
    the channel. 
    
depth
    the image depth. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageType](http://www.imagemagick.org/api/MagickCore/attribute_8c.html)

SetImageType() sets the type of image. Choose from these types:

Bilevel Grayscale GrayscaleMatte Palette PaletteMatte TrueColor TrueColorMatte ColorSeparation ColorSeparationMatte OptimizeType

The format of the SetImageType method is:
    
    
    MagickBooleanType SetImageType(Image *image,const ImageType type,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
type
    Image type. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](attribute.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
