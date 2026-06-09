[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](montage.html#usage) • [Option Summary](montage.html#options)

Use the `montage` program to create a composite image by combining several separate images. The images are tiled on the composite image optionally adorned with a border, frame, image name, and more. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `montage` command or see below for example usages of the command.

## Example Usage

We list a few examples of the `montage` command here to illustrate its usefulness and ease of use. To get started, let's montage two images into a single composite:
    
    
    montage -background '#336699' -geometry +4+4 rose.jpg red-ball.png montage.jpg
    

[ ![rose](../images/rose.jpg) ](../images/rose.jpg) [ ![red ball](../images/red-ball.png) ](../images/red-ball.png) ![==>](../images/right.gif) [ ![montage](../images/montage.jpg) ](../images/montage.jpg) 


Ok, let's add some decorations:
    
    
    montage -label %f -frame 5 -background '#336699' -geometry +4+4 rose.jpg red-ball.png frame.jpg
    

[ ![rose.jpg](../images/rose.jpg) ](../images/rose.jpg) [ ![red ball](../images/red-ball.png) ](../images/red-ball.png) ![==>](../images/right.gif) [ ![frame](../images/frame.jpg) ](../images/frame.jpg) 


You can find additional examples of using `montage` at [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/montage/) and [Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf/?ca=dnt-428). Further discussion is available in [More Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf2/?ca=dgr-lnxw15GraphicsLine) and [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/).

## Option Summary

The `montage` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-adaptive-sharpen geometry](command-line-options.html#adaptive-sharpen) | adaptively sharpen pixels; increase effect near edges  
[-adjoin](command-line-options.html#adjoin) | join images into a single multi-image file  
[-affine matrix](command-line-options.html#affine) | affine transform matrix  
[-alpha](command-line-options.html#alpha) | on, activate, off, deactivate, set, opaque, copy", transparent, extract, background, or shape the alpha channel  
[-annotate geometry text](command-line-options.html#annotate) | annotate the image with text  
[-authenticate value](command-line-options.html#authenticate) | decrypt image with this password  
[-auto-orient](command-line-options.html#auto-orient) | automagically orient image  
[-background color](command-line-options.html#background) | background color  
[-blue-primary point](command-line-options.html#blue-primary) | chromaticity blue primary point  
[-blur geometry](command-line-options.html#blur) | reduce image noise and reduce detail levels  
[-border geometry](command-line-options.html#border) | surround image with a border of color  
[-bordercolor color](command-line-options.html#bordercolor) | border color  
[-caption string](command-line-options.html#caption) | assign a caption to an image  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-clone index](command-line-options.html#clone) | clone an image  
[-coalesce](command-line-options.html#coalesce) | merge a sequence of images  
[-colors value](command-line-options.html#colors) | preferred number of colors in the image  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-comment string](command-line-options.html#comment) | annotate image with comment  
[-compose operator](command-line-options.html#compose) | set image composite operator  
[-composite](command-line-options.html#composite) | composite image  
[-compress type](command-line-options.html#compress) | image compression type  
[-crop geometry](command-line-options.html#crop) | preferred size and location of the cropped image  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-display server](command-line-options.html#display) | get image or font from this X server  
[-dispose method](command-line-options.html#dispose) | layer disposal method  
[-dither method](command-line-options.html#dither) | apply error diffusion to image  
[-draw string](command-line-options.html#draw) | annotate the image with a graphic primitive  
[-duplicate count,indexes](command-line-options.html#duplicate) | duplicate an image one or more times  
[-endian type](command-line-options.html#endian) | endianness (MSB or LSB) of the image  
[-extent geometry](command-line-options.html#extent) | set the image size  
[-extract geometry](command-line-options.html#extract) | extract area from image  
[-fill color](command-line-options.html#fill) | color to use when filling a graphic primitive  
[-filter type](command-line-options.html#filter) | use this filter when resizing an image  
[-flatten](command-line-options.html#flatten) | flatten a sequence of images  
[-flip](command-line-options.html#flip) | flip image in the vertical direction  
[-flop](command-line-options.html#flop) | flop image in the horizontal direction  
[-font name](command-line-options.html#font) | render text with this font  
[-frame geometry](command-line-options.html#frame) | surround image with an ornamental border  
[-gamma value](command-line-options.html#gamma) | level of gamma correction  
[-geometry geometry](command-line-options.html#geometry) | preferred size or location of the image  
[-gravity type](command-line-options.html#gravity) | horizontal and vertical text placement  
[-green-primary point](command-line-options.html#green-primary) | chromaticity green primary point  
[-help](command-line-options.html#help) | print program options  
[-identify](command-line-options.html#identify) | identify the format and characteristics of the image  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-interpolate method](command-line-options.html#interpolate) | pixel color interpolation method  
[-kerning value](command-line-options.html#kerning) | the space between two characters  
[-label string](command-line-options.html#label) | assign a label to an image  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-log format](command-line-options.html#log) | format of debugging information  
[-mattecolor color](command-line-options.html#mattecolor) | frame color  
[-mode type](command-line-options.html#mode) | framing style  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-monochrome](command-line-options.html#monochrome) | transform image to black and white  
[-origin geometry](command-line-options.html#origin) | image origin  
[-page geometry](command-line-options.html#page) | size and location of an image canvas (setting)  
[-pointsize value](command-line-options.html#pointsize) | font point size  
[-polaroid angle](command-line-options.html#polaroid) | simulate a Polaroid picture  
[-profile filename](command-line-options.html#profile) | add, delete, or apply an image profile  
[-quality value](command-line-options.html#quality) | JPEG/MIFF/PNG compression level  
[-quantize colorspace](command-line-options.html#quantize) | reduce image colors in this colorspace  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-red-primary point](command-line-options.html#red-primary) | chromaticity red primary point  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-repage geometry](command-line-options.html#repage) | size and location of an image canvas  
[-resize geometry](command-line-options.html#resize) | resize the image  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-rotate degrees](command-line-options.html#rotate) | apply Paeth rotation to the image  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-scale geometry](command-line-options.html#scale) | scale the image  
[-scenesrange](command-line-options.html#scenes) | image scene range  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-shadow geometry](command-line-options.html#shadow) | simulate an image shadow  
[-size geometry](command-line-options.html#size) | width and height of image  
[-strip](command-line-options.html#strip) | strip image of all profiles and comments  
[-stroke color](command-line-options.html#stroke) | graphic primitive stroke color  
[-synchronize](command-line-options.html#synchronize) | synchronize image to storage device  
[-taint](command-line-options.html#taint) | mark the image as modified  
[-texture filename](command-line-options.html#texture) | name of texture to tile onto the image background  
[-tile filename](command-line-options.html#tile) | tile image when filling a graphic primitive  
[-tile-offset geometry](command-line-options.html#tile-offset) | set the image tile offset  
[-title](command-line-options.html#title) | decorate the montage image with a title  
[-transform](command-line-options.html#transform) | affine transform image  
[-transparent color](command-line-options.html#transparent) | make this color transparent within the image  
[-transpose](command-line-options.html#transpose) | flip image in the vertical direction and rotate 90 degrees  
[-transparent-color color](command-line-options.html#transparent-color) | transparent color  
[-treedepth value](command-line-options.html#treedepth) | color tree depth  
[-trim](command-line-options.html#trim) | trim image edges  
[-type type](command-line-options.html#type) | image type  
[-units type](command-line-options.html#units) | the units of image resolution  
[-unsharp geometry](command-line-options.html#unsharp) | sharpen the image  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-view](command-line-options.html#view) | FlashPix viewing transforms  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
[-white-point point](command-line-options.html#white-point) | chromaticity white point  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](montage.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
