# TIFFSTRIP

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFDefaultStripSize, TIFFStripSize, TIFFVStripSize, TIFFRawStripSize, TIFFComputeStrip, TIFFNumberOfStrips − strip-related utility routines

## SYNOPSIS

|  |  **#include <tiffio.h>** **uint32 TIFFDefaultStripSize(TIFF ***_tif_**, uint32** _estimate_**)  
tsize_t TIFFStripSize(TIFF ***_tif_**)  
tsize_t TIFFVStripSize(TIFF ***_tif_**, uint32** _nrows_**)  
tsize_t TIFFRawStripSize(TIFF ***_tif_**, tstrip_t** _strip_**)  
tstrip_t TIFFComputeStrip(TIFF ***_tif_**, uint32** _row_**, tsample_t** _sample_**)  
tstrip_t TIFFNumberOfStrips(TIFF ***_tif_**)**

## DESCRIPTION

|  |  _TIFFDefaultStripSize_ returns the number of rows for a reasonable-sized strip according to the current settings of the _ImageWidth_ , _BitsPerSample_ , _SamplesPerPixel_ , tags and any compression-specific requirements. If the _estimate_ parameter, if non-zero, then it is taken as an estimate of the desired strip size and adjusted according to any compression-specific requirements. The value returned by this function is typically used to define the _RowsPerStrip_ tag. In lieu of any unusual requirements _TIFFDefaultStripSize_ tries to create strips that have approximately 8 kilobytes of uncompressed data. _TIFFStripSize_ returns the equivalent size for a strip of data as it would be returned in a call to _TIFFReadEncodedStrip_ or as it would be expected in a call to _TIFFWriteEncodedStrip_. _TIFFVStripSize_ returns the number of bytes in a strip with _nrows_ rows of data. _TIFFRawStripSize_ returns the number of bytes in a raw strip (i.e. not decoded). _TIFFComputeStrip_ returns the strip that contains the specified coordinates. A valid strip is always returned; out-of-range coordinate values are clamped to the bounds of the image. The _row_ parameter is always used in calculating a strip. The _sample_ parameter is used only if data are organized in separate planes (_PlanarConfiguration_ =2). _TIFFNumberOfStrips_ returns the number of strips in the image.

## DIAGNOSTICS

|  |  None.

## SEE ALSO

|  |  **TIFFReadEncodedStrip**(3TIFF), **TIFFReadRawStrip**(3TIFF), **TIFFWriteEncodedStrip**(3TIFF), **TIFFWriteRawStrip**(3TIFF), **libtiff**(3TIFF), Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
