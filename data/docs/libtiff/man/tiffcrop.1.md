# TIFFCROP

NAME  
SYNOPSIS  
DESCRIPTION  
OPTIONS  
EXAMPLES  
SEE ALSO  


* * *

## NAME

|  |  tiffcrop − copy (and possibly convert and crop or process) a TIFF file

## SYNOPSIS

|  |  **tiffcrop** [ _options_ ] _src1.tif ... srcN.tif dst.tif_

## DESCRIPTION

|  |  _tiffcrop_ combines one or more files created according to the Tag Image File Format, Revision 6.0 into a single TIFF file. The output file may be compressed using a different algorithm than the input files. _tiffcrop_ is most often used to extract portions of an image for processing with bar code recognizer or OCR software when that software cannot restrict the region of interest to a specific portion of the image or to improve efficiency when the regions of interest must be rotated. By default, _tiffcrop_ will copy all the understood tags in a TIFF directory of an input file to the associated directory in the output file. _tiffcrop_ can be used to reorganize the storage characteristics of data in a file, and it will alter or convert the image data content as specified at the same time, unlike tiffcp. _tiffcrop_ will behave exactly like tiffcp if none of the new options are specified.

## OPTIONS

|  |  **− N odd|even|#,#-#,#|last** |  |  sequences and ranges of images within file to process. The words **odd** or **even** may be used to specify all odd or even numbered images. The word **last** may be used in place of a number in the sequence to indicate the final image in the file without knowing how many images there are. Ranges of images may be specified with a dash and multiple sets can be indicated by joining them in a comma-separated list. e.g.. use **− N 1,5-7,last** to process the 1st, 5th through 7th, and final image in the file. |  |  **− E top|bottom|left|right** |  |  use the top, bottom, left, or right edge as origin reference for width and length of crop regions. May be abbreviated to first letter. |  |  **− U in|cm|px** |  |  units to apply to dimensions for margins and crop regions. Inches or centimeters are converted to pixels using the resolution unit specified in the TIFF file (which defaults to inches if not specified in the IFD). |  |  **− m #,#,#,#** |  |  margins to be removed from the image. The order must be top, left, bottom, right with only commas separating the elements of the list. Margins are scaled according to the current units and removed before any other extractions are computed. Capital M was in use. |  |  **− X #** |  |  horizontal (X-axis) dimension of a region to extract relative to the specified origin reference. If the origin is the top or bottom edge, the X axis value will be assumed to start at the left edge. |  |  |  **− Y #** |  |  vertical (Y-axis) dimension of a region to extract relative to the specified origin reference. If the origin is the left or right edge, the Y axis value will be assumed to start at the top. |  |  |  **− Z #:#,#:#** |  |  zones of the image designated as position X of Y equal sized portions measured from the reference edge, e.g. 1:3 would be first third of the image starting from the reference edge minus any margins specified for the confining edges. Multiple zones can be specified as a comma separated list but they must reference the same edge. To extract the top quarter and the bottom third of an image you would use **− Z 1:4,3:3.** |  |  **− F horiz|vert** |  |  flip, i.e. mirror, the image or extracted region horizontally or vertically. |  |  **− R 90|180|270** |  |  rotate the image or extracted region 90, 180, or 270 degrees clockwise. |  |  **− I** |  |  invert the colorspace values for grayscale and bi-level images. This would be used to correct negative images that have incorrect PHOTOMETRIC INTERPRETATION tags. No support for color images. |  |  |  **− b** _image_ |  |  subtract the following monochrome image from all others processed. This can be used to remove a noise bias from a set of images. This bias image is typically an image of noise the camera saw with its shutter closed. Bias image support is not available with options for cropping, rotating, or inverting the image. |  |  **− B** |  |  Force output to be written with Big-Endian byte order. This option only has an effect when the output file is created or overwritten and not when it is appended to. |  |  |  **− C** |  |  Suppress the use of ''strip chopping'' when reading images that have a single strip/tile of uncompressed data. |  |  |  **− c** |  |  Specify the compression to use for data written to the output file: **none** for no compression, **packbits** for PackBits compression, **lzw** for Lempel-Ziv & Welch compression, **jpeg** for baseline JPEG compression, **zip** for Deflate compression, **g3** for CCITT Group 3 (T.4) compression, and **g4** for CCITT Group 4 (T.6) compression. By default _tiffcrop_ will compress data according to the value of the _Compression_ tag found in the source file. |  |  |  The CCITT Group 3 and Group 4 compression algorithms can only be used with bi-level data. Group 3 compression can be specified together with several T.4-specific options: **1d** for 1-dimensional encoding, **2d** for 2-dimensional encoding, and **fill** to force each encoded scanline to be zero-filled so that the terminating EOL code lies on a byte boundary. Group 3-specific options are specified by appending a '':''-separated list to the ''g3'' option; e.g. **− c g3:2d:fill** to get 2D-encoded data with byte-aligned EOL codes. LZW compression can be specified together with a _predictor_ value. A predictor value of 2 causes each scanline of the output image to undergo horizontal differencing before it is encoded; a value of 1 forces each scanline to be encoded without differencing. LZW-specific options are specified by appending a '':''-separated list to the ''lzw'' option; e.g. **− c lzw:2** for LZW compression with horizontal differencing. |  |  **− f** |  |  Specify the bit fill order to use in writing output data. By default, _tiffcrop_ will create a new file with the same fill order as the original. Specifying **− f lsb2msb** will force data to be written with the FillOrder tag set to LSB2MSB, while **− f msb2lsb** will force data to be written with the FillOrder tag set to MSB2LSB. |  |  |  **− i** |  |  Ignore non-fatal read errors and continue processing of the input file. |  |  |  **− l** |  |  Specify the length of a tile (in pixels). _tiffcrop_ attempts to set the tile dimensions so that no more than 8 kilobytes of data appear in a tile. |  |  |  **− L** |  |  Force output to be written with Little-Endian byte order. This option only has an effect when the output file is created or overwritten and not when it is appended to. |  |  |  **− M** |  |  Suppress the use of memory-mapped files when reading images. |  |  |  **− p** |  |  Specify the planar configuration to use in writing image data that has one 8-bit sample per pixel. By default, _tiffcrop_ will create a new file with the same planar configuration as the original. Specifying **− p contig** will force data to be written with multi-sample data packed together, while **− p separate** will force samples to be written in separate planes. |  |  |  **− r** |  |  Specify the number of rows (scanlines) in each strip of data written to the output file. By default (or when value **0** is specified), _tiffcrop_ attempts to set the rows/strip that no more than 8 kilobytes of data appear in a strip. If you specify special value **-1** it will results in infinite number of the rows per strip. The entire image will be the one strip in that case. |  |  |  **− s** |  |  Force the output file to be written with data organized in strips (rather than tiles). |  |  |  **− t** |  |  Force the output file to be written with data organized in tiles (rather than strips). options can be used to force the resultant image to be written as strips or tiles of data, respectively. |  |  |  **− w** |  |  Specify the width of a tile (in pixels). _tiffcrop_ attempts to set the tile dimensions so that no more than 8 kilobytes of data appear in a tile. _tiffcrop_ attempts to set the tile dimensions so that no more than 8 kilobytes of data appear in a tile. |  |  |  **− ,={character}** |  |  substitute {character} for ',' in parsing image directory indices in files. This is necessary if filenames contain commas. Note that ',=' with whitespace immediately following will disable the special meaning of the ',' entirely. See examples.

## EXAMPLES

|  |  The following concatenates two files and writes the result using LZW encoding: |  | 
    
    
    tiffcrop -c lzw a.tif b.tif result.tif
    

|  |  To convert a G3 1d-encoded TIFF to a single strip of G4-encoded data the following might be used: |  | 
    
    
    tiffcrop -c g4 -r 10000 g3.tif g4.tif
    

|  |  (1000 is just a number that is larger than the number of rows in the source file.) To extract a selected set of images from a multi-image TIFF file use the -N option described above. Thus, to copy the 1st and 3rd images of image file "album.tif" to "result.tif": |  | 
    
    
    tiffcrop -N 1,3 album.tif result.tif
    

|  |  Given file "CCD.tif" whose first image is a noise bias followed by images which include that bias, subtract the noise from all those images following it (while decompressing) with the command: |  | 
    
    
    tiffcrop -c none -b CCD.tif CCD.tif -d 2 result.tif
    

## SEE ALSO

|  |  **pal2rgb**(1), **tiffinfo**(1), **tiffcmp**(1), **tiffcp**(1), **tiffmedian**(1), **tiffsplit**(1), **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
