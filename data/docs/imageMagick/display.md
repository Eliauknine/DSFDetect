[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](display.html#usage) • [Option Summary](display.html#options)

Use the `display` program to display an image or image sequence on any X server. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `display` command or see below for example usages of the command.

## Example Usage

We list a few examples of the `display` command here to illustrate its usefulness and ease of use. To get started, lets display an image in the JPEG format:
    
    
    display rose.jpg
    

To tile a slate texture onto the root window, use:
    
    
    display -size 1280x1024 -window root slate.png
    

To display a visual image directory of all your JPEG images, use:
    
    
    display 'vid:*.jpg'
    

The display program defaults to the X screen resolution. To display vecotr formats at their intended size, override the default resolution:
    
    
    display -density 72 drawing.svg
    

You can find additional examples of using `display` in [Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf/). Further discussion is available in [More Graphics from the Command Line](https://www.ibm.com/developerworks/library/l-graf2/) and [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/).

## Option Summary

The `display` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-alpha](command-line-options.html#alpha) | on, activate, off, deactivate, set, opaque, copy", transparent, extract, background, or shape the alpha channel  
[-antialias](command-line-options.html#antialias) | remove pixel-aliasing  
[-authenticate value](command-line-options.html#authenticate) | decrypt image with this password  
[-backdrop](command-line-options.html#backdrop) | display image centered on a backdrop  
[-background color](command-line-options.html#background) | background color  
[-border geometry](command-line-options.html#border) | surround image with a border of color  
[-bordercolor color](command-line-options.html#bordercolor) | border color  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-clip](command-line-options.html#clip) | clip along the first path from the 8BIM profile  
[-clip-path id](command-line-options.html#clip-path) | clip along a named path from the 8BIM profile  
[-coalesce](command-line-options.html#coalesce) | merge a sequence of images  
[-colormap type](command-line-options.html#colormap) | Shared or Private  
[-colors value](command-line-options.html#colors) | preferred number of colors in the image  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-comment string](command-line-options.html#comment) | annotate image with comment  
[-compress type](command-line-options.html#compress) | image compression type  
[-contrast](command-line-options.html#contrast) | enhance or reduce the image contrast  
[-crop geometry](command-line-options.html#crop) | preferred size and location of the cropped image  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-decipher filename](command-line-options.html#decipher) | convert cipher pixels to plain  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-delay value](command-line-options.html#delay) | display the next image after pausing  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-despeckle](command-line-options.html#despeckle) | reduce the speckles within an image  
[-display server](command-line-options.html#display) | get image or font from this X server  
[-dispose method](command-line-options.html#dispose) | layer disposal method  
[-dither method](command-line-options.html#dither) | apply error diffusion to image  
[-edge radius](command-line-options.html#edge) | apply a filter to detect edges in the image  
[-endian type](command-line-options.html#endian) | endianness (MSB or LSB) of the image  
[-enhance](command-line-options.html#enhance) | apply a digital filter to enhance a noisy image  
[-equalize](command-line-options.html#equalize) | perform histogram equalization to an image  
[-extract geometry](command-line-options.html#extract) | extract area from image  
[-filter type](command-line-options.html#filter) | use this filter when resizing an image  
[-flatten](command-line-options.html#flatten) | flatten a sequence of images  
[-flip](command-line-options.html#flip) | flip image in the vertical direction  
[-flop](command-line-options.html#flop) | flop image in the horizontal direction  
[-frame geometry](command-line-options.html#frame) | surround image with an ornamental border  
[-fuzz distance](command-line-options.html#fuzz) | colors within this distance are considered equal  
[-gamma value](command-line-options.html#gamma) | level of gamma correction  
[-geometry geometry](command-line-options.html#geometry) | preferred size or location of the image  
[-gravity geometry](command-line-options.html#gravity) | horizontal and vertical backdrop placement  
[-help](command-line-options.html#help) | print program options  
[-identify](command-line-options.html#identify) | identify the format and characteristics of the image  
[-immutable type](command-line-options.html#immutable) | prohibit image edits  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-interpolate method](command-line-options.html#interpolate) | pixel color interpolation method  
[-label name](command-line-options.html#label) | assign a label to an image  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-log format](command-line-options.html#log) | format of debugging information  
[-map filename](command-line-options.html#map) | transform image colors to match this set of colors  
[-mattecolor color](command-line-options.html#mattecolor) | frame color  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-monochrome](command-line-options.html#monochrome) | transform image to black and white  
[-negate](command-line-options.html#negate) | replace each pixel with its complementary color   
[-normalize](command-line-options.html#normalize) | transform image to span the full range of colors  
[-page geometry](command-line-options.html#page) | size and location of an image canvas (setting)  
[-profile filename](command-line-options.html#profile) | add, delete, or apply an image profile  
[-quantize colorspace](command-line-options.html#quantize) | reduce image colors in this colorspace  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-raise value](command-line-options.html#raise) | lighten/darken image edges to create a 3-D effect  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-remote command](command-line-options.html#remote) | execute a command in an remote display process  
[-resample geometry](command-line-options.html#resample) | change the resolution of an image  
[-resize geometry](command-line-options.html#resize) | resize the image  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-roll geometry](command-line-options.html#roll) | roll an image vertically or horizontally  
[-rotate degrees](command-line-options.html#rotate) | apply Paeth rotation to the image  
[-sample geometry](command-line-options.html#sample) | scale image with pixel sampling  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-scene value](command-line-options.html#scene) | image scene number  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-segment values](command-line-options.html#segment) | segment an image  
[-set attribute value](command-line-options.html#set) | set an image attribute  
[-sharpen geometry](command-line-options.html#sharpen) | sharpen the image  
[-size geometry](command-line-options.html#size) | width and height of image  
[-strip](command-line-options.html#strip) | strip image of all profiles and comments  
[-thumbnail geometry](command-line-options.html#thumbnail) | create a thumbnail of the image  
[-transparent-color color](command-line-options.html#transparent-color) | transparent color  
[-black-threshold value](command-line-options.html#black-threshold) | force all pixels below the threshold into black  
[-trim](command-line-options.html#trim) | trim image edges  
[-update seconds](command-line-options.html#update) | detect when image file is modified and redisplay  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
[-visual](command-line-options.html#visual) | display image using this visual type  
[-window id](command-line-options.html#write) | display image to background of this window  
[-window-group id](command-line-options.html#write) | exit program when this window id is destroyed  
[-write filename](command-line-options.html#write) | write images to this file  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](display.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
