[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](stream.html#usage) • [Option Summary](stream.html#options)

`Stream` is a lightweight tool to stream one or more pixel components of the image or portion of the image to your choice of storage formats. It writes the pixel components as they are read from the input image a row at a time making `stream` desirable when working with large images or when you require raw pixel components.

## Example Usage

We list a few examples of the `stream` command here to illustrate its usefulness and ease of use. To get started, lets stream the red, green, blue components of a 640x480 JPEG image to disk as unsigned characters:
    
    
    stream -map rgb -storage-type char image.jpg pixels.dat
    display -depth 8 -size 640x480 rgb:pixels.dat
    

Here we extract a 100x100 region from a TIFF image in the grayscale format as doubles:
    
    
    stream -map i -storage-type double -extract 100x100+30+40 image.tif gray.raw
    

You can also associate the region to extract with the image filename:
    
    
    stream -map i -storage-type double 'image.tif[100x100+30+40]' gray.raw
    

## Option Summary

The `stream` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-authenticate value](command-line-options.html#authenticate) | decrypt image with this password  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-extract geometry](command-line-options.html#extract) | extract area from image  
[-help](command-line-options.html#help) | print program options  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-interpolate method](command-line-options.html#interpolate) | pixel color interpolation method  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-list type](command-line-options.html#list) | Color, Configure, Delegate, Format, Magic, Module, Resource, or Type  
[-log format](command-line-options.html#log) | format of debugging information  
[-map components](command-line-options.html#stream-map) | store pixels in this format.  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-quantize colorspace](command-line-options.html#quantize) | reduce image colors in this colorspace  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-set attribute value](command-line-options.html#set) | set an image attribute  
[-size geometry](command-line-options.html#size) | width and height of image  
[-storage-type type](command-line-options.html#storage-type) | store pixels with this storage type.  
[-synchronize](command-line-options.html#synchronize) | synchronize image to storage device  
[-taint](command-line-options.html#taint) | mark the image as modified  
[-transparent-color color](command-line-options.html#transparent-color) | transparent color  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](stream.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
