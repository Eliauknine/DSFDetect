# MEMORY

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  _TIFFmalloc, _TIFFrealloc, _TIFFfree, _TIFFmemset, _TIFFmemcpy, _TIFFmemcmp, − memory management-related functions for use with TIFF files

## SYNOPSIS

|  |  **#include <tiffio.h>** **tdata_t _TIFFmalloc(tsize_t** _size_**);  
tdata_t _TIFFrealloc(tdata_t** _buffer_**, tsize_t** _size_**);  
void _TIFFfree(tdata_t** _buffer_**);  
void _TIFFmemset(tdata_t** _s_**, int** _c_**, tsize_t** _n_**);  
void _TIFFmemcpy(tdata_t** _dest_**, const tdata_t** _src_**, tsize_t** _n_**);  
int _TIFFmemcmp(const tdata_t** _s1_**, const tdata_t** _s2_**, tsize_t** _n_**);**

## DESCRIPTION

|  |  These routines are provided for writing portable software that uses _libtiff_ ; they hide any memory-management related issues, such as dealing with segmented architectures found on 16-bit machines. __TIFFmalloc_ and __TIFFrealloc_ are used to dynamically allocate and reallocate memory used by _libtiff_ ; such as memory passed into the I/O routines. Memory allocated through these interfaces is released back to the system using the __TIFFfree_ routine. Memory allocated through one of the above interfaces can be set to a known value using __TIFFmemset_ , copied to another memory location using __TIFFmemcpy_ , or compared for equality using __TIFFmemcmp_. These routines conform to the equivalent ANSI C routines: _memset_ , _memcpy_ , and _memcmp_ , repsectively.

## DIAGNOSTICS

|  |  None.

## SEE ALSO

|  |  **malloc**(3), **memory**(3), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
