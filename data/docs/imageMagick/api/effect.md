[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AdaptiveBlurImage](effect.html#AdaptiveBlurImage) • [AdaptiveSharpenImage](effect.html#AdaptiveSharpenImage) • [BlurImage](effect.html#BlurImage) • [ConvolveImage](effect.html#ConvolveImage) • [DespeckleImage](effect.html#DespeckleImage) • [EdgeImage](effect.html#EdgeImage) • [EmbossImage](effect.html#EmbossImage) • [GaussianBlurImage](effect.html#GaussianBlurImage) • [KuwaharaImage](effect.html#KuwaharaImage) • [LocalContrastImage](effect.html#LocalContrastImage) • [MotionBlurImage](effect.html#MotionBlurImage) • [PreviewImage](effect.html#PreviewImage) • [RotationalBlurImage](effect.html#RotationalBlurImage) • [SelectiveBlurImage](effect.html#SelectiveBlurImage) • [ShadeImage](effect.html#ShadeImage) • [SharpenImage](effect.html#SharpenImage) • [SpreadImage](effect.html#SpreadImage) • [UnsharpMaskImage](effect.html#UnsharpMaskImage)

## [AdaptiveBlurImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

AdaptiveBlurImage() adaptively blurs the image by blurring less intensely near image edges and more intensely far from edges. We blur the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and AdaptiveBlurImage() selects a suitable radius for you.

The format of the AdaptiveBlurImage method is:
    
    
    Image *AdaptiveBlurImage(const Image *image,const double radius,
      const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Laplacian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [AdaptiveSharpenImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

AdaptiveSharpenImage() adaptively sharpens the image by sharpening more intensely near image edges and less intensely far from edges. We sharpen the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and AdaptiveSharpenImage() selects a suitable radius for you.

The format of the AdaptiveSharpenImage method is:
    
    
    Image *AdaptiveSharpenImage(const Image *image,const double radius,
      const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Laplacian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [BlurImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

BlurImage() blurs an image. We convolve the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, the radius should be larger than sigma. Use a radius of 0 and BlurImage() selects a suitable radius for you.

The format of the BlurImage method is:
    
    
    Image *BlurImage(const Image *image,const double radius,
      const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [ConvolveImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

ConvolveImage() applies a custom convolution kernel to the image.

The format of the ConvolveImage method is:
    
    
    Image *ConvolveImage(const Image *image,const KernelInfo *kernel,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
kernel
    the filtering kernel. 
    
exception
    return any errors or warnings in this structure. 
    

## [DespeckleImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

DespeckleImage() reduces the speckle noise in an image while perserving the edges of the original image. A speckle removing filter uses a complementary hulling technique (raising pixels that are darker than their surrounding neighbors, then complementarily lowering pixels that are brighter than their surrounding neighbors) to reduce the speckle index of that image (reference Crimmins speckle removal).

The format of the DespeckleImage method is:
    
    
    Image *DespeckleImage(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [EdgeImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

EdgeImage() finds edges in an image. Radius defines the radius of the convolution filter. Use a radius of 0 and EdgeImage() selects a suitable radius for you.

The format of the EdgeImage method is:
    
    
    Image *EdgeImage(const Image *image,const double radius,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the pixel neighborhood. 
    
exception
    return any errors or warnings in this structure. 
    

## [EmbossImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

EmbossImage() returns a grayscale image with a three-dimensional effect. We convolve the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and Emboss() selects a suitable radius for you.

The format of the EmbossImage method is:
    
    
    Image *EmbossImage(const Image *image,const double radius,
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
    

## [GaussianBlurImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

GaussianBlurImage() blurs an image. We convolve the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, the radius should be larger than sigma. Use a radius of 0 and GaussianBlurImage() selects a suitable radius for you

The format of the GaussianBlurImage method is:
    
    
    Image *GaussianBlurImage(const Image *image,onst double radius,
      const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [KuwaharaImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

KuwaharaImage() is an edge preserving noise reduction filter.

The format of the KuwaharaImage method is:
    
    
    Image *KuwaharaImage(const Image *image,const double radius,
      const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the square window radius. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [LocalContrastImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

LocalContrastImage() attempts to increase the appearance of large-scale light-dark transitions. Local contrast enhancement works similarly to sharpening with an unsharp mask, however the mask is instead created using an image with a greater blur distance.

The format of the LocalContrastImage method is:
    
    
    Image *LocalContrastImage(const Image *image, const double radius,
      const double strength, ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian blur, in percentage with 100 resulting in a blur radius of 20 of largest dimension. 
    
strength
    the strength of the blur mask in percentage. 
    
exception
    return any errors or warnings in this structure. 
    

## [MotionBlurImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

MotionBlurImage() simulates motion blur. We convolve the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and MotionBlurImage() selects a suitable radius for you. Angle gives the angle of the blurring motion.

Andrew Protano contributed this effect.

The format of the MotionBlurImage method is:
    
    
        Image *MotionBlurImage(const Image *image,const double radius,
    const double sigma,const double angle,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
angle
    Apply the effect along this angle. 
    
exception
    return any errors or warnings in this structure. 
    

## [PreviewImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

PreviewImage() tiles 9 thumbnails of the specified image with an image processing operation applied with varying parameters. This may be helpful pin-pointing an appropriate parameter for a particular image processing operation.

The format of the PreviewImages method is:
    
    
    Image *PreviewImages(const Image *image,const PreviewType preview,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
preview
    the image processing operation. 
    
exception
    return any errors or warnings in this structure. 
    

## [RotationalBlurImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

RotationalBlurImage() applies a radial blur to the image.

Andrew Protano contributed this effect.

The format of the RotationalBlurImage method is:
    
    
        Image *RotationalBlurImage(const Image *image,const double angle,
    ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
angle
    the angle of the radial blur. 
    
blur
    the blur. 
    
exception
    return any errors or warnings in this structure. 
    

## [SelectiveBlurImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

SelectiveBlurImage() selectively blur pixels within a contrast threshold. It is similar to the unsharpen mask that sharpens everything with contrast above a certain threshold.

The format of the SelectiveBlurImage method is:
    
    
    Image *SelectiveBlurImage(const Image *image,const double radius,
      const double sigma,const double threshold,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
threshold
    only pixels within this contrast threshold are included in the blur operation. 
    
exception
    return any errors or warnings in this structure. 
    

## [ShadeImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

ShadeImage() shines a distant light on an image to create a three-dimensional effect. You control the positioning of the light with azimuth and elevation; azimuth is measured in degrees off the x axis and elevation is measured in pixels above the Z axis.

The format of the ShadeImage method is:
    
    
    Image *ShadeImage(const Image *image,const MagickBooleanType gray,
      const double azimuth,const double elevation,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
gray
    A value other than zero shades the intensity of each pixel. 
    
azimuth, elevation
     Define the light source direction. 
    
exception
    return any errors or warnings in this structure. 
    

## [SharpenImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

SharpenImage() sharpens the image. We convolve the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and SharpenImage() selects a suitable radius for you.

Using a separable kernel would be faster, but the negative weights cancel out on the corners of the kernel producing often undesirable ringing in the filtered result; this can be avoided by using a 2D gaussian shaped image sharpening kernel instead.

The format of the SharpenImage method is:
    
    
        Image *SharpenImage(const Image *image,const double radius,
    const double sigma,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Laplacian, in pixels. 
    
exception
    return any errors or warnings in this structure. 
    

## [SpreadImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

SpreadImage() is a special effects method that randomly displaces each pixel in a square area defined by the radius parameter.

The format of the SpreadImage method is:
    
    
    Image *SpreadImage(const Image *image,
      const PixelInterpolateMethod method,const double radius,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
method
     intepolation method. 
    
radius
     choose a random pixel in a neighborhood of this extent. 
    
exception
    return any errors or warnings in this structure. 
    

## [UnsharpMaskImage](http://www.imagemagick.org/api/MagickCore/effect_8c.html)

UnsharpMaskImage() sharpens one or more image channels. We convolve the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 and UnsharpMaskImage() selects a suitable radius for you.

The format of the UnsharpMaskImage method is:
    
    
        Image *UnsharpMaskImage(const Image *image,const double radius,
    const double sigma,const double amount,const double threshold,
    ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the Gaussian, in pixels, not counting the center pixel. 
    
sigma
    the standard deviation of the Gaussian, in pixels. 
    
gain
    the percentage of the difference between the original and the blur image that is added back into the original. 
    
threshold
    the threshold in pixels needed to apply the diffence gain. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](effect.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
