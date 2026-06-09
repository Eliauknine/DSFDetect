[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[CloneImageView](image-view.html#CloneImageView) • [DestroyImageView](image-view.html#DestroyImageView) • [DuplexTransferImageViewIterator](image-view.html#DuplexTransferImageViewIterator) • [GetImageViewAuthenticMetacontent](image-view.html#GetImageViewAuthenticMetacontent) • [GetImageViewAuthenticPixels](image-view.html#GetImageViewAuthenticPixels) • [GetImageViewException](image-view.html#GetImageViewException) • [GetImageViewExtent](image-view.html#GetImageViewExtent) • [GetImageViewImage](image-view.html#GetImageViewImage) • [GetImageViewIterator](image-view.html#GetImageViewIterator) • [GetImageViewVirtualMetacontent](image-view.html#GetImageViewVirtualMetacontent) • [GetImageViewVirtualPixels](image-view.html#GetImageViewVirtualPixels) • [IsImageView](image-view.html#IsImageView) • [NewImageView](image-view.html#NewImageView) • [NewImageViewRegion](image-view.html#NewImageViewRegion) • [SetImageViewDescription](image-view.html#SetImageViewDescription) • [SetImageViewIterator](image-view.html#SetImageViewIterator) • [TransferImageViewIterator](image-view.html#TransferImageViewIterator) • [UpdateImageViewIterator](image-view.html#UpdateImageViewIterator)

## [CloneImageView](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

CloneImageView() makes a copy of the specified image view.

The format of the CloneImageView method is:
    
    
    ImageView *CloneImageView(const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [DestroyImageView](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

DestroyImageView() deallocates memory associated with a image view.

The format of the DestroyImageView method is:
    
    
    ImageView *DestroyImageView(ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [DuplexTransferImageViewIterator](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

DuplexTransferImageViewIterator() iterates over three image views in parallel and calls your transfer method for each scanline of the view. The source and duplex pixel extent is not confined to the image canvas-- that is you can include negative offsets or widths or heights that exceed the image dimension. However, the destination image view is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension are permitted.

The callback signature is:
    
    
    MagickBooleanType DuplexTransferImageViewMethod(const ImageView *source,
      const ImageView *duplex,ImageView *destination,const ssize_t y,
      const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback transfer method that must be executed by a single thread at a time.

The format of the DuplexTransferImageViewIterator method is:
    
    
    MagickBooleanType DuplexTransferImageViewIterator(ImageView *source,
      ImageView *duplex,ImageView *destination,
      DuplexTransferImageViewMethod transfer,void *context)
    

A description of each parameter follows:

    
    

source
    the source image view. 
    
duplex
    the duplex image view. 
    
destination
    the destination image view. 
    
transfer
    the transfer callback method. 
    
context
    the user defined context. 
    

## [GetImageViewAuthenticMetacontent](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewAuthenticMetacontent() returns the image view authentic meta-content.

The format of the GetImageViewAuthenticPixels method is:
    
    
    void *GetImageViewAuthenticMetacontent(
      const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [GetImageViewAuthenticPixels](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewAuthenticPixels() returns the image view authentic pixels.

The format of the GetImageViewAuthenticPixels method is:
    
    
    Quantum *GetImageViewAuthenticPixels(const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [GetImageViewException](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewException() returns the severity, reason, and description of any error that occurs when utilizing a image view.

The format of the GetImageViewException method is:
    
    
    char *GetImageViewException(const PixelImage *image_view,
      ExceptionType *severity)
    

A description of each parameter follows:

    
    

image_view
    the pixel image_view. 
    
severity
    the severity of the error is returned here. 
    

## [GetImageViewExtent](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewExtent() returns the image view extent.

The format of the GetImageViewExtent method is:
    
    
    RectangleInfo GetImageViewExtent(const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [GetImageViewImage](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewImage() returns the image associated with the image view.

The format of the GetImageViewImage method is:
    
    
    MagickCore *GetImageViewImage(const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [GetImageViewIterator](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewIterator() iterates over the image view in parallel and calls your get method for each scanline of the view. The pixel extent is not confined to the image canvas-- that is you can include negative offsets or widths or heights that exceed the image dimension. Any updates to the pixels in your callback are ignored.

The callback signature is:
    
    
    MagickBooleanType GetImageViewMethod(const ImageView *source,
      const ssize_t y,const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback get method that must be executed by a single thread at a time.

The format of the GetImageViewIterator method is:
    
    
    MagickBooleanType GetImageViewIterator(ImageView *source,
      GetImageViewMethod get,void *context)
    

A description of each parameter follows:

    
    

source
    the source image view. 
    
get
    the get callback method. 
    
context
    the user defined context. 
    

## [GetImageViewVirtualMetacontent](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewVirtualMetacontent() returns the image view virtual meta-content.

The format of the GetImageViewVirtualMetacontent method is:
    
    
    const void *GetImageViewVirtualMetacontent(
      const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [GetImageViewVirtualPixels](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

GetImageViewVirtualPixels() returns the image view virtual pixels.

The format of the GetImageViewVirtualPixels method is:
    
    
    const Quantum *GetImageViewVirtualPixels(const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [IsImageView](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

IsImageView() returns MagickTrue if the the parameter is verified as a image view object.

The format of the IsImageView method is:
    
    
    MagickBooleanType IsImageView(const ImageView *image_view)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    

## [NewImageView](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

NewImageView() returns a image view required for all other methods in the Image View API.

The format of the NewImageView method is:
    
    
    ImageView *NewImageView(MagickCore *wand,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [NewImageViewRegion](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

NewImageViewRegion() returns a image view required for all other methods in the Image View API.

The format of the NewImageViewRegion method is:
    
    
    ImageView *NewImageViewRegion(MagickCore *wand,const ssize_t x,
      const ssize_t y,const size_t width,const size_t height,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
x,y,columns,rows
     These values define the perimeter of a extent of pixel_wands view. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageViewDescription](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

SetImageViewDescription() associates a description with an image view.

The format of the SetImageViewDescription method is:
    
    
    void SetImageViewDescription(ImageView *image_view,
      const char *description)
    

A description of each parameter follows:

    
    

image_view
    the image view. 
    
description
    the image view description. 
    

## [SetImageViewIterator](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

SetImageViewIterator() iterates over the image view in parallel and calls your set method for each scanline of the view. The pixel extent is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension. The pixels are initiallly undefined and any settings you make in the callback method are automagically synced back to your image.

The callback signature is:
    
    
    MagickBooleanType SetImageViewMethod(ImageView *destination,
      const ssize_t y,const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback set method that must be executed by a single thread at a time.

The format of the SetImageViewIterator method is:
    
    
    MagickBooleanType SetImageViewIterator(ImageView *destination,
      SetImageViewMethod set,void *context)
    

A description of each parameter follows:

    
    

destination
    the image view. 
    
set
    the set callback method. 
    
context
    the user defined context. 
    

## [TransferImageViewIterator](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

TransferImageViewIterator() iterates over two image views in parallel and calls your transfer method for each scanline of the view. The source pixel extent is not confined to the image canvas-- that is you can include negative offsets or widths or heights that exceed the image dimension. However, the destination image view is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension are permitted.

The callback signature is:
    
    
    MagickBooleanType TransferImageViewMethod(const ImageView *source,
      ImageView *destination,const ssize_t y,const int thread_id,
      void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback transfer method that must be executed by a single thread at a time.

The format of the TransferImageViewIterator method is:
    
    
    MagickBooleanType TransferImageViewIterator(ImageView *source,
      ImageView *destination,TransferImageViewMethod transfer,void *context)
    

A description of each parameter follows:

    
    

source
    the source image view. 
    
destination
    the destination image view. 
    
transfer
    the transfer callback method. 
    
context
    the user defined context. 
    

## [UpdateImageViewIterator](http://www.imagemagick.org/api/MagickCore/image-view_8c.html)

UpdateImageViewIterator() iterates over the image view in parallel and calls your update method for each scanline of the view. The pixel extent is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension are permitted. Updates to pixels in your callback are automagically synced back to the image.

The callback signature is:
    
    
    MagickBooleanType UpdateImageViewMethod(ImageView *source,
      const ssize_t y,const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback update method that must be executed by a single thread at a time.

The format of the UpdateImageViewIterator method is:
    
    
    MagickBooleanType UpdateImageViewIterator(ImageView *source,
      UpdateImageViewMethod update,void *context)
    

A description of each parameter follows:

    
    

source
    the source image view. 
    
update
    the update callback method. 
    
context
    the user defined context. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](image-view.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
