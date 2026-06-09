[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ComplexImages](fourier.html#ComplexImages) • [ForwardFourierTransformImage](fourier.html#ForwardFourierTransformImage) • [InverseFourierTransformImage](fourier.html#InverseFourierTransformImage)

## [ComplexImages](http://www.imagemagick.org/api/MagickCore/fourier_8c.html)

ComplexImages() performs complex mathematics on an image sequence.

The format of the ComplexImages method is:
    
    
    MagickBooleanType ComplexImages(Image *images,const ComplexOperator op,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
op
    A complex op. 
    
exception
    return any errors or warnings in this structure. 
    

## [ForwardFourierTransformImage](http://www.imagemagick.org/api/MagickCore/fourier_8c.html)

ForwardFourierTransformImage() implements the discrete Fourier transform (DFT) of the image either as a magnitude / phase or real / imaginary image pair.

The format of the ForwadFourierTransformImage method is:
    
    
    Image *ForwardFourierTransformImage(const Image *image,
      const MagickBooleanType modulus,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
modulus
    if true, return as transform as a magnitude / phase pair otherwise a real / imaginary image pair. 
    
exception
    return any errors or warnings in this structure. 
    

## [InverseFourierTransformImage](http://www.imagemagick.org/api/MagickCore/fourier_8c.html)

InverseFourierTransformImage() implements the inverse discrete Fourier transform (DFT) of the image either as a magnitude / phase or real / imaginary image pair.

The format of the InverseFourierTransformImage method is:
    
    
    Image *InverseFourierTransformImage(const Image *magnitude_image,
      const Image *phase_image,const MagickBooleanType modulus,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

magnitude_image
    the magnitude or real image. 
    
phase_image
    the phase or imaginary image. 
    
modulus
    if true, return transform as a magnitude / phase pair otherwise a real / imaginary image pair. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](fourier.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
