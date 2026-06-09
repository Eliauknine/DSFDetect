[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](composite.html#usage) • [Option Summary](composite.html#options)

Use the `composite` program to overlap one image over another. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `composite` command or see below for example usages of the command.

## Example Usage

We list a few examples of the `composite` command here to illustrate its usefulness and ease of use. To get started, lets overlay a smiley face over a rose:
    
    
    composite -gravity center smile.gif  rose: rose-over.png
    

[![smile](../images/smile.gif)](../images/smile.gif) ![over](../images/over.gif) [![rose](../images/rose.jpg)](../images/rose.jpg) ![==>](../images/right.gif) [![rose](../images/rose-over.png)](../images/rose-over.png) 


You can create three-dimensional effect with the Atop:
    
    
    convert -size 70x70 canvas:none -fill red -draw 'circle 35,35 10,30' red-circle.png
    convert -size 70x70 canvas:none -draw 'circle 35,35 35,20' -negate \
    -channel A -gaussian-blur 0x8 white-highlight.png
    composite -compose atop -geometry -13-17 white-highlight.png red-circle.png red-ball.png
    

[![white highlight](../images/white-highlight.png)](../images/white-highlight.png) ![atop](../images/atop.gif) [![red circle](../images/red-circle.png)](../images/red-circle.png) ![==>](../images/right.gif) [![red ball](../images/red-ball.png)](../images/red-ball.png) 


You can find additional examples of using `composite` in [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/). You can find out more about them and the mathematics by looking at [SVG Alpha Compositing](http://www.w3.org/TR/SVG12/rendering.html)

## Option Summary

The `composite` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-affine matrix](command-line-options.html#affine) | affine transform matrix  
[-alpha](command-line-options.html#alpha) | on, activate, off, deactivate, set, opaque, copy", transparent, extract, background, or shape the alpha channel  
[-authenticate value](command-line-options.html#authenticate) | decrypt image with this password  
[-blend geometry](command-line-options.html#blend) | blend images  
[-blue-primary point](command-line-options.html#blue-primary) | chromaticity blue primary point  
[-border geometry](command-line-options.html#border) | surround image with a border of color  
[-bordercolor color](command-line-options.html#bordercolor) | border color  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-colors value](command-line-options.html#colors) | preferred number of colors in the image  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-comment string](command-line-options.html#comment) | annotate image with comment  
[-compose operator](command-line-options.html#compose) | set image composite operator  
[-compress type](command-line-options.html#compress) | image compression type  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-decipher filename](command-line-options.html#decipher) | convert cipher pixels to plain  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-displace geometry](command-line-options.html#displace) | shift image pixels defined by a displacement map  
[-dissolve value](command-line-options.html#dissolve) | dissolve the two images a given percent  
[-dither method](command-line-options.html#dither) | apply error diffusion to image  
[-encipher filename](command-line-options.html#encipher) | convert plain pixels to cipher pixels  
[-encoding type](command-line-options.html#encoding) | text encoding type  
[-endian type](command-line-options.html#endian) | endianness (MSB or LSB) of the image  
[-extract geometry](command-line-options.html#extract) | extract area from image  
[-filter type](command-line-options.html#filter) | use this filter when resizing an image  
[-font name](command-line-options.html#font) | render text with this font  
[-geometry geometry](command-line-options.html#geometry) | preferred size or location of the image  
[-gravity type](command-line-options.html#gravity) | horizontal and vertical text placement  
[-green-primary point](command-line-options.html#green-primary) | chromaticity green primary point  
[-help](command-line-options.html#help) | print program options  
[-identify](command-line-options.html#identify) | identify the format and characteristics of the image  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-interpolate method](command-line-options.html#interpolate) | pixel color interpolation method  
[-label string](command-line-options.html#label) | assign a label to an image  
[-level value](command-line-options.html#level) | adjust the level of image contrast  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-log format](command-line-options.html#log) | format of debugging information  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-monochrome](command-line-options.html#monochrome) | transform image to black and white  
[-negate](command-line-options.html#negate) | replace each pixel with its complementary color   
[-page geometry](command-line-options.html#page) | size and location of an image canvas (setting)  
[-pointsize value](command-line-options.html#pointsize) | font point size  
[-profile filename](command-line-options.html#profile) | add, delete, or apply an image profile  
[-quality value](command-line-options.html#quality) | JPEG/MIFF/PNG compression level  
[-quantize colorspace](command-line-options.html#quantize) | reduce image colors in this colorspace  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-red-primary point](command-line-options.html#red-primary) | chromaticity red primary point  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-rotate degrees](command-line-options.html#rotate) | apply Paeth rotation to the image  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-scene value](command-line-options.html#scene) | image scene number  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-set attribute value](command-line-options.html#set) | set an image attribute  
[-sharpen geometry](command-line-options.html#sharpen) | sharpen the image  
[-shave geometry](command-line-options.html#shave) | shave pixels from the image edges  
[-size geometry](command-line-options.html#size) | width and height of image  
[-stegano offset](command-line-options.html#stegano) | hide watermark within an image  
[-stereo geometry](command-line-options.html#stereo) | combine two image to create a stereo anaglyph  
[-strip](command-line-options.html#strip) | strip image of all profiles and comments  
[-swap indexes](command-line-options.html#swap) | swap two images in the image sequence  
[-synchronize](command-line-options.html#synchronize) | synchronize image to storage device  
[-taint](command-line-options.html#taint) | mark the image as modified  
[-thumbnail geometry](command-line-options.html#thumbnail) | create a thumbnail of the image  
[-tile](command-line-options.html#tile) | repeat composite operation across and down image  
[-transform](command-line-options.html#transform) | affine transform image  
[-transparent-color color](command-line-options.html#transparent-color) | transparent color  
[-treedepth value](command-line-options.html#treedepth) | color tree depth  
[-type type](command-line-options.html#type) | image type  
[-units type](command-line-options.html#units) | the units of image resolution  
[-unsharp geometry](command-line-options.html#unsharp) | sharpen the image  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
[-watermark geometry](command-line-options.html#watermark) | percent brightness and saturation of a watermark  
[-white-point point](command-line-options.html#white-point) | chromaticity white point  
[-white-threshold value](command-line-options.html#white-threshold) | force all pixels above the threshold into white  
[-write filename](command-line-options.html#write) | write images to this file  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](composite.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
