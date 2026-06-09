[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireAuthenticCacheView](cache-view.html#AcquireAuthenticCacheView) • [AcquireVirtualCacheView](cache-view.html#AcquireVirtualCacheView) • [CloneCacheView](cache-view.html#CloneCacheView) • [DestroyCacheView](cache-view.html#DestroyCacheView) • [GetCacheViewAuthenticPixels](cache-view.html#GetCacheViewAuthenticPixels) • [GetCacheViewAuthenticMetacontent](cache-view.html#GetCacheViewAuthenticMetacontent) • [GetCacheViewAuthenticPixelQueue](cache-view.html#GetCacheViewAuthenticPixelQueue) • [GetCacheViewColorspace](cache-view.html#GetCacheViewColorspace) • [GetCacheViewImage](cache-view.html#GetCacheViewImage) • [GetCacheViewStorageClass](cache-view.html#GetCacheViewStorageClass) • [GetCacheViewVirtualMetacontent](cache-view.html#GetCacheViewVirtualMetacontent) • [GetCacheViewVirtualPixelQueue](cache-view.html#GetCacheViewVirtualPixelQueue) • [GetCacheViewVirtualPixels](cache-view.html#GetCacheViewVirtualPixels) • [GetOneCacheViewAuthenticPixel](cache-view.html#GetOneCacheViewAuthenticPixel) • [GetOneCacheViewVirtualPixel](cache-view.html#GetOneCacheViewVirtualPixel) • [GetOneCacheViewVirtualPixelInfo](cache-view.html#GetOneCacheViewVirtualPixelInfo) • [GetOneCacheViewVirtualMethodPixel](cache-view.html#GetOneCacheViewVirtualMethodPixel) • [QueueCacheViewAuthenticPixels](cache-view.html#QueueCacheViewAuthenticPixels) • [SetCacheViewStorageClass](cache-view.html#SetCacheViewStorageClass) • [SetCacheViewVirtualPixelMethod](cache-view.html#SetCacheViewVirtualPixelMethod) • [SyncCacheViewAuthenticPixels](cache-view.html#SyncCacheViewAuthenticPixels)

## [AcquireAuthenticCacheView](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

AcquireAuthenticCacheView() acquires an authentic view into the pixel cache. It always succeeds but may return a warning or informational exception.

The format of the AcquireAuthenticCacheView method is:
    
    
    CacheView *AcquireAuthenticCacheView(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [AcquireVirtualCacheView](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

AcquireVirtualCacheView() acquires a virtual view into the pixel cache, using the VirtualPixelMethod that is defined within the given image itself. It always succeeds but may return a warning or informational exception.

The format of the AcquireVirtualCacheView method is:
    
    
    CacheView *AcquireVirtualCacheView(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [CloneCacheView](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

CloneCacheView() makes an exact copy of the specified cache view.

The format of the CloneCacheView method is:
    
    
    CacheView *CloneCacheView(const CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [DestroyCacheView](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

DestroyCacheView() destroys the specified view returned by a previous call to AcquireCacheView().

The format of the DestroyCacheView method is:
    
    
    CacheView *DestroyCacheView(CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewAuthenticPixels](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewAuthenticPixels() gets pixels from the in-memory or disk pixel cache as defined by the geometry parameters. A pointer to the pixels is returned if the pixels are transferred, otherwise a NULL is returned.

The format of the GetCacheViewAuthenticPixels method is:
    
    
    Quantum *GetCacheViewAuthenticPixels(CacheView *cache_view,
      const ssize_t x,const ssize_t y,const size_t columns,
      const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
x,y,columns,rows
     These values define the perimeter of a region of pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetCacheViewAuthenticMetacontent](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewAuthenticMetacontent() returns the meta-content corresponding with the last call to SetCacheViewIndexes() or GetCacheViewAuthenticMetacontent(). The meta-content are authentic and can be updated.

The format of the GetCacheViewAuthenticMetacontent() method is:
    
    
    void *GetCacheViewAuthenticMetacontent(CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewAuthenticPixelQueue](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewAuthenticPixelQueue() returns the pixels associated with the last call to QueueCacheViewAuthenticPixels() or GetCacheViewAuthenticPixels(). The pixels are authentic and therefore can be updated.

The format of the GetCacheViewAuthenticPixelQueue() method is:
    
    
    Quantum *GetCacheViewAuthenticPixelQueue(CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewColorspace](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewColorspace() returns the image colorspace associated with the specified view.

The format of the GetCacheViewColorspace method is:
    
    
    ColorspaceType GetCacheViewColorspace(const CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewImage](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewImage() returns the image associated with the specified view.

The format of the GetCacheViewImage method is:
    
    
    const Image *GetCacheViewImage(const CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewStorageClass](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewStorageClass() returns the image storage class associated with the specified view.

The format of the GetCacheViewStorageClass method is:
    
    
    ClassType GetCacheViewStorageClass(const CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewVirtualMetacontent](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewVirtualMetacontent() returns the meta-content corresponding with the last call to GetCacheViewVirtualMetacontent(). The meta-content is virtual and therefore cannot be updated.

The format of the GetCacheViewVirtualMetacontent() method is:
    
    
    const void *GetCacheViewVirtualMetacontent(
      const CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewVirtualPixelQueue](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewVirtualPixelQueue() returns the the pixels associated with the last call to GetCacheViewVirtualPixels(). The pixels are virtual and therefore cannot be updated.

The format of the GetCacheViewVirtualPixelQueue() method is:
    
    
    const Quantum *GetCacheViewVirtualPixelQueue(
      const CacheView *cache_view)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    

## [GetCacheViewVirtualPixels](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetCacheViewVirtualPixels() gets virtual pixels from the in-memory or disk pixel cache as defined by the geometry parameters. A pointer to the pixels is returned if the pixels are transferred, otherwise a NULL is returned.

The format of the GetCacheViewVirtualPixels method is:
    
    
    const Quantum *GetCacheViewVirtualPixels(
      const CacheView *cache_view,const ssize_t x,const ssize_t y,
      const size_t columns,const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
x,y,columns,rows
     These values define the perimeter of a region of pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetOneCacheViewAuthenticPixel](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetOneCacheViewAuthenticPixel() returns a single pixel at the specified (x,y) location. The image background color is returned if an error occurs.

The format of the GetOneCacheViewAuthenticPixel method is:
    
    
    MagickBooleaNType GetOneCacheViewAuthenticPixel(
      const CacheView *cache_view,const ssize_t x,const ssize_t y,
      Quantum *pixel,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
x,y
     These values define the offset of the pixel. 
    
pixel
    return a pixel at the specified (x,y) location. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetOneCacheViewVirtualPixel](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetOneCacheViewVirtualPixel() returns a single pixel at the specified (x,y) location. The image background color is returned if an error occurs. If you plan to modify the pixel, use GetOneCacheViewAuthenticPixel() instead.

The format of the GetOneCacheViewVirtualPixel method is:
    
    
    MagickBooleanType GetOneCacheViewVirtualPixel(
      const CacheView *cache_view,const ssize_t x,const ssize_t y,
      Quantum *pixel,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
x,y
     These values define the offset of the pixel. 
    
pixel
    return a pixel at the specified (x,y) location. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetOneCacheViewVirtualPixelInfo](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetOneCacheViewVirtualPixelInfo() returns a single pixel at the specified (x,y) location. The image background color is returned if an error occurs. If you plan to modify the pixel, use GetOneCacheViewAuthenticPixel() instead.

The format of the GetOneCacheViewVirtualPixelInfo method is:
    
    
    MagickBooleanType GetOneCacheViewVirtualPixelInfo(
      const CacheView *cache_view,const ssize_t x,const ssize_t y,
      PixelInfo *pixel,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
x,y
     These values define the offset of the pixel. 
    
pixel
    return a pixel at the specified (x,y) location. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetOneCacheViewVirtualMethodPixel](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

GetOneCacheViewVirtualMethodPixel() returns a single virtual pixel at the specified (x,y) location. The image background color is returned if an error occurs. If you plan to modify the pixel, use GetOneCacheViewAuthenticPixel() instead.

The format of the GetOneCacheViewVirtualPixel method is:
    
    
    MagickBooleanType GetOneCacheViewVirtualMethodPixel(
      const CacheView *cache_view,
      const VirtualPixelMethod virtual_pixel_method,const ssize_t x,
      const ssize_t y,Quantum *pixel,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
virtual_pixel_method
    the virtual pixel method. 
    
x,y
     These values define the offset of the pixel. 
    
pixel
    return a pixel at the specified (x,y) location. 
    
exception
    return any errors or warnings in this structure. 
    

## [QueueCacheViewAuthenticPixels](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

QueueCacheViewAuthenticPixels() queues authentic pixels from the in-memory or disk pixel cache as defined by the geometry parameters. A pointer to the pixels is returned if the pixels are transferred, otherwise a NULL is returned.

The format of the QueueCacheViewAuthenticPixels method is:
    
    
    Quantum *QueueCacheViewAuthenticPixels(CacheView *cache_view,
      const ssize_t x,const ssize_t y,const size_t columns,
      const size_t rows,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
x,y,columns,rows
     These values define the perimeter of a region of pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetCacheViewStorageClass](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

SetCacheViewStorageClass() sets the image storage class associated with the specified view.

The format of the SetCacheViewStorageClass method is:
    
    
    MagickBooleanType SetCacheViewStorageClass(CacheView *cache_view,
      const ClassType storage_class,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
storage_class
    the image storage class: PseudoClass or DirectClass. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetCacheViewVirtualPixelMethod](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

SetCacheViewVirtualPixelMethod() sets the virtual pixel method associated with the specified cache view.

The format of the SetCacheViewVirtualPixelMethod method is:
    
    
    MagickBooleanType SetCacheViewVirtualPixelMethod(CacheView *cache_view,
      const VirtualPixelMethod virtual_pixel_method)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
virtual_pixel_method
    the virtual pixel method. 
    

## [SyncCacheViewAuthenticPixels](http://www.imagemagick.org/api/MagickCore/cache-view_8c.html)

SyncCacheViewAuthenticPixels() saves the cache view pixels to the in-memory or disk cache. It returns MagickTrue if the pixel region is flushed, otherwise MagickFalse.

The format of the SyncCacheViewAuthenticPixels method is:
    
    
    MagickBooleanType SyncCacheViewAuthenticPixels(CacheView *cache_view,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

cache_view
    the cache view. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](cache-view.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
