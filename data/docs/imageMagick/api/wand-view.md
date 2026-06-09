[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[CloneWandView](wand-view.html#CloneWandView) • [DestroyWandView](wand-view.html#DestroyWandView) • [DuplexTransferWandViewIterator](wand-view.html#DuplexTransferWandViewIterator) • [GetWandViewException](wand-view.html#GetWandViewException) • [GetWandViewExtent](wand-view.html#GetWandViewExtent) • [GetWandViewIterator](wand-view.html#GetWandViewIterator) • [GetWandViewPixels](wand-view.html#GetWandViewPixels) • [GetWandViewWand](wand-view.html#GetWandViewWand) • [IsWandView](wand-view.html#IsWandView) • [NewWandView](wand-view.html#NewWandView) • [NewWandViewExtent](wand-view.html#NewWandViewExtent) • [SetWandViewDescription](wand-view.html#SetWandViewDescription) • [SetWandViewIterator](wand-view.html#SetWandViewIterator) • [TransferWandViewIterator](wand-view.html#TransferWandViewIterator) • [UpdateWandViewIterator](wand-view.html#UpdateWandViewIterator)

## [CloneWandView](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

CloneWandView() makes a copy of the specified wand view.

The format of the CloneWandView method is:
    
    
    WandView *CloneWandView(const WandView *wand_view)
    

A description of each parameter follows:

    
    

wand_view
    the wand view. 
    

## [DestroyWandView](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

DestroyWandView() deallocates memory associated with a wand view.

The format of the DestroyWandView method is:
    
    
    WandView *DestroyWandView(WandView *wand_view)
    

A description of each parameter follows:

    
    

wand_view
    the wand view. 
    

## [DuplexTransferWandViewIterator](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

DuplexTransferWandViewIterator() iterates over three wand views in parallel and calls your transfer method for each scanline of the view. The source and duplex pixel extent is not confined to the image canvas-- that is you can include negative offsets or widths or heights that exceed the image dimension. However, the destination wand view is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension are permitted.

The callback signature is:
    
    
    MagickBooleanType DuplexTransferImageViewMethod(const WandView *source,
      const WandView *duplex,WandView *destination,const ssize_t y,
      const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback transfer method that must be executed by a single thread at a time.

The format of the DuplexTransferWandViewIterator method is:
    
    
    MagickBooleanType DuplexTransferWandViewIterator(WandView *source,
      WandView *duplex,WandView *destination,
      DuplexTransferWandViewMethod transfer,void *context)
    

A description of each parameter follows:

    
    

source
    the source wand view. 
    
duplex
    the duplex wand view. 
    
destination
    the destination wand view. 
    
transfer
    the transfer callback method. 
    
context
    the user defined context. 
    

## [GetWandViewException](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

GetWandViewException() returns the severity, reason, and description of any error that occurs when utilizing a wand view.

The format of the GetWandViewException method is:
    
    
    char *GetWandViewException(const WandView *wand_view,
      ExceptionType *severity)
    

A description of each parameter follows:

    
    

wand_view
    the pixel wand_view. 
    
severity
    the severity of the error is returned here. 
    

## [GetWandViewExtent](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

GetWandViewExtent() returns the wand view extent.

The format of the GetWandViewExtent method is:
    
    
    RectangleInfo GetWandViewExtent(const WandView *wand_view)
    

A description of each parameter follows:

    
    

wand_view
    the wand view. 
    

## [GetWandViewIterator](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

GetWandViewIterator() iterates over the wand view in parallel and calls your get method for each scanline of the view. The pixel extent is not confined to the image canvas-- that is you can include negative offsets or widths or heights that exceed the image dimension. Any updates to the pixels in your callback are ignored.

The callback signature is:
    
    
    MagickBooleanType GetImageViewMethod(const WandView *source,
      const ssize_t y,const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback get method that must be executed by a single thread at a time.

The format of the GetWandViewIterator method is:
    
    
    MagickBooleanType GetWandViewIterator(WandView *source,
      GetWandViewMethod get,void *context)
    

A description of each parameter follows:

    
    

source
    the source wand view. 
    
get
    the get callback method. 
    
context
    the user defined context. 
    

## [GetWandViewPixels](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

GetWandViewPixels() returns the wand view pixel_wands.

The format of the GetWandViewPixels method is:
    
    
    PixelWand *GetWandViewPixels(const WandView *wand_view)
    

A description of each parameter follows:

    
    

wand_view
    the wand view. 
    

## [GetWandViewWand](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

GetWandViewWand() returns the magick wand associated with the wand view.

The format of the GetWandViewWand method is:
    
    
    MagickWand *GetWandViewWand(const WandView *wand_view)
    

A description of each parameter follows:

    
    

wand_view
    the wand view. 
    

## [IsWandView](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

IsWandView() returns MagickTrue if the the parameter is verified as a wand view object.

The format of the IsWandView method is:
    
    
    MagickBooleanType IsWandView(const WandView *wand_view)
    

A description of each parameter follows:

    
    

wand_view
    the wand view. 
    

## [NewWandView](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

NewWandView() returns a wand view required for all other methods in the Wand View API.

The format of the NewWandView method is:
    
    
    WandView *NewWandView(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the wand. 
    

## [NewWandViewExtent](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

NewWandViewExtent() returns a wand view required for all other methods in the Wand View API.

The format of the NewWandViewExtent method is:
    
    
    WandView *NewWandViewExtent(MagickWand *wand,const ssize_t x,
      const ssize_t y,const size_t width,const size_t height)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
x,y,columns,rows
     These values define the perimeter of a extent of pixel_wands view. 
    

## [SetWandViewDescription](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

SetWandViewDescription() associates a description with an image view.

The format of the SetWandViewDescription method is:
    
    
    void SetWandViewDescription(WandView *image_view,const char *description)
    

A description of each parameter follows:

    
    

wand_view
    the wand view. 
    
description
    the wand view description. 
    

## [SetWandViewIterator](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

SetWandViewIterator() iterates over the wand view in parallel and calls your set method for each scanline of the view. The pixel extent is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension. The pixels are initiallly undefined and any settings you make in the callback method are automagically synced back to your image.

The callback signature is:
    
    
    MagickBooleanType SetImageViewMethod(ImageView *destination,
      const ssize_t y,const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback set method that must be executed by a single thread at a time.

The format of the SetWandViewIterator method is:
    
    
    MagickBooleanType SetWandViewIterator(WandView *destination,
      SetWandViewMethod set,void *context)
    

A description of each parameter follows:

    
    

destination
    the wand view. 
    
set
    the set callback method. 
    
context
    the user defined context. 
    

## [TransferWandViewIterator](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

TransferWandViewIterator() iterates over two wand views in parallel and calls your transfer method for each scanline of the view. The source pixel extent is not confined to the image canvas-- that is you can include negative offsets or widths or heights that exceed the image dimension. However, the destination wand view is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension are permitted.

The callback signature is:
    
    
    MagickBooleanType TransferImageViewMethod(const WandView *source,
      WandView *destination,const ssize_t y,const int thread_id,
      void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback transfer method that must be executed by a single thread at a time.

The format of the TransferWandViewIterator method is:
    
    
    MagickBooleanType TransferWandViewIterator(WandView *source,
      WandView *destination,TransferWandViewMethod transfer,void *context)
    

A description of each parameter follows:

    
    

source
    the source wand view. 
    
destination
    the destination wand view. 
    
transfer
    the transfer callback method. 
    
context
    the user defined context. 
    

## [UpdateWandViewIterator](http://www.imagemagick.org/api/MagickWand/wand-view_8c.html)

UpdateWandViewIterator() iterates over the wand view in parallel and calls your update method for each scanline of the view. The pixel extent is confined to the image canvas-- that is no negative offsets or widths or heights that exceed the image dimension are permitted. Updates to pixels in your callback are automagically synced back to the image.

The callback signature is:
    
    
    MagickBooleanType UpdateImageViewMethod(WandView *source,const ssize_t y,
      const int thread_id,void *context)
    

Use this pragma if the view is not single threaded:
    
    
        #pragma omp critical
    

to define a section of code in your callback update method that must be executed by a single thread at a time.

The format of the UpdateWandViewIterator method is:
    
    
    MagickBooleanType UpdateWandViewIterator(WandView *source,
      UpdateWandViewMethod update,void *context)
    

A description of each parameter follows:

    
    

source
    the source wand view. 
    
update
    the update callback method. 
    
context
    the user defined context. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](wand-view.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
