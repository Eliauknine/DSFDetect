# TIFFReadScanline

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
BUGS  
SEE ALSO  


* * *

## NAME

|  |  TIFFReadScanline − read and decode a scanline of data from an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFReadScanline(TIFF ***_tif_**, tdata_t** _buf_**, uint32** _row_**, tsample_t** _sample_**)**

## DESCRIPTION

|  |  Read the data for the specified row into the (user supplied) data buffer _buf_. The data are returned decompressed and, in the native byte- and bit-ordering, but are otherwise packed (see further below). The buffer must be large enough to hold an entire scanline of data. Applications should call the routine _TIFFScanlineSize_ to find out the size (in bytes) of a scanline buffer. The _row_ parameter is always used by _TIFFReadScanline_ ; the _sample_ parameter is used only if data are organized in separate planes (_PlanarConfiguration_ =2).

## NOTES

|  |  The library attempts to hide bit- and byte-ordering differences between the image and the native machine by converting data to the native machine order. Bit reversal is done if the _FillOrder_ tag is opposite to the native machine bit order. 16- and 32-bit samples are automatically byte-swapped if the file was written with a byte order opposite to the native machine byte order, In C++ the _sample_ parameter defaults to 0.

## RETURN VALUES

|  |  _TIFFReadScanline_ returns −1 if it detects an error; otherwise 1 is returned.

## DIAGNOSTICS

|  |  All error messages are directed to the _TIFFError_(3TIFF) routine. **Compression algorithm does not support random access**. Data was requested in a non-sequential order from a file that uses a compression algorithm and that has _RowsPerStrip_ greater than one. That is, data in the image is stored in a compressed form, and with multiple rows packed into a strip. In this case, the library does not support random access to the data. The data should either be accessed sequentially, or the file should be converted so that each strip is made up of one row of data.

## BUGS

|  |  Reading subsampled YCbCR data does not work correctly because, for _PlanarConfiguration_ =2 the size of a scanline is not calculated on a per-sample basis, and for _PlanarConfiguration_ =1 the library does not unpack the block-interleaved samples; use the strip- and tile-based interfaces to read these formats.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFReadEncodedStrip**(3TIFF), **TIFFReadRawStrip**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
