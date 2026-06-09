# TIFFSV

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
NOTE  
BUGS  
SEE ALSO  


* * *

## NAME

|  |  tiffsv − save an image from the framebuffer in a TIFF file (Silicon Graphics version)

## SYNOPSIS

|  |  **tiffsv** [ _options_ ] _output.tif_ [ _x1 x2 y1 y2_ ]

## DESCRIPTION

|  |  _tiffsv_ saves all or part of the framebuffer in a file using the Tag Image File Format, Revision 6.0. By default, the image is saved with data samples packed (_PlanarConfiguration_ =1), compressed with the Lempel-Ziv & Welch algorithm (_Compression_ =5), and with each strip no more than 8 kilobytes. These characteristics can be overridden, or explicitly specified with the options described below.

## OPTIONS

|  |  **− b** |  |  Save the image as a greyscale image as if it were processed by _tiff2bw_(1). This option is included for compatibility with the standard _scrsave_(6D) program. |  |  |  **− c** |  |  Specify the compression to use for data written to the output file: **none** for no compression, **packbits** for PackBits compression, **jpeg** for baseline JPEG compression, **zip** for Deflate compression, and **lzw** for Lempel-Ziv & Welch compression (default). |  |  |  LZW compression can be specified together with a _predictor_ value. A predictor value of 2 causes each scanline of the output image to undergo horizontal differencing before it is encoded; a value of 1 forces each scanline to be encoded without differencing. LZW-specific options are specified by appending a '':''-separated list to the ''lzw'' option; e.g. **− c lzw:2** for LZW compression with horizontal differencing. |  |  **− p** |  |  Specify the planar configuration to use in writing image data. By default, _tiffsv_ will create a new file with the data samples packed contiguously. Specifying **− p contig** will force data to be written with multi-sample data packed together, while **− p separate** will force samples to be written in separate planes. |  |  |  **− r** |  |  Specify the number of rows (scanlines) in each strip of data written to the output file. By default, _tiffsv_ attempts to set the rows/strip that no more than 8 kilobytes of data appear in a strip. | 

## NOTE

|  |  Except for the use of TIFF, this program is equivalent to the standard _scrsave_ program. This means, for example, that you can use it in conjunction with the standard _icut_ program simply by creating a link called _scrsave_ , or by creating a shell script called _scrsave_ that invokes _tiffgt_ with the appropriate options.

## BUGS

|  |  If data are saved compressed and in separate planes, then the rows in each strip is silently set to one to avoid limitations in the **libtiff**(3TIFF) library.

## SEE ALSO

|  |  **scrsave**(6D) **pal2rgb**(1), **tiffdump**(1), **tiffgt**(1), **tiffinfo**(1), **tiffcp**(1), **tiffmedian**(1), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
