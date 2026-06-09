[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](identify.html#usage) • [Option Summary](identify.html#options)

The `identify` program describes the format and characteristics of one or more image files. It also reports if an image is incomplete or corrupt. The information returned includes the image number, the file name, the width and height of the image, whether the image is colormapped or not, the number of colors in the image, the number of bytes in the image, the format of the image (JPEG, PNM, etc.), and finally the number of seconds it took to read and process the image. Many more attributes are available with the verbose option. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `identify` command or see below for example usages of the command.

## Example Usage

We list a few examples of the `identify` command here to illustrate its usefulness and ease of use. To get started, lets identify an image in the JPEG format:
    
    
    -> identify rose.jpg
    rose.jpg JPEG 70x46 70x46+0+0 8-bit sRGB 2.36KB 0.000u 0:00.000
    

Next, we look at the same image in greater detail:
    
    
    -> identify -verbose rose.jpg
    Image: rose.jpg
      Format: JPEG (Joint Photographic Experts Group JFIF format)
      Mime type: images/jpeg
      Class: DirectClass
      Geometry: 70x46+0+0
      Units: Undefined
      Type: TrueColor
      Endianess: Undefined
      Colorspace: sRGB
      Depth: 8-bit
      Channel depth:
        red: 8-bit
        green: 8-bit
        blue: 8-bit
      Channel statistics:
        Pixels: 3220
        Red:
          min: 35 (0.137255)
          max: 255 (1)
          mean: 145.57 (0.570865)
          standard deviation: 67.2976 (0.263912)
          kurtosis: -1.37971
          skewness: 0.0942169
          entropy: 0.974889
        Green:
          min: 33 (0.129412)
          max: 255 (1)
          mean: 89.2193 (0.349879)
          standard deviation: 52.0803 (0.204236)
          kurtosis: 2.70722
          skewness: 1.82562
          entropy: 0.877139
        Blue:
          min: 11 (0.0431373)
          max: 255 (1)
          mean: 80.3742 (0.315193)
          standard deviation: 53.8536 (0.21119)
          kurtosis: 2.90978
          skewness: 1.92617
          entropy: 0.866692
      Image statistics:
        Overall:
          min: 11 (0.0431373)
          max: 255 (1)
          mean: 105.055 (0.411979)
          standard deviation: 58.1422 (0.228008)
          kurtosis: 1.25759
          skewness: 1.4277
          entropy: 0.90624
      Rendering intent: Perceptual
      Gamma: 0.454545
      Chromaticity:
        red primary: (0.64,0.33)
        green primary: (0.3,0.6)
        blue primary: (0.15,0.06)
        white point: (0.3127,0.329)
      Background color: white
      Border color: srgb(223,223,223)
      Matte color: grey74
      Transparent color: black
      Interlace: None
      Intensity: Undefined
      Compose: Over
      Page geometry: 70x46+0+0
      Dispose: Undefined
      Iterations: 0
      Compression: JPEG
      Quality: 92
      Orientation: Undefined
      Properties:
        date:create: 2014-11-09T09:00:35-05:00
        date:modify: 2014-11-09T09:00:35-05:00
        jpeg:colorspace: 2
        jpeg:sampling-factor: 2x2,1x1,1x1
        signature: 22a99838bd5594250f706d1d9383b2830f439fcbaf1455cbe2f7f59a4deb065a
      Artifacts:
        filename: rose.jpg
        verbose: true
      Tainted: False
      Filesize: 2.36KB
      Number pixels: 3.22K
      Pixels per second: 3.22EB
      User time: 0.000u
      Elapsed time: 0:01.000
      Version: ImageMagick Q16 http://www.imagemagick.org
    

To get the print size in inches of an image at 72 DPI, use:
    
    
    -> identify -format "%[fx:w/72] by %[fx:h/72] inches" document.png
    8.5 x 11 inches
    

The depth and dimensions of a raw image must be specified on the command line:
    
    
    -> identify -depth 8 -size 640x480 image.raw
    image.raw RGB 640x480 sRGB 9kb 0.000u 0:01
    

Here we display the image texture features, moments, perceptual hash, and the number of unique colors in the image:
    
    
    -> identify -verbose -features 1 -moments -unique image.png
    

Here is a special define that outputs the location of the minimum or maximum pixel of the image:
    
    
    identify -precision 5 -define identify:locate=maximum -define identify:limit=3 image.png
    

You can find additional examples of using `identify` in [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/).

## Option Summary

The `identify` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-alpha](command-line-options.html#alpha) | on, activate, off, deactivate, set, opaque, copy", transparent, extract, background, or shape the alpha channel  
[-antialias](command-line-options.html#antialias) | remove pixel-aliasing  
[-authenticate value](command-line-options.html#authenticate) | decrypt image with this password  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-clip](command-line-options.html#clip) | clip along the first path from the 8BIM profile  
[-clip-mask](command-line-options.html#clip-mask) filename | associate clip mask with the image  
[-clip-path id](command-line-options.html#clip-path) | clip along a named path from the 8BIM profile  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-crop geometry](command-line-options.html#crop) | crop the image  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-endian type](command-line-options.html#endian) | endianness (MSB or LSB) of the image  
[-extract geometry](command-line-options.html#extract) | extract area from image  
[-features distance](command-line-options.html#features) | analyze image features (e.g. contract, correlations, etc.).  
[-format string](command-line-options.html#format_identify_) | output formatted image characteristics  
[-gamma value](command-line-options.html#gamma) | level of gamma correction  
[-grayscale method](command-line-options.html#intensity) | convert image to grayscale  
[-help](command-line-options.html#help) | print program options  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-interpolate method](command-line-options.html#interpolate) | pixel color interpolation method  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-list type](command-line-options.html#list) | Color, Configure, Delegate, Format, Magic, Module, Resource, or Type  
[-log format](command-line-options.html#log) | format of debugging information  
[-mask filename](command-line-options.html#mask) | associate a mask with the image  
[-moments](command-line-options.html#moments) | display image moments and perceptual hash.  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-negate](command-line-options.html#negate) | replace each pixel with its complementary color   
[-precision value](command-line-options.html#precision) | set the maximum number of significant digits to be printed  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-set attribute value](command-line-options.html#set) | set an image attribute  
[-size geometry](command-line-options.html#size) | width and height of image  
[-strip](command-line-options.html#strip) | strip image of all profiles and comments  
[-unique](command-line-options.html#unique) | display image the number of unique colors in the image.  
[-units type](command-line-options.html#units) | the units of image resolution  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](identify.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
