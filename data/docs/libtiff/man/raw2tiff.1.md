# RAW2TIFF

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
GUESSING THE IMAGE GEOMETRY  
SEE ALSO  


* * *

## NAME

|  |  raw2tiff − create a TIFF file from a raw data

## SYNOPSIS

|  |  **raw2tiff** [ _options_ ] _input.raw output.tif_

## DESCRIPTION

|  |  _raw2tiff_ converts a raw byte sequence into TIFF. By default, the TIFF image is created with data samples packed (_PlanarConfiguration_ =1), compressed with the PackBits algorithm (_Compression_ =32773), and with each strip no more than 8 kilobytes. These characteristics can overridden, or explicitly specified with the options described below.

## OPTIONS

|  |  **− H** _number_ |  |  size of input image file header in bytes (0 by default). This amount of data just will be skipped from the start of file while reading. |  |  **− w** _number_ |  |  width of input image in pixels (can be guessed, see **GUESSING THE IMAGE GEOMETRY** below). |  |  **− l** _number_ |  |  length of input image in lines (can be guessed, see **GUESSING THE IMAGE GEOMETRY** below). |  |  **− b** _number_ |  |  number of bands in input image (1 by default). |  |  **− d** _data_type_ |  |  type of samples in input image, where _data_type_ may be: |  |  **byte** |  8-bit unsigned integer (default), |  |  **short** |  16-bit unsigned integer, |  |  **long** |  32-bit unsigned integer, |  |  **sbyte** |  8-bit signed integer, |  |  **sshort** |  16-bit signed integer, |  |  **slong** |  32-bit signed integer, |  |  **float** |  32-bit IEEE floating point, |  |  **double** |  64-bit IEEE floating point. |  |  **− i** _config_ |  |  type of samples interleaving in input image, where _config_ may be: |  |  **pixel** |  pixel interleaved data (default), |  |  **band** |  band interleaved data. |  |  **− p** _photo_ |  |  photometric interpretation (color space) of the input image, where _photo_ may be: |  |  **miniswhite** |  white color represented with 0 value, |  |  **minisblack** |  black color represented with 0 value (default), |  |  **rgb** |  image has RGB color model, |  |  **cmyk** |  image has CMYK (separated) color model, |  |  **ycbcr** |  image has YCbCr color model, |  |  **cielab** |  image has CIE L*a*b color model, |  |  **icclab** |  image has ICC L*a*b color model, |  |  **itulab** |  image has ITU L*a*b color model. |  |  **− s** |  |  swap bytes fetched from the input file. |  |  |  **− L** |  |  input data has LSB2MSB bit order (default). |  |  |  **− M** |  |  input data has MSB2LSB bit order. |  |  |  **− c** |  |  Specify a compression scheme to use when writing image data: **− c none** for no compression, **− c packbits** for the PackBits compression algorithm (the default), **− c jpeg** for the baseline JPEG compression algorithm, **− c zip** for the Deflate compression algorithm, and **− c lzw** for Lempel-Ziv & Welch. |  |  |  **− r** _number_ |  |  Write data with a specified number of rows per strip; by default the number of rows/strip is selected so that each strip is approximately 8 kilobytes.

## GUESSING THE IMAGE GEOMETRY

|  |  _raw2tiff_ can guess image width and height in case one or both of these parameters are not specified. If you omit one of those parameters, the complementary one will be calculated based on the file size (taking into account header size, number of bands and data type). If you omit both parameters, the statistical approach will be used. Utility will compute correlation coefficient between two lines at the image center using several appropriate line sizes and the highest absolute value of the coefficient will indicate the right line size. That is why you should be cautious with the very large images, because guessing process may take a while (depending on your system performance). Of course, the utility can't guess the header size, number of bands and data type, so it should be specified manually. If you don't know anything about your image, just try with the several combinations of those options. There is no magic, it is just a mathematical statistics, so it can be wrong in some cases. But for most ordinary images guessing method will work fine.

## SEE ALSO

|  |  **pal2rgb**(1), **tiffcp**(1), **tiffmedian**(1), **libtiff**(3) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
