# TIFFWriteScanline

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

|  |  TIFFWriteScanline − write a scanline to an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFWriteScanline(TIFF ***_tif_**, tdata_t** _buf_**, uint32** _row_**, tsample_t** _sample_**)**

## DESCRIPTION

|  |  Write data to a file at the specified row. The _sample_ parameter is used only if data are organized in separate planes (_PlanarConfiguration_ =2). The data are assumed to be uncompressed and in the native bit- and byte-order of the host machine. The data written to the file is compressed according to the compression scheme of the current TIFF directory (see further below). If the current scanline is past the end of the current subfile, the _ImageLength_ field is automatically increased to include the scanline (except for _PlanarConfiguration_ =2, where the _ImageLength_ cannot be changed once the first data are written). If the _ImageLength_ is increased, the _StripOffsets_ and _StripByteCounts_ fields are similarly enlarged to reflect data written past the previous end of image.

## NOTES

|  |  The library writes encoded data using the native machine byte order. Correctly implemented TIFF readers are expected to do any necessary byte-swapping to correctly process image data with BitsPerSample greater than 8\. The library attempts to hide bit-ordering differences between the image and the native machine by converting data from the native machine order. In C++ the _sample_ parameter defaults to 0. Once data are written to a file for the current directory, the values of certain tags may not be altered; see _TIFFSetField_(3TIFF) for more information. It is not possible to write scanlines to a file that uses a tiled organization. The routine _TIFFIsTiled_ can be used to determine if the file is organized as tiles or strips.

## RETURN VALUES

|  |  _TIFFWriteScanline_ returns −1 if it immediately detects an error and 1 for a successful write.

## DIAGNOSTICS

|  |  All error messages are directed to the _TIFFError_(3TIFF) routine. **%s: File not open for writing .** The file was opened for reading, not writing. **Can not write scanlines to a tiled image**. An attempt was made to write a scanline to a tiled image. The image is assumed to be organized in tiles because the _TileWidth_ and _TileLength_ tags have been set with _TIFFSetField_(3TIFF). **Compression algorithm does not support random access**. Data was written in a non-sequential order to a file that uses a compression algorithm and that has _RowsPerStrip_ greater than one. That is, data in the image is to be stored in a compressed form, and with multiple rows packed into a strip. In this case, the library does not support random access to the data. The data should either be written as entire strips, sequentially by rows, or the value of _RowsPerStrip_ should be set to one. **%s: Must set "ImageWidth" before writing data**. The image's width has not be set before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **%s: Must set "PlanarConfiguration" before writing data**. The organization of data has not be defined before the first write. See **TIFFSetField**(3TIFF) for information on how to do this. **Can not change "ImageLength" when using separate planes**. Separate image planes are being used (_PlanarConfiguration_ =2), but the number of rows has not been specified before the first write. The library supports the dynamic growth of an image only when data are organized in a contiguous manner (_PlanarConfiguration_ =1). **%d: Sample out of range, max %d**. The _sample_ parameter was greater than the value of the SamplesPerPixel tag. **%s: No space for strip arrays .** There was not enough space for the arrays that hold strip offsets and byte counts.

## BUGS

|  |  Writing subsampled YCbCR data does not work correctly because, for _PlanarConfiguration_ =2 the size of a scanline is not calculated on a per-sample basis, and for _PlanarConfiguration_ =1 the library does not pack the block-interleaved samples.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFWriteEncodedStrip**(3TIFF), **TIFFWriteRawStrip**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
