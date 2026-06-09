[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AutoOrientImage](transform.html#AutoOrientImage) • [ChopImage](transform.html#ChopImage) • [CropImage](transform.html#CropImage) • [CropImageToTiles](transform.html#CropImageToTiles) • [ExcerptImage](transform.html#ExcerptImage) • [ExtentImage](transform.html#ExtentImage) • [FlipImage](transform.html#FlipImage) • [FlopImage](transform.html#FlopImage) • [RollImage](transform.html#RollImage) • [ShaveImage](transform.html#ShaveImage) • [SpliceImage](transform.html#SpliceImage) • [TransformImage](transform.html#TransformImage) • [TransposeImage](transform.html#TransposeImage) • [TransverseImage](transform.html#TransverseImage) • [TrimImage](transform.html#TrimImage)

## [AutoOrientImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

AutoOrientImage() adjusts an image so that its orientation is suitable for viewing (i.e. top-left orientation).

The format of the AutoOrientImage method is:
    
    
    Image *AutoOrientImage(const Image *image,
      const OrientationType orientation,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    The image. 
    
orientation
    Current image orientation. 
    
exception
    Return any errors or warnings in this structure. 
    

## [ChopImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

ChopImage() removes a region of an image and collapses the image to occupy the removed portion.

The format of the ChopImage method is:
    
    
    Image *ChopImage(const Image *image,const RectangleInfo *chop_info)
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
chop_info
    Define the region of the image to chop. 
    
exception
    return any errors or warnings in this structure. 
    

## [CropImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

CropImage() extracts a region of the image starting at the offset defined by geometry. Region must be fully defined, and no special handling of geometry flags is performed.

The format of the CropImage method is:
    
    
    Image *CropImage(const Image *image,const RectangleInfo *geometry,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
geometry
    Define the region of the image to crop with members x, y, width, and height. 
    
exception
    return any errors or warnings in this structure. 
    

## [CropImageToTiles](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

CropImageToTiles() crops a single image, into a possible list of tiles. This may include a single sub-region of the image. This basically applies all the normal geometry flags for Crop.

Image *CropImageToTiles(const Image *image, const RectangleInfo *crop_geometry, ExceptionInfo *exception)

A description of each parameter follows:

    
    

image
    the image The transformed image is returned as this parameter. 
    
crop_geometry
    A crop geometry string. 
    
exception
    return any errors or warnings in this structure. 
    

## [ExcerptImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

ExcerptImage() returns a excerpt of the image as defined by the geometry.

The format of the ExcerptImage method is:
    
    
    Image *ExcerptImage(const Image *image,const RectangleInfo *geometry,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
geometry
    Define the region of the image to extend with members x, y, width, and height. 
    
exception
    return any errors or warnings in this structure. 
    

## [ExtentImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

ExtentImage() extends the image as defined by the geometry, gravity, and image background color. Set the (x,y) offset of the geometry to move the original image relative to the extended image.

The format of the ExtentImage method is:
    
    
    Image *ExtentImage(const Image *image,const RectangleInfo *geometry,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
geometry
    Define the region of the image to extend with members x, y, width, and height. 
    
exception
    return any errors or warnings in this structure. 
    

## [FlipImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

FlipImage() creates a vertical mirror image by reflecting the pixels around the central x-axis.

The format of the FlipImage method is:
    
    
    Image *FlipImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [FlopImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

FlopImage() creates a horizontal mirror image by reflecting the pixels around the central y-axis.

The format of the FlopImage method is:
    
    
    Image *FlopImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [RollImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

RollImage() offsets an image as defined by x_offset and y_offset.

The format of the RollImage method is:
    
    
    Image *RollImage(const Image *image,const ssize_t x_offset,
      const ssize_t y_offset,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
x_offset
    the number of columns to roll in the horizontal direction. 
    
y_offset
    the number of rows to roll in the vertical direction. 
    
exception
    return any errors or warnings in this structure. 
    

## [ShaveImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

ShaveImage() shaves pixels from the image edges. It allocates the memory necessary for the new Image structure and returns a pointer to the new image.

The format of the ShaveImage method is:
    
    
    Image *ShaveImage(const Image *image,const RectangleInfo *shave_info,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

shave_image
    Method ShaveImage returns a pointer to the shaved image. A null image is returned if there is a memory shortage or if the image width or height is zero. 
    
image
    the image. 
    
shave_info
    Specifies a pointer to a RectangleInfo which defines the region of the image to crop. 
    
exception
    return any errors or warnings in this structure. 
    

## [SpliceImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

SpliceImage() splices a solid color into the image as defined by the geometry.

The format of the SpliceImage method is:
    
    
    Image *SpliceImage(const Image *image,const RectangleInfo *geometry,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
geometry
    Define the region of the image to splice with members x, y, width, and height. 
    
exception
    return any errors or warnings in this structure. 
    

## [TransformImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

TransformImage() is a convenience method that behaves like ResizeImage() or CropImage() but accepts scaling and/or cropping information as a region geometry specification. If the operation fails, the original image handle is left as is.

This should only be used for single images.

This function destroys what it assumes to be a single image list. If the input image is part of a larger list, all other images in that list will be simply 'lost', not destroyed.

Also if the crop generates a list of images only the first image is resized. And finally if the crop succeeds and the resize failed, you will get a cropped image, as well as a 'false' or 'failed' report.

This function and should probably be deprecated in favor of direct calls to CropImageToTiles() or ResizeImage(), as appropriate.

The format of the TransformImage method is:
    
    
    MagickBooleanType TransformImage(Image **image,const char *crop_geometry,
      const char *image_geometry,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image The transformed image is returned as this parameter. 
    
crop_geometry
    A crop geometry string. This geometry defines a subregion of the image to crop. 
    
image_geometry
    An image geometry string. This geometry defines the final size of the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [TransposeImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

TransposeImage() creates a horizontal mirror image by reflecting the pixels around the central y-axis while rotating them by 90 degrees.

The format of the TransposeImage method is:
    
    
    Image *TransposeImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [TransverseImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

TransverseImage() creates a vertical mirror image by reflecting the pixels around the central x-axis while rotating them by 270 degrees.

The format of the TransverseImage method is:
    
    
    Image *TransverseImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [TrimImage](http://www.imagemagick.org/api/MagickCore/transform_8c.html)

TrimImage() trims pixels from the image edges. It allocates the memory necessary for the new Image structure and returns a pointer to the new image.

The format of the TrimImage method is:
    
    
    Image *TrimImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](transform.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
