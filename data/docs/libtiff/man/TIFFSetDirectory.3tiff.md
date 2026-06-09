# TIFFSetDirectory

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFSetDirectory, TIFFSetSubDirectory − set the current directory for an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFSetDirectory(TIFF ***_tif_**, tdir_t** _dirnum_**)  
int TIFFSetSubDirectory(TIFF ***_tif_**, uint32** _diroff_**)**

## DESCRIPTION

|  |  _TIFFSetDirectory_ changes the current directory and reads its contents with _TIFFReadDirectory_. The parameter _dirnum_ specifies the subfile/directory as an integer number, with the first directory numbered zero. _TIFFSetSubDirectory_ acts like _TIFFSetDirectory_ , except the directory is specified as a file offset instead of an index; this is required for accessing subdirectories linked through a _SubIFD_ tag.

## RETURN VALUES

|  |  On successful return 1 is returned. Otherwise, 0 is returned if _dirnum_ or _diroff_ specifies a non-existent directory, or if an error was encountered while reading the directory's contents.

## DIAGNOSTICS

|  |  All error messages are directed to the _TIFFError_(3TIFF) routine. **%s: Error fetching directory count**. An error was encountered while reading the ''directory count'' field. **%s: Error fetching directory link**. An error was encountered while reading the ''link value'' that points to the next directory in a file.

## SEE ALSO

|  |  _TIFFCurrentDirectory_(3TIFF), _TIFFOpen_(3TIFF), _TIFFReadDirectory_(3TIFF), _TIFFWriteDirectory_(3TIFF), _libtiff_(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
