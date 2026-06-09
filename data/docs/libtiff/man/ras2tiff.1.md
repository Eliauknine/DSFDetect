# RAS2TIFF

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
BUGS  
SEE ALSO  


* * *

## NAME

|  |  ras2tiff − create a TIFF file from a Sun rasterfile

## SYNOPSIS

|  |  **ras2tiff** [ _options_ ] _input.ras output.tif_

## DESCRIPTION

|  |  _ras2tiff_ converts a file in the Sun rasterfile format to TIFF. By default, the TIFF image is created with data samples packed (_PlanarConfiguration_ =1), compressed with the Lempel-Ziv & Welch algorithm (_Compression_ =5), and with each strip no more than 8 kilobytes. These characteristics can overridden, or explicitly specified with the options described below. Any colormap information in the rasterfile is carried over to the TIFF file by including a _Colormap_ tag in the output file. If the rasterfile has a colormap, the _PhotometricInterpretation_ tag is set to 3 (palette); otherwise it is set to 2 (RGB) if the depth is 24 or 1 (min-is-black) if the depth is not 24.

## OPTIONS

|  |  **− c** |  |  Specify a compression scheme to use when writing image data: **− c none** for no compression, **− c packbits** for the PackBits compression algorithm, **− c jpeg** for the baseline JPEG compression algorithm, **− c zip** for the Deflate compression algorithm, and **− c lzw** for Lempel-Ziv & Welch (the default). |  |  |  **− r** |  |  Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes. | 

## BUGS

|  |  Does not handle all possible rasterfiles. In particular, _ras2tiff_ does not handle run-length encoded images.

## SEE ALSO

|  |  **pal2rgb**(1), **tiffinfo**(1), **tiffcp**(1), **tiffmedian**(1), **libtiff**(3) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
