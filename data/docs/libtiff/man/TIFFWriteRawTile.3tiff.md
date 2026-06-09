# TIFFWriteRawtile

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFWriteRawTile − write a tile of raw data to an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFWriteRawTile(TIFF ***_tif_**, ttile_t** _tile_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Append _size_ bytes of raw data to the specified tile.

## RETURN VALUES

|  |  −1 is returned if an error occurred. Otherwise, the value of _size_ is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine. **%s: File not open for writing**. The file was opened for reading, not writing. **Can not write tiles to a stripped image**. The image is assumed to be organized in strips because neither of the _TileWidth_ or _TileLength_ tags have been set with **TIFFSetField**(3TIFF). **%s: Must set "ImageWidth" before writing data**. The image's width has not be set before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **%s: Must set "PlanarConfiguration" before writing data**. The organization of data has not be defined before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **%s: No space for tile arrays "**. There was not enough space for the arrays that hold tile offsets and byte counts. **%s: Specified tile %d out of range, max %d**. The specified tile is not valid according to the currently specified image dimensions.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFWriteEncodedTile**(3TIFF), **TIFFWriteScanline**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
