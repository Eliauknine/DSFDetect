# TIFFWriteEncodedTile

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFWritedEncodedTile − compress and write a tile of data to an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFWriteEncodedTile(TIFF ***_tif_**, ttile_t** _tile_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Compress _size_ bytes of raw data from _buf_ and **append** the result to the end of the specified tile. Note that the value of _tile_ is a ''raw tile number.'' That is, the caller must take into account whether or not the data are organized in separate places (_PlanarConfiguration_ =2). _TIFFComputeTile_ automatically does this when converting an (x,y,z,sample) coordinate quadruple to a tile number.

## NOTES

|  |  The library writes encoded data using the native machine byte order. Correctly implemented TIFF readers are expected to do any necessary byte-swapping to correctly process image data with BitsPerSample greater than 8.

## RETURN VALUES

|  |  −1 is returned if an error was encountered. Otherwise, the value of _size_ is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine. **%s: File not open for writing**. The file was opened for reading, not writing. **Can not write tiles to a stripped image**. The image is assumed to be organized in strips because neither of the _TileWidth_ or _TileLength_ tags have been set with **TIFFSetField**(3TIFF). **%s: Must set "ImageWidth" before writing data**. The image's width has not be set before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **%s: Must set "PlanarConfiguration" before writing data**. The organization of data has not be defined before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **%s: No space for tile arrays "**. There was not enough space for the arrays that hold tile offsets and byte counts.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFWriteTile**(3TIFF), **TIFFWriteRawTile**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
