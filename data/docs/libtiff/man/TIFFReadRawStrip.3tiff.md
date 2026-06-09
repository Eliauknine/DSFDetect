# TIFFReadRawStrip

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadRawStrip − return the undecoded contents of a strip of data from an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFReadRawStrip(TIFF ***_tif_**, tstrip_t** _strip_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Read the contents of the specified strip into the (user supplied) data buffer. Note that the value of _strip_ is a ''raw strip number.'' That is, the caller must take into account whether or not the data is organized in separate planes (_PlanarConfiguration_ =2). To read a full strip of data the data buffer should typically be at least as large as the number returned by _TIFFStripSize_.

## RETURN VALUES

|  |  The actual number of bytes of data that were placed in _buf_ is returned; _TIFFReadEncodedStrip_ returns −1 if an error was encountered.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFReadEncodedStrip**(3TIFF), **TIFFReadScanline**(3TIFF), **TIFFStripSize**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
