[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[A Word about Colorspaces](formats.html#colorspace) • [Supported Formats](formats.html#supported) • [Pseudo Formats](formats.html#pseudo) • [Built-in Images](formats.html#builtin-images) • [Built-in Patterns](formats.html#builtin-patterns) • [Embedded Profiles](formats.html#embedded)

ImageMagick uses an ASCII string known as magick (e.g. `GIF`) to identify file formats, algorithms acting as formats, built-in patterns, and embedded profile types. Support for some of the formats are delegated to libraries or external programs. The Installation Guide describes where to find these distributions and any special configuration options required.

To get a complete listing of which image formats are supported on your system, type
    
    
    identify -list format
    

On some platforms, ImageMagick automagically processes these extensions: .gz for Zip compression, .Z for Unix compression, .bz2 for block compression, and .pgp for PGP encryption. For example, a PNM image called image.pnm.gz is automagically uncompressed.

## A Word about Colorspaces

A majority of the image formats assume an sRGB colorspace (e.g. JPEG, PNG, etc.). A few support only linear RGB (e.g. EXR, DPX, CIN, HDR) or only linear GRAY (e.g. PGM). A few formats support CMYK. Then there is the occasional format that also supports LAB (that is CieLAB) (e.g. TIFF, PSD, JPG, JP2). To determine the colorspace of your image, use this command:
    
    
    -> identify -verbose image.jpg
    Image: image.jpg
    Format: JPEG (Joint Photographic Experts Group JFIF format)
    ...
    Colorspace: sRGB
    

OR use the appropriate percent escape 
    
    
    -> convert image.jpg -print "%[colorspace]\n" null:
    sRGB
    

When processing an image, be aware of the colorspace. Many image processing algorithms assume a linear RGB colorspace. Although you may get satisfactory results processing in the sRGB colorspace, you may get improved results in linear RGB (essentially sRGB with the gamma function removed). For example,
    
    
    convert image.jpg -colorspace RGB -resize 50% -colorspace sRGB resize.jpg
    

As of IM 6.7.8-2 one can properly work in LAB colorspace whether or not Imagemagick is [HDRI](high-dynamic-range.html)-enabled. Essentually the A and B channels are stored with a 50% gray bias, to allow it to handle the negatives required by the format.
    
    
    convert lab.tif -resize 50% resize.jpg
    

Again, it may not make sense for some image processing operators to work directly in LAB space, but ImageMagick permits it and generally returns reasonable results.

Prior to IM 6.7.8-2, the A and B channels has a discontinuity, making them non-linear. As such to process such images, you needed to first convert the colorspace some other linear colorspace, before apply your processing operator. Afterward you can transform back to the LAB colorspace. For example,
    
    
      convert lab.tif -colorspace RGB -resize 50% -colorspace Lab resize.jpg
    

## Supported Image Formats

ImageMagick supports reading over 100 major file formats (not including sub-formats). The following table provides a summary of the supported image formats.

Tag | Mode | Description | Notes  
---|---|---|---  
AAI | RW | AAI Dune image |   
ART | RW | PFS: 1st Publisher | Format originally used on the Macintosh (MacPaint?) and later used for PFS: 1st Publisher clip art.  
ARW | R | Sony Digital Camera Alpha Raw Image Format |   
[AVI](http://www.jmcgowan.com/avi.html) | R | Microsoft Audio/Visual Interleaved |   
AVS | RW | AVS X image |   
[BPG](http://bellard.org/bpg/) | RW | Better Portable Graphics | Use [-quality](command-line-options.html#quality) to specify the image compression quality. To meet the requirements of BPG, the quality argument divided by 2 (e.g. -quality 92 assigns 46 as the BPG compression.  
[BMP, BMP2, BMP3](http://www.fileformat.info/format/bmp/egff.htm) | RW | Microsoft Windows bitmap | By default the BMP format is version 4. Use BMP3 and BMP2 to write versions 3 and 2 respectively.  
[CALS](http://www.fileformat.info/format/cals/egff.htm) | R | Continuous Acquisition and Life-cycle Support Type 1 image | Specified in MIL-R-28002 and MIL-PRF-28002. Standard blueprint archive format as used by the US military to replace microfiche.  
[CGM](http://www.fileformat.info/format/cgm/egff.htm) | R | Computer Graphics Metafile | Requires [ralcgm](http://www.agocg.ac.uk/train/cgm/ralcgm.htm) to render CGM files.  
[CIN](http://www.cineon.com/ff_draft.html) | RW | Kodak Cineon Image Format | Use [-set](command-line-options.html#set) to specify the image gamma or black and white points (e.g. `-set gamma 1.7`, `-set reference-black 95`, `-set reference-white 685`). Properties include cin:file.create_date, cin:file.create_time, cin:file.filename, cin:file.version, cin:film.count, cin:film.format, cin:film.frame_id, cin:film.frame_position, cin:film.frame_rate, cin:film.id, cin:film.offset, cin:film.prefix, cin:film.slate_info, cin:film.type, cin:image.label, cin:origination.create_date, cin:origination.create_time, cin:origination.device, cin:origination.filename, cin:origination.model, cin:origination.serial, cin:origination.x_offset, cin:origination.x_pitch, cin:origination.y_offset, cin:origination.y_pitch, cin:user.data.  
CMYK | RW | Raw cyan, magenta, yellow, and black samples | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth. To specify a single precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 32 for single precision floats, 64 for double precision, and 16 for half-precision.  
CMYKA | RW | Raw cyan, magenta, yellow, black, and alpha samples | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth. To specify a single precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 32 for single precision floats, 64 for double precision, and 16 for half-precision.  
CR2 | R | Canon Digital Camera Raw Image Format | Requires an explicit image format otherwise the image is interpreted as a TIFF image (e.g. cr2:image.cr2).  
CRW | R | Canon Digital Camera Raw Image Format |   
CUR | R | Microsoft Cursor Icon |   
CUT | R | DR Halo |   
DCM | R | Digital Imaging and Communications in Medicine (DICOM) image | Used by the medical community for images like X-rays. ImageMagick sets the initial display range based on the Window Center (0028,1050) and Window Width (0028,1051) tags. Use [-define dcm:display-range=reset](command-line-options.html#define) to set the display range to the minimum and maximum pixel values.  
DCR | R | Kodak Digital Camera Raw Image File |   
DCX | RW | ZSoft IBM PC multi-page Paintbrush image |   
[DDS](http://en.wikipedia.org/wiki/DirectDraw_Surface) | RW | Microsoft Direct Draw Surface | Use [-define](command-line-options.html#define) to specify the compression (e.g. `-define dds:compression={dxt1, dxt5, none}`). Other defines include `dds:cluster-fit={true,false}`, `dds:weight-by-alpha={true,false}`, and use `dds:mipmaps` to set the number of mipmaps.  
DIB | RW | Microsoft Windows Device Independent Bitmap | DIB is a [BMP](formats.html#BMP) file without the [BMP](formats.html#BMP) header. Used to support embedded images in compound formats like WMF.  
[DJVU](http://www.djvu.org/) | R |  |   
[DNG](http://www.adobe.com/products/dng/main.html) | R | Digital Negative | Requires an explicit image format otherwise the image is interpreted as a TIFF image (e.g. dng:image.dng).  
[DOT](http://www.graphviz.org) | R | Graph Visualization | Use [-define](command-line-options.html#define) to specify the layout engine (e.g. `-define dot:layout-engine=twopi`).  
[DPX](motion-picture.html) | RW | SMPTE Digital Moving Picture Exchange 2.0 (SMPTE 268M-2003) | Use [-set](command-line-options.html#set) to specify the image gamma or black and white points (e.g. `-set gamma 1.7`, `-set reference-black 95`, `-set reference-white 685`).  
EMF | R | Microsoft Enhanced Metafile (32-bit) | Only available under Microsoft Windows. Use [-size](command-line-options.html#size) command line option to specify the maximum width and height.  
EPDF | RW | Encapsulated Portable Document Format |   
EPI | RW | Adobe Encapsulated PostScript Interchange format | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
EPS | RW | Adobe Encapsulated PostScript | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
EPS2 | W | Adobe Level II Encapsulated PostScript | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
EPS3 | W | Adobe Level III Encapsulated PostScript | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
EPSF | RW | Adobe Encapsulated PostScript | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
EPSI | RW | Adobe Encapsulated PostScript Interchange format | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
EPT | RW | Adobe Encapsulated PostScript Interchange format with [TIFF](formats.html#TIFF) preview | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
[EXR](http://www.openexr.org) | RW | High dynamic-range (HDR) file format developed by Industrial Light & Magic | See [High Dynamic-Range Images](high-dynamic-range.html) for details on this image format. To specify the output color type, use `-define exr:color-type={RGB,RGBA,YC,YCA,Y,YA,R,G,B,A}`. Use [-sampling-factor](command-line-options.html#sampling-factor) to specify the sampling rate for YC(A) (e.g. `2x2 or 4:2:0`). Requires the [OpenEXR](http://www.openexr.org/) delegate library.  
FAX | RW | Group 3 TIFF | This format is a fixed width of 1728 as required by the standard. See [TIFF](formats.html#TIFF) format. Note that FAX machines use non-square pixels which are 1.5 times wider than they are tall but computer displays use square pixels so FAX images may appear to be narrow unless they are explicitly resized using a resize specification of `100x150%`.  
[FIG](http://homepage.usask.ca/~ijm451/fig/) | R | FIG graphics format | Requires [TransFig](ftp://ftp.x.org/contrib/applications/drawing_tools/transfig).  
[FITS](http://www.cv.nrao.edu/fits/) | RW | Flexible Image Transport System | To specify a single-precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 64 for a double-precision floating-point format.  
FPX | RW | FlashPix Format | FlashPix has the option to store mega- and giga-pixel images at various resolutions in a single file which permits conservative bandwidth and fast reveal times when displayed within a Web browser. Requires the [FlashPix SDK](http://www.imagemagick.org/download/delegates). Specify the FlashPix viewing parameters with the [-define fpx:view](command-line-options.html#define).  
[GIF](http://www.fileformat.info/format/gif/egff.htm) | RW | CompuServe Graphics Interchange Format | 8-bit RGB PseudoColor with up to 256 palette entries. Specify the format `GIF87` to write the older version 87a of the format. Use [-transparent-color](command-line-options.html#transparent-color) to specify the GIF transparent color (e.g. `-transparent-color wheat`).  
GPLT | R | Gnuplot plot files | Requires [gnuplot4.0.tar.Z](http://www.gnuplot.info/) or later.  
GRAY | RW | Raw gray samples | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth. To specify a single precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 32 for single precision floats, 64 for double precision, and 16 for half-precision.  
[HDR](http://en.wikipedia.org/wiki/RGBE_image_format) | RW | Radiance RGBE image format |   
HPGL | R | HP-GL plotter language | Requires [hp2xx-3.4.4.tar.gz](http://ftp.gnu.org/gnu/hp2xx)  
HRZ | RW | Slow Scane TeleVision |   
HTML | RW | Hypertext Markup Language with a client-side image map | Also known as `HTM`. Requires [html2ps](http://user.it.uu.se/%7Ejan/html2ps.html) to read.  
ICO | R | Microsoft icon | Also known as `ICON`.  
INFO | W | Format and characteristics of the image |   
INLINE | RW | Base64-encoded inline image | The inline image look similar to `inline:data:;base64,/9j/4AAQSk...knrn//2Q==`. If the inline image exceeds 5000 characters, reference it from a file (e.g. `inline:inline.txt`). You can also write a base64-encoded image. Embed the mime type in the filename, for example, `convert myimage inline:jpeg:myimage.txt`.  
JBIG | RW | Joint Bi-level Image experts Group file interchange format | Also known as `BIE` and `JBG`. Requires [jbigkit-1.6.tar.gz](http://www.cl.cam.ac.uk/~mgk25/jbigkit/).  
[JNG](http://www.libmng.com/) | RW | Multiple-image Network Graphics | JPEG in a PNG-style wrapper with transparency. Requires libjpeg and libpng-1.0.11 or later, [libpng-1.2.5](http://www.libpng.org/pub/png/libpng.html) or later recommended.  
[JP2](http://www.openjpeg.org/) | RW | JPEG-2000 JP2 File Format Syntax | Specify the encoding options with the [-define](command-line-options.html#define) option. See [JP2 Encoding Options](jp2.html) for more details.  
[JPT](http://www.openjpeg.org/) | RW | JPEG-2000 Code Stream Syntax | Specify the encoding options with the [-define](command-line-options.html#define) option See [JP2 Encoding Options](jp2.html) for more details.  
[J2C](http://www.openjpeg.org/) | RW | JPEG-2000 Code Stream Syntax | Specify the encoding options with the [-define](command-line-options.html#define) option See [JP2 Encoding Options](jp2.html) for more details.  
[J2K](http://www.openjpeg.org/) | RW | JPEG-2000 Code Stream Syntax | Specify the encoding options with the [-define](command-line-options.html#define) option See [JP2 Encoding Options](jp2.html) for more details.  
[JPEG](http://www.jpeg.org/) | RW | Joint Photographic Experts Group JFIF format | Note, JPEG is a lossy compression. In addition, you cannot create black and white images with JPEG nor can you save transparency.  
  
Requires [jpegsrc.v8c.tar.gz](http://www.ijg.org/files/). You can set quality scaling for luminance and chrominance separately (e.g. [-quality](command-line-options.html#quality) 90,70). You can optionally define the DCT method, for example to specify the float method, use [-define jpeg:dct-method=float](command-line-options.html#define). By default we compute optimal Huffman coding tables. Specify [-define jpeg:optimize-coding=false](command-line-options.html#define) to use the default Huffman tables. Two other options include [-define jpeg:block-smoothing](command-line-options.html#define) and [-define jpeg:fancy-upsampling](command-line-options.html#define). Set the sampling factor with [-define jpeg:sampling-factor](command-line-options.html#define). You can size the image with `jpeg:size`, for example [-define jpeg:size=128x128](command-line-options.html#define). To restrict the maximum file size, use `jpeg:extent`, for example [-define jpeg:extent=400KB](command-line-options.html#define). To define one or more custom quantization tables, use [-define jpeg:q-table=_filename_](command-line-options.html#define). To avoid reading a particular associated image profile, use [-define profile:skip=_name_](command-line-options.html#define) (e.g. profile:skip=ICC).  
[JXR](https://en.wikipedia.org/wiki/JPEG_XR) | RW | JPEG extended range | Requires the [jxrlib](https://jxrlib.codeplex.com/) delegate library. Put the JxrDecApp and JxrEncApp applications in your execution path.   
[JSON](http://www.json.org) | W | JavaScript Object Notation, a lightweight data-interchange format | Include additional attributes about the image with these defines: [-define json:locate](command-line-options.html#define), [-define json:limit](command-line-options.html#define), [-define json:moments](command-line-options.html#define), or [-define json:features](command-line-options.html#define).  
MAN | R | Unix reference manual pages | Requires that GNU groff and Ghostcript are installed.  
MAT | R | MATLAB image format |   
[MIFF](miff.html) | RW | Magick image file format | This format persists all image attributes known to ImageMagick. To specify a single precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 32 for single precision floats, 64 for double precision, and 16 for half-precision.  
MONO | RW | Bi-level bitmap in least-significant-byte first order |   
[MNG](http://www.libpng.org/pub/mng/) | RW | Multiple-image Network Graphics | A PNG-like Image Format Supporting Multiple Images, Animation and Transparent JPEG. Requires libpng-1.0.11 or later, [libpng-1.2.5](http://www.libpng.org/pub/png/libpng.html) or later recommended. An interframe delay of 0 generates one frame with each additional layer composited on top. For motion, be sure to specify a non-zero delay.  
[M2V](http://www.ffmpeg.org/) | RW | Motion Picture Experts Group file interchange format (version 2) | Requires [ffmpeg](http://www.ffmpeg.org/download.html).  
[MPEG](http://www.ffmpeg.org/) | RW | Motion Picture Experts Group file interchange format (version 1) | Requires [ffmpeg](http://www.ffmpeg.org/download.html).  
MPC | RW | Magick Persistent Cache image file format | The most efficient data processing pattern is a write-once, read-many-times pattern. The image is generated or copied from source, then various analyses are performed on the image pixels over time. MPC supports this pattern. MPC is the native in-memory ImageMagick uncompressed file format. This file format is identical to that used by ImageMagick to represent images in memory and is read by mapping the file directly into memory. The MPC format is not portable and is not suitable as an archive format. It is suitable as an intermediate format for high-performance image processing. The MPC format requires two files to support one image. Image attributes are written to a file with the extension `.mpc`, whereas, image pixels are written to a file with the extension `.cache`.  
MPR | RW | Magick Persistent Registry | This format permits you to write to and read images from memory. The image persists until the program exits. For example, let's use the MPR to create a checkerboard: 
    
    
    convert \( -size 15x15 canvas:black canvas:white -append \) \
      \( +clone -flip \) +append -write mpr:checkers +delete \
      -size 240x240 tile:mpr:checkers board.png
      
  
MRW | R | Sony (Minolta) Raw Image File |   
MSL | RW | Magick Scripting Language | MSL is the XML-based scripting language supported by the [conjure](conjure.html) utility. MSL requires the [libxml2](http://xmlsoft.org/) delegate library.  
[MTV](http://www.fileformat.info/format/mtv/egff.htm) | RW | MTV Raytracing image format |   
[MVG](magick-vector-graphics.html) | RW | Magick Vector Graphics. | The native ImageMagick vector metafile format. A text file containing vector drawing commands accepted by [convert](convert.html)'s [-draw](command-line-options.html#draw) option.  
NEF | R | Nikon Digital SLR Camera Raw Image File |   
ORF | R | Olympus Digital Camera Raw Image File |   
OTB | RW | On-the-air Bitmap |   
P7 | RW | Xv's Visual Schnauzer thumbnail format |   
PALM | RW | Palm pixmap |   
[PAM](http://netpbm.sourceforge.net/doc/pam.html) | W | Common 2-dimensional bitmap format |   
CLIPBOARD | RW | Windows Clipboard | Only available under Microsoft Windows.  
[PBM](http://netpbm.sourceforge.net/doc/pbm.html) | RW | Portable bitmap format (black and white) |   
PCD | RW | Photo CD | The maximum resolution written is 768x512 pixels since larger images require huffman compression (which is not supported).  
PCDS | RW | Photo CD | Decode with the sRGB color tables.  
PCL | W | HP Page Control Language | Use [-define](command-line-options.html#define) to specify fit to page option (e.g. `-define pcl:fit-to-page=true`).  
[PCX](http://www.fileformat.info/format/pcx/egff.htm) | RW | ZSoft IBM PC Paintbrush file |   
PDB | RW | Palm Database ImageViewer Format |   
PDF | RW | Portable Document Format | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read. By default, ImageMagick sets the page size to the MediaBox. Some PDF files, however, have a CropBox or TrimBox that is smaller than the MediaBox and may include white space, registration or cutting marks outside the CropBox or TrimBox. To force ImageMagick to use the CropBox or TrimBox rather than the MediaBox, use [-define](command-line-options.html#define) (e.g. `-define pdf:use-cropbox=true` or `-define pdf:use-trimbox=true`). Use [-density](command-line-options.html#density) to improve the appearance of your PDF rendering (e.g. -density 300x300). Use [-alpha remove ](command-line-options.html#alpha) to remove transparency. To specify direct conversion from Postscript to PDF, use `-define delegate:bimodel=true`. Use `-define pdf:fit-page=true` to scale to the page size. To immediately stop processing upon an error, set `-define pdf:stop-on-error` to `true`. To set the page direction preferences to right-to-left, try `-define pdf:page-direction=right-to-left`.  
PEF | R | Pentax Electronic File | Requires an explicit image format otherwise the image is interpreted as a TIFF image (e.g. pef:image.pef).  
PFA | R | Postscript Type 1 font (ASCII) | Opening as file returns a preview image.  
PFB | R | Postscript Type 1 font (binary) | Opening as file returns a preview image.  
[PFM](http://netpbm.sourceforge.net/doc/pfm.html) | RW | Portable float map format |   
[PGM](http://netpbm.sourceforge.net/doc/pgm.html) | RW | Portable graymap format (gray scale) |   
PICON | RW | Personal Icon |   
PICT | RW | Apple Macintosh QuickDraw/PICT file |   
PIX | R | Alias/Wavefront RLE image format |   
[PNG](http://www.libpng.org/pub/png/) | RW | Portable Network Graphics | Requires libpng-1.0.11 or later, [libpng-1.2.5](http://www.libpng.org/pub/png/libpng.html) or later recommended. The PNG specification does not support pixels-per-inch units, only pixels-per-centimeter. To avoid reading a particular associated image profile, use [-define profile:skip=_name_](command-line-options.html#define) (e.g. profile:skip=ICC).  
[PNG8](http://www.libpng.org/pub/png/) | RW | Portable Network Graphics | 8-bit indexed with optional binary transparency  
[PNG00](http://www.libpng.org/pub/png/) | RW | Portable Network Graphics | PNG inheriting subformat from original if possible  
[PNG24](http://www.libpng.org/pub/png/) | RW | Portable Network Graphics | opaque or binary transparent 24-bit RGB  
[PNG32](http://www.libpng.org/pub/png/) | RW | Portable Network Graphics | opaque or transparent 32-bit RGBA  
[PNG48](http://www.libpng.org/pub/png/) | RW | Portable Network Graphics | opaque or binary transparent 48-bit RGB  
[PNG64](http://www.libpng.org/pub/png/) | RW | Portable Network Graphics | opaque or transparent 64-bit RGB  
[PNM](http://netpbm.sourceforge.net/doc/pnm.html) | RW | Portable anymap | PNM is a family of formats supporting portable bitmaps (PBM) , graymaps (PGM), and pixmaps (PPM). There is no file format associated with pnm itself. If PNM is used as the output format specifier, then ImageMagick automagically selects the most appropriate format to represent the image. The default is to write the binary version of the formats. Use [-compress none](command-line-options.html#compress) to write the ASCII version of the formats.  
[PPM](http://netpbm.sourceforge.net/doc/ppm.html) | RW | Portable pixmap format (color) |   
PS | RW | Adobe PostScript file | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read. To force ImageMagick to respect the crop box, use [-define](command-line-options.html#define) (e.g. `-define eps:use-cropbox=true`). Use [-density](command-line-options.html#density) to improve the appearance of your Postscript rendering (e.g. -density 300x300). Use [-alpha remove ](command-line-options.html#alpha) to remove transparency. To specify direct conversion from PDF to Postscript, use `-define delegate:bimodel=true`.  
PS2 | RW | Adobe Level II PostScript file | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
PS3 | RW | Adobe Level III PostScript file | Requires [Ghostscript](http://www.cs.wisc.edu/%7Eghost) to read.  
[PSB](http://www.adobe.com/devnet-apps/photoshop/fileformatashtml/) | RW | Adobe Large Document Format |   
[PSD](http://www.adobe.com/devnet-apps/photoshop/fileformatashtml/) | RW | Adobe Photoshop bitmap file | Use [-define psd:alpha-unblend=off](command-line-options.html#define) to disable alpha blenning in the merged image.  
PTIF | RW | Pyramid encoded [TIFF](formats.html#TIFF) | Multi-resolution [TIFF](formats.html#TIFF) containing successively smaller versions of the image down to the size of an icon.  
[PWP](http://www.photoworks.com/) | R | Seattle File Works multi-image file |   
RAD | R | Radiance image file | Requires that _ra_ppm_ from the Radiance software package be installed.  
RAF | R | Fuji CCD-RAW Graphic File |   
RGB | RW | Raw red, green, and blue samples | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth. To specify a single precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 32 for single precision floats, 64 for double precision, and 16 for half-precision.  
RGBA | RW | Raw red, green, blue, and alpha samples | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth. To specify a single precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 32 for single precision floats, 64 for double precision, and 16 for half-precision.  
RFG | RW | LEGO Mindstorms EV3 Robot Graphics File |   
RLA | R | Alias/Wavefront image file |   
RLE | R | Utah Run length encoded image file |   
[SCT](http://www.oreilly.com/www/centers/gff/formats/scitex/) | R | Scitex Continuous Tone Picture |   
[SFW](http://www.photoworks.com/) | R | Seattle File Works image |   
SGI | RW | Irix RGB image |   
SHTML | W | Hypertext Markup Language client-side image map | Used to write HTML clickable image maps based on a the output of [montage](montage.html) or a format which supports tiled images such as [MIFF](formats.html#MIFF).  
SID, MrSID | R | Multiresolution seamless image | Requires the [mrsidgeodecode](http://www.lizardtech.com/downloads/downloads.html?dl=/download/files/lin/geoexpress_commandlineutils_linux.tgz) command line utility that decompresses MG2 or MG3 SID image files.  
SPARSE-COLOR | W | Raw text file | Format compatible with the [-sparse-color](command-line-options.html#sparse-color) option. Lists only non-fully-transparent pixels.  
SUN | RW | SUN Rasterfile |   
[SVG](http://www.w3.org/Graphics/SVG) | RW | Scalable Vector Graphics | ImageMagick utilizes [inkscape](http://www.inkscape.org/) if its in your execution path otherwise [RSVG](http://developer.gnome.org/rsvg/). If neither are available, ImageMagick reverts to its internal SVG renderer. The default resolution is 90 DPI. Use [-size](command-line-options.html#size) command line option to specify the maximum width and height.  
TGA | RW | Truevision Targa image | Also known as formats `ICB`, `VDA`, and `VST`.  
[TIFF](http://www.libtiff.org/) | RW | Tagged Image File Format | Also known as `TIF`. Requires [tiff-v3.6.1.tar.gz](http://www.libtiff.org/) or later. Use [-define](command-line-options.html#define) to specify the rows per strip (e.g. `-define tiff:rows-per-strip=8`). To define the tile geometry, use for example, `-define tiff:tile-geometry=128x128`. To specify a signed format, use `-define quantum:format=signed`. To specify a single-precision floating-point format, use `-define quantum:format=floating-point`. Set the depth to 64 for a double-precision floating-point format. Use `-define quantum:polarity=min-is-black` or `-define quantum:polarity=min-is-white` toggle the photometric interpretation for a bilevel image. Specify the extra samples as associated or unassociated alpha with, for example, `-define tiff:alpha=unassociated`. Set the fill order with `-define tiff:fill-order=msb|lsb`. Set the TIFF endianess with `-define tiff:endian=msb|lsb`. Use `-define tiff:exif-properties=false` to skip reading the EXIF properties. You can set a number of TIFF software attributes including document name, host computer, artist, timestamp, make, model, software, and copyright. For example, [-set tiff:software "My Company"](command-line-options.html#set). If you want to ignore certain TIFF tags, use this option: `-define tiff:ignore-tags=comma-separated-list-of-tag-IDs`. Since version 6.9.1-4 there is support for reading photoshop layers in TIFF files, this can be disabled with `-define tiff:ignore-layers=true`  
TIM | R | PSX TIM file |   
[TTF](http://www.freetype.org/) | R | TrueType font file | Requires [freetype 2](http://www.freetype.org/). Opening as file returns a preview image. Use [-set](command-line-options.html#set) if you do not want to hint glyph outlines after their scaling to device pixels (e.g. `-set type:hinting off`).  
TXT | RW | Raw text file | Use [-define](command-line-options.html#define) to specify the color compliance (e.g. `-define txt:compliance=css`).  
UIL | W | X-Motif UIL table |   
UYVY | RW | Interleaved YUV raw image | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) command line options to specify width and height. Use [-sampling-factor](command-line-options.html#sampling-factor) to set the desired subsampling (e.g. -sampling-factor 4:2:2).  
VICAR | RW | VICAR rasterfile format |   
[VIFF](http://www.fileformat.info/format/viff/egff.htm) | RW | Khoros Visualization Image File Format |   
[WBMP](http://www.openmobilealliance.org/Technical/wapindex.aspx) | RW | Wireless bitmap | Support for uncompressed monochrome only.  
[WDP](https://en.wikipedia.org/wiki/JPEG_XR) | RW | JPEG extended range | Requires the [jxrlib](https://jxrlib.codeplex.com/) delegate library. Put the JxrDecApp and JxrEncApp applications in your execution path.   
[WEBP](http://en.wikipedia.org/wiki/WebP) | RW | Weppy image format | Requires the [WEBP](https://developers.google.com/speed/webp/download) delegate library. Specify the encoding options with the [-define](command-line-options.html#define) option See [WebP Encoding Options](webp.html) for more details.  
[WMF](http://www.fileformat.info/format/wmf/egff.htm) | R | Windows Metafile | Requires [libwmf](http://sourceforge.net/projects/wvware/). By default, renders WMF files using the dimensions specified by the metafile header. Use the -density option to adjust the output resolution, and thereby adjust the output size. The default output resolution is 72DPI so `-density 144` results in an image twice as large as the default. Use `-background color` to specify the WMF background color (default white) or `-texture filename` to specify a background texture image.  
[WPG](http://www.fileformat.info/format/wpg/egff.htm) | R | Word Perfect Graphics File |   
X | RW | display or import an image to or from an X11 server | Use [-define](command-line-options.html#define) to obtain the image from the root window (e.g. `-define x:screen=true`). Set `x:silent=true` to turn off the beep when importing an image.  
[XBM](http://www.fileformat.info/format/xbm/egff.htm) | RW | X Windows system bitmap, black and white only | Used by the X Windows System to store monochrome icons.  
XCF | R | GIMP image |   
[XPM](http://www.fileformat.info/format/xpm/egff.htm) | RW | X Windows system pixmap | Also known as `PM`. Used by the X Windows System to store color icons.  
[XWD](http://www.fileformat.info/format/xwd/egff.htm) | RW | X Windows system window dump | Used by the X Windows System to save/display screen dumps.  
X3F | R | Sigma Camera RAW Picture File |   
YCbCr | RW | Raw Y, Cb, and Cr samples | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth.  
YCbCrA | RW | Raw Y, Cb, Cr, and alpha samples | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth.  
YUV | RW | CCIR 601 4:1:1 | Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) command line options to specify width, height, and depth. Use [-sampling-factor](command-line-options.html#sampling-factor) to set the desired subsampling (e.g. -sampling-factor 4:2:2).  
  
## Pseudo-image Formats

ImageMagick supports a number of image format specifications which refer to images prepared via an algorithm, or input/output targets. The following table lists these pseudo-image formats:

Tag | Mode | Description | Notes  
---|---|---|---  
CANVAS | R | Canvas image of specified color | Useful to create solid color canvas images. Use [-size](command-line-options.html#size) and [-depth](command-line-options.html#depth) to specify the image width, height, and depth. Example canvas color specifications include `canvas:red` and `canvas:#FF0000`.  
If no color is specified a '`white`' canvas image is generated. If no [-size](command-line-options.html#size) is specified a single pixel image of the specified color is generated.  
CAPTION | R | Image caption |   
CLIP | RW | Clip path of image |   
CLIPBOARD | RW | Windows Clipboard | Only available under Microsoft Windows.  
FRACTAL | R | Plasma fractal image |   
GRADIENT | R | Gradual passing from one shade to another | Returns a rendered linear top-to-bottom [gradient image](gradient.html) using the specified image size.  
HALD | R | Identity Hald CLUT Image | Select order with filename, e.g. hald:5 for order 5.  
HISTOGRAM | W | Histogram of the image | The histogram includes the unique colors of the image as an image comment. If you have no need for the unique color list, use `-define histogram:unique-colors=false` to forego this expensive operation.  
LABEL | R | Text image format | Specify the desired text as the filename (e.g. `label:"This a label"`).  
MAP | RW | Colormap intensities and indices | Set -depth to set the sample size of the intensities; indices are 16-bit if colors > 256.  
MASK | RW | Image mask |   
MATTE | W | MATTE format | Write only.  
NULL | RW | NULL image | Useful for creating blank tiles with [montage](montage.html) (use `NULL:`). Also useful as an output format when evaluating image read performance.  
PANGO | R | Image caption | You can configure the caption layout with these defines: `-define pango:auto-dir=`true/false, `-define pango:ellipsize=`start/middle/end, `-define pango:gravity-hint=`natural/strong/line, `-define pango:hinting=`none/auto/full, `-define pango:indent=`points, `-define pango:justify=`true/false, `-define pango:language=`en_US/etc, `-define pango:markup=`true/false, `-define pango:single-paragraph=`true/false and `-define pango:wrap=`word/char/word-char.  
PLASMA | R | Plasma fractal image |   
PREVIEW | W | Show a preview an image enhancement, effect, or f/x | Creates a preview montage of images prepared over a parametric range in order to assist with parameter selection. Specify the desired preview type via the -preview option).  
PRINT | W | Send image to your computer printer | Unix users may set the PRINTER (for 'lpr') or LPDEST (for 'lp') environment variables to select the desired printer.  
SCAN | R | Import image from a scanner device | Requires [SANE](http://www.sane-project.org/) Specify the device name and path as the filename (e.g. `scan:'hpaio:/usb/Officejet_6200_series?serial=CN4ATCE3G20453'`).  
RADIAL_GRADIENT | R | Gradual radial passing from one shade to another | Returns a rendered radial top-to-bottom [gradient image](gradient.html) using the specified image size.  
SCANX | R | Import image from the default scanner device |   
SCREENSHOT | R | an image that shows the contents of a computer display |   
STEGANO | R | Steganographic image | Use [-size](command-line-options.html#size) command line option to specify width, height, and offset of the steganographic image  
TILE | R | Tiled image | Create a tiled version of an image at by tiling a image. Use [-size](command-line-options.html#size) to specify the tiled image size. Tiles are composited on an image background and therefore is responsive to the [-compose](command-line-options.html#compose) option. The image is specified similar to `TILE:image.miff`.  
UNIQUE | W | Write only unique pixels to the image file. |   
VID | RW | Visual Image Directory | Used to create a thumbnailed directory (tiled thumbnails) of a set of images which may be used to select images to view via the [display](display.html) program, or saved to a [MIFF](formats.html#MIFF) or [SHTML](formats.html#SHTML) file.  
WIN | RW | Select image from or display image to your computer screen | Only supported under Microsoft Windows.  
X | RW | Select image from or display image to your X server screen | Also see the [import](import.html) and [display](display.html) programs.  
XC | R | Canvas image of specified color | An backward compatible alias for the '`canvas:`' psuedo-file format, used to create a solid color canvas image.   
  
## Built-in Images

ImageMagick includes a number of built-in (embedded) images which may be referenced as if they were an image file. The `magick:` format tag may be used via the syntax `magick:`name to request an embedded image (e.g. `magick:logo`). For backwards compatibility, the image specifications `GRANITE:`, `LOGO:`, `NETSCAPE:`, and `ROSE:` may also be used to request images with those names.

Tag | Mode | Description | Notes  
---|---|---|---  
GRANITE | R | 128x128 granite texture pattern | ![GRANITE](../images/granite.png)  
[LOGO](../images/logo.png) | R | ImageMagick Logo, 640x480 | ![Logo](../images/logo.jpg)  
NETSCAPE | R | image using colors in Netscape 216 (6x6x6 ) color cube, 216x144 | Most commonly used with the [convert](convert.html) and [mogrify](mogrify.html) programs with the [-map](command-line-options.html#map) option to create web safe images.  
ROSE | R | Picture of a rose, 70x46 | ![ROSE](../images/rose.png)  
[WIZARD](../images/wizard.png) | R | ImageMagick Wizard, 480x640 | ![Logo](../images/wizard.jpg)  
  
## Built-in Patterns

ImageMagick includes a number of built-in (embedded) patterns which may be referenced as if they were an image file. The `pattern:` format tag may be used via the syntax `pattern:`name to request an embedded pattern (e.g. `pattern:checkerboard`). The pattern size is controlled with the [-size](command-line-options.html#size) command line option.

Tag | Mode | Description | Notes  
---|---|---|---  
BRICKS | R | brick pattern, 16x16 | ![BRICKS](../images/patterns/bricks.png)  
CHECKERBOARD | R | checkerboard pattern, 30x30 | ![CHECKERBOARD](../images/patterns/checkerboard.png)  
CIRCLES | R | circles pattern, 16x16 | ![CIRCLES](../images/patterns/circles.png)  
CROSSHATCH | R | crosshatch pattern, 8x4 | ![CROSSHATCH](../images/patterns/crosshatch.png)  
CROSSHATCH30 | R | crosshatch pattern with lines at 30 degrees, 8x4 | ![CROSSHATCH30](../images/patterns/crosshatch30.png)  
CROSSHATCH45 | R | crosshatch pattern with lines at 45 degrees, 8x4 | ![CROSSHATCH45](../images/patterns/crosshatch45.png)  
FISHSCALES | R | fish scales pattern, 16x8 | ![FISHSCALES](../images/patterns/fishscales.png)  
GRAY0 | R | 0% intensity gray, 32x32 | ![GRAY0](../images/patterns/gray0.png)  
GRAY5 | R | 5% intensity gray, 32x32 | ![GRAY5](../images/patterns/gray5.png)  
GRAY10 | R | 10% intensity gray, 32x32 |  ![GRAY10](../images/patterns/gray10.png)  
GRAY15 | R | 15% intensity gray, 32x32 | ![GRAY15](../images/patterns/gray15.png)  
GRAY20 | R | 20% intensity gray, 32x32 | ![GRAY20](../images/patterns/gray20.png)  
GRAY25 | R | 25% intensity gray, 32x32 | ![GRAY25](../images/patterns/gray25.png)  
GRAY30 | R | 30% intensity gray, 32x32 | ![GRAY30](../images/patterns/gray30.png)  
GRAY35 | R | 35% intensity gray, 32x32 | ![GRAY35](../images/patterns/gray35.png)  
GRAY40 | R | 40% intensity gray, 32x32 | ![GRAY40](../images/patterns/gray40.png)  
GRAY45 | R | 45% intensity gray, 32x32 | ![GRAY45](../images/patterns/gray45.png)  
GRAY50 | R | 50% intensity gray, 32x32 | ![GRAY50](../images/patterns/gray50.png)  
GRAY55 | R | 55% intensity gray, 32x32 | ![GRAY55](../images/patterns/gray55.png)  
GRAY60 | R | 60% intensity gray, 32x32 | ![GRAY60](../images/patterns/gray60.png)  
GRAY65 | R | 65% intensity gray, 32x32 | ![GRAY65](../images/patterns/gray65.png)  
GRAY70 | R | 70% intensity gray, 32x32 | ![GRAY70](../images/patterns/gray70.png)  
GRAY75 | R | 75% intensity gray, 32x32 | ![GRAY75](../images/patterns/gray75.png)  
GRAY80 | R | 80% intensity gray, 32x32 |  ![GRAY80](../images/patterns/gray80.png)  
GRAY85 | R | 85% intensity gray, 32x32 | ![GRAY85](../images/patterns/gray85.png)  
GRAY90 | R | 100% intensity gray, 32x32 | ![GRAY90](../images/patterns/gray90.png)  
GRAY95 | R | 100% intensity gray, 32x32 | ![GRAY95](../images/patterns/gray95.png)  
GRAY100 | R | 100% intensity gray, 32x32 | ![GRAY100](../images/patterns/gray100.png)  
HEXAGONS | R | hexagon pattern, 30x18 | ![HEXAGONS](../images/patterns/hexagons.png)  
HORIZONTAL | R | horizontal line pattern, 8x4 | ![HORIZONTAL](../images/patterns/horizontal.png)  
HORIZONTAL2 | R | horizontal line pattern, 8x8 | ![HORIZONTAL2](../images/patterns/horizontal2.png)  
HORIZONTAL3 | R | horizontal line pattern, 9x9 | ![HORIZONTAL3](../images/patterns/horizontal3.png)  
HORIZONTALSAW | R | horizontal saw-tooth pattern, 16x8 | ![HORIZONTALSAW](../images/patterns/horizontalsaw.png)  
HS_BDIAGONAL | R | backward diagonal line pattern (45 degrees slope), 8x8 | ![HS_BDIAGONAL](../images/patterns/hs_bdiagonal.png)  
HS_CROSS | R | cross line pattern, 8x8 | ![HS_CROSS](../images/patterns/hs_cross.png)  
HS_DIAGCROSS | R | diagonal line cross pattern (45 degrees slope), 8x8 | ![HS_DIAGCROSS](../images/patterns/hs_diagcross.png)  
HS_FDIAGONAL | R | forward diagonal line pattern (45 degrees slope), 8x8 | ![HS_FDIAGONAL](../images/patterns/hs_fdiagonal.png)  
HS_HORIZONTAL | R | horizontal line pattern, 8x8 | ![HS_HORIZONTAL](../images/patterns/hs_horizontal.png)  
HS_VERTICAL | R | vertical line pattern, 8x8 | ![HS_VERTICAL](../images/patterns/hs_vertical.png)  
LEFT30 | R | forward diagonal pattern (30 degrees slope), 8x4 | ![LEFT0](../images/patterns/left30.png)  
LEFT45 | R | forward diagonal line pattern (45 degrees slope), 8x8 | ![LEFT45](../images/patterns/left45.png)  
LEFTSHINGLE | R | left shingle pattern, 24x24 | ![LEFTSHINGLE](../images/patterns/leftshingle.png)  
OCTAGONS | R | octagons pattern, 16x16 | ![OCTAGONS](../images/patterns/octagons.png)  
RIGHT30 | R | backward diagonal line pattern (30 degrees) 8x4 | ![RIGHT30](../images/patterns/right30.png)  
RIGHT45 | R | backward diagonal line pattern (30 degrees), 8x8 | ![RIGHT45](../images/patterns/right45.png)  
RIGHTSHINGLE | R | right shingle pattern, 24x24 | ![RIGHTSHINGLE](../images/patterns/rightshingle.png)  
SMALLFISHSCALES | R | small fish scales pattern, 8x8 | ![SMALLFISHSCALES](../images/patterns/smallfishscales.png)  
VERTICAL | R | vertical line pattern, 8x8 | ![VERTICAL](../images/patterns/vertical.png)  
VERTICAL2 | R | vertical line pattern, 8x8 | ![VERTICAL2](../images/patterns/vertical2.png)  
VERTICAL3 | R | vertical line pattern, 9x9 | ![VERTICAL3](../images/patterns/vertical3.png)  
VERTICALBRICKS | R | vertical brick pattern, 16x16 | ![VERTICALBRICKS](../images/patterns/verticalbricks.png)  
VERTICALLEFTSHINGLE | R | vertical left shingle pattern, 24x24 | ![VERTICALLEFTSHINGLE](../images/patterns/verticalleftshingle.png)  
VERTICALRIGHTSHINGLE | R | vertical right shingle pattern, 24x24 | ![VERTICALRIGHTSHINGLE](../images/patterns/verticalrightshingle.png)  
VERTICALSAW | R | vertical saw-tooth pattern, 8x16 | ![VERTICALSAW](../images/patterns/verticalsaw.png)  
  
## Embedded Image Profiles

ImageMagick provides a number of format identifiers which are used to add, remove, and save embedded profiles for images which can support embedded profiles. Image types which may contain embedded profiles are TIFF, JPEG, and PDF.

Tag | Mode | Description | Notes  
---|---|---|---  
8BIM | RW | Photoshop resource format (binary) |   
8BIMTEXT | RW | Photoshop resource format (ASCII) | An ASCII representation of the 8BIM format.  
APP1 | RW | Raw application information |   
APP1JPEG | RW | Raw JPEG binary data | Profile in JPEG wrapper.  
ICC | RW | International Color Consortium color profile | Also known as `ICM`. To read, use [-profile](command-line-options.html#profile) with [convert](convert.html).  
IPTC | RW | IPTC Newsphoto (binary) | To read, use [-profile](command-line-options.html#profile) with [convert](convert.html)  
IPTCTEXT | RW | IPTC Newsphoto (ASCII) | An ASCII representation of the IPTC format.  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](formats.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
