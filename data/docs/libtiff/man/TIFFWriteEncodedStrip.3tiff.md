# TIFFWriteEncodedStrip

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFWritedEncodedStrip − compress and write a strip of data to an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFWriteEncodedStrip(TIFF ***_tif_**, tstrip_t** _strip_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Compress _size_ bytes of raw data from _buf_ and write the result to the specified strip; replacing any previously written data. Note that the value of _strip_ is a ''raw strip number.'' That is, the caller must take into account whether or not the data are organized in separate planes (_PlanarConfiguration_ =2).

## NOTES

|  |  The library writes encoded data using the native machine byte order. Correctly implemented TIFF readers are expected to do any necessary byte-swapping to correctly process image data with BitsPerSample greater than 8. The strip number must be valid according to the current settings of the _ImageLength_ and _RowsPerStrip_ tags. An image may be dynamically grown by increasing the value of _ImageLength_ prior to each call to _TIFFWriteEncodedStrip_.

## RETURN VALUES

|  |  −1 is returned if an error was encountered. Otherwise, the value of _size_ is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the _TIFFError_(3TIFF) routine. **%s: File not open for writing**. The file was opened for reading, not writing. **Can not write scanlines to a tiled image**. The image is assumed to be organized in tiles because the _TileWidth_ and _TileLength_ tags have been set with _TIFFSetField_(3TIFF). **%s: Must set "ImageWidth" before writing data**. The image's width has not be set before the first write. See _TIFFSetField_(3TIFF) for information on how to do this. **%s: Must set "PlanarConfiguration" before writing data**. The organization of data has not be defined before the first write. See _TIFFSetField_(3TIFF) for information on how to do this. **%s: No space for strip arrays "**. There was not enough space for the arrays that hold strip offsets and byte counts.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFWriteScanline**(3TIFF), **TIFFWriteRawStrip**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
