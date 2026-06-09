[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](compare.html#usage) • [Option Summary](compare.html#options)

Use the `compare` program to mathematically and visually annotate the difference between an image and its reconstruction. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `compare` command or see below for example usages of the command.

## Example Usage

We list a few examples of the `compare` command here to illustrate its usefulness and ease of use. To get started, lets compare an image to one thats been sharpened:
    
    
    convert rose.jpg -sharpen 0x1 reconstruct.jpg
    compare rose.jpg reconstruct.jpg difference.png
    compare -compose src rose.jpg reconstruct.jpg difference.png
    

[![rose](../images/rose.jpg)](../images/rose.jpg) [![rose](../images/reconstruct.jpg)](../images/reconstruct.jpg) ![==>](../images/right.gif) [![rose](../images/difference.png)](../images/difference.png) 


The red areas of the difference image emphasizes (highlight) pixels that are affected by the image sharpening, whereas white de-emphasizes (lowlight) pixels that are untouched by the sharpening process.

In addition to the visual interpretation of the difference in an image and its reconstruction, we report a mathematical measure of the difference:
    
    
    -> compare -verbose -metric mae rose.jpg reconstruct.jpg difference.png
    Image: rose.jpg
     Channel distortion: MAE
      red: 2282.91 (0.034835)
      green: 1853.99 (0.0282901)
      blue: 2008.67 (0.0306503)
      all: 1536.39 (0.0234439)
    

Or, if you just want the red channel distortion, use this command:
    
    
    -> compare -channel red -metric PSNR rose.jpg reconstruct.jpg difference.png
    19.63
    

Or, if you just want the overall image distortion, use this command:
    
    
    -> compare -metric PSNR rose.jpg reconstruct.jpg difference.png
    28.31
    

If the reconstructed image is a subimage of the image, the compare program returns the best match offset. In addition, it returns a similarity image such that an exact match location is completely white and if none of the pixels match, black, otherwise some gray level in-between:
    
    
    -> compare -metric RMSE -subimage-search logo.png wizard.jpg similarity.gif
    85.05 (0.00129778) @ 353,157
    

You can find additional examples of using `compare` in [Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf/?ca=dnt-428). Further discussion is available in [More Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf2/?ca=dgr-lnxw15GraphicsLine) and [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/).

The compare program returns 2 on error otherwise 0 if the images are similar or 1 if they are dissimilar.

## Option Summary

The `compare` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-alpha](command-line-options.html#alpha) | on, activate, off, deactivate, set, opaque, copy", transparent, extract, background, or shape the alpha channel  
[-authenticate value](command-line-options.html#authenticate) | decrypt image with this password  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-compose operator](command-line-options.html#compose) | set image composite operator  
[-decipher filename](command-line-options.html#decipher) | convert cipher pixels to plain  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-dissimilarity-threshold value](command-line-options.html#dissimilarity-threshold) | maximum distortion for (sub)image match (default 0.2)  
[-encipher filename](command-line-options.html#encipher) | convert plain pixels to cipher pixels  
[-extract geometry](command-line-options.html#extract) | extract area from image  
[-fuzz distance](command-line-options.html#fuzz) | colors within this distance are considered equal  
[-help](command-line-options.html#help) | print program options  
[-highlight-color color](command-line-options.html#highlight-color) | emphasize pixel differences with this color  
[-identify](command-line-options.html#identify) | identify the format and characteristics of the image  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-log format](command-line-options.html#log) | format of debugging information  
[-lowlight-color color](command-line-options.html#lowlight-color) | de-emphasize pixel differences with this color  
[-metric type](command-line-options.html#metric) | measure differences between images with this metric  
[-profile filename](command-line-options.html#profile) | add, delete, or apply an image profile  
[-quality value](command-line-options.html#quality) | JPEG/MIFF/PNG compression level  
[-quantize colorspace](command-line-options.html#quantize) | reduce image colors in this colorspace  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-set attribute value](command-line-options.html#set) | set an image attribute  
[-similarity-threshold value](command-line-options.html#similarity-threshold) | minimum distortion for (sub)image match (default 0.0)  
[-size geometry](command-line-options.html#size) | width and height of image  
[-subimage-search](command-line-options.html#subimage-search) | search for subimage  
[-synchronize](command-line-options.html#synchronize) | synchronize image to storage device  
[-taint](command-line-options.html#taint) | mark the image as modified  
[-transparent-color color](command-line-options.html#transparent-color) | transparent color  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](compare.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
