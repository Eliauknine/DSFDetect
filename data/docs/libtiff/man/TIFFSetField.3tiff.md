# TIFFSetField

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFSetField, TIFFVSetField − set the value(s) of a tag in a TIFF file open for writing

## SYNOPSIS

|  |  **#include <tiffio.h>** **int TIFFSetField(TIFF ***_tif_**, ttag_t** _tag_**,** _..._**)** **#include <stdarg.h>** **int TIFFVSetField(TIFF ***_tif_**, ttag_t** _tag_**, va_list** _ap_**)**

## DESCRIPTION

|  |  _TIFFSetField_ sets the value of a field or pseudo-tag in the current directory associated with the open TIFF file _tif_. (A _pseudo-tag_ is a parameter that is used to control the operation of the TIFF library but whose value is not read or written to the underlying file.) To set the value of a field the file must have been previously opened for writing with _TIFFOpen_(3TIFF); pseudo-tags can be set whether the file was opened for reading or writing. The field is identified by _tag_ , one of the values defined in the include file **tiff.h** (see also the table below). The actual value is specified using a variable argument list, as prescribed by the _stdarg_(3) interface (or, on some machines, the _varargs_(3) interface.) _TIFFVSetField_ is functionally equivalent to _TIFFSetField_ except that it takes a pointer to a variable argument list. _TIFFVSetField_ is useful for writing routines that are layered on top of the functionality provided by _TIFFSetField_. The tags understood by _libtiff_ , the number of parameter values, and the expected types for the parameter values are shown below. The data types are: _char*_ is null-terminated string and corresponds to the ASCII data type; _uint16_ is an unsigned 16-bit value; _uint32_ is an unsigned 32-bit value; _uint16*_ is an array of unsigned 16-bit values. _void*_ is an array of data values of unspecified type. Consult the TIFF specification for information on the meaning of each tag. _Tag Name Count Types Notes_ |  |  TIFFTAG_ARTIST |  1 |  char* |  |  |  TIFFTAG_BADFAXLINES |  1 |  uint32 |  |  |  TIFFTAG_BITSPERSAMPLE |  1 |  uint16 |  † |  |  TIFFTAG_CLEANFAXDATA |  1 |  uint16 |  |  |  TIFFTAG_COLORMAP |  3 |  uint16* |  1<<BitsPerSample arrays |  |  TIFFTAG_COMPRESSION |  1 |  uint16 |  † |  |  TIFFTAG_CONSECUTIVEBADFAXLINES |  1 |  uint32 |  |  |  TIFFTAG_COPYRIGHT |  1 |  char* |  |  |  TIFFTAG_DATETIME |  1 |  char* |  |  |  TIFFTAG_DOCUMENTNAME |  1 |  char* |  |  |  TIFFTAG_DOTRANGE |  2 |  uint16 |  |  |  TIFFTAG_EXTRASAMPLES |  2 |  uint16,uint16* |  † count & types array |  |  TIFFTAG_FAXFILLFUNC |  1 |  TIFFFaxFillFunc |  G3/G4 compression pseudo-tag |  |  TIFFTAG_FAXMODE |  1 |  int |  † G3/G4 compression pseudo-tag |  |  TIFFTAG_FILLORDER |  1 |  uint16 |  † |  |  TIFFTAG_GROUP3OPTIONS |  1 |  uint32 |  † |  |  TIFFTAG_GROUP4OPTIONS |  1 |  uint32 |  † |  |  TIFFTAG_HALFTONEHINTS |  2 |  uint16 |  |  |  TIFFTAG_HOSTCOMPUTER |  1 |  char* |  |  |  TIFFTAG_ICCPROFILE |  2 |  uint32,void* |  count, profile data |  |  TIFFTAG_IMAGEDEPTH |  1 |  uint32 |  † |  |  TIFFTAG_IMAGEDESCRIPTION |  1 |  char* |  |  |  TIFFTAG_IMAGELENGTH |  1 |  uint32 |  |  |  TIFFTAG_IMAGEWIDTH |  1 |  uint32 |  † |  |  TIFFTAG_INKNAMES |  2 |  uint16, char* |  |  |  TIFFTAG_INKSET |  1 |  uint16 |  † |  |  TIFFTAG_JPEGCOLORMODE |  1 |  int |  † JPEG pseudo-tag |  |  TIFFTAG_JPEGQUALITY |  1 |  int |  JPEG pseudo-tag |  |  TIFFTAG_JPEGTABLES |  2 |  uint32*,void* |  † count & tables |  |  TIFFTAG_JPEGTABLESMODE |  1 |  int |  † JPEG pseudo-tag |  |  TIFFTAG_MAKE |  1 |  char* |  |  |  TIFFTAG_MATTEING |  1 |  uint16 |  † |  |  TIFFTAG_MAXSAMPLEVALUE |  1 |  uint16 |  |  |  TIFFTAG_MINSAMPLEVALUE |  1 |  uint16 |  |  |  TIFFTAG_MODEL |  1 |  char* |  |  |  TIFFTAG_ORIENTATION |  1 |  uint16 |  |  |  TIFFTAG_PAGENAME |  1 |  char* |  |  |  TIFFTAG_PAGENUMBER |  2 |  uint16 |  |  |  TIFFTAG_PHOTOMETRIC |  1 |  uint16 |  |  |  TIFFTAG_PHOTOSHOP |  ? |  uint32,void* |  count, data |  |  TIFFTAG_PLANARCONFIG |  1 |  uint16 |  † |  |  TIFFTAG_PREDICTOR |  1 |  uint16 |  † |  |  TIFFTAG_PRIMARYCHROMATICITIES |  1 |  float* |  6-entry array |  |  TIFFTAG_REFERENCEBLACKWHITE |  1 |  float* |  † 2*SamplesPerPixel array |  |  TIFFTAG_RESOLUTIONUNIT |  1 |  uint16 |  |  |  TIFFTAG_RICHTIFFIPTC |  2 |  uint32,void* |  count, data |  |  TIFFTAG_ROWSPERSTRIP |  1 |  uint32 |  † must be > 0 |  |  TIFFTAG_SAMPLEFORMAT |  1 |  uint16 |  † |  |  TIFFTAG_SAMPLESPERPIXEL |  1 |  uint16 |  † value must be <= 4 |  |  TIFFTAG_SMAXSAMPLEVALUE |  1 |  double |  |  |  TIFFTAG_SMINSAMPLEVALUE |  1 |  double |  |  |  TIFFTAG_SOFTWARE |  1 |  char* |  |  |  TIFFTAG_STONITS |  1 |  double |  † |  |  TIFFTAG_SUBFILETYPE |  1 |  uint32 |  |  |  TIFFTAG_SUBIFD |  2 |  uint16,uint32* |  count & offsets array |  |  TIFFTAG_TARGETPRINTER |  1 |  char* |  |  |  TIFFTAG_THRESHHOLDING |  1 |  uint16 |  |  |  TIFFTAG_TILEDEPTH |  1 |  uint32 |  † |  |  TIFFTAG_TILELENGTH |  1 |  uint32 |  † must be a multiple of 8 |  |  TIFFTAG_TILEWIDTH |  1 |  uint32 |  † must be a multiple of 8 |  |  TIFFTAG_TRANSFERFUNCTION |  1 or 3‡ uint16* |  |  1<<BitsPerSample entry arrays |  |  TIFFTAG_WHITEPOINT |  1 |  float* |  2-entry array |  |  TIFFTAG_XMLPACKET |  2 |  uint32,void* |  count, data |  |  TIFFTAG_XPOSITION |  1 |  float |  |  |  TIFFTAG_XRESOLUTION |  1 |  float |  |  |  TIFFTAG_YCBCRCOEFFICIENTS |  1 |  float* |  † 3-entry array |  |  TIFFTAG_YCBCRPOSITIONING |  1 |  uint16 |  † |  |  TIFFTAG_YCBCRSAMPLING |  2 |  uint16 |  † |  |  TIFFTAG_YPOSITION |  1 |  float |  |  |  TIFFTAG_YRESOLUTION |  1 |  float |  |  |  † Tag may not have its values changed once data is written.  
‡ If _SamplesPerPixel_ is one, then a single array is passed; otherwise three arrays should be passed.  
* The contents of this field are quite complex. See **The ICC Profile Format Specification** , Annex B.3 "Embedding ICC Profiles in TIFF Files" (available at http://www.color.org) for an explanation.

## RETURN VALUES

|  |  1 is returned if the operation was successful. Otherwise, 0 is returned if an error was detected.

## DIAGNOSTICS

|  |  All error messages are directed to the **TIFFError**(3TIFF) routine. **%s: Cannot modify tag "%s" while writing**. Data has already been written to the file, so the specified tag's value can not be changed. This restriction is applied to all tags that affect the format of written data. **%d: Bad value for "%s"**. An invalid value was supplied for the named tag.

## SEE ALSO

|  |  **TIFFOpen**(3TIFF), **TIFFGetField**(3TIFF), **TIFFSetDirectory**(3TIFF), **TIFFWriteDirectory**(3TIFF), **TIFFReadDirectory**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
