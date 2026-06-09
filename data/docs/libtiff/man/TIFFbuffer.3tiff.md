# TIFFBUFFER

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadBufferSetup, TIFFWriteBufferSetup − I/O buffering control routines

## SYNOPSIS

|  | 
    
    
    **#include <tiffio.h>
    
    int TIFFReadBufferSetup(TIFF ***_tif_**, tdata_t** _buffer_**, tsize_t** _size_**);
    int TIFFWriteBufferSetup(TIFF ***_tif_**, tdata_t** _buffer_**, tsize_t** _size_**);**

## DESCRIPTION

|  |  The following routines are provided for client-control of the I/O buffers used by the library. Applications need never use these routines; they are provided only for ''intelligent clients'' that wish to optimize memory usage and/or eliminate potential copy operations that can occur when working with images that have data stored without compression. _TIFFReadBufferSetup_ sets up the data buffer used to read raw (encoded) data from a file. If the specified pointer is NULL (zero), then a buffer of the appropriate size is allocated. Otherwise the caller must guarantee that the buffer is large enough to hold any individual strip of raw data. _TIFFReadBufferSetup_ returns a non-zero value if the setup was successful and zero otherwise. _TIFFWriteBufferSetup_ sets up the data buffer used to write raw (encoded) data to a file. If the specified _size_ is −1 then the buffer size is selected to hold a complete tile or strip, or at least 8 kilobytes, whichever is greater. If the specified _buffer_ is NULL (zero), then a buffer of the appropriate size is dynamically allocated. _TIFFWriteBufferSetup_ returns a non-zero value if the setup was successful and zero otherwise.

## DIAGNOSTICS

|  |  **%s: No space for data buffer at scanline %ld**. _TIFFReadBufferSetup_ was unable to dynamically allocate space for a data buffer. **%s: No space for output buffer**. _TIFFWriteBufferSetup_ was unable to dynamically allocate space for a data buffer.

## SEE ALSO

|  |  **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
