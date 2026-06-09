# TIFFClose

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFClose − close a previously opened TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **void TIFFClose(TIFF ***_tif_**)**

## DESCRIPTION

|  |  _TIFFClose_ closes a file that was previously opened with **TIFFOpen**(3TIFF). Any buffered data are flushed to the file, including the contents of the current directory (if modified); and all resources are reclaimed.

## DIAGNOSTICS

|  |  All error messages are directed to the routine. Likewise, warning messages are directed to the **TIFFWarning**(3TIFF) routine.

## SEE ALSO

|  |  **libtiff**(3TIFF), **TIFFOpen**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
