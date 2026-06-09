# TIFFSIZE

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFScanlineSize, TIFFRasterScanlineSize, − return the size of various items associated with an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFRasterScanlineSize(TIFF ***_tif_**)  
tsize_t TIFFScanlineSize(TIFF ***_tif_**)**

## DESCRIPTION

|  |  _TIFFScanlineSize_ returns the size in bytes of a row of data as it would be returned in a call to _TIFFReadScanline_ , or as it would be expected in a call to _TIFFWriteScanline_. _TIFFRasterScanlineSize_ returns the size in bytes of a complete decoded and packed raster scanline. Note that this value may be different from the value returned by _TIFFScanlineSize_ if data is stored as separate planes.

## DIAGNOSTICS

|  |  None.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFReadScanline**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
