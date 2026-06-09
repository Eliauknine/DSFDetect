# TIFFMEDIAN

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
NOTES  
SEE ALSO  


* * *

## NAME

|  |  tiffmedian − apply the median cut algorithm to data in a TIFF file

## SYNOPSIS

|  |  **tiffmedian** [ _options_ ] _input.tif output.tif_

## DESCRIPTION

|  |  _tiffmedian_ applies the median cut algorithm to an RGB image in _input.tif_ to generate a palette image that is written to _output.tif_. The generated colormap has, by default, 256 entries. The image data is quantized by mapping each pixel to the closest color values in the colormap.

## OPTIONS

|  |  **− c** |  |  Specify the compression to use for data written to the output file: **none** for no compression, **packbits** for PackBits compression, **lzw** for Lempel-Ziv & Welch compression, and **zip** for Deflate compression. By default _tiffmedian_ will compress data according to the value of the _Compression_ tag found in the source file. |  |  |  LZW compression can be specified together with a _predictor_ value. A predictor value of 2 causes each scanline of the output image to undergo horizontal differencing before it is encoded; a value of 1 forces each scanline to be encoded without differencing. LZW-specific options are specified by appending a '':''-separated list to the ''lzw'' option; e.g. **− c lzw:2** for LZW compression with horizontal differencing. |  |  **− C** |  |  Specify the number of entries to use in the generated colormap. By default all 256 entries/colors are used. |  |  |  **− f** |  |  Apply Floyd-Steinberg dithering before selecting a colormap entry. |  |  |  **− r** |  |  Specify the number of rows (scanlines) in each strip of data written to the output file. By default, _tiffmedian_ attempts to set the rows/strip that no more than 8 kilobytes of data appear in a strip. | 

## NOTES

|  |  This program is derived from Paul Heckbert's _median_ program.

## SEE ALSO

|  |  **pal2rgb**(1), **tiffinfo**(1), **tiffcp**(1), **tiffcmp**(1), **libtiff**(3TIFF) **Color Image Quantization for Frame Buffer Display** , Paul Heckbert, SIGGRAPH proceedings, 1982, pp. 297-307. Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
