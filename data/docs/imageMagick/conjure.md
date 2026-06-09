[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Example Usage](conjure.html#usage) • [Option Summary](conjure.html#options) • [Magick Scripting Language (MSL)](conjure.html#msl)

The `conjure` program gives you the ability to perform custom image processing tasks from a script written in the Magick Scripting Language (MSL). MSL is XML-based and consists of action statements with attributes. Actions include reading an image, processing an image, getting attributes from an image, writing an image, and more. An attribute is a key/value pair that modifies the behavior of an action. See [Command Line Processing](command-line-processing.html) for advice on how to structure your `conjure` command or see below for example usages of the command.

## Example Usage

We list a few examples of the `conjure` command here to illustrate its usefulness and ease of use. To get started, here is simple `conjure` command:
    
    
    conjure -dimensions 400x400 incantation.msl
    

The MSL script [incantation.msl](../source/incantation.msl) used above is here:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <image>
      <read filename="image.gif" />
      <get width="base-width" height="base-height" />
      <resize geometry="%[dimensions]" />
      <get width="resize-width" height="resize-height" />
      <print output="Image sized from %[base-width]x%[base-height] to %[resize-width]x%[resize-height].\n" />
      <write filename="image.png" />
    </image>
    

In this example, a family stayed home for their vacation but as far as their friends are concerned they went to a beautiful beach in the Caribbean:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <group>
        <image id="family">
            <read filename="family.gif"/>
            <resize geometry="300x300"/>
        </image>
        <image id="palm-trees">
            <read filename="palm-trees.gif"/>
            <resize geometry="300x100"/>
        </image>
        <image>
            <read filename="beach.jpg"/>
            <composite image="family" geometry="+30+40"/>
            <composite image="palm-trees" geometry="+320+90"/>
        </image>
        <write filename="family-vacation.png"/>
    </group>
    

Here we display the width in pixels of text for a particular font and pointsize.
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <image>
      <query-font-metrics text="ImageMagick" font="helvetica" pointsize="48" />
      <print output="Text width is %[msl:font-metrics.width] pixels.\n" />
    </image>
    

The `query-font-metrics` tag supports these properties:
    
    
    msl:font-metrics.pixels_per_em.x
    msl:font-metrics.pixels_per_em.y
    msl:font-metrics.ascent
    msl:font-metrics.descent
    msl:font-metrics.width
    msl:font-metrics.height
    msl:font-metrics.max_advance
    msl:font-metrics.bounds.x1
    msl:font-metrics.bounds.y1
    msl:font-metrics.bounds.x2
    msl:font-metrics.bounds.y2
    msl:font-metrics.origin.x
    msl:font-metrics.origin.y
    

MSL supports most methods and attributes discussed in the [Perl API for ImageMagick](perl-magick.html). 

In addition, MSL supports the `swap` element with a single `indexes` element.

You can find additional examples of using `conjure` in [Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf/?ca=dnt-428). Further discussion is available in [More Graphics from the Command Line](http://www.ibm.com/developerworks/library/l-graf2/?ca=dgr-lnxw15GraphicsLine) and [Examples of ImageMagick Usage](http://www.imagemagick.org/Usage/).

## Option Summary

The `conjure` command recognizes these options. Click on an option to get more details about how that option works.

Option | Description  
---|---  
[-debug events](command-line-options.html#debug) | display copious debugging information  
[-help](command-line-options.html#help) | print program options  
[-log format](command-line-options.html#log) | format of debugging information  
[-monitor](command-line-options.html#monitor) | monitor progress  
[-quiet](command-line-options.html#quiet) | suppress all warning messages  
[-regard-warnings](command-line-options.html#regard-warnings) | pay attention to warning messages.  
[-seed value](command-line-options.html#seed) | seed a new sequence of pseudo-random numbers  
[-verbose](command-line-options.html#verbose) | print detailed information about the image  
[-version](command-line-options.html#version) | print version information  
  
## Magick Scripting Language

The `conjure` command recognizes these MSL elements. Any element with a strike-thru is not supported yet.

Magick Scripting Language (MSL) Method | Parameters | Description  
---|---|---  
~~adaptiveblur~~ | geometry="geometry", radius="double", sigma="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | adaptively blur the image with a Gaussian operator of the given radius and standard deviation (sigma). Decrease the effect near edges.  
~~adaptiveresize~~ | geometry="geometry", width="integer", height="integer", filter="Point, Box, Triangle, Hermite, Hanning, Hamming, Blackman, Gaussian, Quadratic, Cubic, Catrom, Mitchell, Lanczos, Bessel, Sinc", support="double", blur="double" | adaptively resize image using data dependant triangulation. Specify blur > 1 for blurry or < 1 for sharp  
~~adaptivesharpen~~ | geometry="geometry", radius="double", sigma="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | adaptively sharpen the image with a Gaussian operator of the given radius and standard deviation (sigma). Increase the effect near edges.  
~~adaptivethreshold~~ | geometry="geometry", width="integer", height="integer", offset="integer" | local adaptive thresholding.  
~~addnoise~~ | noise="Uniform, Gaussian, Multiplicative, Impulse, Laplacian, Poisson", attenuate="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | add noise to an image  
~~affinetransform~~ | affine="array of float values", translate="float, float", scale= "float, float", rotate="float", skewX="float", skewY="float", interpolate="Average, Bicubic, Bilinear, Filter, Integer, Mesh, NearestNeighbor", background="color name" | affine transform image  
~~affinity~~ | image="image-handle", method="None, FloydSteinberg, Riemersma" | choose a particular set of colors from this image  
<annotate> | text="string", font="string", family="string", style="Normal, Italic, Oblique, Any", stretch="Normal, UltraCondensed, ExtraCondensed, Condensed, SemiCondensed, SemiExpanded, Expanded, ExtraExpanded, UltraExpanded", weight="integer", pointsize="integer", density="geometry", stroke="color name", strokewidth="integer", fill="color name", undercolor="color name", kerning="float", geometry="geometry", gravity="NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast", antialias="true, false", x="integer", y="integer", affine="array of float values", translate="float, float", scale="float, float", rotate="float". skewX="float", skewY= "float", align="Left, Center, Right", encoding="UTF-8", interline-spacing="double", interword-spacing="double", direction="right-to-left, left-to-right" | annotate an image with text. See QueryFontMetrics to get font metrics without rendering any text.  
~~autogamma~~ | channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | automagically adjust gamma level of image  
~~autolevel~~ | channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | automagically adjust color levels of image  
~~autoorient~~ |  | adjusts an image so that its orientation is suitable for viewing (i.e. top-left orientation)  
~~blackthreshold~~ | threshold="string", , channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | force all pixels below the threshold intensity into black  
~~blueshift~~ | factor="double", | simulate a scene at nighttime in the moonlight. Start with a factor of 1.5.  
<blur> | geometry="geometry", radius="double", sigma="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | reduce image noise and reduce detail levels with a Gaussian operator of the given radius and standard deviation (sigma).  
<border> | geometry="geometry", width="integer", height="integer", bordercolor="color name", compose="Undefined, Add, Atop, Blend, Bumpmap, Clear, ColorBurn, ColorDodge, Colorize, CopyBlack, CopyBlue, CopyCMYK, Cyan, CopyGreen, Copy, CopyMagenta, CopyOpacity, CopyRed, RGB, CopyYellow, Darken, Dst, Difference, Displace, Dissolve, DstAtop, DstIn, DstOut, DstOver, Dst, Exclusion, HardLight, Hue, In, Lighten, Luminize, Minus, Modulate, Multiply, None, Out, Overlay, Over, Plus, ReplaceCompositeOp, Saturate, Screen, SoftLight, Src, SrcAtop, SrcIn, SrcOut, SrcOver, Src, Subtract, Threshold, Xor ", | surround the image with a border of color  
<charcoal> | geometry="geometry", radius="double", sigma="double" | simulate a charcoal drawing  
<chop> | geometry="geometry", width="integer", height="integer", x="integer", y="integer" | chop an image  
~~clamp~~ | channel="Red, RGB, All, etc." | set each pixel whose value is below zero to zero and any the pixel whose value is above the quantum range to the quantum range (e.g. 65535) otherwise the pixel value remains unchanged.  
~~clip~~ | id="name", inside=""true, false"", | apply along a named path from the 8BIM profile.  
~~clipmask~~ | mask="image-handle" | clip image as defined by the image mask  
~~clut~~ | image="image-handle", interpolate="Average, Bicubic, Bilinear, Filter, Integer, Mesh, NearestNeighbor", channel="Red, RGB, All, etc." | apply a color lookup table to an image sequence  
~~coalesce~~ |  | merge a sequence of images  
~~color~~ | color="color name" | set the entire image to this color.  
~~colordecisionlist~~ | filename="string", | color correct with a color decision list.  
<colorize> | fill="color name", blend="string" | colorize the image with the fill color  
~~colormatrix~~ | matrix="array of float values" | apply color correction to the image. Although you can use variable sized matrices, typically you use a 5 x 5 for an RGBA image and a 6x6 for CMYKA. A 6x6 matrix is required for offsets (populate the last column with normalized values).  
<comment> | string | add a comment to your image  
~~comparelayers~~ | method="any, clear, overlay" | compares each image with the next in a sequence and returns the minimum bounding region of any pixel differences it discovers. Images do not have to be the same size, though it is best that all the images are coalesced (images are all the same size, on a flattened canvas, so as to represent exactly how a specific frame should look).  
<composite> | image="image-handle", compose="Undefined, Add, Atop, Blend, Bumpmap, Clear, ColorBurn, ColorDodge, Colorize, CopyBlack, CopyBlue, CopyCMYK, Cyan, CopyGreen, Copy, CopyMagenta, CopyOpacity, CopyRed, RGB, CopyYellow, Darken, Dst, Difference, Displace, Dissolve, DstAtop, DstIn, DstOut, DstOver, Dst, Exclusion, HardLight, Hue, In, Lighten, Luminize, Minus, Modulate, Multiply, None, Out, Overlay, Over, Plus, ReplaceCompositeOp, Saturate, Screen, SoftLight, Src, SrcAtop, SrcIn, SrcOut, SrcOver, Src, Subtract, Threshold, Xor ", mask="image-handle", geometry="geometry", x="integer", y="integer", gravity="NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast", opacity="integer", tile="True, False", rotate="double", color="color name", blend="geometry", interpolate="undefined, average, bicubic, bilinear, filter, integer, mesh, nearest-neighbor, spline" | composite one image onto another. Use the rotate parameter in concert with the tile parameter.  
<contrast> | sharpen="True, False" | enhance or reduce the image contrast  
~~contraststretch~~ | levels="string", 'black-point'="double", 'white-point'="double", channel="Red, RGB, All, etc." | improve the contrast in an image by `stretching' the range of intensity values  
~~convolve~~ | coefficients="array of float values", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", bias="double" | apply a convolution kernel to the image. Given a kernel "order" , you would supply "order*order" float values (e.g. 3x3 implies 9 values).  
<crop> | geometry="geometry", width="integer", height="integer", x="integer", y="integer", fuzz="double", gravity="NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast" | crop an image  
~~cyclecolormap~~ | amount="integer" | displace image colormap by amount  
~~decipher~~ | passphrase="string" | convert cipher pixels to plain pixels  
~~deconstruct~~ |  | break down an image sequence into constituent parts  
~~deskew~~ | geometry="string",threshold="double" | straighten the image  
<despeckle> |  | reduce the speckles within an image  
~~difference~~ | image="image-handle" | compute the difference metrics between two images   
~~distort~~ | points="array of float values", method="Affine, AffineProjection, Bilinear, Perspective, Resize, ScaleRotateTranslate", virtual-pixel="Background Black Constant Dither Edge Gray Mirror Random Tile Transparent White", best-fit="True, False" | distort image  
<draw> | primitive="point, line, rectangle, arc, ellipse, circle, path, polyline, polygon, bezier, color, matte, text, @"filename"", points="string" , method=""Point, Replace, Floodfill, FillToBorder, Reset"", stroke="color name", fill="color name", font="string", pointsize="integer", strokewidth="float", antialias="true, false", bordercolor="color name", x="float", y="float", dash-offset="float", dash-pattern="array of float values", affine="array of float values", translate="float, float", scale="float, float", rotate="float", skewX="float", skewY="float", interpolate="undefined, average, bicubic, bilinear, mesh, nearest-neighbor, spline", kerning="float", text="string", vector-graphics="string", interline-spacing="double", interword-spacing="double", direction="right-to-left, left-to-right" | annotate an image with one or more graphic primitives.  
~~encipher~~ | passphrase="string" | convert plain pixels to cipher pixels  
<edge> | radius="double" | enhance edges within the image with a convolution filter of the given radius.  
<emboss> | geometry="geometry", radius="double", sigma="double" | emboss the image with a convolution filter of the given radius and standard deviation (sigma).  
<enhance> |  | apply a digital filter to enhance a noisy image  
<equalize> | channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow"  | perform histogram equalization to the image  
~~extent~~ | geometry="geometry", width="integer", height="integer", x="integer", y="integer", fuzz="double", background="color name", gravity="NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast" | set the image size  
~~evaluate~~ | value="double", operator=""Add, And, Divide, LeftShift, Max, Min, Multiply, Or, Rightshift, Subtract, Xor"", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow"  | apply an arithmetic, relational, or logical expression to the image  
~~filter~~ | kernel="string", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", bias="double" | apply a convolution kernel to the image.  
<flip> |  | reflect the image scanlines in the vertical direction  
<flop> |  | reflect the image scanlines in the horizontal direction  
~~floodfillpaint~~ | geometry="geometry", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", x="integer", y="integer" , fill="color name", bordercolor="color name", fuzz="double", invert="True, False" | changes the color value of any pixel that matches the color of the target pixel and is a neighbor. If you specify a border color, the color value is changed for any neighbor pixel that is not that color.  
~~forwardfouriertransform~~ | magnitude="True, False" | implements the forward discrete Fourier transform (DFT)  
<frame> | geometry="geometry", width="integer", height="integer", inner="integer", outer="integer", fill="color name", compose="Undefined, Add, Atop, Blend, Bumpmap, Clear, ColorBurn, ColorDodge, Colorize, CopyBlack, CopyBlue, CopyCMYK, Cyan, CopyGreen, Copy, CopyMagenta, CopyOpacity, CopyRed, RGB, CopyYellow, Darken, Dst, Difference, Displace, Dissolve, DstAtop, DstIn, DstOut, DstOver, Dst, Exclusion, HardLight, Hue, In, Lighten, Luminize, Minus, Modulate, Multiply, None, Out, Overlay, Over, Plus, ReplaceCompositeOp, Saturate, Screen, SoftLight, Src, SrcAtop, SrcIn, SrcOut, SrcOver, Src, Subtract, Threshold, Xor ", | surround the image with an ornamental border  
~~function~~ | parameters="array of float values", function="Sin", virtual-pixel="Background Black Constant Dither Edge Gray Mirror Random Tile Transparent White" | apply a function to the image  
<gamma> | gamma="string", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | gamma correct the image  
~~gaussianblur~~ | geometry="geometry", radius="double", sigma="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | reduce image noise and reduce detail levels with a Gaussian operator of the given radius and standard deviation (sigma).  
~~getpixel~~ | geometry="geometry", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", normalize="true, false", x="integer", y="integer" | get a single pixel. By default normalized pixel values are returned.  
~~getpixels~~ | geometry="geometry", width="integer", height="integer", x="integer", y="integer", map="string", normalize="true, false" | get image pixels as defined by the map (e.g. "RGB", "RGBA", etc.). By default non-normalized pixel values are returned.  
~~grayscale~~ | channel="Average, Brightness, Lightness, Rec601Luma, Rec601Luminance, Rec709Luma, Rec709Luminance, RMS" | convert image to grayscale  
~~haldclut~~ | image="image-handle", channel="Red, RGB, All, etc." | apply a Hald color lookup table to an image sequence  
~~identify~~ | file="file", features="distance", unique="True, False" | identify the attributes of an image  
<implode> | amount="double", interpolate="undefined, average, bicubic, bilinear, mesh, nearest-neighbor, spline" | implode image pixels about the center  
~~inversediscretefouriertransform~~ | magnitude="True, False" | implements the inverse discrete Fourier transform (DFT)  
<label> | string | assign a label to an image  
~~layers~~ | method="coalesce, compare-any, compare-clear, compare-over, composite, dispose, flatten, merge, mosaic, optimize, optimize-image, optimize-plus, optimize-trans, remove-dups, remove-zero", compose="Undefined, Add, Atop, Blend, Bumpmap, Clear, ColorBurn, ColorDodge, Colorize, CopyBlack, CopyBlue, CopyCMYK, Cyan, CopyGreen, Copy, CopyMagenta, CopyOpacity, CopyRed, RGB, CopyYellow, Darken, Dst, Difference, Displace, Dissolve, DstAtop, DstIn, DstOut, DstOver, Dst, Exclusion, HardLight, Hue, In, Lighten, LinearLight, Luminize, Minus, Modulate, Multiply, None, Out, Overlay, Over, Plus, ReplaceCompositeOp, Saturate, Screen, SoftLight, Src, SrcAtop, SrcIn, SrcOut, SrcOver, Src, Subtract, Threshold, Xor ", dither="true, false" | compare each image the GIF disposed forms of the previous image in the sequence. From this, attempt to select the smallest cropped image to replace each frame, while preserving the results of the animation.  
<level> | levels="string", 'black-point'="double", 'gamma'="double", 'white-point'="double", channel="Red, RGB, All, etc." | adjust the level of image contrast  
~~levelcolors~~ | invert=>"True, False", 'black-point'="string", 'white-point'="string", channel="Red, RGB, All, etc." | level image with the given colors  
~~linearstretch~~ | levels="string", 'black-point'="double", 'white-point'="double" | linear with saturation stretch  
~~liquidresize~~ | geometry="geometry", width="integer", height="integer", delta-x="double", rigidity="double" | rescale image with seam-carving.  
<magnify> |  | double the size of the image with pixel art scaling  
~~mask~~ | mask="image-handle" | composite image pixels as defined by the mask  
~~mattefloodfill~~ | geometry="geometry", x="integer", y="integer" , matte="integer", bordercolor="color name", fuzz="double", invert="True, False" | changes the matte value of any pixel that matches the color of the target pixel and is a neighbor. If you specify a border color, the matte value is changed for any neighbor pixel that is not that color.  
~~medianfilter~~ | geometry="geometry", width="integer", height="integer", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | replace each pixel with the median intensity pixel of a neighborhood.  
<minify> |  | half the size of an image  
~~mode~~ | geometry="geometry", width="integer", height="integer", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | make each pixel the "predominant color" of the neighborhood.  
<modulate> | factor="geometry", brightness="double", saturation="double", hue="double", lightness="double", whiteness="double", blackness="double"  | vary the brightness, saturation, and hue of an image by the specified percentage  
~~morphology~~ | kernel="string", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", iterations="integer" | apply a morphology method to the image.  
~~motionblur~~ | geometry="geometry", radius="double", sigma="double", angle="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | reduce image noise and reduce detail levels with a Gaussian operator of the given radius and standard deviation (sigma) at the given angle to simulate the effect of motion  
<negate> | gray="True, False", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | replace each pixel with its complementary color (white becomes black, yellow becomes blue, etc.)  
<normalize> | channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow"  | transform image to span the full range of color values  
~~oilpaint~~ | radius="integer" | simulate an oil painting  
<opaque> | color="color name", fill="color name", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", invert="True, False" | change this color to the fill color within the image  
~~ordereddither~~ | threshold="threshold, checks, o2x2, o3x3, o4x4, o8x8, h4x4a, h6x6a, h8x8a, h4x4o, h6x6o, h8x8o, h16x16o, hlines6x4", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | order dither image  
~~perceptible~~ | epsilon="double", channel="Red, RGB, All, etc." | set each pixel whose value is less than |"epsilon"| to "-epsilon" or "epsilon" (whichever is closer) otherwise the pixel value remains unchanged..  
~~polaroid~~ | caption="string", angle="double", pointsize="double", font="string", stroke= "color name", strokewidth="integer", fill="color name", gravity="NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast", background="color name" | simulate a Polaroid picture.  
~~posterize~~ | levels="integer", dither="True, False" | reduce the image to a limited number of color level  
<profile> | name="string", profile="blob", rendering-intent="Undefined, Saturation, Perceptual, Absolute, Relative", black-point-compensation="True, False" | add or remove ICC or IPTC image profile; name is formal name (e.g. ICC or filename; set profile to '' to remove profile  
<quantize> | colors="integer", colorspace="RGB, Gray, Transparent, OHTA, XYZ, YCbCr, YIQ, YPbPr, YUV, CMYK, sRGB, HSL, HSB", treedepth= "integer", dither="True, False", dither-method="Riemersma, Floyd-Steinberg", measure_error="True, False", global_colormap="True, False", transparent-color="color" | preferred number of colors in the image  
~~radialblur~~ | geometry="geometry", angle="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | radial blur the image.  
<raise> | geometry="geometry", width="integer", height="integer", x="integer", y="integer", raise="True, False" | lighten or darken image edges to create a 3-D effect  
~~reducenoise~~ | geometry="geometry", width="integer", height="integer", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | reduce noise in the image with a noise peak elimination filter  
~~remap~~ | image="image-handle", dither="true, false", dither-method="Riemersma, Floyd-Steinberg" | replace the colors of an image with the closest color from a reference image.  
<resample> | density="geometry", x="double", y="double", filter="Point, Box, Triangle, Hermite, Hanning, Hamming, Blackman, Gaussian, Quadratic, Cubic, Catrom, Mitchell, Lanczos, Bessel, Sinc", support="double" | resample image to desired resolution. Specify blur > 1 for blurry or < 1 for sharp  
<resize> | geometry="geometry", width="integer", height="integer", filter="Point, Box, Triangle, Hermite, Hanning, Hamming, Blackman, Gaussian, Quadratic, Cubic, Catrom, Mitchell, Lanczos, Bessel, Sinc", support="double", blur="double" | scale image to desired size. Specify blur > 1 for blurry or < 1 for sharp  
<roll> | geometry="geometry", x="integer", y="integer" | roll an image vertically or horizontally  
<rotate> | degrees="double", background="color name" | rotate an image  
<sample> | geometry="geometry", width="integer", height="integer" | scale image with pixel sampling.  
<scale> | geometry="geometry", width="integer", height="integer" | scale image to desired size  
<segment> | colorspace="RGB, Gray, Transparent, OHTA, XYZ, YCbCr, YCC, YIQ, YPbPr, YUV, CMYK", verbose="True, False", cluster-threshold="double", smoothing-threshold="double" | segment an image by analyzing the histograms of the color components and identifying units that are homogeneous  
~~selectiveblur~~ | geometry="geometry", radius="double", sigma="double", threshold="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | selectively blur pixels within a contrast threshold.  
~~separate~~ | channel="Red, RGB, All, etc." | separate a channel from the image into a grayscale image  
<shade> | geometry="geometry", azimuth="double", elevation="double", gray="true, false" | shade the image using a distant light source  
~~setpixel~~ | geometry="geometry", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", color="array of float values", x="integer", y="integer", color="array of float values" | set a single pixel. By default normalized pixel values are expected.  
<shadow> | geometry="geometry", opacity="double", sigma="double", x="integer", y="integer" | simulate an image shadow  
<sharpen> | geometry="geometry", radius="double", sigma="double", bias="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | sharpen the image with a Gaussian operator of the given radius and standard deviation (sigma).  
<shave> | geometry="geometry", width="integer", height="integer" | shave pixels from the image edges  
<shear> | geometry="geometry", x="double", y="double" fill="color name" | shear the image along the X or Y axis by a positive or negative shear angle  
~~sigmoidalcontrast~~ | geometry="string", 'contrast'="double", 'mid-point'="double" channel="Red, RGB, All, etc.", sharpen="True, False" | sigmoidal non-lineraity contrast control. Increase the contrast of the image using a sigmoidal transfer function without saturating highlights or shadows. Contrast" indicates how much to increase the contrast (0 is none; 3 is typical; 20 is a lot); mid-point" indicates where midtones fall in the resultant image (0 is white; 50% is middle-gray; 100% is black). To decrease contrast, set sharpen to False.  
<signature> |  | generate an SHA-256 message digest for the image pixel stream  
~~sketch~~ | geometry="geometry", radius="double", sigma="double", angle="double" | sketch the image with a Gaussian operator of the given radius and standard deviation (sigma) at the given angle  
<solarize> | geometry="string", threshold="double", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | negate all pixels above the threshold level  
~~sparsecolor~~ | points="array of float values", method="Barycentric, Bilinear, Shepards, Voronoi", virtual-pixel="Background Black Constant Dither Edge Gray Mirror Random Tile Transparent White" | interpolate the image colors around the supplied points  
~~splice~~ | geometry="geometry", width="integer", height="integer", x="integer", y="integer", fuzz="double", background="color name", gravity="NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast" | splice an image  
<spread> | radius="double", interpolate="undefined, average, bicubic, bilinear, mesh, nearest-neighbor, spline" | displace image pixels by a random amount  
~~statistic~~ | geometry="geometry", width="integer", height="integer", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow", type="Median, Mode, Mean, Maximum, Minimum, ReduceNoise" | replace each pixel with corresponding statistic from the neighborhood.  
<stegano> | image="image-handle", offset="integer" | hide a digital watermark within the image  
<stereo> | image="image-handle", x="integer", y="integer" | composites two images and produces a single image that is the composite of a left and right image of a stereo pair  
<strip> |  | strip an image of all profiles and comments.  
<swirl> | degrees="double", interpolate="undefined, average, bicubic, bilinear, mesh, nearest-neighbor, spline" | swirl image pixels about the center  
~~texture~~ | texture="image-handle" | name of texture to tile onto the image background  
~~thumbnail~~ | geometry="geometry", width="integer", height="integer" | changes the size of an image to the given dimensions and removes any associated profiles.  
<threshold> | threshold="string", channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | threshold the image  
~~tint~~ | fill="color name", blend="string" | tint the image with the fill color.  
<transparent> | color="color name", invert="True, False" | make this color transparent within the image  
~~transpose~~ |  | flip image in the vertical direction and rotate 90 degrees  
~~transverse~~ |  | flop image in the horizontal direction and rotate 270 degrees  
<trim> |  | remove edges that are the background color from the image  
~~unsharpmask~~ | geometry="geometry", radius="double", sigma="double", gain="double", threshold="double" | sharpen the image with the unsharp mask algorithm.  
~~vignette~~ | geometry="geometry", radius="double", sigma="double", x="integer", y="integer", background="color name" | offset the edges of the image in vignette style  
~~wave~~ | geometry="geometry", amplitude="double", wavelength="double", interpolate="undefined, average, bicubic, bilinear, mesh, nearest-neighbor, spline" | alter an image along a sine wave  
~~whitethreshold~~ | threshold="string", , channel="All, Default, Alpha, Black, Blue, CMYK, Cyan, Gray, Green, Index, Magenta, Opacity, Red, RGB, Yellow" | force all pixels above the threshold intensity into white  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](conjure.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
