# TIFFFlush

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFFlush, TIFFFlushData − flush pending writes to an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFFlush(TIFF ***_tif_**)  
int TIFFFlushData(TIFF ***_tif_**)**

## DESCRIPTION

|  |  _TIFFFlush_ causes any pending writes for the specified file (including writes for the current directory) to be done. In normal operation this call is never needed − the library automatically does any flushing required. _TIFFFlushData_ flushes any pending image data for the specified file to be written out; directory-related data are not flushed. In normal operation this call is never needed − the library automatically does any flushing required.

## RETURN VALUES

|  |  0 is returned if an error is encountered, otherwise 1 is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFWriteEncodedStrip**(3TIFF), **TIFFWriteEncodedTile**(3TIFF), **TIFFWriteRawStrip**(3TIFF), **TIFFWriteRawTile**(3TIFF), **TIFFWriteScanline**(3TIFF), **TIFFWriteTile**(3TIFF) **libtiff**(3TIFF), Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
