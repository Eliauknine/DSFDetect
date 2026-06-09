[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[MIFF Header](miff.html#miff-header) • [MIFF Binary Data](miff.html#binary)

The Magick Image File Format (MIFF) is ImageMagick's own platform-independent format for storing bitmap images. It has an advantage over other image formats in that it stores all metadata known to ImageMagick (e.g. image color profiles, comments, author, copyright, etc.), whereas, other formats may only support a small portion of available metadata or none at all. A MIFF image file consist of two sections. The first section is a header composed of keys describing the image in text form. The next section is the binary image data. We discuss these sections in detail below.

## MIFF Header

The MIFF header is composed entirely of ISO-8859-1 characters. The fields in the header are key and value combination in the key = value format, with each key and value separated by an equal sign (`=`). Each key = value combination is delimited by at least one control or whitespace character. Comments may appear in the header section and are always delimited by braces. The MIFF header always ends with a colon (`:`) character, followed by a ctrl-Z character. It is also common to proceed the colon with a formfeed and a newline character. The formfeed prevents the listing of binary data when using the `more` Unix program, whereas, the ctrl-Z has the same effect with the `type` command on the Windows command line.

The following is a partial list of  key = value combinations that are typically be found in a MIFF file:

background-color = color |   
---|---  
border-color = color |   
matte-color = color | these optional keys reflect the image background, border, and matte colors respectively. A [color](color.html) can be a name (e.g. white) or a hex value (e.g. #ccc).  
class = { DirectClass, PseudoClass } | the type of binary pixel data stored in the MIFF file. If this key is not present, DirectClass pixel data is assumed.  
colors =  value | the number of colors in a DirectClass image. For a PseudoClass image, this key specifies the number of entries in the colormap. If this key is not present in the header, and the image is PseudoClass, a linear 256 color grayscale colormap is assumed. The maximum number of colormap entries is 65536.  
colorspace = { RGB, CMYK, ... } | the colorspace of the pixel data. The default is RGB.  
columns = value | the width of the image in pixels. This a required key and has no default value.  
compression = {BZip, None, Zip, ... } | the type of algorithm used to compress the image data. If this key is not present, the pixel data is assumed to be uncompressed.  
delay = microseconds | the interframe delay in an image sequence in microseconds.  
depth = { 8, 16, 32 } | the depth of a single color value representing values from 0 to 255 (depth 8), 0 - 65535 (depth 16), or 0 - 4294967295 (depth 32). If this key is absent, a depth of 8 is assumed.  
dispose = value | layer disposal method. Here are the valid values: 

    0. No disposal specified.
    1. Do not dispose between frames.
    2. Overwrite frame with background color from header.
    3. Overwrite with previous frame.

  
gamma = value | the gamma of the image. If it is not specified, a gamma of 1.0 (linear brightness response) is assumed.  
id = ImageMagick | identifies the file as a MIFF-format image file. This key is required and has no default. Although this key can appear anywhere in the header, it should start as the first key of the header in column 1. This will allow programs like `file`(1) to easily identify the file as MIFF.  
iterations = value | the number of times an image sequence loops before stopping.  
label = { string ] | defines a short title or caption for the image. If any whitespace appears in the label, it must be enclosed within braces.  
matte = { True, False } | specifies whether a the image has matte data. Matte data is generally useful for image compositing.  
montage = <width>x<height>[+-]<x offset>[+-]<y offset> | size and location of the individual tiles of a composite image. Use this key when the image is a composite of a number of different tiles. A tile consists of an image and optionally a border and a label. Width is the size in pixels of each individual tile in the horizontal direction and height is the size in the vertical direction. Each tile must have an equal number of pixels in width and equal in height. However, the width can differ from the height. X offset is the offset in number of pixels from the vertical edge of the composite image where the first tile of a row begins and y offset is the offset from the horizontal edge where the first tile of a column begins. If this key is specified, a directory of tile names must follow the image header. The format of the directory is explained below.  
page = value | preferred size and location of an image canvas.  
profile-icc = value | the number of bytes in the International Color Consortium color profile. The profile is defined by the ICC profile specification located at <http://www.color.org/icc_specs2.html>.  
red-primary = x,y |  | green-primary = x,y |   
blue-primary = x,y |  | white-point = x,y | this optional key reflects the chromaticity primaries and white point.  
rendering-intent = { saturation, perceptual, absolute, relative } | Rendering intent is the CSS-1 property that has been defined by the International Color Consortium (<http://www.color.org>).  
resolution = <x-resolution>x<y-resolution> | vertical and horizontal resolution of the image. See units for the specific resolution units (e.g. pixels per inch).  
rows = value | the height of the image in pixels. This a required key and has no default value.  
scene = value | the sequence number for this MIFF image file. This optional key is useful when a MIFF image file is one in a sequence of files used in an animation.  
signature = value | this optional key contains a string that uniquely identifies the image pixel contents. NIST's SHA-256 message digest algorithm is recommended.  
units = { pixels-per-inch, pixels-per-centimeter } | image resolution units.  
  
Other key value pairs are permitted. If a value contains whitespace it must be enclosed with braces as illustrated here:
    
    
    id=ImageMagick
    class=PseudoClass  colors=256  matte=False
    columns=1280  rows=1024  depth=8
    compression=RLE
    colorspace=RGB
    copyright={Copyright (c) 1999-2016 ImageMagick Studio LLC}
    ⋮
    

Note that key = value combinations may be separated by newlines or spaces and may occur in any order within the header. Comments (within braces) may appear anywhere before the colon.

If you specify the montage key in the header, follow the header with a directory of image tiles. This directory consists of a name for each tile of the composite image separated by a newline character. The list is terminated with a NULL character.

If you specify the color-profile key in the header, follow the header (or montage directory if the montage key is in the header) with the binary color profile.

The header is separated from the image data by a `:` character immediately followed by a newline.

## MIFF Binary Data

Next comes the binary image data itself. How the image data is formatted depends upon the class of the image as specified (or not specified) by the value of the class key in the header.

DirectClass images are continuous-tone, images stored as RGB (red, green, blue), RGBA (red, green, blue, alpha), CMYK (cyan, yellow, magenta, black), or CMYKA (cyan, yellow, magenta, black, alpha) intensity values as defined by the colorspace key. Each intensity value is one byte in length for images of depth 8 (0..255), two bytes for a depth of 16 (0..65535), and images of depth 32 (0..4294967295) require four bytes in most significant byte first order.

PseudoClass images are colormapped RGB images. The colormap is stored as a series of red, green, and blue pixel values, each value being a byte in size. If the image depth is 16, each colormap entry consumes two bytes with the most significant byte being first. The number of colormap entries is defined by the colors key. The colormap data occurs immediately following the header (or image directory if the montage key is in the header). PseudoClass image data is an array of index values into the color map. If there are 256 or fewer colors in the image, each byte of image data contains an index value. If the image contains more than 256 colors or the image depth is 16, the index value is stored as two contiguous bytes with the most significant byte being first. If matte is true, each colormap index is followed by a 1 or 2-byte alpha value.

The image pixel data in a MIFF file may be uncompressed, runlength encoded, Zip compressed, or BZip compressed. The compression key in the header defines how the image data is compressed. Uncompressed pixels are stored one scanline at a time in row order. Runlength-encoded compression counts runs of identical adjacent pixels and stores the pixels followed by a length byte (the number of identical pixels minus 1). Zip and BZip compression compresses each row of an image and precedes the compressed row with the length of compressed pixel bytes as a word in most significant byte first order.

MIFF files may contain more than one image. Simply concatenate each individual image (composed of a header and image data) into one file.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](miff.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
