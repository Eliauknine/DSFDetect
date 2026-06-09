# TIFFDataWidth

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
SEE ALSO  


* * *

## NAME

|  |  TIFFDataWidth − Get the size of TIFF data types

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFDataWidth(TIFFDataType** _type_**)**

## DESCRIPTION

|  |  _TIFFDataWidth_ returns a size of _type_ in bytes. Currently following data types are supported:_  
TIFF_BYTE  
TIFF_ASCII  
TIFF_SBYTE  
TIFF_UNDEFINED  
TIFF_SHORT  
TIFF_SSHORT  
TIFF_LONG  
TIFF_SLONG  
TIFF_FLOAT  
TIFF_IFD  
TIFF_RATIONAL  
TIFF_SRATIONAL  
TIFF_DOUBLE_

## RETURN VALUES

|  |  _TIFFDataWidth_ returns a number of bytes occupied by the item of given type. 0 returned when uknown data type supplied.

## SEE ALSO

|  |  **libtiff**(3TIFF), Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
