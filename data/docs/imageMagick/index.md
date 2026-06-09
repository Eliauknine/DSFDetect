[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](http://www.imagemagick.org/discourse-server/)

[Features and Capabilities](http://nextgen.imagemagick.org/www/index.html#features) • [News](http://nextgen.imagemagick.org/www/index.html#news) • [Community](http://nextgen.imagemagick.org/www/index.html#community)

[![And Now a Touch of Magick](../images/wizard.jpg)](../images/wizard.png "And Now a Touch of Magick") ImageMagick[®](http://tarr.uspto.gov/servlet/tarr?regser=serial&entry=78333969) is a software suite to create, edit, compose, or convert bitmap images. It can read and write images in a variety of [formats](formats.html) (over 200) including PNG, JPEG, JPEG-2000, GIF, TIFF, [DPX](motion-picture.html), [EXR](high-dynamic-range.html), WebP, Postscript, PDF, and SVG. Use ImageMagick to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves.

The functionality of ImageMagick is typically utilized from the [command-line](command-line-processing.html) or you can use the features from programs written in your favorite language. Choose from these interfaces: [G2F](api.html#ada) (Ada), [MagickCore](api.html#c) (C), [MagickWand](api.html#c) (C), [ChMagick](api.html#ch) (Ch), [ImageMagickObject](api.html#com_) (COM+), [Magick++](api.html#c__) (C++), [JMagick](api.html#java) (Java), [L-Magick](api.html#lisp) (Lisp), [Lua](api.html#lua) (LuaJIT), [NMagick](api.html#neko) (Neko/haXe), [Magick.NET](api.html#dot-net) (.NET), [PascalMagick](api.html#pascal) (Pascal), [PerlMagick](api.html#perl) (Perl), [MagickWand for PHP](api.html#php) (PHP), [IMagick](api.html#php) (PHP), [PythonMagick](api.html#python) (Python), [RMagick](api.html#ruby) (Ruby), or [TclMagick](api.html#tcl) (Tcl/TK). With a language interface, use ImageMagick to modify or create images dynamically and automagically.

ImageMagick utilizes multiple computational threads to increase performance and can read, process, or write mega-, giga-, or tera-pixel image sizes.

ImageMagick is free software delivered as a ready-to-run binary distribution or as source code that you may use, copy, modify, and distribute in both open and proprietary applications. It is distributed under the Apache 2.0 [license](http://www.imagemagick.org/www/license.html).

The ImageMagick development process ensures a stable API and ABI. Before each ImageMagick release, we perform a comprehensive security assessment that includes [memory error](https://code.google.com/p/address-sanitizer/) and [thread data race](https://code.google.com/p/data-race-test/wiki/ThreadSanitizer) detection to prevent security vulnerabilities.

The current release is ImageMagick [7.0.0-0](http://www.imagemagick.org/www/binary-releases.html). It runs on [Linux](http://www.imagemagick.org/www/binary-releases.html#unix), [Windows](http://www.imagemagick.org/www/binary-releases.html#windows), [Mac Os X](http://www.imagemagick.org/www/binary-releases.html#macosx), [iOS](http://www.imagemagick.org/www/binary-releases.html#iOS), Android OS, and others.

The authoritative ImageMagick web site is [http://www.imagemagick.org](http://www.imagemagick.org/). The authoritative source code repository is <http://git.imagemagick.org/repos/ImageMagick>. We maintain a source code mirror at [GitLab](https://gitlab.com/ImageMagick/ImageMagick) and [GitHub](https://github.com/ImageMagick/ImageMagick).

## Features and Capabilities

Here are just a few [examples](examples.html) of what ImageMagick can do for you:

[Animation](http://www.imagemagick.org/Usage/anim_basics/) | create a GIF animation sequence from a group of images.  
---|---  
[Color management](color-management.html) | accurate color management with color profiles or in lieu of-- built-in gamma compression or expansion as demanded by the colorspace.  
[Command-line processing](command-line-processing.html) | utilize ImageMagick from the command-line.  
[Composite](composite.html) | overlap one image over another.  
[Connected component labeling](connected-components.html) | uniquely label connected regions in an image.  
[Decorate](http://www.imagemagick.org/Usage/crop/) | add a border or frame to an image.  
[Delineate image features](http://www.imagemagick.org/Usage/transform/#vision) | [Canny edge detection](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=25405), [Hough lines](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=25476).  
[Discrete Fourier transform](http://www.imagemagick.org/Usage/fourier/) | implements the forward and inverse [DFT](http://en.wikipedia.org/wiki/Discrete_Fourier_transform).  
[Distributed pixel cache](distribute-pixel-cache.html) | offload intermediate pixel storage to one or more remote servers.  
[Draw](http://www.imagemagick.org/Usage/draw/) | add shapes or text to an image.  
[Encipher or decipher an image](cipher.html) | convert ordinary images into unintelligible gibberish and back again.  
[Format conversion](convert.html) | convert an image from one [format ](formats.html) to another (e.g. PNG to JPEG).  
[Generalized pixel distortion](http://www.imagemagick.org/Usage/distorts/) | correct for, or induce image distortions including perspective.  
[Heterogeneous distributed processing](architecture.html#distributed) | certain algorithms are [OpenCL](opencl.html)-enabled to take advantage of speed-ups offered by executing in concert across heterogeneous platforms consisting of CPUs, GPUs, and other processors.  
[High dynamic-range images](high-dynamic-range.html) | accurately represent the wide range of intensity levels found in real scenes ranging from the brightest direct sunlight to the deepest darkest shadows.  
[Image calculator](fx.html) | apply a mathematical expression to an image or image channels.  
[Image gradients](gradient.html) | create a gradual blend of two colors whose shape is horizontal, vertical, circular, or elliptical.  
[Image identification](identify.html) | describe the format and attributes of an image.  
[ImageMagick on the iPhone](binary-releases.html#iOS) | convert, edit, or compose images on your [iOS](http://www.apple.com/ios/) device such as the iPhone or iPad.  
[Large image support](architecture.html#tera-pixel) | read, process, or write mega-, giga-, or tera-pixel image sizes.  
[Montage](montage.html) | juxtapose image thumbnails on an image canvas.  
[Morphology of shapes](http://www.imagemagick.org/Usage/morphology/) | extract features, describe shapes, and recognize patterns in images.  
[Motion picture support](motion-picture.html) | read and write the common image formats used in digital film work.  
[Noise and color reduction](http://www.imagemagick.org/Usage/transform/#vision) | [Kuwahara Filter](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=26480), [mean-shift](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=25504).  
[Perceptual hash](http://www.fmwconcepts.com/misc_tests/perceptual_hash_test_results_510/index.html) | map visually identical images to the same or similar hash-- useful in image retrieval, authentication, indexing, or copy detection as well as digital watermarking.  
[Special effects](http://www.imagemagick.org/Usage/blur/) | blur, sharpen, threshold, or tint an image.  
[Text & comments](http://www.imagemagick.org/Usage/text/) | insert descriptive or artistic text in an image.  
[Threads of execution support](architecture.html#threads) | ImageMagick is thread safe and most internal algorithms execute in [parallel](openmp.html) to take advantage of speed-ups offered by multicore processor chips.  
[Transform](http://www.imagemagick.org/Usage/resize/) | resize, rotate, deskew, crop, flip or trim an image.  
[Transparency](http://www.imagemagick.org/Usage/masking/) | render portions of an image invisible.  
[Virtual pixel support](architecture.html#virtual-pixels) | convenient access to pixels outside the image region.  
  
[Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/) shows how to use ImageMagick from the [command-line](command-line-processing.html) to accomplish any of these tasks and much more. Also, see [Fred's ImageMagick Scripts](http://www.fmwconcepts.com/imagemagick/): a plethora of command-line scripts that perform geometric transforms, blurs, sharpens, edging, noise removal, and color manipulations. With [Magick.NET](https://magick.codeplex.com/), use ImageMagick without having to install ImageMagick on your server or desktop.

## News

The design of ImageMagick is an evolutionary process, with the design and implementation efforts serving to influence and guide further progress in the other. With [ImageMagick version 7](http://nextgen.imagemagick.org/index.html), we aim to improve the design based on lessons learned from the version 6 implementation. See the [porting](porting.html) guide to track the progress of the version 7 development effort.

## Community

To join the ImageMagick community, try the [discourse server](http://www.imagemagick.org/discourse-server/). You can review questions or comments (with informed responses) posed by ImageMagick users or ask your own questions. If you want to contribute image processing algorithms, other enhancements, or bug fixes, open an [issue](http://git.imagemagick.org/repos/ImageMagick/issues). 

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](http://nextgen.imagemagick.org/www/index.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
