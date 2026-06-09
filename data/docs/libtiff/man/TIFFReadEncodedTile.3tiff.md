# TIFFReadEncodedTile

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadEncodedTile − read and decode a tile of data from an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFReadEncodedTile(TIFF ***_tif_**, ttile_t** _tile_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Read the specified tile of data and place up to _size_ bytes of decompressed information in the (user supplied) data buffer.

## NOTES

|  |  The value of _tile_ is a ''raw tile number.'' That is, the caller must take into account whether or not the data are organized in separate planes (_PlanarConfiguration_ =2). _TIFFComputeTile_ automatically does this when converting an (x,y,z,sample) coordinate quadruple to a tile number. To read a full tile of data the data buffer should be at least as large as the value returned by _TIFFTileSize_. The library attempts to hide bit- and byte-ordering differences between the image and the native machine by converting data to the native machine order. Bit reversal is done if the _FillOrder_ tag is opposite to the native machine bit order. 16- and 32-bit samples are automatically byte-swapped if the file was written with a byte order opposite to the native machine byte order,

## RETURN VALUES

|  |  The actual number of bytes of data that were placed in _buf_ is returned; _TIFFReadEncodedTile_ returns −1 if an error was encountered.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFReadRawTile**(3TIFF), **TIFFReadTile**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
