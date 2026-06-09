# SWAB

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFGetBitRevTable, TIFFReverseBits, TIFFSwabShort, TIFFSwabLong, TIFFSwabArrayOfShort, TIFFSwabArrayOfLong − byte- and bit-swapping routines

## SYNOPSIS

|  |  **#include <tiffio.h>** **const unsigned char* TIFFGetBitRevTable(int** _reversed_**)  
void TIFFReverseBits(u_char ***_data_**, unsigned long** _nbytes_**)  
void TIFFSwabShort(uint16 ***_data_**)  
void TIFFSwabLong(uint32 ***_data_**)  
void TIFFSwabArrayOfShort(uint16 ***_data_**, unsigned long** _nshorts_**)  
void TIFFSwabArrayOfLong(uint32 ***_data_**, unsigned long** _nlongs_**)**

## DESCRIPTION

|  |  The following routines are used by the library to swap 16- and 32-bit data and to reverse the order of bits in bytes. _TIFFSwabShort_ and _TIFFSwabLong_ swap the bytes in a single 16-bit and 32-bit item, respectively. _TIFFSwabArrayOfShort_ and _TIFFSwabArrayOfLong_ swap the bytes in an array of 16-bit and 32-bit items, respectively. _TIFFReverseBits_ replaces each byte in _data_ with the equivalent bit-reversed value. This operation is performed with a lookup table, which is returned using the _TIFFGetBitRevTable_ function. _reversed_ parameter specifies which table should be returned. Supply _1_ if you want bit reversal table. Supply _0_ to get the table that do not reverse bit values. It is a lookup table that can be used as an _identity function_ ; i.e. _TIFFNoBitRevTable[n] == n_.

## DIAGNOSTICS

|  |  None.

## SEE ALSO

|  |  **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
