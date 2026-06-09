# TIFFWriteRawstrip

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFWriteRawStrip − write a strip of raw data to an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFWriteRawStrip(TIFF ***_tif_**, tstrip_t** _strip_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Append _size_ bytes of raw data to the specified strip.

## NOTES

|  |  The strip number must be valid according to the current settings of the _ImageLength_ and _RowsPerStrip_ tags. An image may be dynamically grown by increasing the value of _ImageLength_ prior to each call to _TIFFWriteRawStrip_.

## RETURN VALUES

|  |  −1 is returned if an error occurred. Otherwise, the value of _size_ is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine. **%s: File not open for writing**. The file was opened for reading, not writing. **Can not write scanlines to a tiled image**. The image is assumed to be organized in tiles because the _TileWidth_ and _TileLength_ tags have been set with **TIFFSetField**(3TIFF). **%s: Must set "ImageWidth" before writing data**. The image's width has not be set before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **%s: Must set "PlanarConfiguration" before writing data**. The organization of data has not be defined before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **%s: No space for strip arrays "**. There was not enough space for the arrays that hold strip offsets and byte counts. **%s: Strip %d out of range, max %d**. The specified strip is not a valid strip according to the currently specified image dimensions.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFWriteEncodedStrip**(3TIFF), **TIFFWriteScanline**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
