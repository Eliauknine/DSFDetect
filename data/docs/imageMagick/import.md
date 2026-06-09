[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](import.html#usage) • [Option Summary](import.html#options)

Use the `import` program to capture some or all of an X server screen and save the image to a file. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `import` command or see below for example usages of the command.

## Example Usage

We list a few examples of the `import` command here to illustrate its usefulness and ease of use. To get started, lets import an image in the JPEG format:
    
    
    import rose.jpg
    

To capture the entire X server screen in the Postscript image format:
    
    
    import -window root screen.ps
    

You can find additional examples of using `import` in [Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf/?ca=dnt-428). Further discussion is available in [More Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf2/?ca=dgr-lnxw15GraphicsLine) and [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/).

## Option Summary

The `import` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-adjoin](command-line-options.html#adjoin) | join images into a single multi-image file  
[-annotate geometry text](command-line-options.html#annotate) | annotate the image with text  
[-border](command-line-options.html#border) | include window border in the output image  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-colors value](command-line-options.html#colors) | preferred number of colors in the image  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-comment string](command-line-options.html#comment) | annotate image with comment  
[-compress type](command-line-options.html#compress) | image compression type  
[-contrast](command-line-options.html#contrast) | enhance or reduce the image contrast  
[-crop geometry](command-line-options.html#crop) | preferred size and location of the cropped image  
[-debug events](command-line-options.html#debug) | import copious debugging information  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-delay value](command-line-options.html#delay) | import the next image after pausing  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-descend](command-line-options.html#despeckle) | obtain image by descending window hierarchy  
[-display server](command-line-options.html#display) | get image or font from this X server  
[-dispose method](command-line-options.html#dispose) | layer disposal method  
[-dither method](command-line-options.html#dither) | apply error diffusion to image  
[-encipher filename](command-line-options.html#encipher) | convert plain pixels to cipher pixels  
[-encoding type](command-line-options.html#encoding) | text encoding type  
[-endian type](command-line-options.html#endian) | endianness (MSB or LSB) of the image  
[-filter type](command-line-options.html#filter) | use this filter when resizing an image  
[-frame](command-line-options.html#frame) | include window manager frame  
[-geometry geometry](command-line-options.html#geometry) | preferred size or location of the image  
[-gravity type](command-line-options.html#gravity) | horizontal and vertical text placement  
[-help](command-line-options.html#help) | print program options  
[-identify](command-line-options.html#identify) | identify the format and characteristics of the image  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-interpolate method](command-line-options.html#interpolate) | pixel color interpolation method  
[-label name](command-line-options.html#label) | assign a label to an image  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-log format](command-line-options.html#log) | format of debugging information  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-monochrome](command-line-options.html#monochrome) | transform image to black and white  
[-negate](command-line-options.html#negate) | replace each pixel with its complementary color   
[-page geometry](command-line-options.html#page) | size and location of an image canvas (setting)  
[-pause seconds](command-line-options.html#pause) | seconds delay between snapshots  
[-quality value](command-line-options.html#quality) | JPEG/MIFF/PNG compression level  
[-quantize colorspace](command-line-options.html#quantize) | reduce image colors in this colorspace  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-repage geometry](command-line-options.html#repage) | size and location of an image canvas  
[-resize geometry](command-line-options.html#resize) | resize the image  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-rotate degrees](command-line-options.html#rotate) | apply Paeth rotation to the image  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-scene value](command-line-options.html#scene) | image scene number  
[-screen](command-line-options.html#screen) | select image from root window  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-set attribute value](command-line-options.html#set) | set an image attribute  
[-silent](command-line-options.html#sharpen) | operate silently, i.e. don't ring any bells  
[-strip](command-line-options.html#strip) | strip image of all profiles and comments  
[-synchronize](command-line-options.html#synchronize) | synchronize image to storage device  
[-taint](command-line-options.html#taint) | mark the image as modified  
[-transparent-color color](command-line-options.html#transparent-color) | transparent color  
[-trim](command-line-options.html#trim) | trim image edges  
[-type type](command-line-options.html#update) | image type  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
[-window id](command-line-options.html#write) | select window with this id or name  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](import.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
