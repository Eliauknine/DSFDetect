[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ClearPixelIterator](pixel-iterator.html#ClearPixelIterator) • [ClonePixelIterator](pixel-iterator.html#ClonePixelIterator) • [DestroyPixelIterator](pixel-iterator.html#DestroyPixelIterator) • [IsPixelIterator](pixel-iterator.html#IsPixelIterator) • [NewPixelIterator](pixel-iterator.html#NewPixelIterator) • [PixelClearIteratorException](pixel-iterator.html#PixelClearIteratorException) • [NewPixelRegionIterator](pixel-iterator.html#NewPixelRegionIterator) • [PixelGetCurrentIteratorRow](pixel-iterator.html#PixelGetCurrentIteratorRow) • [PixelGetIteratorException](pixel-iterator.html#PixelGetIteratorException) • [PixelGetIteratorExceptionType](pixel-iterator.html#PixelGetIteratorExceptionType) • [PixelGetIteratorRow](pixel-iterator.html#PixelGetIteratorRow) • [PixelGetNextIteratorRow](pixel-iterator.html#PixelGetNextIteratorRow) • [PixelGetPreviousIteratorRow](pixel-iterator.html#PixelGetPreviousIteratorRow) • [PixelResetIterator](pixel-iterator.html#PixelResetIterator) • [PixelSetFirstIteratorRow](pixel-iterator.html#PixelSetFirstIteratorRow) • [PixelSetIteratorRow](pixel-iterator.html#PixelSetIteratorRow) • [PixelSetLastIteratorRow](pixel-iterator.html#PixelSetLastIteratorRow) • [PixelSyncIterator](pixel-iterator.html#PixelSyncIterator)

## [ClearPixelIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

ClearPixelIterator() clear resources associated with a PixelIterator.

The format of the ClearPixelIterator method is:
    
    
    void ClearPixelIterator(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

## [ClonePixelIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

ClonePixelIterator() makes an exact copy of the specified iterator.

The format of the ClonePixelIterator method is:
    
    
    PixelIterator *ClonePixelIterator(const PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the magick iterator. 
    

## [DestroyPixelIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

DestroyPixelIterator() deallocates resources associated with a PixelIterator.

The format of the DestroyPixelIterator method is:
    
    
    PixelIterator *DestroyPixelIterator(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

## [IsPixelIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

IsPixelIterator() returns MagickTrue if the iterator is verified as a pixel iterator.

The format of the IsPixelIterator method is:
    
    
    MagickBooleanType IsPixelIterator(const PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the magick iterator. 
    

## [NewPixelIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

NewPixelIterator() returns a new pixel iterator.

The format of the NewPixelIterator method is:
    
    
    PixelIterator *NewPixelIterator(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [PixelClearIteratorException](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelClearIteratorException() clear any exceptions associated with the iterator.

The format of the PixelClearIteratorException method is:
    
    
    MagickBooleanType PixelClearIteratorException(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

## [NewPixelRegionIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

NewPixelRegionIterator() returns a new pixel iterator.

The format of the NewPixelRegionIterator method is:
    
    
    PixelIterator *NewPixelRegionIterator(MagickWand *wand,const ssize_t x,
      const ssize_t y,const size_t width,const size_t height)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
x,y,columns,rows
     These values define the perimeter of a region of pixels. 
    

## [PixelGetCurrentIteratorRow](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelGetCurrentIteratorRow() returns the current row as an array of pixel wands from the pixel iterator.

The format of the PixelGetCurrentIteratorRow method is:
    
    
    PixelWand **PixelGetCurrentIteratorRow(PixelIterator *iterator,
      size_t *number_wands)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    
number_wands
    the number of pixel wands. 
    

## [PixelGetIteratorException](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelGetIteratorException() returns the severity, reason, and description of any error that occurs when using other methods in this API.

The format of the PixelGetIteratorException method is:
    
    
    char *PixelGetIteratorException(const PixelIterator *iterator,
      ExceptionType *severity)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    
severity
    the severity of the error is returned here. 
    

## [PixelGetIteratorExceptionType](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelGetIteratorExceptionType() the exception type associated with the iterator. If no exception has occurred, UndefinedExceptionType is returned.

The format of the PixelGetIteratorExceptionType method is:
    
    
    ExceptionType PixelGetIteratorExceptionType(
      const PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

## [PixelGetIteratorRow](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelGetIteratorRow() returns the current pixel iterator row.

The format of the PixelGetIteratorRow method is:
    
    
    MagickBooleanType PixelGetIteratorRow(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

## [PixelGetNextIteratorRow](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelGetNextIteratorRow() returns the next row as an array of pixel wands from the pixel iterator.

The format of the PixelGetNextIteratorRow method is:
    
    
    PixelWand **PixelGetNextIteratorRow(PixelIterator *iterator,
      size_t *number_wands)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    
number_wands
    the number of pixel wands. 
    

## [PixelGetPreviousIteratorRow](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelGetPreviousIteratorRow() returns the previous row as an array of pixel wands from the pixel iterator.

The format of the PixelGetPreviousIteratorRow method is:
    
    
    PixelWand **PixelGetPreviousIteratorRow(PixelIterator *iterator,
      size_t *number_wands)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    
number_wands
    the number of pixel wands. 
    

## [PixelResetIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelResetIterator() resets the pixel iterator. Use it in conjunction with PixelGetNextIteratorRow() to iterate over all the pixels in a pixel container.

The format of the PixelResetIterator method is:
    
    
    void PixelResetIterator(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

## [PixelSetFirstIteratorRow](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelSetFirstIteratorRow() sets the pixel iterator to the first pixel row.

The format of the PixelSetFirstIteratorRow method is:
    
    
    void PixelSetFirstIteratorRow(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the magick iterator. 
    

## [PixelSetIteratorRow](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelSetIteratorRow() set the pixel iterator row.

The format of the PixelSetIteratorRow method is:
    
    
    MagickBooleanType PixelSetIteratorRow(PixelIterator *iterator,
      const ssize_t row)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

## [PixelSetLastIteratorRow](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelSetLastIteratorRow() sets the pixel iterator to the last pixel row.

The format of the PixelSetLastIteratorRow method is:
    
    
    void PixelSetLastIteratorRow(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the magick iterator. 
    

## [PixelSyncIterator](http://www.imagemagick.org/api/MagickWand/pixel-iterator_8c.html)

PixelSyncIterator() syncs the pixel iterator.

The format of the PixelSyncIterator method is:
    
    
    MagickBooleanType PixelSyncIterator(PixelIterator *iterator)
    

A description of each parameter follows:

    
    

iterator
    the pixel iterator. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](pixel-iterator.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
