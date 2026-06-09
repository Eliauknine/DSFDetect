[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireImage](image.html#AcquireImage) • [AcquireImageInfo](image.html#AcquireImageInfo) • [AcquireNextImage](image.html#AcquireNextImage) • [AppendImages](image.html#AppendImages) • [CatchImageException](image.html#CatchImageException) • [ClipImagePath](image.html#ClipImagePath) • [CloneImage](image.html#CloneImage) • [CloneImageInfo](image.html#CloneImageInfo) • [CopyImagePixels](image.html#CopyImagePixels) • [DestroyImage](image.html#DestroyImage) • [DestroyImageInfo](image.html#DestroyImageInfo) • [GetImageInfo](image.html#GetImageInfo) • [GetImageInfoFile](image.html#GetImageInfoFile) • [GetImageMask](image.html#GetImageMask) • [GetImageVirtualPixelMethod](image.html#GetImageVirtualPixelMethod) • [InterpretImageFilename](image.html#InterpretImageFilename) • [IsHighDynamicRangeImage](image.html#IsHighDynamicRangeImage) • [IsImageObject](image.html#IsImageObject) • [IsTaintImage](image.html#IsTaintImage) • [ModifyImage](image.html#ModifyImage) • [NewMagickImage](image.html#NewMagickImage) • [ReferenceImage](image.html#ReferenceImage) • [ResetImagePage](image.html#ResetImagePage) • [SetImageBackgroundColor](image.html#SetImageBackgroundColor) • [SetImageChannelMask](image.html#SetImageChannelMask) • [SetImageColor](image.html#SetImageColor) • [SetImageStorageClass](image.html#SetImageStorageClass) • [SetImageExtent](image.html#SetImageExtent) • [SetImageInfoBlob](image.html#SetImageInfoBlob) • [SetImageInfoFile](image.html#SetImageInfoFile) • [SetImageMask](image.html#SetImageMask) • [SetImageAlpha](image.html#SetImageAlpha) • [SetImageVirtualPixelMethod](image.html#SetImageVirtualPixelMethod) • [SmushImages](image.html#SmushImages) • [StripImage](image.html#StripImage) • [SyncImageSettings](image.html#SyncImageSettings)

## [AcquireImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

AcquireImage() returns a pointer to an image structure initialized to default values.

The format of the AcquireImage method is:
    
    
    Image *AcquireImage(const ImageInfo *image_info,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    Many of the image default values are set from this structure. For example, filename, compression, depth, background color, and others. 
    
exception
    return any errors or warnings in this structure. 
    

## [AcquireImageInfo](http://www.imagemagick.org/api/MagickCore/image_8c.html)

AcquireImageInfo() allocates the ImageInfo structure.

The format of the AcquireImageInfo method is:
    
    
    ImageInfo *AcquireImageInfo(void)
    

## [AcquireNextImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

AcquireNextImage() initializes the next image in a sequence to default values. The next member of image points to the newly allocated image. If there is a memory shortage, next is assigned NULL.

The format of the AcquireNextImage method is:
    
    
    void AcquireNextImage(const ImageInfo *image_info,Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    Many of the image default values are set from this structure. For example, filename, compression, depth, background color, and others. 
    
image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [AppendImages](http://www.imagemagick.org/api/MagickCore/image_8c.html)

AppendImages() takes all images from the current image pointer to the end of the image list and appends them to each other top-to-bottom if the stack parameter is true, otherwise left-to-right.

The current gravity setting effects how the image is justified in the final image.

The format of the AppendImages method is:
    
    
    Image *AppendImages(const Image *images,const MagickBooleanType stack,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
stack
    A value other than 0 stacks the images top-to-bottom. 
    
exception
    return any errors or warnings in this structure. 
    

## [CatchImageException](http://www.imagemagick.org/api/MagickCore/image_8c.html)

CatchImageException() returns if no exceptions are found in the image sequence, otherwise it determines the most severe exception and reports it as a warning or error depending on the severity.

The format of the CatchImageException method is:
    
    
    ExceptionType CatchImageException(Image *image)
    

A description of each parameter follows:

    
    

image
    An image sequence. 
    

## [ClipImagePath](http://www.imagemagick.org/api/MagickCore/image_8c.html)

ClipImagePath() sets the image clip mask based any clipping path information if it exists.

The format of the ClipImagePath method is:
    
    
    MagickBooleanType ClipImagePath(Image *image,const char *pathname,
      const MagickBooleanType inside,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
pathname
    name of clipping path resource. If name is preceded by #, use clipping path numbered by name. 
    
inside
    if non-zero, later operations take effect inside clipping path. Otherwise later operations take effect outside clipping path. 
    
exception
    return any errors or warnings in this structure. 
    

## [CloneImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

CloneImage() copies an image and returns the copy as a new image object.

If the specified columns and rows is 0, an exact copy of the image is returned, otherwise the pixel data is undefined and must be initialized with the QueueAuthenticPixels() and SyncAuthenticPixels() methods. On failure, a NULL image is returned and exception describes the reason for the failure.

The format of the CloneImage method is:
    
    
    Image *CloneImage(const Image *image,const size_t columns,
      const size_t rows,const MagickBooleanType orphan,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
    the number of columns in the cloned image. 
    
rows
    the number of rows in the cloned image. 
    
detach
     With a value other than 0, the cloned image is detached from its parent I/O stream. 
    
exception
    return any errors or warnings in this structure. 
    

## [CloneImageInfo](http://www.imagemagick.org/api/MagickCore/image_8c.html)

CloneImageInfo() makes a copy of the given image info structure. If NULL is specified, a new image info structure is created initialized to default values.

The format of the CloneImageInfo method is:
    
    
    ImageInfo *CloneImageInfo(const ImageInfo *image_info)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    

## [CopyImagePixels](http://www.imagemagick.org/api/MagickCore/image_8c.html)

CopyImagePixels() copies pixels from the source image as defined by the geometry the destination image at the specified offset.

The format of the CopyImagePixels method is:
    
    
    MagickBooleanType CopyImagePixels(Image *image,const Image *source_image,
      const RectangleInfo *geometry,const OffsetInfo *offset,
      ExceptionInfo *exception);
    

A description of each parameter follows:

    
    

image
    the destination image. 
    
source_image
    the source image. 
    
geometry
    define the dimensions of the source pixel rectangle. 
    
offset
    define the offset in the destination image. 
    
exception
    return any errors or warnings in this structure. 
    

## [DestroyImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

DestroyImage() dereferences an image, deallocating memory associated with the image if the reference count becomes zero.

The format of the DestroyImage method is:
    
    
    Image *DestroyImage(Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [DestroyImageInfo](http://www.imagemagick.org/api/MagickCore/image_8c.html)

DestroyImageInfo() deallocates memory associated with an ImageInfo structure.

The format of the DestroyImageInfo method is:
    
    
    ImageInfo *DestroyImageInfo(ImageInfo *image_info)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    

## [GetImageInfo](http://www.imagemagick.org/api/MagickCore/image_8c.html)

GetImageInfo() initializes image_info to default values.

The format of the GetImageInfo method is:
    
    
    void GetImageInfo(ImageInfo *image_info)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    

## [GetImageInfoFile](http://www.imagemagick.org/api/MagickCore/image_8c.html)

GetImageInfoFile() returns the image info file member.

The format of the GetImageInfoFile method is:
    
    
    FILE *GetImageInfoFile(const ImageInfo *image_info)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    

## [GetImageMask](http://www.imagemagick.org/api/MagickCore/image_8c.html)

GetImageMask() returns the mask associated with the image.

The format of the GetImageMask method is:
    
    
    Image *GetImageMask(const Image *image,const PixelMask type,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
type
    the mask type, ReadPixelMask or WritePixelMask. 
    

## [GetImageVirtualPixelMethod](http://www.imagemagick.org/api/MagickCore/image_8c.html)

GetImageVirtualPixelMethod() gets the "virtual pixels" method for the image. A virtual pixel is any pixel access that is outside the boundaries of the image cache.

The format of the GetImageVirtualPixelMethod() method is:
    
    
    VirtualPixelMethod GetImageVirtualPixelMethod(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [InterpretImageFilename](http://www.imagemagick.org/api/MagickCore/image_8c.html)

InterpretImageFilename() interprets embedded characters in an image filename. The filename length is returned.

The format of the InterpretImageFilename method is:
    
    
    size_t InterpretImageFilename(const ImageInfo *image_info,Image *image,
      const char *format,int value,char *filename,ExceptionInfo *exception)
    

A description of each parameter follows.

image_info

the image info..

image

the image.

format

A filename describing the format to use to write the numeric argument. Only the first numeric format identifier is replaced.

value

Numeric value to substitute into format filename.

filename

return the formatted filename in this character buffer.

exception

return any errors or warnings in this structure.

## [IsHighDynamicRangeImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

IsHighDynamicRangeImage() returns MagickTrue if any pixel component is non-integer or exceeds the bounds of the quantum depth (e.g. for Q16 0..65535.

The format of the IsHighDynamicRangeImage method is:
    
    
    MagickBooleanType IsHighDynamicRangeImage(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [IsImageObject](http://www.imagemagick.org/api/MagickCore/image_8c.html)

IsImageObject() returns MagickTrue if the image sequence contains a valid set of image objects.

The format of the IsImageObject method is:
    
    
    MagickBooleanType IsImageObject(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [IsTaintImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

IsTaintImage() returns MagickTrue any pixel in the image has been altered since it was first constituted.

The format of the IsTaintImage method is:
    
    
    MagickBooleanType IsTaintImage(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [ModifyImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

ModifyImage() ensures that there is only a single reference to the image to be modified, updating the provided image pointer to point to a clone of the original image if necessary.

The format of the ModifyImage method is:
    
    
    MagickBooleanType ModifyImage(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [NewMagickImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

NewMagickImage() creates a blank image canvas of the specified size and background color.

The format of the NewMagickImage method is:
    
    
    Image *NewMagickImage(const ImageInfo *image_info,const size_t width,
      const size_t height,const PixelInfo *background,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
width
    the image width. 
    
height
    the image height. 
    
background
    the image color. 
    
exception
    return any errors or warnings in this structure. 
    

## [ReferenceImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

ReferenceImage() increments the reference count associated with an image returning a pointer to the image.

The format of the ReferenceImage method is:
    
    
    Image *ReferenceImage(Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [ResetImagePage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

ResetImagePage() resets the image page canvas and position.

The format of the ResetImagePage method is:
    
    
    MagickBooleanType ResetImagePage(Image *image,const char *page)
    

A description of each parameter follows:

    
    

image
    the image. 
    
page
    the relative page specification. 
    

## [SetImageBackgroundColor](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageBackgroundColor() initializes the image pixels to the image background color. The background color is defined by the background_color member of the image structure.

The format of the SetImage method is:
    
    
    MagickBooleanType SetImageBackgroundColor(Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageChannelMask](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageChannelMask() sets the image channel mask from the specified channel mask.

The format of the SetImageChannelMask method is:
    
    
    ChannelType SetImageChannelMask(Image *image,
      const ChannelType channel_mask)
    

A description of each parameter follows:

    
    

image
    the image. 
    
channel_mask
    the channel mask. 
    

## [SetImageColor](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageColor() set the entire image canvas to the specified color.

The format of the SetImageColor method is:
    
    
    MagickBooleanType SetImageColor(Image *image,const PixelInfo *color,
      ExeptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
background
    the image color. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageStorageClass](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageStorageClass() sets the image class: DirectClass for true color images or PseudoClass for colormapped images.

The format of the SetImageStorageClass method is:
    
    
    MagickBooleanType SetImageStorageClass(Image *image,
      const ClassType storage_class,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
storage_class
     The image class. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageExtent](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageExtent() sets the image size (i.e. columns & rows).

The format of the SetImageExtent method is:
    
    
    MagickBooleanType SetImageExtent(Image *image,const size_t columns,
      const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
columns
     The image width in pixels. 
    
rows
     The image height in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageInfoBlob](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageInfoBlob() sets the image info blob member.

The format of the SetImageInfoBlob method is:
    
    
    void SetImageInfoBlob(ImageInfo *image_info,const void *blob,
      const size_t length)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
blob
    the blob. 
    
length
    the blob length. 
    

## [SetImageInfoFile](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageInfoFile() sets the image info file member.

The format of the SetImageInfoFile method is:
    
    
    void SetImageInfoFile(ImageInfo *image_info,FILE *file)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
file
    the file. 
    

## [SetImageMask](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageMask() associates a mask with the image. The mask must be the same dimensions as the image.

The format of the SetImageMask method is:
    
    
    MagickBooleanType SetImageMask(Image *image,const PixelMask type,
      const Image *mask,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
type
    the mask type, ReadPixelMask or WritePixelMask. 
    
mask
    the image mask. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageAlpha](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageAlpha() sets the alpha levels of the image.

The format of the SetImageAlpha method is:
    
    
    MagickBooleanType SetImageAlpha(Image *image,const Quantum alpha,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
Alpha
    the level of transparency: 0 is fully opaque and QuantumRange is fully transparent. 
    

## [SetImageVirtualPixelMethod](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SetImageVirtualPixelMethod() sets the "virtual pixels" method for the image and returns the previous setting. A virtual pixel is any pixel access that is outside the boundaries of the image cache.

The format of the SetImageVirtualPixelMethod() method is:
    
    
    VirtualPixelMethod SetImageVirtualPixelMethod(Image *image,
      const VirtualPixelMethod virtual_pixel_method,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
virtual_pixel_method
    choose the type of virtual pixel. 
    
exception
    return any errors or warnings in this structure. 
    

## [SmushImages](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SmushImages() takes all images from the current image pointer to the end of the image list and smushes them to each other top-to-bottom if the stack parameter is true, otherwise left-to-right.

The current gravity setting now effects how the image is justified in the final image.

The format of the SmushImages method is:
    
    
    Image *SmushImages(const Image *images,const MagickBooleanType stack,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
stack
    A value other than 0 stacks the images top-to-bottom. 
    
offset
    minimum distance in pixels between images. 
    
exception
    return any errors or warnings in this structure. 
    

## [StripImage](http://www.imagemagick.org/api/MagickCore/image_8c.html)

StripImage() strips an image of all profiles and comments.

The format of the StripImage method is:
    
    
    MagickBooleanType StripImage(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [SyncImageSettings](http://www.imagemagick.org/api/MagickCore/image_8c.html)

SyncImageSettings() syncs any image_info global options into per-image attributes.

Note: in IMv6 free form 'options' were always mapped into 'artifacts', so that operations and coders can find such settings. In IMv7 if a desired per-image artifact is not set, then it will directly look for a global option as a fallback, as such this copy is no longer needed, only the link set up.

The format of the SyncImageSettings method is:
    
    
    MagickBooleanType SyncImageSettings(const ImageInfo *image_info,
      Image *image,ExceptionInfo *exception)
    MagickBooleanType SyncImagesSettings(const ImageInfo *image_info,
      Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](image.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
