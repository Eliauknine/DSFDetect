[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[EvaluateImage](statistic.html#EvaluateImage) • [FunctionImage](statistic.html#FunctionImage) • [GetImageEntropy](statistic.html#GetImageEntropy) • [GetImageExtrema](statistic.html#GetImageExtrema) • [GetImageKurtosis](statistic.html#GetImageKurtosis) • [GetImageMean](statistic.html#GetImageMean) • [GetImageMoments](statistic.html#GetImageMoments) • [GetImagePerceptualHash](statistic.html#GetImagePerceptualHash) • [GetImageRange](statistic.html#GetImageRange) • [GetImageStatistics](statistic.html#GetImageStatistics) • [PolynomialImage](statistic.html#PolynomialImage) • [StatisticImage](statistic.html#StatisticImage)

## [EvaluateImage](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

EvaluateImage() applies a value to the image with an arithmetic, relational, or logical operator to an image. Use these operations to lighten or darken an image, to increase or decrease contrast in an image, or to produce the "negative" of an image.

The format of the EvaluateImage method is:
    
    
    MagickBooleanType EvaluateImage(Image *image,
      const MagickEvaluateOperator op,const double value,
      ExceptionInfo *exception)
    MagickBooleanType EvaluateImages(Image *images,
      const MagickEvaluateOperator op,const double value,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
op
    A channel op. 
    
value
    A value value. 
    
exception
    return any errors or warnings in this structure. 
    

## [FunctionImage](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

FunctionImage() applies a value to the image with an arithmetic, relational, or logical operator to an image. Use these operations to lighten or darken an image, to increase or decrease contrast in an image, or to produce the "negative" of an image.

The format of the FunctionImage method is:
    
    
    MagickBooleanType FunctionImage(Image *image,
      const MagickFunction function,const ssize_t number_parameters,
      const double *parameters,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
function
    A channel function. 
    
parameters
    one or more parameters. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageEntropy](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImageEntropy() returns the entropy of one or more image channels.

The format of the GetImageEntropy method is:
    
    
    MagickBooleanType GetImageEntropy(const Image *image,double *entropy,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
entropy
    the average entropy of the selected channels. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageExtrema](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImageExtrema() returns the extrema of one or more image channels.

The format of the GetImageExtrema method is:
    
    
    MagickBooleanType GetImageExtrema(const Image *image,size_t *minima,
      size_t *maxima,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
minima
    the minimum value in the channel. 
    
maxima
    the maximum value in the channel. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageKurtosis](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImageKurtosis() returns the kurtosis and skewness of one or more image channels.

The format of the GetImageKurtosis method is:
    
    
    MagickBooleanType GetImageKurtosis(const Image *image,double *kurtosis,
      double *skewness,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
kurtosis
    the kurtosis of the channel. 
    
skewness
    the skewness of the channel. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageMean](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImageMean() returns the mean and standard deviation of one or more image channels.

The format of the GetImageMean method is:
    
    
    MagickBooleanType GetImageMean(const Image *image,double *mean,
      double *standard_deviation,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
mean
    the average value in the channel. 
    
standard_deviation
    the standard deviation of the channel. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageMoments](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImageMoments() returns the normalized moments of one or more image channels.

The format of the GetImageMoments method is:
    
    
    ChannelMoments *GetImageMoments(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImagePerceptualHash](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImagePerceptualHash() returns the perceptual hash of one or more image channels.

The format of the GetImagePerceptualHash method is:
    
    
    ChannelPerceptualHash *GetImagePerceptualHash(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageRange](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImageRange() returns the range of one or more image channels.

The format of the GetImageRange method is:
    
    
    MagickBooleanType GetImageRange(const Image *image,double *minima,
      double *maxima,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
minima
    the minimum value in the channel. 
    
maxima
    the maximum value in the channel. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageStatistics](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

GetImageStatistics() returns statistics for each channel in the image. The statistics include the channel depth, its minima, maxima, mean, standard deviation, kurtosis and skewness. You can access the red channel mean, for example, like this:
    
    
    channel_statistics=GetImageStatistics(image,exception);
    red_mean=channel_statistics[RedPixelChannel].mean;
    

Use MagickRelinquishMemory() to free the statistics buffer.

The format of the GetImageStatistics method is:
    
    
    ChannelStatistics *GetImageStatistics(const Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [PolynomialImage](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

PolynomialImage() returns a new image where each pixel is the sum of the pixels in the image sequence after applying its corresponding terms (coefficient and degree pairs).

The format of the PolynomialImage method is:
    
    
    Image *PolynomialImage(const Image *images,const size_t number_terms,
      const double *terms,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
number_terms
    the number of terms in the list. The actual list length is 2 x number_terms + 1 (the constant). 
    
terms
    the list of polynomial coefficients and degree pairs and a constant. 
    
exception
    return any errors or warnings in this structure. 
    

## [StatisticImage](http://www.imagemagick.org/api/MagickCore/statistic_8c.html)

StatisticImage() makes each pixel the min / max / median / mode / etc. of the neighborhood of the specified width and height.

The format of the StatisticImage method is:
    
    
    Image *StatisticImage(const Image *image,const StatisticType type,
      const size_t width,const size_t height,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
type
    the statistic type (median, mode, etc.). 
    
width
    the width of the pixel neighborhood. 
    
height
    the height of the pixel neighborhood. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](statistic.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
