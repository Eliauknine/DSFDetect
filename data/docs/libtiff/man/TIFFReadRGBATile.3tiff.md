# TIFFReadRGBATile

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadRGBATile − read and decode an image tile into a fixed-format raster

## SYNOPSIS

|  |  **#include <tiffio.h>** |  |  **#define TIFFGetR(abgr)** |  |  |  **((abgr) & 0xff)** |  |  **#define TIFFGetG(abgr)** |  |  |  **(((abgr) >> 8) & 0xff)** |  |  **#define TIFFGetB(abgr)** |  |  |  **(((abgr) >> 16) & 0xff)** |  |  **#define TIFFGetA(abgr)** |  |  |  **(((abgr) >> 24) & 0xff)** |  |  **int TIFFReadRGBATile(TIFF ***_tif_**, uint32** _x_**, uint32** _y_**, uint32 ***_raster_**)**

## DESCRIPTION

|  |  _TIFFReadRGBATile_ reads a single tile of a tile-based image into memory, storing the result in the user supplied RGBA _raster_. The raster is assumed to be an array of width times length 32-bit entries, where width is the width of a tile (TIFFTAG_TILEWIDTH) and length is the height of a tile (TIFFTAG_TILELENGTH). The _x_ and _y_ values are the offsets from the top left corner to the top left corner of the tile to be read. They must be an exact multiple of the tile width and length. Note that the raster is assume to be organized such that the pixel at location (_x_ ,_y_) is _raster_[_y_ *_width_ +_x_]; with the raster origin in the _lower-left hand corner_ of the tile. That is bottom to top organization. Edge tiles which partly fall off the image will be filled out with appropriate zeroed areas. Raster pixels are 8-bit packed red, green, blue, alpha samples. The macros _TIFFGetR_ , _TIFFGetG_ , _TIFFGetB_ , and _TIFFGetA_ should be used to access individual samples. Images without Associated Alpha matting information have a constant Alpha of 1.0 (255). See the _TIFFRGBAImage_(3TIFF) page for more details on how various image types are converted to RGBA values.

## NOTES

|  |  Samples must be either 1, 2, 4, 8, or 16 bits. Colorimetric samples/pixel must be either 1, 3, or 4 (i.e. _SamplesPerPixel_ minus _ExtraSamples_). Palette image colormaps that appear to be incorrectly written as 8-bit values are automatically scaled to 16-bits. _TIFFReadRGBATile_ is just a wrapper around the more general _TIFFRGBAImage_(3TIFF) facilities. It's main advantage over the similar _TIFFReadRGBAImage()_ function is that for large images a single buffer capable of holding the whole image doesn't need to be allocated, only enough for one tile. The _TIFFReadRGBAStrip()_ function does a similar operation for stripped images.

## RETURN VALUES

|  |  1 is returned if the image was successfully read and converted. Otherwise, 0 is returned if an error was encountered.

## DIAGNOSTICS

|  |  All error messages are directed to the _TIFFError_(3TIFF) routine. **Sorry, can not handle %d-bit pictures**. The image had _BitsPerSample_ other than 1, 2, 4, 8, or 16. **Sorry, can not handle %d-channel images**. The image had _SamplesPerPixel_ other than 1, 3, or 4. **Missing needed "PhotometricInterpretation" tag**. The image did not have a tag that describes how to display the data. **No "PhotometricInterpretation" tag, assuming RGB**. The image was missing a tag that describes how to display it, but because it has 3 or 4 samples/pixel, it is assumed to be RGB. **No "PhotometricInterpretation" tag, assuming min-is-black**. The image was missing a tag that describes how to display it, but because it has 1 sample/pixel, it is assumed to be a grayscale or bilevel image. **No space for photometric conversion table**. There was insufficient memory for a table used to convert image samples to 8-bit RGB. **Missing required "Colormap" tag**. A Palette image did not have a required _Colormap_ tag. **No space for tile buffer**. There was insufficient memory to allocate an i/o buffer. **No space for strip buffer**. There was insufficient memory to allocate an i/o buffer. **Can not handle format**. The image has a format (combination of _BitsPerSample_ , _SamplesPerPixel_ , and _PhotometricInterpretation_) that _TIFFReadRGBAImage_ can not handle. **No space for B &W mapping table**. There was insufficient memory to allocate a table used to map grayscale data to RGB. **No space for Palette mapping table**. There was insufficient memory to allocate a table used to map data to 8-bit RGB.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFRGBAImage**(3TIFF), **TIFFReadRGBAImage**(3TIFF), **TIFFReadRGBAStrip**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
