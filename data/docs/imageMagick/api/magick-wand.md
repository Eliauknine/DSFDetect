[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ClearMagickWand](magick-wand.html#ClearMagickWand) • [CloneMagickWand](magick-wand.html#CloneMagickWand) • [DestroyMagickWand](magick-wand.html#DestroyMagickWand) • [IsMagickWand](magick-wand.html#IsMagickWand) • [MagickClearException](magick-wand.html#MagickClearException) • [MagickGetException](magick-wand.html#MagickGetException) • [MagickGetExceptionType](magick-wand.html#MagickGetExceptionType) • [MagickGetIteratorIndex](magick-wand.html#MagickGetIteratorIndex) • [MagickQueryConfigureOption](magick-wand.html#MagickQueryConfigureOption) • [MagickQueryConfigureOptions](magick-wand.html#MagickQueryConfigureOptions) • [MagickQueryFontMetrics](magick-wand.html#MagickQueryFontMetrics) • [MagickQueryMultilineFontMetrics](magick-wand.html#MagickQueryMultilineFontMetrics) • [MagickQueryFonts](magick-wand.html#MagickQueryFonts) • [MagickQueryFormats](magick-wand.html#MagickQueryFormats) • [MagickRelinquishMemory](magick-wand.html#MagickRelinquishMemory) • [MagickResetIterator](magick-wand.html#MagickResetIterator) • [MagickSetFirstIterator](magick-wand.html#MagickSetFirstIterator) • [MagickSetIteratorIndex](magick-wand.html#MagickSetIteratorIndex) • [MagickSetLastIterator](magick-wand.html#MagickSetLastIterator) • [MagickWandGenesis](magick-wand.html#MagickWandGenesis) • [MagickWandTerminus](magick-wand.html#MagickWandTerminus) • [NewMagickWand](magick-wand.html#NewMagickWand) • [NewMagickWandFromImage](magick-wand.html#NewMagickWandFromImage) • [IsMagickWandInstantiated](magick-wand.html#IsMagickWandInstantiated)

## [ClearMagickWand](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

ClearMagickWand() clears resources associated with the wand, leaving the wand blank, and ready to be used for a new set of images.

The format of the ClearMagickWand method is:
    
    
    void ClearMagickWand(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [CloneMagickWand](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

CloneMagickWand() makes an exact copy of the specified wand.

The format of the CloneMagickWand method is:
    
    
    MagickWand *CloneMagickWand(const MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [DestroyMagickWand](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

DestroyMagickWand() deallocates memory associated with an MagickWand.

The format of the DestroyMagickWand method is:
    
    
    MagickWand *DestroyMagickWand(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [IsMagickWand](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

IsMagickWand() returns MagickTrue if the wand is verified as a magick wand.

The format of the IsMagickWand method is:
    
    
    MagickBooleanType IsMagickWand(const MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickClearException](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickClearException() clears any exceptions associated with the wand.

The format of the MagickClearException method is:
    
    
    MagickBooleanType MagickClearException(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetException](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickGetException() returns the severity, reason, and description of any error that occurs when using other methods in this API.

The format of the MagickGetException method is:
    
    
    char *MagickGetException(const MagickWand *wand,ExceptionType *severity)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
severity
    the severity of the error is returned here. 
    

## [MagickGetExceptionType](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickGetExceptionType() returns the exception type associated with the wand. If no exception has occurred, UndefinedExceptionType is returned.

The format of the MagickGetExceptionType method is:
    
    
    ExceptionType MagickGetExceptionType(const MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetIteratorIndex](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickGetIteratorIndex() returns the position of the iterator in the image list.

The format of the MagickGetIteratorIndex method is:
    
    
    ssize_t MagickGetIteratorIndex(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickQueryConfigureOption](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickQueryConfigureOption() returns the value associated with the specified configure option.

The format of the MagickQueryConfigureOption function is:
    
    
    char *MagickQueryConfigureOption(const char *option)
    

A description of each parameter follows:

    
    

option
    the option name. 
    

## [MagickQueryConfigureOptions](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickQueryConfigureOptions() returns any configure options that match the specified pattern (e.g. "*" for all). Options include NAME, VERSION, LIB_VERSION, etc.

The format of the MagickQueryConfigureOptions function is:
    
    
    char **MagickQueryConfigureOptions(const char *pattern,
      size_t *number_options)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_options
     Returns the number of configure options in the list. 
    
    

## [MagickQueryFontMetrics](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickQueryFontMetrics() returns a 13 element array representing the following font metrics:
    
    
        Element Description
        -------------------------------------------------
        0 character width
        1 character height
        2 ascender
        3 descender
        4 text width
        5 text height
        6 maximum horizontal advance
        7 bounding box: x1
        8 bounding box: y1
        9 bounding box: x2
       10 bounding box: y2
       11 origin: x
       12 origin: y
    

The format of the MagickQueryFontMetrics method is:
    
    
    double *MagickQueryFontMetrics(MagickWand *wand,
      const DrawingWand *drawing_wand,const char *text)
    

A description of each parameter follows:

    
    

wand
    the Magick wand. 
    
drawing_wand
    the drawing wand. 
    
text
    the text. 
    

## [MagickQueryMultilineFontMetrics](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickQueryMultilineFontMetrics() returns a 13 element array representing the following font metrics:
    
    
        Element Description
        -------------------------------------------------
        0 character width
        1 character height
        2 ascender
        3 descender
        4 text width
        5 text height
        6 maximum horizontal advance
        7 bounding box: x1
        8 bounding box: y1
        9 bounding box: x2
       10 bounding box: y2
       11 origin: x
       12 origin: y
    

This method is like MagickQueryFontMetrics() but it returns the maximum text width and height for multiple lines of text.

The format of the MagickQueryFontMetrics method is:
    
    
    double *MagickQueryMultilineFontMetrics(MagickWand *wand,
      const DrawingWand *drawing_wand,const char *text)
    

A description of each parameter follows:

    
    

wand
    the Magick wand. 
    
drawing_wand
    the drawing wand. 
    
text
    the text. 
    

## [MagickQueryFonts](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickQueryFonts() returns any font that match the specified pattern (e.g. "*" for all).

The format of the MagickQueryFonts function is:
    
    
    char **MagickQueryFonts(const char *pattern,size_t *number_fonts)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_fonts
     Returns the number of fonts in the list. 
    
    

## [MagickQueryFormats](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickQueryFormats() returns any image formats that match the specified pattern (e.g. "*" for all).

The format of the MagickQueryFormats function is:
    
    
    char **MagickQueryFormats(const char *pattern,size_t *number_formats)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_formats
     This integer returns the number of image formats in the list. 
    

## [MagickRelinquishMemory](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickRelinquishMemory() relinquishes memory resources returned by such methods as MagickIdentifyImage(), MagickGetException(), etc.

The format of the MagickRelinquishMemory method is:
    
    
    void *MagickRelinquishMemory(void *resource)
    

A description of each parameter follows:

    
    

resource
    Relinquish the memory associated with this resource. 
    

## [MagickResetIterator](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickResetIterator() resets the wand iterator.

It is typically used either before iterating though images, or before calling specific functions such as MagickAppendImages() to append all images together.

Afterward you can use MagickNextImage() to iterate over all the images in a wand container, starting with the first image.

Using this before MagickAddImages() or MagickReadImages() will cause new images to be inserted between the first and second image.

The format of the MagickResetIterator method is:
    
    
    void MagickResetIterator(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickSetFirstIterator](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickSetFirstIterator() sets the wand iterator to the first image.

After using any images added to the wand using MagickAddImage() or MagickReadImage() will be prepended before any image in the wand.

Also the current image has been set to the first image (if any) in the Magick Wand. Using MagickNextImage() will then set teh current image to the second image in the list (if present).

This operation is similar to MagickResetIterator() but differs in how MagickAddImage(), MagickReadImage(), and MagickNextImage() behaves afterward.

The format of the MagickSetFirstIterator method is:
    
    
    void MagickSetFirstIterator(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickSetIteratorIndex](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickSetIteratorIndex() set the iterator to the given position in the image list specified with the index parameter. A zero index will set the first image as current, and so on. Negative indexes can be used to specify an image relative to the end of the images in the wand, with -1 being the last image in the wand.

If the index is invalid (range too large for number of images in wand) the function will return MagickFalse, but no 'exception' will be raised, as it is not actually an error. In that case the current image will not change.

After using any images added to the wand using MagickAddImage() or MagickReadImage() will be added after the image indexed, regardless of if a zero (first image in list) or negative index (from end) is used.

Jumping to index 0 is similar to MagickResetIterator() but differs in how MagickNextImage() behaves afterward.

The format of the MagickSetIteratorIndex method is:
    
    
    MagickBooleanType MagickSetIteratorIndex(MagickWand *wand,
      const ssize_t index)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
index
    the scene number. 
    

## [MagickSetLastIterator](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickSetLastIterator() sets the wand iterator to the last image.

The last image is actually the current image, and the next use of MagickPreviousImage() will not change this allowing this function to be used to iterate over the images in the reverse direction. In this sense it is more like MagickResetIterator() than MagickSetFirstIterator().

Typically this function is used before MagickAddImage(), MagickReadImage() functions to ensure new images are appended to the very end of wand's image list.

The format of the MagickSetLastIterator method is:
    
    
    void MagickSetLastIterator(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickWandGenesis](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickWandGenesis() initializes the MagickWand environment.

The format of the MagickWandGenesis method is:
    
    
    void MagickWandGenesis(void)
    

## [MagickWandTerminus](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

MagickWandTerminus() terminates the MagickWand environment.

The format of the MaickWandTerminus method is:
    
    
    void MagickWandTerminus(void)
    

## [NewMagickWand](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

NewMagickWand() returns a wand required for all other methods in the API. A fatal exception is thrown if there is not enough memory to allocate the wand. Use DestroyMagickWand() to dispose of the wand when it is no longer needed.

The format of the NewMagickWand method is:
    
    
    MagickWand *NewMagickWand(void)
    

## [NewMagickWandFromImage](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

NewMagickWandFromImage() returns a wand with an image.

The format of the NewMagickWandFromImage method is:
    
    
    MagickWand *NewMagickWandFromImage(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [IsMagickWandInstantiated](http://www.imagemagick.org/api/MagickWand/magick-wand_8c.html)

IsMagickWandInstantiated() returns MagickTrue if the ImageMagick environment is currently instantiated-- that is, MagickWandGenesis() has been called but MagickWandTerminus() has not.

The format of the IsMagickWandInstantiated method is:
    
    
    MagickBooleanType IsMagickWandInstantiated(void)
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](magick-wand.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
