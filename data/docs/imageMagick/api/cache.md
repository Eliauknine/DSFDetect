[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquirePixelCacheNexus](cache.html#AcquirePixelCacheNexus) • [GetAuthenticMetacontent](cache.html#GetAuthenticMetacontent) • [GetAuthenticPixelQueue](cache.html#GetAuthenticPixelQueue) • [GetAuthenticPixels](cache.html#GetAuthenticPixels) • [GetOneAuthenticPixel](cache.html#GetOneAuthenticPixel) • [GetOneVirtualPixel](cache.html#GetOneVirtualPixel) • [GetOneVirtualPixelInfo](cache.html#GetOneVirtualPixelInfo) • [GetVirtualMetacontent](cache.html#GetVirtualMetacontent) • [GetVirtualPixelQueue](cache.html#GetVirtualPixelQueue) • [GetVirtualPixels](cache.html#GetVirtualPixels) • [QueueAuthenticPixels](cache.html#QueueAuthenticPixels) • [SetPixelCacheVirtualMethod](cache.html#SetPixelCacheVirtualMethod) • [SyncAuthenticPixels](cache.html#SyncAuthenticPixels)

## [AcquirePixelCacheNexus](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

AcquirePixelCacheNexus() allocates the NexusInfo structure.

The format of the AcquirePixelCacheNexus method is:
    
    
    NexusInfo **AcquirePixelCacheNexus(const size_t number_threads)
    

A description of each parameter follows:

    
    

number_threads
    the number of nexus threads. 
    

## [GetAuthenticMetacontent](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetAuthenticMetacontent() returns the authentic metacontent corresponding with the last call to QueueAuthenticPixels() or GetVirtualPixels(). NULL is returned if the associated pixels are not available.

The format of the GetAuthenticMetacontent() method is:
    
    
    void *GetAuthenticMetacontent(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [GetAuthenticPixelQueue](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetAuthenticPixelQueue() returns the authentic pixels associated corresponding with the last call to QueueAuthenticPixels() or GetAuthenticPixels().

The format of the GetAuthenticPixelQueue() method is:
    
    
    Quantum *GetAuthenticPixelQueue(const Image image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [GetAuthenticPixels](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetAuthenticPixels() obtains a pixel region for read/write access. If the region is successfully accessed, a pointer to a Quantum array representing the region is returned, otherwise NULL is returned.

The returned pointer may point to a temporary working copy of the pixels or it may point to the original pixels in memory. Performance is maximized if the selected region is part of one row, or one or more full rows, since then there is opportunity to access the pixels in-place (without a copy) if the image is in memory, or in a memory-mapped file. The returned pointer must *never* be deallocated by the user.

Pixels accessed via the returned pointer represent a simple array of type Quantum. If the image has corresponding metacontent,call GetAuthenticMetacontent() after invoking GetAuthenticPixels() to obtain the meta-content corresponding to the region. Once the Quantum array has been updated, the changes must be saved back to the underlying image using SyncAuthenticPixels() or they may be lost.

The format of the GetAuthenticPixels() method is:
    
    
    Quantum *GetAuthenticPixels(Image *image,const ssize_t x,
      const ssize_t y,const size_t columns,const size_t rows,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
x,y,columns,rows
     These values define the perimeter of a region of pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetOneAuthenticPixel](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetOneAuthenticPixel() returns a single pixel at the specified (x,y) location. The image background color is returned if an error occurs.

The format of the GetOneAuthenticPixel() method is:
    
    
    MagickBooleanType GetOneAuthenticPixel(const Image image,const ssize_t x,
      const ssize_t y,Quantum *pixel,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
x,y
     These values define the location of the pixel to return. 
    
pixel
    return a pixel at the specified (x,y) location. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetOneVirtualPixel](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetOneVirtualPixel() returns a single virtual pixel at the specified (x,y) location. The image background color is returned if an error occurs. If you plan to modify the pixel, use GetOneAuthenticPixel() instead.

The format of the GetOneVirtualPixel() method is:
    
    
    MagickBooleanType GetOneVirtualPixel(const Image image,const ssize_t x,
      const ssize_t y,Quantum *pixel,ExceptionInfo exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
x,y
     These values define the location of the pixel to return. 
    
pixel
    return a pixel at the specified (x,y) location. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetOneVirtualPixelInfo](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetOneVirtualPixelInfo() returns a single pixel at the specified (x,y) location. The image background color is returned if an error occurs. If you plan to modify the pixel, use GetOneAuthenticPixel() instead.

The format of the GetOneVirtualPixelInfo() method is:
    
    
    MagickBooleanType GetOneVirtualPixelInfo(const Image image,
      const VirtualPixelMethod virtual_pixel_method,const ssize_t x,
      const ssize_t y,PixelInfo *pixel,ExceptionInfo exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
virtual_pixel_method
    the virtual pixel method. 
    
x,y
     these values define the location of the pixel to return. 
    
pixel
    return a pixel at the specified (x,y) location. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetVirtualMetacontent](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetVirtualMetacontent() returns the virtual metacontent corresponding with the last call to QueueAuthenticPixels() or GetVirtualPixels(). NULL is returned if the meta-content are not available.

The format of the GetVirtualMetacontent() method is:
    
    
    const void *GetVirtualMetacontent(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [GetVirtualPixelQueue](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetVirtualPixelQueue() returns the virtual pixels associated corresponding with the last call to QueueAuthenticPixels() or GetVirtualPixels().

The format of the GetVirtualPixelQueue() method is:
    
    
    const Quantum *GetVirtualPixelQueue(const Image image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [GetVirtualPixels](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

GetVirtualPixels() returns an immutable pixel region. If the region is successfully accessed, a pointer to it is returned, otherwise NULL is returned. The returned pointer may point to a temporary working copy of the pixels or it may point to the original pixels in memory. Performance is maximized if the selected region is part of one row, or one or more full rows, since there is opportunity to access the pixels in-place (without a copy) if the image is in memory, or in a memory-mapped file. The returned pointer must *never* be deallocated by the user.

Pixels accessed via the returned pointer represent a simple array of type Quantum. If the image type is CMYK or the storage class is PseudoClass, call GetAuthenticMetacontent() after invoking GetAuthenticPixels() to access the meta-content (of type void) corresponding to the the region.

If you plan to modify the pixels, use GetAuthenticPixels() instead.

Note, the GetVirtualPixels() and GetAuthenticPixels() methods are not thread- safe. In a threaded environment, use GetCacheViewVirtualPixels() or GetCacheViewAuthenticPixels() instead.

The format of the GetVirtualPixels() method is:
    
    
    const Quantum *GetVirtualPixels(const Image *image,const ssize_t x,
      const ssize_t y,const size_t columns,const size_t rows,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
x,y,columns,rows
     These values define the perimeter of a region of pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [QueueAuthenticPixels](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

QueueAuthenticPixels() queues a mutable pixel region. If the region is successfully initialized a pointer to a Quantum array representing the region is returned, otherwise NULL is returned. The returned pointer may point to a temporary working buffer for the pixels or it may point to the final location of the pixels in memory.

Write-only access means that any existing pixel values corresponding to the region are ignored. This is useful if the initial image is being created from scratch, or if the existing pixel values are to be completely replaced without need to refer to their pre-existing values. The application is free to read and write the pixel buffer returned by QueueAuthenticPixels() any way it pleases. QueueAuthenticPixels() does not initialize the pixel array values. Initializing pixel array values is the application's responsibility.

Performance is maximized if the selected region is part of one row, or one or more full rows, since then there is opportunity to access the pixels in-place (without a copy) if the image is in memory, or in a memory-mapped file. The returned pointer must *never* be deallocated by the user.

Pixels accessed via the returned pointer represent a simple array of type Quantum. If the image type is CMYK or the storage class is PseudoClass, call GetAuthenticMetacontent() after invoking GetAuthenticPixels() to obtain the meta-content (of type void) corresponding to the region. Once the Quantum (and/or Quantum) array has been updated, the changes must be saved back to the underlying image using SyncAuthenticPixels() or they may be lost.

The format of the QueueAuthenticPixels() method is:
    
    
    Quantum *QueueAuthenticPixels(Image *image,const ssize_t x,
      const ssize_t y,const size_t columns,const size_t rows,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
x,y,columns,rows
     These values define the perimeter of a region of pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetPixelCacheVirtualMethod](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

SetPixelCacheVirtualMethod() sets the "virtual pixels" method for the pixel cache and returns the previous setting. A virtual pixel is any pixel access that is outside the boundaries of the image cache.

The format of the SetPixelCacheVirtualMethod() method is:
    
    
    VirtualPixelMethod SetPixelCacheVirtualMethod(Image *image,
      const VirtualPixelMethod virtual_pixel_method,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
virtual_pixel_method
    choose the type of virtual pixel. 
    
exception
    return any errors or warnings in this structure. 
    

## [SyncAuthenticPixels](http://www.imagemagick.org/api/MagickCore/cache_8c.html)

SyncAuthenticPixels() saves the image pixels to the in-memory or disk cache. The method returns MagickTrue if the pixel region is flushed, otherwise MagickFalse.

The format of the SyncAuthenticPixels() method is:
    
    
    MagickBooleanType SyncAuthenticPixels(Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](cache.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
