# TIFFSET

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
EXAMPLES  
SEE ALSO  


* * *

## NAME

|  |  tiffset − set a field in a TIFF header

## SYNOPSIS

|  |  **tiffset** [ _options_ ] _filename.tif_

## DESCRIPTION

|  |  _Tiffset_ sets the value of a TIFF header to a specified value.

## OPTIONS

|  |  **− s** _tagnumber_ [ _count_ ] _value ..._ |  |  Set the value of the named tag to the value or values specified. |  |  **− sf** _tagnumber filename_ |  |  Set the value of the tag to the contents of filename. This option is supported for ASCII tags only.

## EXAMPLES

|  |  The following example sets the image description tag (270) of a.tif to the contents of the file descrip: |  | 
    
    
    tiffset −sf 270 descrip a.tif
    

|  |  The following example sets the artist tag (315) of a.tif to the string ''Anonymous'': |  | 
    
    
    tiffset −s 305 Anonymous a.tif
    

|  |  This example sets the resolution of the file a.tif to 300 dpi: |  | 
    
    
    tiffset −s 296 2 a.tif
    tiffset −s 282 300.0 a.tif
    tiffset −s 283 300.0 a.tif
    

## SEE ALSO

|  |  **tiffdump**(1), **tiffinfo**(1), **tiffcp**(1), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
