#  ![](images/smallliz.jpg) Contributed TIFF Software 

The **contrib** directory has contributed software that uses the TIFF library or which is associated with the library (typically glue and guidance for ports to non-UNIX platforms, or tools that aren't directly TIFF related).   


**contrib/vms** |  scripts and files from Karsten Spang for building the library and tools under VMS   
---|---  
**contrib/dbs** |  various tools from Dan & Chris Sears, including a simple X-based viewer   
**contrib/ras** |  two programs by Patrick Naughton for converting between Sun rasterfile format and TIFF (these require `libpixrect.a`, as opposed to the one in tools that doesn't)   
**contrib/mac-mpw**  
**contrib/mac-cw** |  scripts and files from Niles Ritter for building the library and tools under Macintosh/MPW C and code warrior.   
**contrib/acorn** |  scripts and files from Peter Greenham for building the library and tools on an Acorn RISC OS system.   
**contrib/win32** |  scripts and files from Scott Wagner for building the library under Windows NT and Windows 95. (The makefile.vc in the libtiff/libtiff directory may be sufficient for most users.)   
**contrib/win_dib** |  two separate implementations of TIFF to DIB code suitable for any Win32 platform. Contributed by Mark James, and Philippe Tenenhaus.   
**contrib/ojpeg** |  Patch for IJG JPEG library related to support for some Old JPEG in TIFF files. Contributed by Scott Marovich.   
**contrib/dosdjgpp** |  scripts and files from Alexander Lehmann for building the library under MSDOS with the DJGPP v2 compiler.   
**contrib/tags** |  scripts and files from Niles Ritter for adding private tag support at runtime, without changing libtiff.   
**contrib/mfs** |  code from Mike Johnson to read+write images in memory without modifying the library   
**contrib/pds** |  various routines from Conrad Poelman; a TIFF image iterator and code to support ``private sub-directories''   
**contrib/iptcutil** |  A utility by [Bill Radcliffe](mailto:billr@corbis.com) to convert an extracted IPTC Newsphoto caption from a binary blob to ASCII text, and vice versa. IPTC binary blobs can be extracted from images via the [ImageMagick](http://www.ImageMagick.org/) convert(1) utility.   
**contrib/addtiffo** |  A utility (and supporting subroutine) for building one or more reduce resolution overviews to an existing TIFF file. Supplied by [Frank Warmerdam](http://pobox.com/~warmerdam).   
**contrib/stream** |  A class (TiffStream) for accessing TIFF files through a C++ stream interface. Supplied by [Avi Bleiweiss](mailto:avi@shutterfly.com).   
  
Questions regarding these packages are usually best directed toward their authors. 

* * *

Last updated: $Date$ 
