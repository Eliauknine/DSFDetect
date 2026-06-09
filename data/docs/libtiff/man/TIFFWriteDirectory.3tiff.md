# TIFFWriteDirectory

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFWriteDirectory, TIFFRewriteDirectory, TIFFCheckpointDirectory − write the current directory in an open TIFF file

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFWriteDirectory(TIFF ***_tif_**)  
int TIFFRewriteDirectory(TIFF ***_tif_**)  
int TIFFCheckpointDirectory(TIFF ***_tif_**)**

## DESCRIPTION

|  |  _TIFFWriteDirectory_ will write the contents of the current directory to the file and setup to create a new subfile in the same file. Applications only need to call _TIFFWriteDirectory_ when writing multiple subfiles to a single TIFF file. _TIFFWriteDirectory_ is automatically called by _TIFFClose_ and _TIFFFlush_ to write a modified directory if the file is open for writing. The _TIFFRewriteDirectory_ function operates similarly to _TIFFWriteDirectory,_ but can be called with directories previously read or written that already have an established location in the file. It will rewrite the directory, but instead of place it at it's old location (as _TIFFWriteDirectory_ would) it will place them at the end of the file, correcting the pointer from the preceeding directory or file header to point to it's new location. This is particularly important in cases where the size of the directory and pointed to data has grown, so it won't fit in the space available at the old location. The _TIFFCheckpointDirectory_ writes the current state of the tiff directory into the file to make what is currently in the file readable. Unlike _TIFFWriteDirectory, TIFFCheckpointDirectory_ does not free up the directory data structures in memory, so they can be updated (as strips/tiles are written) and written again. Reading such a partial file you will at worst get a tiff read error for the first strip/tile encountered that is incomplete, but you will at least get all the valid data in the file before that. When the file is complete, just use _TIFFWriteDirectory_ as usual to finish it off cleanly.

## RETURN VALUES

|  |  1 is returned when the contents are successfully written to the file. Otherwise, 0 is returned if an error was encountered when writing the directory contents.

## DIAGNOSTICS

|  |  All error messages are directed to the _TIFFError_(3TIFF) routine. **Error post-encoding before directory write**. Before writing the contents of the current directory, any pending data are flushed. This message indicates that an error occurred while doing this. **Error flushing data before directory write**. Before writing the contents of the current directory, any pending data are flushed. This message indicates that an error occurred while doing this. **Cannot write directory, out of space**. There was not enough space to allocate a temporary area for the directory that was to be written. **Error writing directory count**. A write error occurred when writing the count of fields in the directory. **Error writing directory contents**. A write error occurred when writing the directory fields. **Error writing directory link**. A write error occurred when writing the link to the next directory. **Error writing data for field "%s"**. A write error occurred when writing indirect data for the specified field. **Error writing TIFF header**. A write error occurred when re-writing header at the front of the file. **Error fetching directory count**. A read error occurred when fetching the directory count field for a previous directory. This can occur when setting up a link to the directory that is being written. **Error fetching directory link**. A read error occurred when fetching the directory link field for a previous directory. This can occur when setting up a link to the directory that is being written.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFError**(3TIFF), **TIFFReadDirectory**(3TIFF), **TIFFSetDirectory**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
