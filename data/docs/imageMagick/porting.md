[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ImageMagick Version 7](porting.html#imv7) • [High Dynamic Range Imaging](porting.html#hdri) • [Pixel Channels](porting.html#channels) • [Alpha](porting.html#alpha) • [Grayscale](porting.html#grayscale) • [Masks](porting.html#mask) • [MagickCore API](porting.html#core) • [Header Files](porting.html#headers) • [Deprecated Features Removed](porting.html#deprecate) • [Command-line Interface](porting.html#cli) • [Version 7 Change Summary](porting.html#summary)

The design of ImageMagick is an evolutionary process, with the design and implementation efforts serving to influence and guide further progress in the other. With ImageMagick version 7 we aim to improve the design based on lessons learned from the version 6 implementation. ImageMagick was originally designed to display RGB images to an X Windows server. Over time we extended support to RGBA images and then to the CMYK and CMYKA image format. With ImageMagick version 7, we extend support to arbitrary colorspaces with an arbitrary number of pixel channels. Other design changes are in the works and we will document them here so be sure to revisit periodically.

To support variable pixel channels in the MagickCore API, pixel handling has changed when getting or setting the pixel channels. You can access channels as an array, pixel[i], or use an accessor method such as GetPixelRed() or SetPixelRed(). There are some modest changes to the MagickCore and MagickWand API's. The Magick++ and PerlMagick API's have not changed and matches that of the ImageMagick version 6.

The shell API (command line) of ImageMagick version 7 is also undergoing a major overhaul, with specific emphasis on the ability to read 'options' not only from the command line, but also from scripts, and file streams. This allows for the use of 'co-processing' programming techniques or performing image handling using 'deamon/server backends', and even multi-machine distributed processing.

With shell API overhaul other improvements are being made, including: better reporting of which option failed, the consolidation and deprecation of options, and more global use of 'image properties' (more commonly known as 'percent escapes' in option arguments. 

ImageMagick version 7 is available now as an [Beta](http://www.imagemagick.org/download/beta/) release. Look for an official release around 1st Q 2016. An official ImageMagick version 7 release depends on how smoothly the Beta cycle progresses. During the Beta cycle, version 6 developers can attempt to port their software to version 7.

Once ImageMagick version 7 is released, we will continue to support and enhance version 6 for a minimum of 10 years.

## High Dynamic Range Imaging

ImageMagick version 7 enables [high dynamic range imaging](high-dynamic-range.html) (HDRI) by default. HDRI accurately represents the wide range of intensity levels found in real scenes ranging from the brightest direct sunlight to the deepest darkest shadows. In addition, image processing results are more accurate. The disadvantage is it requires more memory and may result in slower processing times. If you see differences in the results of your version 6 command-line with version 7, it is likely due to HDRI. You may need to add `-clamp` to your command-line to constrain pixels to the 0 .. QuantumRange range, or disable HDRI when you build ImageMagick version 7. To disable HDRI (recommended for smart phone builds such as iOS or production sites where performance is a premium), simply add `--disable-hdri` to the configure script command line when building ImageMagick.

## Pixel Channels

A pixel is comprised of one or more color values, or channels (e.g. red pixel channel).

Prior versions of ImageMagick (4-6), support 4 to 5 pixel channels (RGBA or CMYKA). The first 4 channels are accessed with the PixelPacket data structure. The structure includes 4 members of type Quantum (typically 16-bits) of red, green, blue, and opacity. The black channel or colormap indexes are supported by a separate method and structure, IndexPacket. As an example, here is a code snippet from ImageMagick version 6 that negates the color components (but not the alpha component) of the image pixels:

` for (y=0; y < (ssize_t) image->rows; y++) { register IndexPacket *indexes; register PixelPacket *q; q=GetCacheViewAuthenticPixels(image_view,0,y,image->columns,1,exception); if (q == (PixelPacket *) NULL) { status=MagickFalse; continue; } indexes=GetCacheViewAuthenticIndexQueue(image_view); for (x=0; x < (ssize_t) image->columns; x++) { if ((channel & RedChannel) != 0) q->red=(Quantum) QuantumRange-q->red; if ((channel & GreenChannel) != 0) q->green=(Quantum) QuantumRange-q->green; if ((channel & BlueChannel) != 0) q->blue=(Quantum) QuantumRange-q->blue; if (((channel & IndexChannel) != 0) && (image->colorspace == CMYKColorspace)) indexes[x]=(IndexPacket) QuantumRange-indexes[x]; q++; } if (SyncCacheViewAuthenticPixels(image_view,exception) == MagickFalse) status=MagickFalse; } `

ImageMagick version 7 supports any number of channels from 1 to 32 (and beyond) and simplifies access with a single method that returns an array of pixel channels of type Quantum. Source code that compiles against prior versions of ImageMagick requires refactoring to work with ImageMagick version 7. We illustrate with an example. Let's naively refactor the version 6 code snippet from above so it works with the ImageMagick version 7 API:

` for (y=0; y < (ssize_t) image->rows; y++) { register Quantum *q; q=GetCacheViewAuthenticPixels(image_view,0,y,image->columns,1,exception); if (q == (Quantum *) NULL) { status=MagickFalse; continue; } for (x=0; x < (ssize_t) image->columns; x++) { if ((GetPixelRedTraits(image) & UpdatePixelTrait) != 0) SetPixelRed(image,QuantumRange-GetPixelRed(image,q),q); if ((GetPixelGreenTraits(image) & UpdatePixelTrait) != 0) SetPixelGreen(image,QuantumRange-GetPixelGreen(image,q),q); if ((GetPixelBlueTraits(image) & UpdatePixelTrait) != 0) SetPixelBlue(image,QuantumRange-GetPixelBlue(image,q),q); if ((GetPixelBlackTraits(image) & UpdatePixelTrait) != 0) SetPixelBlack(image,QuantumRange-GetPixelBlack(image,q),q); if ((GetPixelAlphaTraits(image) & UpdatePixelTrait) != 0) SetPixelAlpha(image,QuantumRange-GetPixelAlpha(image,q),q); q+=GetPixelChannels(image); } if (SyncCacheViewAuthenticPixels(image_view,exception) == MagickFalse) status=MagickFalse; }  `

Let's do that again but take full advantage of the new variable pixel channel support:

` for (y=0; y < (ssize_t) image->rows; y++) { register Quantum *q; q=GetCacheViewAuthenticPixels(image_view,0,y,image->columns,1,exception); if (q == (Quantum *) NULL) { status=MagickFalse; continue; } for (x = 0; x < (ssize_t) image->columns; x++) { register ssize_t i; if (GetPixelReadMask(image,q) == 0) { q+=GetPixelChannels(image); continue; } for (i=0; i < (ssize_t) GetPixelChannels(image); i++) { PixelChannel channel=GetPixelChannelChannel(image,i); PixelTrait traits=GetPixelChannelTraits(image,channel); if ((traits & UpdatePixelTrait) == 0) continue; q[i]=QuantumRange-q[i]; } q+=GetPixelChannels(image); } if (SyncCacheViewAuthenticPixels(image_view,exception) == MagickFalse) status=MagickFalse; }  `

Note, how we use GetPixelChannels() to advance to the next set of pixel channels.

The colormap indexes and black pixel channel (for the CMYK colorspace) are no longer stored in the index channel, previously accessed with GetAuthenticIndexQueue() and GetCacheViewAuthenticIndexQueue(). Instead they are now a first class pixel channel and accessed as a member of the pixel array (e.g. `pixel[4]`) or with the convenience pixel accessor methods GetPixelIndex(), SetPixelIndex(), GetPixelBlack(), and SetPixelBlack().

As a consequence of using an array structure for variable pixel channels, auto-vectorization compilers have additional opportunities to speed up pixel loops.

#### Pixel Accessors

You can access pixel channel as array elements (e.g. `pixel[1]`) or use convenience accessors to get or set pixel channels:
    
    
    GetPixela()                  SetPixela()
    GetPixelAlpha()              SetPixelAlpha()
    GetPixelb()                  SetPixelb()
    GetPixelBlack()              SetPixelBlack()
    GetPixelBlue()               SetPixelBlue()
    GetPixelCb()                 SetPixelCb()
    GetPixelCr()                 SetPixelCr()
    GetPixelCyan()               SetPixelCyan()
    GetPixelGray()               SetPixelGray()
    GetPixelGreen()              SetPixelGreen()
    GetPixelIndex()              SetPixelIndex()
    GetPixelL()                  SetPixelL()
    GetPixelMagenta()            SetPixelMagenta()
    GetPixelReadMask()           SetPixelReadMask()
    GetPixelWriteMask()          SetPixelWriteMask()
    GetPixelMetacontentExtent()  SetPixelMetacontentExtent()
    GetPixelOpacity()            SetPixelOpacity()
    GetPixelRed()                SetPixelRed()
    GetPixelYellow()             SetPixelYellow()
    GetPixelY()                  SetPixelY()
    

You can find these accessors defined in the header file, `MagickCore/pixel-accessor.h`

#### Pixel Traits

Each pixel channel includes one or more of these traits:

Undefined
    no traits associated with this pixel channel
Copy
    do not update this pixel channel, just copy it
Update
    update this pixel channel
Blend
    blend this pixel channel with the alpha mask if it's enabled

We provide these methods to set and get pixel traits:
    
    
    GetPixelAlphaTraits()    SetPixelAlphaTraits()
    GetPixelBlackTraits()    SetPixelBlackTraits()
    GetPixelBlueTraits()     SetPixelBlueTraits()
    GetPixelCbTraits()       SetPixelCbTraits()
    GetPixelChannelTraits()  SetPixelChannelTraits()
    GetPixelCrTraits()       SetPixelCrTraits()
    GetPixelGrayTraits()     SetPixelGrayTraits()
    GetPixelGreenTraits()    SetPixelGreenTraits()
    GetPixelIndexTraits()    SetPixelIndexTraits()
    GetPixelMagentaTraits()  SetPixelMagentaTraits()
    GetPixelRedTraits()      SetPixelRedTraits()
    GetPixelYellowTraits()   SetPixelYellowTraits()
    GetPixelYTraits()        SetPixelYTraits()
    

For convenience you can set the active trait for a set of pixel channels with a channel mask and this method:
    
    
    SetImageChannelMask()
    

Previously MagickCore methods had channel analogs, for example, NegateImage() and NegateImageChannels(). The channel analog methods are no longer necessary because the pixel channel traits specify whether to act on a particular pixel channel or whether to blend with the alpha mask. For example, instead of
    
    
    NegateImageChannel(image,channel);
    

we use:
    
    
    channel_mask=SetImageChannelMask(image,channel);
    NegateImage(image,exception);
    (void) SetImageChannelMask(image,channel_mask);
    

#### Pixel User Channels

In version 7, we introduce pixel user channels. Traditionally we utilize 4 channels, red, green, blue, and alpha. For CMYK we also have a black channel. User channels are designed to contain whatever additional channel information that makes sense for your application. Some examples include extra channels in TIFF or PSD images or perhaps you require a channel with infrared information for the pixel. You can associate traits with the user channels so that they when they are acted upon by an image processing algorithm (e.g. blur) the pixels are copied, acted upon by the algorithm, or even blended with the alpha channel if that makes sense.

#### Pixel Metacontent

In version 7, we introduce pixel metacontent. Metacontent is content about content. So rather than being the content itself, it's something that describes or is associated with the content. Here the content is a pixel. The pixel metacontent is for your exclusive use (internally the data is just copied, it is not modified) and is accessed with these MagickCore API methods:
    
    
    SetImageMetacontentExtent()
    GetImageMetacontentExtent()
    GetVirtualMetacontent()
    GetAuthenticMetacontent()
    GetCacheViewAuthenticMetacontent()
    GetCacheViewVirtualMetacontent()
    

## Alpha

We support alpha now, previously opacity. With alpha, a value of `0` means that the pixel does not have any coverage information and is transparent; i.e. there was no color contribution from any geometry because the geometry did not overlap this pixel. A value of `QuantumRange` means that the pixel is opaque because the geometry completely overlapped the pixel. As a consequence, in version 7, the PixelInfo structure member alpha has replaced the previous opacity member. Another consequence is the alpha part of a sRGB value in hexadecimal notation is now reversed (e.g. #0000 is fully transparent).

## Colorspace

The `Rec601Luma` and `Rec709Luma` colorspaces are no longer supported. Instead, specify the `gray` colorspace and choose from these intensity options:
    
    
    Rec601Luma
    Rec601Luminance
    Rec709Luma
    Rec709Luminance
    

For example,
    
    
    convert myImage.png -intensity Rec709Luminance -colorspace gray myImage.jpg
    

## Grayscale

Previously, grayscale images were Rec601Luminance and consumed 4 channels: red, green, blue, and alpha. With version 7, grayscale consumes only 1 channel requiring far less resources as a result.

## Masks

Version 7 supports masks for most image operators. As an example, here are two methods to compute the statistics of any pixel selected by the image mask:
    
    
    identify -verbose -clip statue.tif
    identify -verbose -read-mask mask.png statue.tif
    

## MagickCore API

Here are a list of changes to the MagickCore API:

  * Almost all image processing algorithms are now channel aware.
  * The MagickCore API adds an `ExceptionInfo` argument to those methods that lacked it in version 6, e.g. `NegateImage(image,MagickTrue,exception`);
  * All method channel analogs have been removed (e.g. BlurImageChannel()), they are no longer necessary, use pixel traits instead.
  * Public and private API calls are now declared with the GCC visibility attribute. The MagickCore and MagickWand dynamic libraries now only export public struct and function declarations.
  * The InterpolatePixelMethod enum is now PixelInterpolateMethod.
  * The IntegerPixel storage type is removed (use LongPixel instead) and LongLongPixel is added
  * Image signatures have changed to account for variable pixel channels.
  * All color packet structures, PixelPacket, LongPacket, and DoublePacket, are consolidated to a single color structure, PixelInfo.
  * The ChannelMoments structure member `I` is now `invariant`. `I` conflicts with the `complex.h` header.
  * We added a length parameter to FormatMagickSize() to permit variable length buffers.



## MagickWand API

Here are a list of changes to the MagickWand API:

  * The DrawMatte() method is now called DrawAlpha().
  * The MagickSetImageBias() and MagickSetImageClipMask() methods are no longer supported.



## Header Files

Prior versions of ImageMagick (4-6) reference the ImageMagick header files as `magick/` and `wand/`. ImageMagick 7 instead uses `MagickCore/` and `MagickWand/` respectively. For example,
    
    
    #include <MagickCore/MagickCore.h>
    #include <MagickWand/MagickWand.h>

## Deprecated Features Removed

All deprecated features from ImageMagick version 6 are removed in version 7. These include the `Magick-config` and `Wand-config` configuration utilities. Instead use:
    
    
    MagickCore-config
    MagickWand-config
    

The FilterImage() method has been removed. Use ConvolveImage() instead.

In addition, all deprecated [MagickCore](http://magick.imagemagick.org/api/deprecate.html) and [MagickWand](http://magick.imagemagick.org/api/magick-deprecate.html) methods are no longer available in version 7.

## Shell API or Command-line Interface

As mentioned the primary focus of the changes to the Shell API or Command Line Interface is the abstraction so that not only can options be read from command line arguments, but also from a file (script) or from a file stream (interactive commands, or co-processing). 

To do this the CLI parser needed to be re-written, so as to always perform all options, in a strict, do-it-as-you-see it order. Previously in IMv6 options were performed in groups (known as 'FireOptions), this awkwardness is now gone. However the strict order means that you can no longer give operations before providing an image for the operations to work on. To do so will now produce an error. 

Error reporting is now reporting exactly which option (by argument count on command line, or line,column in scripts) caused the 'exception'. This is not complete as yet but getting better. Also not complete is 'regard-warnings' handling or its replacement, which will allow you to ignore reported errors and continue processing (as appropriate due to error) in co-processes or interactive usage. 

The parenthesis options used to 'push' the current image list, and image settings (EG: '`(`' and '`)`' ) on to a stack now has a completely separate image settings stack. That is parenthesis 'push/pull' image lists, and curly braces (EG: '`{`' and '`}`' ) will 'push/pull' image settings. 

Of course due to the previously reported changes to the underlying channel handling will result be many side effects to almost all options. Here are some specific 

Most algorithms update the red, green, blue, black (for CMYK), and alpha channels. Most operators will blend alpha the other color channels, but other operators (and situations) may require this blending to be disabled, and is currently done by removing alpha from teh active channels via `-channel` option. (e.g. `convert castle.gif -channel RGB -negate castle.png`). 

Reading gray-scale images generate an image with only one channel. If that image is to then accept color the `-colorspace` setting needs to be applied to expand the one channel into separate RGB (or other) channels. 

Previously, command-line arguments were limited to 4096 characters, with ImageMagick version 7 the limit has increased to 131072 characters.

### Command Changes

Here are a list of changes to the ImageMagick commands:

magick
    The "`magick`" command is the new primary command of the Shell API, replacing the old "`convert`" command. This allows you to create a 'magick script' of the form "`#!/path/to/command/magick -script`", or pipe options into a command "`magick -script -`, as abackground process. 
magick-script
    This the same as "`magick`", (only command name is different) but which has an implicit "`-script`" option. This allows you to use it in an "`env`" style script form. That is a magick script starts with the 'she-bang' line of "`#!/usr/bin/env magick-script`" allowing the script interpreter to be found anywhere on the users command "`PATH`". This is required to get around a "one argument she-bang bug" that is common on most UNIX systems (including Linux, but not MacOSX).
animate, compare, composite, conjure, convert, display, identify, import, mogrify, montage, stream
    To reduce the footprint of the command-line utilities, these utilities are symbolic links to the `magick` utility. You can also invoke them from the `magick` utility, for example, use `magick convert logo: logo.png` to invoke the `convert` utility.

### Behavioral Changes

Image settings are applied to each image on the command line. To associate a setting with a particular image, use parenthesis to remove ambiguity. In this example we assign a unique page offset to each image:
    
    
    convert \( -page +10+20 first.png \) \( -page +100+200 second.png \) ...
    

By default, image operations such as convolution blends alpha with each channel. To convolve each channel independently, deactivate the alpha channel as follows:
    
    
    convert ... -alpha discrete -blur 0x1 ...
    

To remove the alpha values from your image, use `-alpha off`.

Some options have changed in ImageMagick version 7. These include:

+combine
    This option now requires an argument, the image colorspace (e.g. +combine sRGB).

### New Options

ImageMagick version 7 supports these new options, though most are limited to the "`magick`" command, or to use in "`magick`" scripts.

{ ... }
    Save (and restore) the current image settings (internally known as the "image_info" structure). This is automatically done with parenthesis (EG: '`(`' and '`)`') is "`-regard-parenthesis`" has been set, just as in IMv6. Caution is advised to prevent un-balanced braces errors.
\--
    End of options, to be used in IMv7 "`mogrify`" command to explicitly separate the operations to be applied and the images that are to be processed 'in-place'. (not yet implemented). However if not provided, "`-read`" can still be used to differentiate secondary image reads (for use in things like alpha composition) from the 'in-place' image being processed. 
    In other commands (such as "magick") it is equivalent to a explicit "`-read`" (see below) of the next option as a image (as it was in IMv6). 
-alpha discrete
    treat the alpha channel independently (do not blend).
-channel-fx expression
    

exchange, extract, or copy one or more image channels.

The expression consists of one or more channels, either mnemonic or numeric (e.g. red or 0, green or 1, etc.), separated by certain operation symbols as follows:
    
    
    <=>  exchange two channels (e.g. red<=>blue)
    =>   copy one channel to another channel (e.g. red=>green)
    =    assign a constant value to a channel (e.g. red=50%)
    ,    write new image with channels in the specified order (e.g. red, green)
    ;    add a new output image for the next set of channel operations (e.g. red; green; blue)
    |    move to the next input image for the source of channel data (e.g. | gray=>alpha)
    

For example, to create 3 grayscale images from the red, green, and blue channels of an image, use:
    
    
    -channel-fx "red; green; blue"
    

A channel without an operation symbol implies separate (i.e, semicolon).

Here we take an sRGB image and a grayscale image and inject the grayscale image into the alpha channel:
    
    
    convert wizard.png mask.pgm -channel-fx '| gray=>alpha' wizard-alpha.png 
    

Use a similar command to define a read mask:
    
    
    convert wizard.png mask.pgm -channel-fx '| gray=>read-mask' wizard-mask.png 
    

Add `-debug pixel` prior to the `-channel-fx` option to track the channel morphology.

-exit
    Stop processing at this point. No further options will be processed after this option. Can be used in a script to force the "`magick`" command to exit, without actually closing the pipeline that it is processing options from. 
    May also be used as a 'final' option on the "`magick`" command line, instead of a implicit output image, to completely prevent any image write. ASIDE: even the "`NULL:`" coder requires at least one image, for it to 'not write'! This option does not require any images at all. 
-read {image}
    Explicit read of an image, rather than an implicit read. This allows you to read from filenames that start with an 'option' character, and which otherwise could be mistaken as an option (unknown or otherwise). This will eventually be used in "`mogrify`" to allow the reading of secondary images, and allow the use of image list operations within that command. 
-read-mask
    prevent updates to image pixels specified by the mask
-region
    not yet implemented in "`magick`". (very soon)
-script {file}
    In "`magick`", stop the processing of command line arguments as image operations, and read all further options from the given file or pipeline.
-write-mask
    prevent pixels from being written.

### Changed Options

These options are known to have changed, in some way.

-bias
    The option is no longer recognized. Use `-define convolve:bias=value` instead.
-draw
    The `matte` primitive is now `alpha` (e.g. `-draw 'alpha 0,0 floodfill'`).
-negate
    currently negates all channels, including alpha if present. As such you may need to use the -channel option to prevent alpha negation. 

### Deprecated warning given, but will work (for now)

-affine
    Replaced by `-draw "affine ..."`. (see transform)
-average
    Replaced by `-evaluate-sequence Mean`.
-box
    Replaced by `-undercolor`.
-deconstruct
    Replaced by `-layers CompareAny`.
-gaussian
    Replaced by `-gaussian-blur`.
-/+map
    Replaced by `-/+remap`.
-/+mask
    Replaced by `-/+read-mask`, `-/+write-mask`.
-/+matte
    Replaced by `-alpha Set/Off`.
-transform
    Replaced by `-distort Affine "..."`.

### Deprecated warning given, and ignored (for now)

Almost 'plus' (+) option that did not do anything has been marked as deprecated, and does nothing. It does not even have associated code. For example "+annotate", "+resize", "+clut", and "+draw" .

-affinity
    Replaced by `-remap`.
-maximum
    Replaced by `-evaluate-sequence Max`.
-median
    Replaced by `-evaluate-sequence Median`.
-minimum
    Replaced by `-evaluate-sequence Min`.
-recolor
    Replaced by `-color-matrix`.

### Removed / Replaced Options ("no such option" error and abort)

-origin
    old option, unknown meaning.
-pen
    Replaced by `-fill`.
-passphrase
    old option, unknown meaning

## Version 7 Change Summary

Changes from ImageMagick version 6 to version 7 are summarized here:

#### High Dynamic Range Imaging

  * ImageMagick version 7 enables HDRI by default. Expect more accurate image processing results with higher memory requirements and possible slower processing times. You can disable this feature for resource constrained system such as a cell phone with a slight loss of accuracy for certain algorithms (e.g. resizing).



#### Pixels

  * Pixels are no longer addressed with PixelPacket structure members (e.g. red, green, blue, opacity) but as an array of channels (e.g. pixel[PixelRedChannel]).
  * Use convenience macros to access pixel channels (e.g. GetPixelRed(), SetPixelRed()).
  * The black channel for the CMYK colorspace is no longer stored in the index channel, previously accessed with GetAuthenticIndexQueue() and GetCacheViewAuthenticIndexQueue(). Instead it is now a pixel channel and accessed with the convenience pixel macros GetPixelBlack() and SetPixelBlack().
  * The index channel for colormapped images is no longer stored in the index channel, previously accessed with GetAuthenticIndexQueue() and GetCacheViewAuthenticIndexQueue(). Instead it is now a pixel channel and accessed with the convenience pixel macros GetPixelIndex() and SetPixelIndex().
  * Use GetPixelChannels() to advance to the next set of pixel channels.
  * Use the metacontent channel to associate metacontent with each pixel.
  * All color packet structures, PixelPacket, LongPacket, and DoublePacket, are consolidated to a single color structure, PixelInfo.



#### Alpha

  * We support alpha rather than opacity (0 transparent; QuantumRange opaque).
  * Use GetPixelAlpha() or SetPixelAlpha() to get or set the alpha pixel channel value.



#### Grayscale

  * Grayscale images consume one pixel channel in ImageMagick version 7. To process RGB, set the colorspace to RGB (e.g. -colorspace sRGB).



#### Masks

  * ImageMagick version 6 only supports read mask in limited circumstances. Version 7 supports both a read and write mask. The read mask is honored by most image-processing algorithms.



#### MagickCore API

  * Almost all image processing algorithms are now channel aware.
  * MagickCore, version 7, adds an ExceptionInfo argument to those methods that lacked it in version 6, e.g. `NegateImage(image,MagickTrue,exception);`
  * All method channel analogs have been removed (e.g. BlurImageChannel()), they are no longer necessary, use pixel traits instead.
  * Public and private API calls are now declared with the GCC visibility attribute. The MagickCore and MagickWand dynamic libraries now only export public struct and function declarations.
  * The InterpolatePixelMethod enum is now PixelInterpolateMethod.
  * To account for variable pixel channels, images may now return a different signature.



#### Deprecated Methods

  * All ImageMagick version 6 MagickCore and MagickWand deprecated methods are removed and no longer available in ImageMagick version 7.
  * All MagickCore channel method analogs are removed (e.g. NegateImageChannels()). For version 7, use pixel traits instead.
  * The FilterImage() method has been removed. Use ConvolveImage() instead.



[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](porting.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
