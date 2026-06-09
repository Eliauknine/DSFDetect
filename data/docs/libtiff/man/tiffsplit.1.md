# TIFFSPLIT

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
BUGS  
SEE ALSO  


* * *

## NAME

|  |  tiffsplit − split a multi-image TIFF into single-image TIFF files

## SYNOPSIS

|  |  **tiffsplit** _src.tif_ [ _prefix_ ]

## DESCRIPTION

|  |  _tiffsplit_ takes a multi-directory (page) TIFF file and creates one or more single-directory (page) TIFF files from it. The output files are given names created by concatenating a prefix, a lexically ordered suffix in the range [_aaa_ -_zzz_], the suffix _.tif_ (e.g. _xaaa.tif_ , _xaab.tif_ , _xzzz.tif_). If a prefix is not specified on the command line, the default prefix of _x_ is used.

## OPTIONS

|  |  None.

## BUGS

|  |  Only a select set of ''known tags'' is copied when splitting.

## SEE ALSO

|  |  **tiffcp**(1), **tiffinfo**(1), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
