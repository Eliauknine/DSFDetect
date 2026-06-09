# BMP2TIFF

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
SEE ALSO  


* * *

## NAME

|  |  bmp2tiff − create a TIFF file from a Microsoft Windows Device Independent Bitmap image file

## SYNOPSIS

|  |  **bmp2tiff** [ _options_ ] _input.bmp output.tiff_

## DESCRIPTION

|  |  _bmp2tiff_ converts a Microsoft Windows Device Independent Bitmap image file to TIFF. By default, the TIFF image is created with data samples packed (_PlanarConfiguration_ =1), compressed with the PackBits algorithm (_Compression_ =_32773),_ and with each strip no more than 8 kilobytes. These characteristics can overridden, or explicitly specified with the options described below.

## OPTIONS

|  |  **− c** |  |  Specify a compression scheme to use when writing image data: **− c none** for no compression, **-c packbits** for the PackBits compression algorithm (the default), **-c jpeg** for the baseline JPEG compression algorithm, **-c zip** for the Deflate compression algorithm, and **− c lzw** for Lempel-Ziv & Welch. |  |  |  **− r <number>** |  |  Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.

## SEE ALSO

|  |  _gif2tiff_(1), _pal2rgb_(1), _ppm2tiff_(1), _raw2tiff_(1), _ras2tiff_(1), _sgi2tiff_(1), _libtiff_(3TIFF)

* * *
