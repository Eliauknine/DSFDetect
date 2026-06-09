# TIFFReadRawTile

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadRawTile − return an undecoded tile of data from an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFReadRawTile(TIFF ***_tif_**, ttile_t** _tile_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Read the contents of the specified tile into the (user supplied) data buffer. Note that the value of _tile_ is a ''raw tile number.'' That is, the caller must take into account whether or not the data is organized in separate planes (_PlanarConfiguration_ =2). _TIFFComputeTile_ automatically does this when converting an (x,y,z,sample) coordinate quadruple to a tile number. To read a full tile of data the data buffer should typically be at least as large as the value returned by _TIFFTileSize_.

## RETURN VALUES

|  |  The actual number of bytes of data that were placed in _buf_ is returned; _TIFFReadEncodedTile_ returns −1 if an error was encountered.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFReadEncodedTile**(3TIFF), **TIFFReadTile**(3TIFF), **TIFFTileSize**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
