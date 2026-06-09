[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AddNoiseImage](fx.html#AddNoiseImage) • [BlueShiftImage](fx.html#BlueShiftImage) • [CharcoalImage](fx.html#CharcoalImage) • [ColorizeImage](fx.html#ColorizeImage) • [ColorMatrixImage](fx.html#ColorMatrixImage) • [FxImage](fx.html#FxImage) • [ImplodeImage](fx.html#ImplodeImage) • [The MorphImages](fx.html#The MorphImages) • [PlasmaImage](fx.html#PlasmaImage) • [PolaroidImage](fx.html#PolaroidImage) • [MagickSepiaToneImage](fx.html#MagickSepiaToneImage) • [ShadowImage](fx.html#ShadowImage) • [SketchImage](fx.html#SketchImage) • [SolarizeImage](fx.html#SolarizeImage) • [SteganoImage](fx.html#SteganoImage) • [StereoAnaglyphImage](fx.html#StereoAnaglyphImage) • [SwirlImage](fx.html#SwirlImage) • [TintImage](fx.html#TintImage) • [VignetteImage](fx.html#VignetteImage) • [WaveImage](fx.html#WaveImage) • [WaveletDenoiseImage](fx.html#WaveletDenoiseImage)

## [AddNoiseImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

AddNoiseImage() adds random noise to the image.

The format of the AddNoiseImage method is:
    
    
    Image *AddNoiseImage(const Image *image,const NoiseType noise_type,
      const double attenuate,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
channel
    the channel type. 
    
noise_type
     The type of noise: Uniform, Gaussian, Multiplicative, Impulse, Laplacian, or Poisson. 
    
attenuate
     attenuate the random distribution. 
    
exception
    return any errors or warnings in this structure. 
    

## [BlueShiftImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

BlueShiftImage() mutes the colors of the image to simulate a scene at nighttime in the moonlight.

The format of the BlueShiftImage method is:
    
    
    Image *BlueShiftImage(const Image *image,const double factor,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
factor
    the shift factor. 
    
exception
    return any errors or warnings in this structure. 
    

## [CharcoalImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

CharcoalImage() creates a new image that is a copy of an existing one with the edge highlighted. It allocates the memory necessary for the new Image structure and returns a pointer to the new image.

The format of the CharcoalImage method is:
    
    
    Image *CharcoalImage(const Image *image,const double radius,
      const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the pixel neighborhood. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [ColorizeImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

ColorizeImage() blends the fill color with each pixel in the image. A percentage blend is specified with opacity. Control the application of different color components by specifying a different percentage for each component (e.g. 90/100/10 is 90 red, 100 green, and 10 blue).

The format of the ColorizeImage method is:
    
    
    Image *ColorizeImage(const Image *image,const char *blend,
      const PixelInfo *colorize,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
blend
     A character string indicating the level of blending as a percentage. 
    
colorize
    A color value. 
    
exception
    return any errors or warnings in this structure. 
    

## [ColorMatrixImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

ColorMatrixImage() applies color transformation to an image. This method permits saturation changes, hue rotation, luminance to alpha, and various other effects. Although variable-sized transformation matrices can be used, typically one uses a 5x5 matrix for an RGBA image and a 6x6 for CMYKA (or RGBA with offsets). The matrix is similar to those used by Adobe Flash except offsets are in column 6 rather than 5 (in support of CMYKA images) and offsets are normalized (divide Flash offset by 255).

The format of the ColorMatrixImage method is:
    
    
    Image *ColorMatrixImage(const Image *image,
      const KernelInfo *color_matrix,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
color_matrix
     the color matrix. 
    
exception
    return any errors or warnings in this structure. 
    

## [FxImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

FxImage() applies a mathematical expression to the specified image.

The format of the FxImage method is:
    
    
    Image *FxImage(const Image *image,const char *expression,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
expression
    A mathematical expression. 
    
exception
    return any errors or warnings in this structure. 
    

## [ImplodeImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

ImplodeImage() creates a new image that is a copy of an existing one with the image pixels "implode" by the specified percentage. It allocates the memory necessary for the new Image structure and returns a pointer to the new image.

The format of the ImplodeImage method is:
    
    
    Image *ImplodeImage(const Image *image,const double amount,
      const PixelInterpolateMethod method,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

implode_image
    Method ImplodeImage returns a pointer to the image after it is implode. A null image is returned if there is a memory shortage. 
    
image
    the image. 
    
amount
     Define the extent of the implosion. 
    
method
    the pixel interpolation method. 
    
exception
    return any errors or warnings in this structure. 
    

## [The MorphImages](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

The MorphImages() method requires a minimum of two images. The first image is transformed into the second by a number of intervening images as specified by frames.

The format of the MorphImage method is:
    
    
    Image *MorphImages(const Image *image,const size_t number_frames,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
number_frames
     Define the number of in-between image to generate. The more in-between frames, the smoother the morph. 
    
exception
    return any errors or warnings in this structure. 
    

## [PlasmaImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

PlasmaImage() initializes an image with plasma fractal values. The image must be initialized with a base color and the random number generator seeded before this method is called.

The format of the PlasmaImage method is:
    
    
    MagickBooleanType PlasmaImage(Image *image,const SegmentInfo *segment,
      size_t attenuate,size_t depth,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
segment
     Define the region to apply plasma fractals values. 
    
attenuate
    Define the plasma attenuation factor. 
    
depth
    Limit the plasma recursion depth. 
    
exception
    return any errors or warnings in this structure. 
    

## [PolaroidImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

PolaroidImage() simulates a Polaroid picture.

The format of the PolaroidImage method is:
    
    
    Image *PolaroidImage(const Image *image,const DrawInfo *draw_info,
      const char *caption,const double angle,
      const PixelInterpolateMethod method,ExceptionInfo exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
caption
    the Polaroid caption. 
    
angle
    Apply the effect along this angle. 
    
method
    the pixel interpolation method. 
    
exception
    return any errors or warnings in this structure. 
    

## [MagickSepiaToneImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

MagickSepiaToneImage() applies a special effect to the image, similar to the effect achieved in a photo darkroom by sepia toning. Threshold ranges from 0 to QuantumRange and is a measure of the extent of the sepia toning. A threshold of 80 is a good starting point for a reasonable tone.

The format of the SepiaToneImage method is:
    
    
    Image *SepiaToneImage(const Image *image,const double threshold,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
threshold
    the tone threshold. 
    
exception
    return any errors or warnings in this structure. 
    

## [ShadowImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

ShadowImage() simulates a shadow from the specified image and returns it.

The format of the ShadowImage method is:
    
    
    Image *ShadowImage(const Image *image,const double alpha,
      const double sigma,const ssize_t x_offset,const ssize_t y_offset,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
alpha
    percentage transparency. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
x_offset
    the shadow x-offset. 
    
y_offset
    the shadow y-offset. 
    
exception
    return any errors or warnings in this structure. 
    

## [SketchImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

SketchImage() simulates a pencil sketch. We convolve the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and SketchImage() selects a suitable radius for you. Angle gives the angle of the sketch.

The format of the SketchImage method is:
    
    
        Image *SketchImage(const Image *image,const double radius,
    const double sigma,const double angle,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
angle
    apply the effect along this angle. 
    
exception
    return any errors or warnings in this structure. 
    

## [SolarizeImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

SolarizeImage() applies a special effect to the image, similar to the effect achieved in a photo darkroom by selectively exposing areas of photo sensitive paper to light. Threshold ranges from 0 to QuantumRange and is a measure of the extent of the solarization.

The format of the SolarizeImage method is:
    
    
    MagickBooleanType SolarizeImage(Image *image,const double threshold,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
threshold
     Define the extent of the solarization. 
    
exception
    return any errors or warnings in this structure. 
    

## [SteganoImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

SteganoImage() hides a digital watermark within the image. Recover the hidden watermark later to prove that the authenticity of an image. Offset defines the start position within the image to hide the watermark.

The format of the SteganoImage method is:
    
    
    Image *SteganoImage(const Image *image,Image *watermark,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
watermark
    the watermark image. 
    
exception
    return any errors or warnings in this structure. 
    

## [StereoAnaglyphImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

StereoAnaglyphImage() combines two images and produces a single image that is the composite of a left and right image of a stereo pair. Special red-green stereo glasses are required to view this effect.

The format of the StereoAnaglyphImage method is:
    
    
    Image *StereoImage(const Image *left_image,const Image *right_image,
      ExceptionInfo *exception)
    Image *StereoAnaglyphImage(const Image *left_image,
      const Image *right_image,const ssize_t x_offset,const ssize_t y_offset,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

left_image
    the left image. 
    
right_image
    the right image. 
    
exception
    return any errors or warnings in this structure. 
    
x_offset
    amount, in pixels, by which the left image is offset to the right of the right image. 
    
y_offset
    amount, in pixels, by which the left image is offset to the bottom of the right image. 
    
    

## [SwirlImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

SwirlImage() swirls the pixels about the center of the image, where degrees indicates the sweep of the arc through which each pixel is moved. You get a more dramatic effect as the degrees move from 1 to 360.

The format of the SwirlImage method is:
    
    
    Image *SwirlImage(const Image *image,double degrees,
      const PixelInterpolateMethod method,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
degrees
    Define the tightness of the swirling effect. 
    
method
    the pixel interpolation method. 
    
exception
    return any errors or warnings in this structure. 
    

## [TintImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

TintImage() applies a color vector to each pixel in the image. The length of the vector is 0 for black and white and at its maximum for the midtones. The vector weighting function is f(x)=(1-(4.0*((x-0.5)*(x-0.5))))

The format of the TintImage method is:
    
    
    Image *TintImage(const Image *image,const char *blend,
      const PixelInfo *tint,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
blend
    A color value used for tinting. 
    
tint
    A color value used for tinting. 
    
exception
    return any errors or warnings in this structure. 
    

## [VignetteImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

VignetteImage() softens the edges of the image in vignette style.

The format of the VignetteImage method is:
    
    
    Image *VignetteImage(const Image *image,const double radius,
      const double sigma,const ssize_t x,const ssize_t y,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the pixel neighborhood. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
x, y
     Define the x and y ellipse offset. 
    
exception
    return any errors or warnings in this structure. 
    

## [WaveImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

WaveImage() creates a "ripple" effect in the image by shifting the pixels vertically along a sine wave whose amplitude and wavelength is specified by the given parameters.

The format of the WaveImage method is:
    
    
    Image *WaveImage(const Image *image,const double amplitude,
      const double wave_length,const PixelInterpolateMethod method,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
amplitude, wave_length
     Define the amplitude and wave length of the sine wave. 
    
interpolate
    the pixel interpolation method. 
    
exception
    return any errors or warnings in this structure. 
    

## [WaveletDenoiseImage](http://www.imagemagick.org/api/MagickCore/fx_8c.html)

WaveletDenoiseImage() removes noise from the image using a wavelet transform. The wavelet transform is a fast hierarchical scheme for processing an image using a set of consecutive lowpass and high_pass filters, followed by a decimation. This results in a decomposition into different scales which can be regarded as different “frequency bands”, determined by the mother wavelet. Adapted from dcraw.c by David Coffin.

The format of the WaveletDenoiseImage method is:
    
    
    Image *WaveletDenoiseImage(const Image *image,const double threshold,
      const double softness,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
threshold
    set the threshold for smoothing. 
    
softness
    attenuate the smoothing threshold. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](fx.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
