# TIFFTILE

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFTileSize, TIFFTileRowSize, TIFFVTileSize, TIFFDefaultTileSize, TIFFComputeTile, TIFFCheckTile, TIFFNumberOfTiles − tile-related utility routines

## SYNOPSIS

|  |  **#include <tiffio.h>** **void TIFFDefaultTileSize(TIFF ***_tif_**, uint32 ***_tw_**, uint32 ***_th_**)  
tsize_t TIFFTileSize(TIFF ***_tif_**)  
tsize_t TIFFTileRowSize(TIFF ***_tif_**)  
tsize_t TIFFVTileSize(TIFF ***_tif_**, uint32** _nrows_**)  
ttile_t TIFFComputeTile(TIFF ***_tif_**, uint32** _x_**, uint32** _y_**, uint32** _z_**, tsample_t** _sample_**)  
int TIFFCheckTile(TIFF ***_tif_**, uint32** _x_**, uint32** _y_**, uint32** _z_**, tsample_t** _sample_**)  
ttile_t TIFFNumberOfTiles(TIFF ***_tif_**)**

## DESCRIPTION

|  |  _TIFFDefaultTileSize_ returns the pixel width and height of a reasonable-sized tile; suitable for setting up the _TileWidth_ and _TileLength_ tags. If the _tw_ and _th_ values passed in are non-zero, then they are adjusted to reflect any compression-specific requirements. The returned width and height are constrained to be a multiple of 16 pixels to conform with the TIFF specification. _TIFFTileSize_ returns the equivalent size for a tile of data as it would be returned in a call to _TIFFReadTile_ or as it would be expected in a call to _TIFFWriteTile_. _TIFFVTileSize_ returns the number of bytes in a row-aligned tile with _nrows_ of data. _TIFFTileRowSize_ returns the number of bytes of a row of data in a tile. _TIFFComputeTile_ returns the tile that contains the specified coordinates. A valid tile is always returned; out-of-range coordinate values are clamped to the bounds of the image. The _x_ and _y_ parameters are always used in calculating a tile. The _z_ parameter is used if the image is deeper than 1 slice (_ImageDepth_ >1). The _sample_ parameter is used only if data are organized in separate planes (_PlanarConfiguration_ =2). _TIFFCheckTile_ returns a non-zero value if the supplied coordinates are within the bounds of the image and zero otherwise. The _x_ parameter is checked against the value of the _ImageWidth_ tag. The _y_ parameter is checked against the value of the _ImageLength_ tag. The _z_ parameter is checked against the value of the _ImageDepth_ tag (if defined). The _sample_ parameter is checked against the value of the _SamplesPerPixel_ parameter if the data are organized in separate planes. _TIFFNumberOfTiles_ returns the number of tiles in the image.

## DIAGNOSTICS

|  |  None.

## SEE ALSO

|  |  **TIFFReadEncodedTile**(3TIFF), **TIFFReadRawTile**(3TIFF), **TIFFReadTile**(3TIFF), **TIFFWriteEncodedTile**(3TIFF), **TIFFWriteRawTile**(3TIFF), **TIFFWriteTile**(3TIFF), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
