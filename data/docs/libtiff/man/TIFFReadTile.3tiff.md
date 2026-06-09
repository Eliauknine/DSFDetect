# TIFFReadTile

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadTile − read and decode a tile of data from an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFReadTile(TIFF ***_tif_**, tdata_t** _buf_**, uint32** _x_**, uint32** _y_**, uint32** _z_**, tsample_t** _sample_**)**

## DESCRIPTION

|  |  Return the data for the tile _containing_ the specified coordinates. The data placed in _buf_ are returned decompressed and, typically, in the native byte- and bit-ordering, but are otherwise packed (see further below). The buffer must be large enough to hold an entire tile of data. Applications should call the routine _TIFFTileSize_ to find out the size (in bytes) of a tile buffer. The _x_ and _y_ parameters are always used by _TIFFReadTile_. The _z_ parameter is used if the image is deeper than 1 slice (_ImageDepth_ >1). The _sample_ parameter is used only if data are organized in separate planes (_PlanarConfiguration_ =2).

## NOTES

|  |  The library attempts to hide bit- and byte-ordering differences between the image and the native machine by converting data to the native machine order. Bit reversal is done if the _FillOrder_ tag is opposite to the native machine bit order. 16- and 32-bit samples are automatically byte-swapped if the file was written with a byte order opposite to the native machine byte order,

## RETURN VALUES

|  |  _TIFFReadTile_ returns −1 if it detects an error; otherwise the number of bytes in the decoded tile is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine.

## SEE ALSO

|  |  **TIFFCheckTile**(3TIFF), **TIFFComputeTile**(3TIFF), **TIFFOpen**(3TIFF), **TIFFReadEncodedTile**(3TIFF), **TIFFReadRawTile**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
