[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AutoGammaImage](enhance.html#AutoGammaImage) • [AutoLevelImage](enhance.html#AutoLevelImage) • [BrightnessContrastImage](enhance.html#BrightnessContrastImage) • [ClutImage](enhance.html#ClutImage) • [ColorDecisionListImage](enhance.html#ColorDecisionListImage) • [ContrastImage](enhance.html#ContrastImage) • [ContrastStretchImage](enhance.html#ContrastStretchImage) • [EnhanceImage](enhance.html#EnhanceImage) • [EqualizeImage](enhance.html#EqualizeImage) • [GammaImage](enhance.html#GammaImage) • [GrayscaleImage](enhance.html#GrayscaleImage) • [HaldClutImage](enhance.html#HaldClutImage) • [LevelImage](enhance.html#LevelImage) • [LevelizeImage](enhance.html#LevelizeImage) • [LevelImageColors](enhance.html#LevelImageColors) • [LinearStretchImage](enhance.html#LinearStretchImage) • [ModulateImage](enhance.html#ModulateImage) • [NegateImage](enhance.html#NegateImage) • [The NormalizeImage](enhance.html#The NormalizeImage) • [SigmoidalContrastImage](enhance.html#SigmoidalContrastImage)

## [AutoGammaImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

AutoGammaImage() extract the 'mean' from the image and adjust the image to try make set its gamma appropriatally.

The format of the AutoGammaImage method is:
    
    
    MagickBooleanType AutoGammaImage(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    The image to auto-level 
    
exception
    return any errors or warnings in this structure. 
    

## [AutoLevelImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

AutoLevelImage() adjusts the levels of a particular image channel by scaling the minimum and maximum values to the full quantum range.

The format of the LevelImage method is:
    
    
    MagickBooleanType AutoLevelImage(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    The image to auto-level 
    
exception
    return any errors or warnings in this structure. 
    

## [BrightnessContrastImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

BrightnessContrastImage() changes the brightness and/or contrast of an image. It converts the brightness and contrast parameters into slope and intercept and calls a polynomical function to apply to the image.

The format of the BrightnessContrastImage method is:
    
    
    MagickBooleanType BrightnessContrastImage(Image *image,
      const double brightness,const double contrast,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
brightness
    the brightness percent (-100 .. 100). 
    
contrast
    the contrast percent (-100 .. 100). 
    
exception
    return any errors or warnings in this structure. 
    

## [ClutImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

ClutImage() replaces each color value in the given image, by using it as an index to lookup a replacement color value in a Color Look UP Table in the form of an image. The values are extracted along a diagonal of the CLUT image so either a horizontal or vertial gradient image can be used.

Typically this is used to either re-color a gray-scale image according to a color gradient in the CLUT image, or to perform a freeform histogram (level) adjustment according to the (typically gray-scale) gradient in the CLUT image.

When the 'channel' mask includes the matte/alpha transparency channel but one image has no such channel it is assumed that that image is a simple gray-scale image that will effect the alpha channel values, either for gray-scale coloring (with transparent or semi-transparent colors), or a histogram adjustment of existing alpha channel values. If both images have matte channels, direct and normal indexing is applied, which is rarely used.

The format of the ClutImage method is:
    
    
    MagickBooleanType ClutImage(Image *image,Image *clut_image,
      const PixelInterpolateMethod method,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image, which is replaced by indexed CLUT values 
    
clut_image
    the color lookup table image for replacement color values. 
    
method
    the pixel interpolation method. 
    
exception
    return any errors or warnings in this structure. 
    

## [ColorDecisionListImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

ColorDecisionListImage() accepts a lightweight Color Correction Collection (CCC) file which solely contains one or more color corrections and applies the correction to the image. Here is a sample CCC file:
    
    
        <ColorCorrectionCollection xmlns="urn:ASC:CDL:v1.2">
        <ColorCorrection id="cc03345">
              <SOPNode>
                   <Slope> 0.9 1.2 0.5 </Slope>
                   <Offset> 0.4 -0.5 0.6 </Offset>
                   <Power> 1.0 0.8 1.5 </Power>
              </SOPNode>
              <SATNode>
                   <Saturation> 0.85 </Saturation>
              </SATNode>
        </ColorCorrection>
        </ColorCorrectionCollection>
    

which includes the slop, offset, and power for each of the RGB channels as well as the saturation.

The format of the ColorDecisionListImage method is:
    
    
    MagickBooleanType ColorDecisionListImage(Image *image,
      const char *color_correction_collection,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
color_correction_collection
    the color correction collection in XML. 
    
exception
    return any errors or warnings in this structure. 
    

## [ContrastImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

ContrastImage() enhances the intensity differences between the lighter and darker elements of the image. Set sharpen to a MagickTrue to increase the image contrast otherwise the contrast is reduced.

The format of the ContrastImage method is:
    
    
    MagickBooleanType ContrastImage(Image *image,
      const MagickBooleanType sharpen,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
sharpen
    Increase or decrease image contrast. 
    
exception
    return any errors or warnings in this structure. 
    

## [ContrastStretchImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

ContrastStretchImage() is a simple image enhancement technique that attempts to improve the contrast in an image by 'stretching' the range of intensity values it contains to span a desired range of values. It differs from the more sophisticated histogram equalization in that it can only apply a linear scaling function to the image pixel values. As a result the 'enhancement' is less harsh.

The format of the ContrastStretchImage method is:
    
    
    MagickBooleanType ContrastStretchImage(Image *image,
      const char *levels,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
black_point
    the black point. 
    
white_point
    the white point. 
    
levels
    Specify the levels where the black and white points have the range of 0 to number-of-pixels (e.g. 1, 10x90, etc.). 
    
exception
    return any errors or warnings in this structure. 
    

## [EnhanceImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

EnhanceImage() applies a digital filter that improves the quality of a noisy image.

The format of the EnhanceImage method is:
    
    
    Image *EnhanceImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [EqualizeImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

EqualizeImage() applies a histogram equalization to the image.

The format of the EqualizeImage method is:
    
    
    MagickBooleanType EqualizeImage(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [GammaImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

GammaImage() gamma-corrects a particular image channel. The same image viewed on different devices will have perceptual differences in the way the image's intensities are represented on the screen. Specify individual gamma levels for the red, green, and blue channels, or adjust all three with the gamma parameter. Values typically range from 0.8 to 2.3.

You can also reduce the influence of a particular channel with a gamma value of 0.

The format of the GammaImage method is:
    
    
    MagickBooleanType GammaImage(Image *image,const double gamma,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
level
    the image gamma as a string (e.g. 1.6,1.2,1.0). 
    
gamma
    the image gamma. 
    

## [GrayscaleImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

GrayscaleImage() converts the image to grayscale.

The format of the GrayscaleImage method is:
    
    
    MagickBooleanType GrayscaleImage(Image *image,
      const PixelIntensityMethod method ,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
method
    the pixel intensity method. 
    
exception
    return any errors or warnings in this structure. 
    

## [HaldClutImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

HaldClutImage() applies a Hald color lookup table to the image. A Hald color lookup table is a 3-dimensional color cube mapped to 2 dimensions. Create it with the HALD coder. You can apply any color transformation to the Hald image and then use this method to apply the transform to the image.

The format of the HaldClutImage method is:
    
    
    MagickBooleanType HaldClutImage(Image *image,Image *hald_image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image, which is replaced by indexed CLUT values 
    
hald_image
    the color lookup table image for replacement color values. 
    
exception
    return any errors or warnings in this structure. 
    

## [LevelImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

LevelImage() adjusts the levels of a particular image channel by scaling the colors falling between specified white and black points to the full available quantum range.

The parameters provided represent the black, and white points. The black point specifies the darkest color in the image. Colors darker than the black point are set to zero. White point specifies the lightest color in the image. Colors brighter than the white point are set to the maximum quantum value.

If a '!' flag is given, map black and white colors to the given levels rather than mapping those levels to black and white. See LevelizeImage() below.

Gamma specifies a gamma correction to apply to the image.

The format of the LevelImage method is:
    
    
    MagickBooleanType LevelImage(Image *image,const double black_point,
      const double white_point,const double gamma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
black_point
    The level to map zero (black) to. 
    
white_point
    The level to map QuantumRange (white) to. 
    
exception
    return any errors or warnings in this structure. 
    

## [LevelizeImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

LevelizeImage() applies the reversed LevelImage() operation to just the specific channels specified. It compresses the full range of color values, so that they lie between the given black and white points. Gamma is applied before the values are mapped.

LevelizeImage() can be called with by using a +level command line API option, or using a '!' on a -level or LevelImage() geometry string.

It can be used to de-contrast a greyscale image to the exact levels specified. Or by using specific levels for each channel of an image you can convert a gray-scale image to any linear color gradient, according to those levels.

The format of the LevelizeImage method is:
    
    
    MagickBooleanType LevelizeImage(Image *image,const double black_point,
      const double white_point,const double gamma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
black_point
    The level to map zero (black) to. 
    
white_point
    The level to map QuantumRange (white) to. 
    
gamma
    adjust gamma by this factor before mapping values. 
    
exception
    return any errors or warnings in this structure. 
    

## [LevelImageColors](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

LevelImageColors() maps the given color to "black" and "white" values, linearly spreading out the colors, and level values on a channel by channel bases, as per LevelImage(). The given colors allows you to specify different level ranges for each of the color channels separately.

If the boolean 'invert' is set true the image values will modifyed in the reverse direction. That is any existing "black" and "white" colors in the image will become the color values given, with all other values compressed appropriatally. This effectivally maps a greyscale gradient into the given color gradient.

The format of the LevelImageColors method is:
    
    
        MagickBooleanType LevelImageColors(Image *image,
    const PixelInfo *black_color,const PixelInfo *white_color,
    const MagickBooleanType invert,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
black_color
    The color to map black to/from 
    
white_point
    The color to map white to/from 
    
invert
    if true map the colors (levelize), rather than from (level) 
    
exception
    return any errors or warnings in this structure. 
    

## [LinearStretchImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

LinearStretchImage() discards any pixels below the black point and above the white point and levels the remaining pixels.

The format of the LinearStretchImage method is:
    
    
    MagickBooleanType LinearStretchImage(Image *image,
      const double black_point,const double white_point,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
black_point
    the black point. 
    
white_point
    the white point. 
    
exception
    return any errors or warnings in this structure. 
    

## [ModulateImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

ModulateImage() lets you control the brightness, saturation, and hue of an image. Modulate represents the brightness, saturation, and hue as one parameter (e.g. 90,150,100). If the image colorspace is HSL, the modulation is lightness, saturation, and hue. For HWB, use blackness, whiteness, and hue. And for HCL, use chrome, luma, and hue.

The format of the ModulateImage method is:
    
    
    MagickBooleanType ModulateImage(Image *image,const char *modulate,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
modulate
    Define the percent change in brightness, saturation, and hue. 
    
exception
    return any errors or warnings in this structure. 
    

## [NegateImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

NegateImage() negates the colors in the reference image. The grayscale option means that only grayscale values within the image are negated.

The format of the NegateImage method is:
    
    
    MagickBooleanType NegateImage(Image *image,
      const MagickBooleanType grayscale,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
grayscale
    If MagickTrue, only negate grayscale pixels within the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [The NormalizeImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

The NormalizeImage() method enhances the contrast of a color image by mapping the darkest 2 percent of all pixel to black and the brightest 1 percent to white.

The format of the NormalizeImage method is:
    
    
    MagickBooleanType NormalizeImage(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [SigmoidalContrastImage](http://www.imagemagick.org/api/MagickCore/enhance_8c.html)

SigmoidalContrastImage() adjusts the contrast of an image with a non-linear sigmoidal contrast algorithm. Increase the contrast of the image using a sigmoidal transfer function without saturating highlights or shadows. Contrast indicates how much to increase the contrast (0 is none; 3 is typical; 20 is pushing it); mid-point indicates where midtones fall in the resultant image (0 is white; 50 is middle-gray; 100 is black). Set sharpen to MagickTrue to increase the image contrast otherwise the contrast is reduced.

The format of the SigmoidalContrastImage method is:
    
    
    MagickBooleanType SigmoidalContrastImage(Image *image,
      const MagickBooleanType sharpen,const char *levels,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
sharpen
    Increase or decrease image contrast. 
    
contrast
    strength of the contrast, the larger the number the more 'threshold-like' it becomes. 
    
midpoint
    midpoint of the function as a color value 0 to QuantumRange. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](enhance.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
