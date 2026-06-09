# TIFFPrintDirectory

NAME  
SYNOPSIS  
DESCRIPTION  
NOTES  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFPrintDirectory − print a description of a TIFF directory

## SYNOPSIS

|  |  **#include <tiffio.h>** **void TIFFPrintDirectory(TIFF ***_tif_**, FILE ***_fd_**, long** _flags_**)**

## DESCRIPTION

|  |  _TIFFPrintDirectory_ prints a description of the current directory in the specified TIFF file to the standard I/O output stream _fd_. The _flags_ parameter is used to control the _level of detail_ of the printed information; it is a bit-or of the flags defined in **tiffio.h** : #define TIFFPRINT_NONE 0x0 /* no extra info */ |  |  #define |  TIFFPRINT_STRIPS |  0x1 |  /* strips/tiles info */ |  |  #define |  TIFFPRINT_CURVES |  0x2 |  /* color/gray response curves */ |  |  #define |  TIFFPRINT_COLORMAP |  0x4 |  /* colormap */ |  |  #define |  TIFFPRINT_JPEGQTABLES |  0x100 |  /* JPEG Q matrices */ |  |  #define |  TIFFPRINT_JPEGACTABLES |  0x200 |  /* JPEG AC tables */ |  |  #define |  TIFFPRINT_JPEGDCTABLES |  0x200 |  /* JPEG DC tables */

## NOTES

|  |  In C++ the _flags_ parameter defaults to 0.

## RETURN VALUES

|  |  None.

## DIAGNOSTICS

|  |  None.

## SEE ALSO

|  |  _libtiff_(3TIFF), _TIFFOpen_(3TIFF), _TIFFReadDirectory_(3TIFF), _TIFFSetDirectory_(3TIFF)

* * *
