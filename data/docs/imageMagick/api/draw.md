[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireDrawInfo](draw.html#AcquireDrawInfo) • [CloneDrawInfo](draw.html#CloneDrawInfo) • [DestroyDrawInfo](draw.html#DestroyDrawInfo) • [DrawAffineImage](draw.html#DrawAffineImage) • [DrawClipPath](draw.html#DrawClipPath) • [DrawImage](draw.html#DrawImage) • [DrawGradientImage](draw.html#DrawGradientImage) • [DrawPatternPath](draw.html#DrawPatternPath) • [DrawPrimitive](draw.html#DrawPrimitive) • [GetAffineMatrix](draw.html#GetAffineMatrix)

## [AcquireDrawInfo](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

AcquireDrawInfo() returns a DrawInfo structure properly initialized.

The format of the AcquireDrawInfo method is:
    
    
    DrawInfo *AcquireDrawInfo(void)
    

## [CloneDrawInfo](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

CloneDrawInfo() makes a copy of the given draw_info structure. If NULL is specified, a new DrawInfo structure is created initialized to default values.

The format of the CloneDrawInfo method is:
    
    
    DrawInfo *CloneDrawInfo(const ImageInfo *image_info,
      const DrawInfo *draw_info)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
draw_info
    the draw info. 
    

## [DestroyDrawInfo](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

DestroyDrawInfo() deallocates memory associated with an DrawInfo structure.

The format of the DestroyDrawInfo method is:
    
    
    DrawInfo *DestroyDrawInfo(DrawInfo *draw_info)
    

A description of each parameter follows:

    
    

draw_info
    the draw info. 
    

## [DrawAffineImage](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

DrawAffineImage() composites the source over the destination image as dictated by the affine transform.

The format of the DrawAffineImage method is:
    
    
    MagickBooleanType DrawAffineImage(Image *image,const Image *source,
      const AffineMatrix *affine,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
source
    the source image. 
    
affine
    the affine transform. 
    
exception
    return any errors or warnings in this structure. 
    

## [DrawClipPath](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

DrawClipPath() draws the clip path on the image mask.

The format of the DrawClipPath method is:
    
    
    MagickBooleanType DrawClipPath(Image *image,const DrawInfo *draw_info,
      const char *name,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
name
    the name of the clip path. 
    
exception
    return any errors or warnings in this structure. 
    

## [DrawImage](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

DrawImage() draws a graphic primitive on your image. The primitive may be represented as a string or filename. Precede the filename with an "at" sign (@) and the contents of the file are drawn on the image. You can affect how text is drawn by setting one or more members of the draw info structure.

The format of the DrawImage method is:
    
    
    MagickBooleanType DrawImage(Image *image,const DrawInfo *draw_info,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
exception
    return any errors or warnings in this structure. 
    

## [DrawGradientImage](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

DrawGradientImage() draws a linear gradient on the image.

The format of the DrawGradientImage method is:
    
    
    MagickBooleanType DrawGradientImage(Image *image,
      const DrawInfo *draw_info,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
exception
    return any errors or warnings in this structure. 
    

## [DrawPatternPath](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

DrawPatternPath() draws a pattern.

The format of the DrawPatternPath method is:
    
    
    MagickBooleanType DrawPatternPath(Image *image,const DrawInfo *draw_info,
      const char *name,Image **pattern,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
name
    the pattern name. 
    
image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [DrawPrimitive](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

DrawPrimitive() draws a primitive (line, rectangle, ellipse) on the image.

The format of the DrawPrimitive method is:
    
    
    MagickBooleanType DrawPrimitive(Image *image,const DrawInfo *draw_info,
      PrimitiveInfo *primitive_info,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
primitive_info
    Specifies a pointer to a PrimitiveInfo structure. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetAffineMatrix](http://www.imagemagick.org/api/MagickCore/draw_8c.html)

GetAffineMatrix() returns an AffineMatrix initialized to the identity matrix.

The format of the GetAffineMatrix method is:
    
    
    void GetAffineMatrix(AffineMatrix *affine_matrix)
    

A description of each parameter follows:

    
    

affine_matrix
    the affine matrix. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](draw.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
