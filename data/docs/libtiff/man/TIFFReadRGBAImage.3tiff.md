# TIFFReadRGBAImage

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadRGBAImage, TIFFReadRGBAImageOriented − read and decode an image into a fixed-format raster

## SYNOPSIS

|  |  **#include <tiffio.h>** **#define TIFFGetR(abgr) ((abgr) & 0xff)  
#define TIFFGetG(abgr) (((abgr) >> 8) & 0xff)  
#define TIFFGetB(abgr) (((abgr) >> 16) & 0xff)  
#define TIFFGetA(abgr) (((abgr) >> 24) & 0xff)** **int TIFFReadRGBAImage(TIFF ***_tif_**, uint32** _width_**, uint32** _height_**, uint32 ***_raster_**, int** _stopOnError_**)  
int TIFFReadRGBAImageOriented(TIFF ***_tif_**, uint32** _width_**, uint32** _height_**, uint32 ***_raster_**, int** _orientation_**, int** _stopOnError_**)**

## DESCRIPTION

|  |  _TIFFReadRGBAImage_ reads a strip- or tile-based image into memory, storing the result in the user supplied _raster_. The raster is assumed to be an array of _width_ times _height_ 32-bit entries, where _width_ must be less than or equal to the width of the image (_height_ may be any non-zero size). If the raster dimensions are smaller than the image, the image data is cropped to the raster bounds. If the raster height is greater than that of the image, then the image data are placed in the lower part of the raster. (Note that the raster is assume to be organized such that the pixel at location (_x_ ,_y_) is _raster_[_y_ *_width_ +_x_]; with the raster origin in the lower-left hand corner.) _TIFFReadRGBAImageOriented_ works like _TIFFReadRGBAImage_ with except of that user can specify the raster origin position with the _orientation_ parameter. Four orientations supported: |  |  **ORIENTATION_TOPLEFT** |  |  origin in top-left corner, |  |  **ORIENTATION_TOPRIGHT** |  |  origin in top-right corner, |  |  **ORIENTATION_BOTLEFT** |  |  origin in bottom-left corner and |  |  **ORIENTATION_BOTRIGHT** |  |  origin in bottom-right corner. |  |  If you choose **ORIENTATION_BOTLEFT** result will be the same as returned by the _TIFFReadRGBAImage._ Raster pixels are 8-bit packed red, green, blue, alpha samples. The macros _TIFFGetR_ , _TIFFGetG_ , _TIFFGetB_ , and _TIFFGetA_ should be used to access individual samples. Images without Associated Alpha matting information have a constant Alpha of 1.0 (255). _TIFFReadRGBAImage_ converts non-8-bit images by scaling sample values. Palette, grayscale, bilevel, CMYK , and YCbCr images are converted to RGB transparently. Raster pixels are returned uncorrected by any colorimetry information present in the directory. The paramater _stopOnError_ specifies how to act if an error is encountered while reading the image. If _stopOnError_ is non-zero, then an error will terminate the operation; otherwise _TIFFReadRGBAImage_ will continue processing data until all the possible data in the image have been requested.

## NOTES

|  |  In C++ the _stopOnError_ parameter defaults to 0. Samples must be either 1, 2, 4, 8, or 16 bits. Colorimetric samples/pixel must be either 1, 3, or 4 (i.e. _SamplesPerPixel_ minus _ExtraSamples_). Palettte image colormaps that appear to be incorrectly written as 8-bit values are automatically scaled to 16-bits. _TIFFReadRGBAImage_ is just a wrapper around the more general _TIFFRGBAImage_(3TIFF) facilities.

## RETURN VALUES

|  |  1 is returned if the image was successfully read and converted. Otherwise, 0 is returned if an error was encountered and _stopOnError_ is zero.

## DIAGNOSTICS

|  |  All error messages are directed to the _TIFFError_(3TIFF) routine. **Sorry, can not handle %d-bit pictures**. The image had _BitsPerSample_ other than 1, 2, 4, 8, or 16. **Sorry, can not handle %d-channel images**. The image had _SamplesPerPixel_ other than 1, 3, or 4. **Missing needed "PhotometricInterpretation" tag**. The image did not have a tag that describes how to display the data. **No "PhotometricInterpretation" tag, assuming RGB**. The image was missing a tag that describes how to display it, but because it has 3 or 4 samples/pixel, it is assumed to be RGB. **No "PhotometricInterpretation" tag, assuming min-is-black**. The image was missing a tag that describes how to display it, but because it has 1 sample/pixel, it is assumed to be a grayscale or bilevel image. **No space for photometric conversion table**. There was insufficient memory for a table used to convert image samples to 8-bit RGB. **Missing required "Colormap" tag**. A Palette image did not have a required _Colormap_ tag. **No space for tile buffer**. There was insufficient memory to allocate an i/o buffer. **No space for strip buffer**. There was insufficient memory to allocate an i/o buffer. **Can not handle format**. The image has a format (combination of _BitsPerSample_ , _SamplesPerPixel_ , and _PhotometricInterpretation_) that _TIFFReadRGBAImage_ can not handle. **No space for B &W mapping table**. There was insufficient memory to allocate a table used to map grayscale data to RGB. **No space for Palette mapping table**. There was insufficient memory to allocate a table used to map data to 8-bit RGB.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFRGBAImage**(3TIFF), **TIFFReadRGBAStrip**(3TIFF), **TIFFReadRGBATile**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
