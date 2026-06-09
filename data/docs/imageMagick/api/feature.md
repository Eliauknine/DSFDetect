[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[CannyEdgeImage](feature.html#CannyEdgeImage) • [GetImageFeatures](feature.html#GetImageFeatures) • [Use HoughLineImage](feature.html#Use HoughLineImage) • [MeanShiftImage](feature.html#MeanShiftImage)

## [CannyEdgeImage](http://www.imagemagick.org/api/MagickCore/feature_8c.html)

CannyEdgeImage() uses a multi-stage algorithm to detect a wide range of edges in images.

The format of the CannyEdgeImage method is:
    
    
    Image *CannyEdgeImage(const Image *image,const double radius,
      const double sigma,const double lower_percent,
      const double upper_percent,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
radius
    the radius of the gaussian smoothing filter. 
    
sigma
    the sigma of the gaussian smoothing filter. 
    
lower_precent
    percentage of edge pixels in the lower threshold. 
    
upper_percent
    percentage of edge pixels in the upper threshold. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageFeatures](http://www.imagemagick.org/api/MagickCore/feature_8c.html)

GetImageFeatures() returns features for each channel in the image in each of four directions (horizontal, vertical, left and right diagonals) for the specified distance. The features include the angular second moment, contrast, correlation, sum of squares: variance, inverse difference moment, sum average, sum varience, sum entropy, entropy, difference variance, difference entropy, information measures of correlation 1, information measures of correlation 2, and maximum correlation coefficient. You can access the red channel contrast, for example, like this:
    
    
    channel_features=GetImageFeatures(image,1,exception);
    contrast=channel_features[RedPixelChannel].contrast[0];
    

Use MagickRelinquishMemory() to free the features buffer.

The format of the GetImageFeatures method is:
    
    
    ChannelFeatures *GetImageFeatures(const Image *image,
      const size_t distance,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
distance
    the distance. 
    
exception
    return any errors or warnings in this structure. 
    

## [Use HoughLineImage](http://www.imagemagick.org/api/MagickCore/feature_8c.html)

Use HoughLineImage() in conjunction with any binary edge extracted image (we recommand Canny) to identify lines in the image. The algorithm accumulates counts for every white pixel for every possible orientation (for angles from 0 to 179 in 1 degree increments) and distance from the center of the image to the corner (in 1 px increments) and stores the counts in an accumulator matrix of angle vs distance. The size of the accumulator is 180x(diagonal/2). Next it searches this space for peaks in counts and converts the locations of the peaks to slope and intercept in the normal x,y input image space. Use the slope/intercepts to find the endpoints clipped to the bounds of the image. The lines are then drawn. The counts are a measure of the length of the lines

The format of the HoughLineImage method is:
    
    
    Image *HoughLineImage(const Image *image,const size_t width,
      const size_t height,const size_t threshold,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
width, height
    find line pairs as local maxima in this neighborhood. 
    
threshold
    the line count threshold. 
    
exception
    return any errors or warnings in this structure. 
    

## [MeanShiftImage](http://www.imagemagick.org/api/MagickCore/feature_8c.html)

MeanShiftImage() delineate arbitrarily shaped clusters in the image. For each pixel, it visits all the pixels in the neighborhood specified by the window centered at the pixel and excludes those that are outside the radius=(window-1)/2 surrounding the pixel. From those pixels, it finds those that are within the specified color distance from the current mean, and computes a new x,y centroid from those coordinates and a new mean. This new x,y centroid is used as the center for a new window. This process iterates until it converges and the final mean is replaces the (original window center) pixel value. It repeats this process for the next pixel, etc., until it processes all pixels in the image. Results are typically better with colorspaces other than sRGB. We recommend YIQ, YUV or YCbCr.

The format of the MeanShiftImage method is:
    
    
    Image *MeanShiftImage(const Image *image,const size_t width,
      const size_t height,const double color_distance,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
width, height
    find pixels in this neighborhood. 
    
color_distance
    the color distance. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](feature.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
