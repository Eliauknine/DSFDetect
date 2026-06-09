[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[SegmentImage](segment.html#SegmentImage)

## [SegmentImage](http://www.imagemagick.org/api/MagickCore/segment_8c.html)

SegmentImage() segment an image by analyzing the histograms of the color components and identifying units that are homogeneous with the fuzzy C-means technique.

The format of the SegmentImage method is:
    
    
    MagickBooleanType SegmentImage(Image *image,
      const ColorspaceType colorspace,const MagickBooleanType verbose,
      const double cluster_threshold,const double smooth_threshold,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

colorspace

Indicate the colorspace.

verbose

Set to MagickTrue to print detailed information about the identified classes.

cluster_threshold

This represents the minimum number of pixels contained in a hexahedra before it can be considered valid (expressed as a percentage).

smooth_threshold

the smoothing threshold eliminates noise in the second derivative of the histogram. As the value is increased, you can expect a smoother second derivative.

exception

return any errors or warnings in this structure.

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](segment.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
