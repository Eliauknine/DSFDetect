[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

Use the `convert` program to convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `convert` command or see below for example usages of the command.

We list a few examples of the `convert` command here to illustrate its usefulness and ease of use. To get started, lets convert an image in the JPEG format to PNG:
    
    
    convert rose.jpg rose.png
    

Next, we reduce the image size before it is written to the PNG format:
    
    
    convert rose.jpg -resize 50% rose.png
    

[ ![rose](../images/rose.jpg) ](../images/rose.jpg) ![==>](../images/right.gif) [ ![rose](../images/rose.png) ](../images/rose.png) 


You can combine multiple image-processing operations to produce complex results:
    
    
    convert -size 320x85 canvas:none -font Bookman-DemiItalic -pointsize 72 \
      -draw "text 25,60 \'Magick\'" -channel RGBA -blur 0x6 -fill darkred -stroke magenta \
      -draw "text 20,55 \'Magick\'" fuzzy-magick.png
    

[![fuzzy-magick](../images/fuzzy-magick.png)](../images/fuzzy-magick.png) 


or here we resize an image with improved quality:
    
    
    convert input.png -colorspace RGB +sigmoidal-contrast 11.6933 \
      -define filter:filter=Sinc -define filter:window=Jinc -define filter:lobes=3 \
      -resize 400% -sigmoidal-contrast 11.6933 -colorspace sRGB output.png');
    

You can find additional examples of using `convert` in [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/).

## Option Summary

The `convert` command recognizes these options. Click on an option to get more details about how that option works.

[-adaptive-blur geometry](command-line-options.html#adaptive-blur) | adaptively blur pixels; decrease effect near edges  
---|---  
[-adaptive-resize geometry](command-line-options.html#adaptive-resize) | adaptively resize image with data dependent triangulation.  
[-adaptive-sharpen geometry](command-line-options.html#adaptive-sharpen) | adaptively sharpen pixels; increase effect near edges  
[-adjoin](command-line-options.html#adjoin) | join images into a single multi-image file  
[-affine matrix](command-line-options.html#affine) | affine transform matrix  
[-alpha](command-line-options.html#alpha) | on, activate, off, deactivate, set, opaque, copy", transparent, extract, background, or shape the alpha channel  
[-annotate geometry text](command-line-options.html#annotate) | annotate the image with text  
[-antialias](command-line-options.html#antialias) | remove pixel-aliasing  
[-append](command-line-options.html#append) | append an image sequence  
[-authenticate value](command-line-options.html#authenticate) | decipher image with this password  
[-auto-gamma](command-line-options.html#auto-gamma) | automagically adjust gamma level of image  
[-auto-level](command-line-options.html#auto-level) | automagically adjust color levels of image  
[-auto-orient](command-line-options.html#auto-orient) | automagically orient image  
[-background color](command-line-options.html#background) | background color  
[-bench iterations](command-line-options.html#bench) | measure performance  
[-bias value](command-line-options.html#bias) | add bias when convolving an image  
[-black-threshold value](command-line-options.html#black-threshold) | force all pixels below the threshold into black  
[-blue-primary point](command-line-options.html#blue-primary) | chromaticity blue primary point  
[-blue-shift factor](command-line-options.html#blue-shift) | simulate a scene at nighttime in the moonlight  
[-blur geometry](command-line-options.html#blur) | reduce image noise and reduce detail levels  
[-border geometry](command-line-options.html#border) | surround image with a border of color  
[-bordercolor color](command-line-options.html#bordercolor) | border color  
[-brightness-contrast geometry](command-line-options.html#brightness-contrast) | improve brightness / contrast of the image  
[-canny geometry](command-line-options.html#canny) | use a multi-stage algorithm to detect a wide range of edges in the image  
[-caption string](command-line-options.html#caption) | assign a caption to an image  
[-cdl filename](command-line-options.html#cdl) | color correct with a color decision list  
[-channel type](command-line-options.html#channel) | apply option to select image channels  
[-charcoal radius](command-line-options.html#charcoal) | simulate a charcoal drawing  
[-chop geometry](command-line-options.html#chop) | remove pixels from the image interior  
[-clamp](command-line-options.html#clamp) | set each pixel whose value is below zero to zero and any the pixel whose value is above the quantum range to the quantum range (e.g. 65535) otherwise the pixel value remains unchanged.  
[-clip](command-line-options.html#clip) | clip along the first path from the 8BIM profile  
[-clip-mask](command-line-options.html#clip-mask) filename | associate clip mask with the image  
[-clip-path id](command-line-options.html#clip-path) | clip along a named path from the 8BIM profile  
[-clone index](command-line-options.html#clone) | clone an image  
[-clut](command-line-options.html#clut) | apply a color lookup table to the image  
[-connected-components connectivity](command-line-options.html#connected-components) | connected-components uniquely labeled, choose from 4 or 8 way connectivity  
[-contrast-stretch geometry](command-line-options.html#contrast-stretch) | improve the contrast in an image by `stretching' the range of intensity value  
[-coalesce](command-line-options.html#coalesce) | merge a sequence of images  
[-colorize value](command-line-options.html#colorize) | colorize the image with the fill color  
[-color-matrix matrix](command-line-options.html#color-matrix) | apply color correction to the image.  
[-colors value](command-line-options.html#colors) | preferred number of colors in the image  
[-colorspace type](command-line-options.html#colorspace) | set image colorspace  
[-combine](command-line-options.html#combine) | combine a sequence of images  
[-comment string](command-line-options.html#comment) | annotate image with comment  
[-compare](command-line-options.html#compare) | compare image  
[-complexoperator](command-line-options.html#complex) | perform complex mathematics on an image sequence  
[-compose operator](command-line-options.html#compose) | set image composite operator  
[-composite](command-line-options.html#composite) | composite image  
[-compress type](command-line-options.html#compress) | image compression type  
[-contrast](command-line-options.html#contrast) | enhance or reduce the image contrast  
[-convolve coefficients](command-line-options.html#convolve) | apply a convolution kernel to the image  
[-copy geometry offset](command-line-options.html#copy) | copy pixels from one area of an image to another  
[-crop geometry](command-line-options.html#crop) | crop the image  
[-cycle amount](command-line-options.html#cycle) | cycle the image colormap  
[-decipher filename](command-line-options.html#decipher) | convert cipher pixels to plain  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-define format:option](command-line-options.html#define) | define one or more image format options  
[-deconstruct](command-line-options.html#deconstruct) | break down an image sequence into constituent parts  
[-delay value](command-line-options.html#delay) | display the next image after pausing  
[-delete index](command-line-options.html#delete) | delete the image from the image sequence  
[-density geometry](command-line-options.html#density) | horizontal and vertical density of the image  
[-depth value](command-line-options.html#depth) | image depth  
[-despeckle](command-line-options.html#despeckle) | reduce the speckles within an image  
[-direction type](command-line-options.html#direction) | render text right-to-left or left-to-right  
[-display server](command-line-options.html#display) | get image or font from this X server  
[-dispose method](command-line-options.html#dispose) | layer disposal method  
[-distribute-cache port](command-line-options.html#distribute-cache) | launch a distributed pixel cache server  
[-distort type coefficients](command-line-options.html#distort) | distort image  
[-dither method](command-line-options.html#dither) | apply error diffusion to image  
[-draw string](command-line-options.html#draw) | annotate the image with a graphic primitive  
[-duplicate count,indexes](command-line-options.html#duplicate) | duplicate an image one or more times  
[-edge radius](command-line-options.html#edge) | apply a filter to detect edges in the image  
[-emboss radius](command-line-options.html#emboss) | emboss an image  
[-encipher filename](command-line-options.html#encipher) | convert plain pixels to cipher pixels  
[-encoding type](command-line-options.html#encoding) | text encoding type  
[-endian type](command-line-options.html#endian) | endianness (MSB or LSB) of the image  
[-enhance](command-line-options.html#enhance) | apply a digital filter to enhance a noisy image  
[-equalize](command-line-options.html#equalize) | perform histogram equalization to an image  
[-evaluate operator value](command-line-options.html#evaluate) | evaluate an arithmetic, relational, or logical expression  
[-evaluate-sequence operator](command-line-options.html#evaluate-sequence) | evaluate an arithmetic, relational, or logical expression for an image sequence  
[-extent geometry](command-line-options.html#extent) | set the image size  
[-extract geometry](command-line-options.html#extract) | extract area from image  
[-family name](command-line-options.html#family) | render text with this font family  
[-features distance](command-line-options.html#features) | analyze image features (e.g. contract, correlations, etc.).  
[-fft](command-line-options.html#fft) | implements the discrete Fourier transform (DFT)  
[-fill color](command-line-options.html#fill) | color to use when filling a graphic primitive  
[-filter type](command-line-options.html#filter) | use this filter when resizing an image  
[-flatten](command-line-options.html#flatten) | flatten a sequence of images  
[-flip](command-line-options.html#flip) | flip image in the vertical direction  
[-floodfill geometry color](command-line-options.html#floodfill) | floodfill the image with color  
[-flop](command-line-options.html#flop) | flop image in the horizontal direction  
[-font name](command-line-options.html#font) | render text with this font  
[-format string](command-line-options.html#format_identify_) | output formatted image characteristics  
[-frame geometry](command-line-options.html#frame) | surround image with an ornamental border  
[-function name](command-line-options.html#function) | apply a function to the image  
[-fuzz distance](command-line-options.html#fuzz) | colors within this distance are considered equal  
[-fx expression](command-line-options.html#fx) | apply mathematical expression to an image channel(s)  
[-gamma value](command-line-options.html#gamma) | level of gamma correction  
[-gaussian-blur geometry](command-line-options.html#gaussian-blur) | reduce image noise and reduce detail levels  
[-geometry geometry](command-line-options.html#geometry) | preferred size or location of the image  
[-gravity type](command-line-options.html#gravity) | horizontal and vertical text placement  
[-grayscale method](command-line-options.html#intensity) | convert image to grayscale  
[-green-primary point](command-line-options.html#green-primary) | chromaticity green primary point  
[-help](command-line-options.html#help) | print program options  
[-hough-lines geometry](command-line-options.html#hough-lines) | identify lines in the image  
[-identify](command-line-options.html#identify) | identify the format and characteristics of the image  
[-ift](command-line-options.html#ift) | implements the inverse discrete Fourier transform (DFT)  
[-implode amount](command-line-options.html#implode) | implode image pixels about the center  
[-insert index](command-line-options.html#insert) | insert last image into the image sequence  
[-intensity method](command-line-options.html#intensity) | method to generate an intensity value from a pixel  
[-intent type](command-line-options.html#intent) | type of rendering intent when managing the image color  
[-interlace type](command-line-options.html#interlace) | type of image interlacing scheme  
[-interline-spacing value](command-line-options.html#interline-spacing) | the space between two text lines  
[-interpolate method](command-line-options.html#interpolate) | pixel color interpolation method  
[-interword-spacing value](command-line-options.html#interword-spacing) | the space between two words  
[-kerning value](command-line-options.html#kerning) | the space between two characters  
[-kuwahara geometry](command-line-options.html#kuwahara) | edge preserving noise reduction filter  
[-label string](command-line-options.html#label) | assign a label to an image  
[-lat geometry](command-line-options.html#lat) | local adaptive thresholding  
[-layers method](command-line-options.html#layers) | optimize or compare image layers  
[-level value](command-line-options.html#level) | adjust the level of image contrast  
[-limit type value](command-line-options.html#limit) | pixel cache resource limit  
[-linear-stretch geometry](command-line-options.html#linear-stretch) | linear with saturation histogram stretch  
[-liquid-rescale geometry](command-line-options.html#liquid-rescale) | rescale image with seam-carving  
[-list type](command-line-options.html#list) | Color, Configure, Delegate, Format, Magic, Module, Resource, or Type  
[-log format](command-line-options.html#log) | format of debugging information  
[-loop iterations](command-line-options.html#loop) | add Netscape loop extension to your GIF animation  
[-mask filename](command-line-options.html#mask) | associate a mask with the image  
[-mattecolor color](command-line-options.html#mattecolor) | frame color  
[-median radius](command-line-options.html#median) | apply a median filter to the image  
[-mean-shift geometry](command-line-options.html#mean-shift) | delineate arbitrarily shaped clusters in the image  
[-metric type](command-line-options.html#metric) | measure differences between images with this metric  
[-mode radius](command-line-options.html#mode) | make each pixel the 'predominant color' of the neighborhood  
[-modulate value](command-line-options.html#modulate) | vary the brightness, saturation, and hue  
[-moments](command-line-options.html#moments) | display image moments.  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-monochrome](command-line-options.html#monochrome) | transform image to black and white  
[-morph value](command-line-options.html#morph) | morph an image sequence  
[-morphology method](command-line-options.html#morphology) kernel | apply a morphology method to the image  
[-motion-blur geometry](command-line-options.html#motion-blur) | simulate motion blur  
[-negate](command-line-options.html#negate) | replace each pixel with its complementary color   
[-noise radius](command-line-options.html#noise) | add or reduce noise in an image  
[-normalize](command-line-options.html#normalize) | transform image to span the full range of colors  
[-opaque color](command-line-options.html#opaque) | change this color to the fill color  
[-ordered-dither NxN](command-line-options.html#ordered-dither) | ordered dither the image  
[-orient type](command-line-options.html#orient) | image orientation  
[-page geometry](command-line-options.html#page) | size and location of an image canvas (setting)  
[-paint radius](command-line-options.html#paint) | simulate an oil painting  
[-perceptible](command-line-options.html#perceptible) | set each pixel whose value is less than |epsilon| to -epsilon or epsilon (whichever is closer) otherwise the pixel value remains unchanged.  
[-ping](command-line-options.html#ping) | efficiently determine image attributes  
[-pointsize value](command-line-options.html#pointsize) | font point size  
[-polaroid angle](command-line-options.html#polaroid) | simulate a Polaroid picture  
[-poly terms](command-line-options.html#poly) | build a polynomial from the image sequence and the corresponding terms (coefficients and degree pairs).  
[-posterize levels](command-line-options.html#posterize) | reduce the image to a limited number of color levels  
[-precision value](command-line-options.html#precision) | set the maximum number of significant digits to be printed  
[-preview type](command-line-options.html#preview) | image preview type  
[-print string](command-line-options.html#print) | interpret string and print to console  
[-process image-filter](command-line-options.html#process) | process the image with a custom image filter  
[-profile filename](command-line-options.html#profile) | add, delete, or apply an image profile  
[-quality value](command-line-options.html#quality) | JPEG/MIFF/PNG compression level  
[-quantize colorspace](command-line-options.html#quantize) | reduce image colors in this colorspace  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-radial-blur angle](command-line-options.html#radial-blur) | radial blur the image  
[-raise value](command-line-options.html#raise) | lighten/darken image edges to create a 3-D effect  
[-random-threshold low,high](command-line-options.html#random-threshold) | random threshold the image  
[-red-primary point](command-line-options.html#red-primary) | chromaticity red primary point  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-region geometry](command-line-options.html#region) | apply options to a portion of the image  
[-remap filename](command-line-options.html#remap) | transform image colors to match this set of colors  
[-render](command-line-options.html#render) | render vector graphics  
[-repage geometry](command-line-options.html#repage) | size and location of an image canvas  
[-resample geometry](command-line-options.html#resample) | change the resolution of an image  
[-resize geometry](command-line-options.html#resize) | resize the image  
[-respect-parentheses](command-line-options.html#respect-parentheses) | settings remain in effect until parenthesis boundary.  
[-roll geometry](command-line-options.html#roll) | roll an image vertically or horizontally  
[-rotate degrees](command-line-options.html#rotate) | apply Paeth rotation to the image  
[-sample geometry](command-line-options.html#sample) | scale image with pixel sampling  
[-sampling-factor geometry](command-line-options.html#sampling-factor) | horizontal and vertical sampling factor  
[-scale geometry](command-line-options.html#scale) | scale the image  
[-scene value](command-line-options.html#scene) | image scene number  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-segment values](command-line-options.html#segment) | segment an image  
[-selective-blur geometry](command-line-options.html#threshold) | selectively blur pixels within a contrast threshold  
[-separate](command-line-options.html#separate) | separate an image channel into a grayscale image  
[-sepia-tone threshold](command-line-options.html#sepia-tone) | simulate a sepia-toned photo  
[-set attribute value](command-line-options.html#set) | set an image attribute  
[-shade degrees](command-line-options.html#shade) | shade the image using a distant light source  
[-shadow geometry](command-line-options.html#shadow) | simulate an image shadow  
[-sharpen geometry](command-line-options.html#sharpen) | sharpen the image  
[-shave geometry](command-line-options.html#shave) | shave pixels from the image edges  
[-shear geometry](command-line-options.html#shear) | slide one edge of the image along the X or Y axis  
[-sigmoidal-contrast geometry](command-line-options.html#sigmoidal) | increase the contrast without saturating highlights or shadows  
[-smush offset](command-line-options.html#smush) | smush an image sequence together  
[-size geometry](command-line-options.html#size) | width and height of image  
[-sketch geometry](command-line-options.html#sketch) | simulate a pencil sketch  
[-solarize threshold](command-line-options.html#solarize) | negate all pixels above the threshold level  
[-splice geometry](command-line-options.html#splice) | splice the background color into the image  
[-spread radius](command-line-options.html#spread) | displace image pixels by a random amount  
[-statistic type geometry](command-line-options.html#statistic) | replace each pixel with corresponding statistic from the neighborhood  
[-strip](command-line-options.html#strip) | strip image of all profiles and comments  
[-stroke color](command-line-options.html#stroke) | graphic primitive stroke color  
[-strokewidth value](command-line-options.html#strokewidth) | graphic primitive stroke width  
[-stretch type](command-line-options.html#stretch) | render text with this font stretch  
[-style type](command-line-options.html#style) | render text with this font style  
[-swap indexes](command-line-options.html#swap) | swap two images in the image sequence  
[-swirl degrees](command-line-options.html#swirl) | swirl image pixels about the center  
[-synchronize](command-line-options.html#synchronize) | synchronize image to storage device  
[-taint](command-line-options.html#taint) | mark the image as modified  
[-texture filename](command-line-options.html#texture) | name of texture to tile onto the image background  
[-threshold value](command-line-options.html#threshold) | threshold the image  
[-thumbnail geometry](command-line-options.html#thumbnail) | create a thumbnail of the image  
[-tile filename](command-line-options.html#tile) | tile image when filling a graphic primitive  
[-tile-offset geometry](command-line-options.html#tile-offset) | set the image tile offset  
[-tint value](command-line-options.html#tint) | tint the image with the fill color  
[-transform](command-line-options.html#transform) | affine transform image  
[-transparent color](command-line-options.html#transparent) | make this color transparent within the image  
[-transparent-color color](command-line-options.html#transparent-color) | transparent color  
[-transpose](command-line-options.html#transpose) | flip image in the vertical direction and rotate 90 degrees  
[-transverse](command-line-options.html#transverse) | flop image in the horizontal direction and rotate 270 degrees  
[-treedepth value](command-line-options.html#treedepth) | color tree depth  
[-trim](command-line-options.html#trim) | trim image edges  
[-type type](command-line-options.html#type) | image type  
[-undercolor color](command-line-options.html#undercolor) | annotation bounding box color  
[-unique-colors](command-line-options.html#unique-colors) | discard all but one of any pixel color.  
[-units type](command-line-options.html#units) | the units of image resolution  
[-unsharp geometry](command-line-options.html#unsharp) | sharpen the image  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
[-view](command-line-options.html#view) | FlashPix viewing transforms  
[-vignette geometry](command-line-options.html#vignette) | soften the edges of the image in vignette style  
[-virtual-pixel method](command-line-options.html#virtual-pixel) | access method for pixels outside the boundaries of the image  
[-wave geometry](command-line-options.html#wave) | alter an image along a sine wave  
[-wavelet-denoise threshold](command-line-options.html#wavelet) | removes noise from the image using a wavelet transform  
[-weight type](command-line-options.html#weight) | render text with this font weight  
[-white-point point](command-line-options.html#white-point) | chromaticity white point  
[-white-threshold value](command-line-options.html#white-threshold) | force all pixels above the threshold into white  
[-write filename](command-line-options.html#write) | write images to this file  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](convert.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
