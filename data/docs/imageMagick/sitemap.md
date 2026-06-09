[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ImageMagick Overview](sitemap.html#overview) • [Download ImageMagick](sitemap.html#download) • [Install ImageMagick](sitemap.html#install) • [Command-line Tools](sitemap.html#command-line) • [Program Interfaces](sitemap.html#program-interfaces) • [Image Formats](sitemap.html#formats) • [Getting Help](sitemap.html#help) • [Support ImageMagick](sitemap.html#support) • [Miscellaneous Topics](sitemap.html#miscellaneous)

Use this ImageMagick sitemap to quickly jump to one of the areas of interest listed below. If you can't find what you want on this page, try our [site search](http://nextgen.imagemagick.org/script/search.php).

## ImageMagick Overview

* [Introduction](../index.html): convert, edit, or compose images from the command-line or program interface.
* [Examples of ImageMagick usage](examples.html): a few examples that show what you can do with an image using ImageMagick.
* [Anthony Thyssen's examples of ImageMagick usage](http://www.imagemagick.org/Usage/): a comprehensive tutorial of using ImageMagick from the command line.
* [Color names](color.html): how to specify a color name, a hex color, or a numerical RGB, RGBA, HSL, HSLA, CMYK, or CMYKA color.
* [Color management](color-management.html): accurate color management with color profiles or in lieu of-- built-in gamma compression or expansion as demanded by the colorspace.
* [Resources](resources.html): ImageMagick depends on external resources including configuration files, loadable modules, fonts, and environment variables.
* [Parallel execution](openmp.html): ImageMagick is threaded to take advantage of speed-ups offered by the multicore processor chips.
* [Architecture](architecture.html): get to know more about the software and algorithms behind ImageMagick.
* [License](license.html): the legally binding and authoritative terms and conditions for use, reproduction, and distribution of ImageMagick.
* [Export classification](export.html): export control status of ImageMagick.
* [ImageMagick version 7](porting.html): ImageMagick version 7 is in development, learn how it differs from previous versions.
* [History](history.html): how ImageMagick was conceived and developed.

## Download ImageMagick

* [Download ImageMagick](download.html): ImageMagick source and binary distributions are available from a variety of FTP and Web mirrors.
* * [Unix source](http://www.imagemagick.org/download): Unix source distributions.
* [Windows source](http://www.imagemagick.org/download/windows): Windows source distributions.
* [Unix and Windows binaries](http://www.imagemagick.org/download/binaries): Unix and Windows binary distributions.
* [Git repository](http://git.imagemagick.org/repos/ImageMagick): stable and development source releases.
* [MagickWand for PHP](http://www.magickwand.org/): a native PHP-extension to the ImageMagick MagickWand API.
* [Delegate libraries](http://www.imagemagick.org/download/delegates): ImageMagick depends on a number of optional delegate libraries to extend its functionality.

## Install ImageMagick

You can install ImageMagick from source. However, if you don't have a proper development environment or if you're anxious to get started, download a ready-to-run Unix or Windows executable.

* [Install from source](install-source.html): ImageMagick builds under Windows, Mac OS X, and Linux.
* [Install from a binary distribution](binary-releases.html): install a ready-to-run Unix or Windows executable.
* [Install ImageMagickObject COM+ component](ImageMagickObject.html): install the Windows ImageMagick COM+ component.

## Command-line Tools

* [Command-line tools](command-line-tools.html): overview of the ImageMagick commands.
* * [animate](animate.html): animates an image sequence on any X server.
* [compare](compare.html): mathematically and visually annotate the difference between an image and its reconstruction.
* [composite](composite.html): overlaps one image over another.
* [conjure](conjure.html): interprets and executes scripts written in the Magick Scripting Language (MSL).
* [convert](convert.html): convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and more.
* [display](display.html): displays an image or image sequence on any X server.
* [identify](identify.html): describes the format and characteristics of one or more image files.
* [import](import.html): saves any visible window on an X server and outputs it as an image file.
* [mogrify](mogrify.html): resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and more.
* [montage](montage.html): create a composite image by combining several separate images.
* [stream](stream.html): a lightweight tool to stream one or more pixel components of the image or portion of the image to your choice of storage formats.
* [Command line processing](command-line-processing.html): the anatomy of the command line.
* [Command line options](command-line-options.html): annotated list of all options that can appear on the command-line.
* [Fx](fx.html): apply a mathematical expression to an image or image channels.
* [Fred's ImageMagick Scripts](http://www.fmwconcepts.com/imagemagick/): a plethora of command-line scripts that perform geometric transforms, blurs, sharpens, edging, noise removal, and color manipulations.

## Program Interfaces

* [Program interfaces](api.html): application programming interfaces.
* * [ChMagick](http://www.imagemagick.org/ChMagick): is a [Ch](http://www.softintegration.com/) an embeddable MagickCore C/C++ interpreter for cross-platform scripting.
* [CL-Magick](http://common-lisp.net/project/cl-magick/): provides a Common Lisp interface to the ImageMagick library.
* [G2F](https://gna.org/projects/g2f/): implements an Ada 95 binding to a subset of the low-level MagickCore library.
* [Magick++](http://www.imagemagick.org/Magick++): provides an object-oriented C++ interface to ImageMagick.
* [IMagick](http://pecl.html.net/package/imagick): is a native PHP extension to create and modify images using the ImageMagick API.
* [JMagick](http://www.yeo.id.au/jmagick/): provides an object-oriented Java interface to ImageMagick.
* [MagickCore](magick-core.html): C API, recommended for wizard-level developers.
* [MagickWand](magick-wand.html): convert, compose, and edit images from the C language.
* [MagickWand for PHP](http://www.magickwand.org/): a native PHP-extension to the ImageMagick MagickWand API.
* [nMagick](http://code.google.com/p/nmagick): is a port of the ImageMagick library to the haXe and Neko platforms.
* [PascalMagick](http://wiki.freepascal.org/PascalMagick): a Pascal binding for the MagickWand API and also the low-level MagickCore library.
* [PerlMagick](perl-magick.html): convert, compose, and edit images from the Perl language.
* [PythonMagick](http://www.imagemagick.org/download/python/): an object-oriented Python interface to ImageMagick.
* [RMagick](http://rmagick.rubyforge.org/): is an interface between the Ruby programming language and ImageMagick.
* [TclMagick](http://tclmagick.sourceforge.net/): a native Tcl-extension to the ImageMagick MagickWand API.

## Image Formats

* [Supported image formats](formats.html): annotated list of all image formats that ImageMagick can read and/or write.
* [Motion picture digital images](motion-picture.html): use SMPTE DPX Version 2.0 to process images used by the motion picture (film and high-definition) industry.
* [High dynamic-range images](high-dynamic-range.html): accurately represent the wide range of intensity levels found in real scenes ranging from the brightest direct sunlight to the deepest darkest shadows.
* [Magick Vector Graphics](magick-vector-graphics.html): a modularized language for describing two-dimensional vector and mixed vector/raster graphics in ImageMagick.
* [Magick Image File Format](miff.html): MIFF is ImageMagick's own platform-independent format for storing bitmap images.

## Getting Help

* [Definitive Guide to ImageMagick](http://www.amazon.com/exec/obidos/redirect?link_code=ur2&camp=1789&tag=imagemagick-20&creative=9325&path=tg/detail/-/1590595904/qid=1123551819/sr=8-1/ref=pd_bbs_sbs_1?v=glance%26s=books%26n=507846): this book explains ImageMagick in a practical, learn-by-example fashion.
* [ImageMagick Tricks](http://www.amazon.com/exec/obidos/redirect?link_code=ur2&camp=1789&tag=imagemagick-20&creative=9325&path=tg/detail/-/1904811868/qid=1123551819/sr=8-1/ref=pd_bbs_sbs_1?v=glance%26s=books%26n=507846): this book is packed with examples of photo manipulations, logo creation, animations, and complete web projects.
* [Discourse server](http://www.imagemagick.org/discourse-server): get help from fellow ImageMagick users and developers, post to these forums.
* [Contact the Wizards](http://nextgen.imagemagick.org/script/contact.php): for bug reports (only if you do not want to sign up to the [discourse server](http://www.imagemagick.org/discourse-server)), a source or documentation patch, a security or license issue, or if you want to be a sponsor of the ImageMagick project.

## Support ImageMagick

* [Report bugs and vulnerabilities](http://www.imagemagick.org/discourse-server/viewforum.html?f=3): our highest priority is to fix security defects and bug reports, usually within 48 hours of your report. The bug discourse server requires that you register. If you do not want to register, you can [contact the ImageMagick developers](http://nextgen.imagemagick.org/script/contact.php) with a convenient web form.
* [Sponsor ImageMagick](support.html): contribute bug fixes, enhancements, hardware, funds, etc. to ensure the ImageMagick project thrives.

## Miscellaneous Topics

* [Animation](http://www.imagemagick.org/Usage/anim_basics/): create a GIF animation sequence from a group of images.
* [Canny edge detection](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=25405): extract edges from an image using the Canny technique.
* [Color management](color-management.html): accurate color management with color profiles or in lieu of-- built-in gamma compression or expansion as demanded by the colorspace.
* [Command-line processing](command-line-processing.html): utilize ImageMagick from the command line.
* [Connected Component Labeling](connected-components.html): uniquely label connected regions in an image.
* [Composite](composite.html): overlap one image over another.
* [Connected Component Labeling](connected-components.html): uniquely label connected regions in an image.
* [Decorate](http://www.imagemagick.org/Usage/crop/): add a border or frame to an image.
* [Discrete Fourier transform](http://www.imagemagick.org/Usage/fourier): implements the forward and inverse DFT.
* [Distributed pixel cache](distribute-pixel-cache.html): offload intermediate pixel storage to one or more remote servers .
* [Draw](http://www.imagemagick.org/Usage/draw/): add shapes or text to an image.
* [Encipher or decipher an image](cipher.html): convert ordinary images into unintelddgible gibberish and back again.
* [Escapes](escape.html): utilize percent escapes in a number of options, for example in [-format](command-line-options.html#format_identify_) or in montage [-label](command-line-options.html#label), to print various properties and other settings associated with an image.
* [Format conversion](convert.html): convert an image from one [format ](formats.html) to another (e.g. PNG to JPEG).
* [Generalized pixel distortion](http://www.imagemagick.org/Usage/distorts/): correct for, or induce image distortions including perspective.
* [Heterogeneous distributed processing](architecture.html#distributed): [certain algorithms](opencl.html) are [OpenCL](http://en.wikipedia.org/wiki/OpenCL)-enabled to take advantage of speed-ups offered by executing in concert across heterogeneous platforms consisting of CPUs, GPUs, and other processors.
* [High dynamic-range images](high-dynamic-range.html): accurately represent the wide range of intensity levels found in real scenes ranging from the brightest direct sunlight to the deepest darkest shadows.
* [Hough lines](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=25476): fit straight lines to edges in an image using the Hough transform technique.
* [Image calculator](fx.html): apply a mathematical expression to an image or image channels.
* [Image gradients](gradient.html): create a gradual blend of two colors whose shape is horizontal, vertical, circular, or elliptical.
* [Image identification](identify.html): describe the format and attributes of an image.
* [ImageMagick on the iPhone](binary-releases.html#iOS): convert, edit, or compose images on your iPhone.
* [Kuwahara Filter](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=26480): apply an edge perserving noise and color reduction filter to an image.
* [Large image support](architecture.html#tera-pixel): read, process, or write mega-, giga-, or tera-pixel image sizes.
* [Mean-shift](http://www.imagemagick.org/discourse-server/viewtopic.html?f=4&t=25504): apply a color reduction technique to an image.
* [Montage](montage.html): juxtapose image thumbnails on an image canvas.
* [Morphology of shapes](http://www.imagemagick.org/Usage/morphology/): extract features, describe shapes and recognize patterns in images.
* [Motion picture support](motion-picture.html): read and write the common image formats used in digital film work.
* [Special effects](http://www.imagemagick.org/Usage/blur/): blur, sharpen, threshold, or tint an image.
* [Text & comments](http://www.imagemagick.org/Usage/text/): insert descriptive or artistic text in an image.
* [Threads of execution support](architecture.html#threads): ImageMagick is thread safe and most internal algorithms execute in parallel to take advantage of speed-ups offered by multicore processor chips.
* [Transform](http://www.imagemagick.org/Usage/resize/): resize, rotate, crop, or trim an image.
* [Transparency](http://www.imagemagick.org/Usage/masking/): render portions of an image invisible.
* [Virtual pixel support](architecture.html#virtual-pixels): convenient access to pixels outside the image region.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](sitemap.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
