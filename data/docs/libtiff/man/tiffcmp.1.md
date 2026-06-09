# TIFFCMP

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
BUGS  
SEE ALSO  


* * *

## NAME

|  |  tiffcmp − compare two TIFF files

## SYNOPSIS

|  |  **tiffcmp** [ _options_ ] _file1.tif file2.tif_

## DESCRIPTION

|  |  _Tiffcmp_ compares the tags and data in two files created according to the Tagged Image File Format, Revision 6.0. The schemes used for compressing data in each file are immaterial when data are compared−data are compared on a scanline-by-scanline basis after decompression. Most directory tags are checked; notable exceptions are: _GrayResponseCurve_ , _ColorResponseCurve_ , and _ColorMap_ tags. Data will not be compared if any of the _BitsPerSample_ , _SamplesPerPixel_ , or _ImageWidth_ values are not equal. By default, _tiffcmp_ will terminate if it encounters any difference.

## OPTIONS

|  |  **− l** |  |  List each byte of image data that differs between the files. |  |  |  **− z** _number_ |  |  List specified number of image data bytes that differs between the files. |  |  **− t** |  |  Ignore any differences in directory tags. | 

## BUGS

|  |  Tags that are not recognized by the library are not compared; they may also generate spurious diagnostics. The image data of tiled files is not compared, since the _TIFFReadScanline()_ function is used. An error will be reported for tiled files. The pixel and/or sample number reported in differences may be off in some exotic cases.

## SEE ALSO

|  |  **pal2rgb**(1), **tiffcp**(1), **tiffmedian**(1), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
