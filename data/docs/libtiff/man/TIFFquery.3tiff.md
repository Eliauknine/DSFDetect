# QUERY

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFCurrentRow, TIFFCurrentStrip, TIFFCurrentTile, TIFFCurrentDirectory, TIFFLastDirectory, TIFFFileno, TIFFFileName, TIFFGetMode, TIFFIsTiled, TIFFIsByteSwapped, TIFFIsUpSampled, TIFFIsMSB2LSB, TIFFGetVersion − query routines

## SYNOPSIS

|  |  **#include <tiffio.h>** **uint32 TIFFCurrentRow(TIFF*** _tif_**)  
tstrip_t TIFFCurrentStrip(TIFF*** _tif_**)  
ttile_t TIFFCurrentTile(TIFF*** _tif_**)  
tdir_t TIFFCurrentDirectory(TIFF*** _tif_**)  
int TIFFLastDirectory(TIFF*** _tif_**)  
int TIFFFileno(TIFF*** _tif_**)  
char* TIFFFileName(TIFF*** _tif_**)  
int TIFFGetMode(TIFF*** _tif_**)  
int TIFFIsTiled(TIFF*** _tif_**)  
int TIFFIsByteSwapped(TIFF*** _tif_**)  
int TIFFIsUpSampled(TIFF*** _tif_**)  
int TIFFIsMSB2LSB(TIFF*** _tif_**)  
const char* TIFFGetVersion(void)**

## DESCRIPTION

|  |  The following routines return status information about an open TIFF file. _TIFFCurrentDirectory_ returns the index of the current directory (directories are numbered starting at 0). This number is suitable for use with the _TIFFSetDirectory_ routine. _TIFFLastDirectory_ returns a non-zero value if the current directory is the last directory in the file; otherwise zero is returned. _TIFFCurrentRow_ , _TIFFCurrentStrip_ , and _TIFFCurrentTile_ , return the current row, strip, and tile, respectively, that is being read or written. These values are updated each time a read or write is done. _TIFFFileno_ returns the underlying file descriptor used to access the TIFF image in the filesystem. _TIFFFileName_ returns the pathname argument passed to _TIFFOpen_ or _TIFFFdOpen_. _TIFFGetMode_ returns the mode with which the underlying file was opened. On UNIX systems, this is the value passed to the _open_(2) system call. _TIFFIsTiled_ returns a non-zero value if the image data has a tiled organization. Zero is returned if the image data is organized in strips. _TIFFIsByteSwapped_ returns a non-zero value if the image data was in a different byte-order than the host machine. Zero is returned if the TIFF file and local host byte-orders are the same. Note that TIFFReadTile(), TIFFReadStrip() and TIFFReadScanline() functions already normally perform byte swapping to local host order if needed. _TIFFIsUpSampled_ returns a non-zero value if image data returned through the read interface routines is being up-sampled. This can be useful to applications that want to calculate I/O buffer sizes to reflect this usage (though the usual strip and tile size routines already do this). _TIFFIsMSB2LSB_ returns a non-zero value if the image data is being returned with bit 0 as the most significant bit. _TIFFGetVersion_ returns an ASCII string that has a version stamp for the TIFF library software.

## DIAGNOSTICS

|  |  None.

## SEE ALSO

|  |  _libtiff_(3TIFF), _TIFFOpen_(3TIFF), _TIFFFdOpen_(3TIFF)

* * *
