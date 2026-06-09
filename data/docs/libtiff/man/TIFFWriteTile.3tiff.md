# TIFFWriteTile

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFWriteTile − encode and write a tile of data to an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFWriteTile(TIFF ***_tif_**, tdata_t** _buf_**, uint32** _x_**, uint32** _y_**, uint32** _z_**, tsample_t** _sample_**)**

## DESCRIPTION

|  |  Write the data for the tile _containing_ the specified coordinates. The data in _buf_ are is (potentially) compressed, and written to the indicated file, normally being appended to the end of the file. The buffer must be contain an entire tile of data. Applications should call the routine _TIFFTileSize_ to find out the size (in bytes) of a tile buffer. The _x_ and _y_ parameters are always used by _TIFFWriteTile_. The _z_ parameter is used if the image is deeper than 1 slice (_ImageDepth_ >1). The _sample_ parameter is used only if data are organized in separate planes (_PlanarConfiguration_ =2).

## RETURN VALUES

|  |  _TIFFWriteTile_ returns −1 if it detects an error; otherwise the number of bytes in the tile is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine.

## SEE ALSO

|  |  **TIFFCheckTile**(3TIFF), **TIFFComputeTile**(3TIFF), **TIFFOpen**(3TIFF), **TIFFReadTile**(3TIFF), **TIFFWriteScanline**(3TIFF), **TIFFWriteEncodedTile**(3TIFF), **TIFFWriteRawTile**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
