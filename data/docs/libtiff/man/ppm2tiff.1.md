# PPM2TIFF

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
SEE ALSO  


* * *

## NAME

|  |  ppm2tiff − create a TIFF file from PPM, PGM and PBM image files

## SYNOPSIS

|  |  **ppm2tiff** [ _options_ ] [ _input.ppm_ ] _output.tif_

## DESCRIPTION

|  |  _ppm2tiff_ converts a file in the PPM, PGM and PBM image formats to TIFF. By default, the TIFF image is created with data samples packed (_PlanarConfiguration_ =1), compressed with the Packbits algorithm (_Compression_ =32773), and with each strip no more than 8 kilobytes. These characteristics can be overridden, or explicitly specified with the options described below If the PPM file contains greyscale data, then the _PhotometricInterpretation_ tag is set to 1 (min-is-black), otherwise it is set to 2 (RGB). If no PPM file is specified on the command line, _ppm2tiff_ will read from the standard input.

## OPTIONS

|  |  **− c** |  |  Specify a compression scheme to use when writing image data: **none** for no compression, **packbits** for PackBits compression (will be used by default), **lzw** for Lempel-Ziv & Welch compression, **jpeg** for baseline JPEG compression, **zip** for Deflate compression, **g3** for CCITT Group 3 (T.4) compression, and **g4** for CCITT Group 4 (T.6) compression. |  |  |  **− r** |  |  Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes. |  |  |  **− R** |  |  Mark the resultant image to have the specified X and Y resolution (in dots/inch). | 

## SEE ALSO

|  |  **tiffinfo**(1), **tiffcp**(1), **tiffmedian**(1), **libtiff**(3) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
