# TIFFReadEncodedStrip

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadEncodedStrip − read and decode a strip of data from an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **tsize_t TIFFReadEncodedStrip(TIFF ***_tif_**, tstrip_t** _strip_**, tdata_t** _buf_**, tsize_t** _size_**)**

## DESCRIPTION

|  |  Read the specified strip of data and place up to _size_ bytes of decompressed information in the (user supplied) data buffer.

## NOTES

|  |  The value of _strip_ is a ''raw strip number.'' That is, the caller must take into account whether or not the data are organized in separate planes (_PlanarConfiguration_ =2). To read a full strip of data the data buffer should typically be at least as large as the number returned by **TIFFStripSize**(3TIFF). If the -1 passed in _size_ parameter, the whole strip will be read. You should be sure you have enough space allocated for the buffer. The library attempts to hide bit- and byte-ordering differences between the image and the native machine by converting data to the native machine order. Bit reversal is done if the _FillOrder_ tag is opposite to the native machine bit order. 16- and 32-bit samples are automatically byte-swapped if the file was written with a byte order opposite to the native machine byte order,

## RETURN VALUES

|  |  The actual number of bytes of data that were placed in _buf_ is returned; _TIFFReadEncodedStrip_ returns −1 if an error was encountered.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFReadRawStrip**(3TIFF), **TIFFReadScanline**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
