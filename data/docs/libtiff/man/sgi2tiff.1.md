# SGI2TIFF

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
BUGS  
SEE ALSO  


* * *

## NAME

|  |  sgi2tiff − create a TIFF file from an SGI image file

## SYNOPSIS

|  |  **sgi2tiff** [ _options_ ] _input.rgb output.tif_

## DESCRIPTION

|  |  _sgi2tiff_ converts a file in the SGI image format to TIFF. By default, the TIFF image is created with data samples packed (_PlanarConfiguration_ =1), compressed with the Lempel-Ziv & Welch algorithm (_Compression_ =5), and with each strip no more than 8 kilobytes. These characteristics can overridden, or explicitly specified with the options described below.

## OPTIONS

|  |  **− c** |  |  Specify a compression scheme to use when writing image data: **− c none** for no compression, **− c packbits** for the PackBits compression algorithm), **− c jpeg** for the baseline JPEG compression algorithm, **− c zip** for the Deflate compression algorithm, and **− c lzw** for Lempel-Ziv & Welch (the default). |  |  |  **− p** |  |  Explicitly select the planar configuration used in organizing data samples in the output image: **− p contig** for samples packed contiguously, and **− p separate** for samples stored separately. By default samples are packed. |  |  |  **− r** |  |  Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes. | 

## BUGS

|  |  Does not record colormap information.

## SEE ALSO

|  |  **tiffinfo**(1), **tiffcp**(1), **tiffmedian**(1), **libtiff**(3) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
