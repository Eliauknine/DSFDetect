[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AffineTransformImage](distort.html#AffineTransformImage) • [DistortImage](distort.html#DistortImage) • [RotateImage](distort.html#RotateImage) • [SparseColorImage](distort.html#SparseColorImage)

## [AffineTransformImage](http://www.imagemagick.org/api/MagickCore/distort_8c.html)

AffineTransformImage() transforms an image as dictated by the affine matrix. It allocates the memory necessary for the new Image structure and returns a pointer to the new image.

The format of the AffineTransformImage method is:
    
    
    Image *AffineTransformImage(const Image *image,
      AffineMatrix *affine_matrix,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
affine_matrix
    the affine matrix. 
    
exception
    return any errors or warnings in this structure. 
    

## [DistortImage](http://www.imagemagick.org/api/MagickCore/distort_8c.html)

DistortImage() distorts an image using various distortion methods, by mapping color lookups of the source image to a new destination image usally of the same size as the source image, unless 'bestfit' is set to true.

If 'bestfit' is enabled, and distortion allows it, the destination image is adjusted to ensure the whole source 'image' will just fit within the final destination image, which will be sized and offset accordingly. Also in many cases the virtual offset of the source image will be taken into account in the mapping.

If the '-verbose' control option has been set print to standard error the equicelent '-fx' formula with coefficients for the function, if practical.

The format of the DistortImage() method is:
    
    
    Image *DistortImage(const Image *image,const DistortMethod method,
      const size_t number_arguments,const double *arguments,
      MagickBooleanType bestfit, ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image to be distorted. 
    
method
    the method of image distortion. 
     ArcDistortion always ignores source image offset, and always 'bestfit' the destination image with the top left corner offset relative to the polar mapping center. 
     Affine, Perspective, and Bilinear, do least squares fitting of the distrotion when more than the minimum number of control point pairs are provided. 
     Perspective, and Bilinear, fall back to a Affine distortion when less than 4 control point pairs are provided. While Affine distortions let you use any number of control point pairs, that is Zero pairs is a No-Op (viewport only) distortion, one pair is a translation and two pairs of control points do a scale-rotate-translate, without any shearing. 
    
number_arguments
    the number of arguments given. 
    
arguments
    an array of floating point arguments for this method. 
    
bestfit
    Attempt to 'bestfit' the size of the resulting image. This also forces the resulting image to be a 'layered' virtual canvas image. Can be overridden using 'distort:viewport' setting. 
    
exception
    return any errors or warnings in this structure 
     Extra Controls from Image meta-data (artifacts)... 
     o "verbose" Output to stderr alternatives, internal coefficents, and FX equivalents for the distortion operation (if feasible). This forms an extra check of the distortion method, and allows users access to the internal constants IM calculates for the distortion. 
     o "distort:viewport" Directly set the output image canvas area and offest to use for the resulting image, rather than use the original images canvas, or a calculated 'bestfit' canvas. 
     o "distort:scale" Scale the size of the output canvas by this amount to provide a method of Zooming, and for super-sampling the results. 
     Other settings that can effect results include 
     o 'interpolate' For source image lookups (scale enlargements) 
     o 'filter' Set filter to use for area-resampling (scale shrinking). Set to 'point' to turn off and use 'interpolate' lookup instead 
    

## [RotateImage](http://www.imagemagick.org/api/MagickCore/distort_8c.html)

RotateImage() creates a new image that is a rotated copy of an existing one. Positive angles rotate counter-clockwise (right-hand rule), while negative angles rotate clockwise. Rotated images are usually larger than the originals and have 'empty' triangular corners. X axis. Empty triangles left over from shearing the image are filled with the background color defined by member 'background_color' of the image. RotateImage allocates the memory necessary for the new Image structure and returns a pointer to the new image.

The format of the RotateImage method is:
    
    
    Image *RotateImage(const Image *image,const double degrees,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

degrees

Specifies the number of degrees to rotate the image.

exception

return any errors or warnings in this structure.

## [SparseColorImage](http://www.imagemagick.org/api/MagickCore/distort_8c.html)

SparseColorImage(), given a set of coordinates, interpolates the colors found at those coordinates, across the whole image, using various methods.

The format of the SparseColorImage() method is:
    
    
    Image *SparseColorImage(const Image *image,
      const SparseColorMethod method,const size_t number_arguments,
      const double *arguments,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image to be filled in. 
    
method
    the method to fill in the gradient between the control points. 
     The methods used for SparseColor() are often simular to methods used for DistortImage(), and even share the same code for determination of the function coefficents, though with more dimensions (or resulting values). 
    
number_arguments
    the number of arguments given. 
    
arguments
    array of floating point arguments for this method-- x,y,color_values-- with color_values given as normalized values. 
    
exception
    return any errors or warnings in this structure 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](distort.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
