[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[CompareImagesCommand](compare.html#CompareImagesCommand)

## [CompareImagesCommand](http://www.imagemagick.org/api/MagickWand/compare_8c.html)

CompareImagesCommand() compares two images and returns the difference between them as a distortion metric and as a new image visually annotating their differences.

The format of the CompareImagesCommand method is:
    
    
    MagickBooleanType CompareImagesCommand(ImageInfo *image_info,int argc,
      char **argv,char **metadata,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
argc
    the number of elements in the argument vector. 
    
argv
    A text array containing the command line arguments. 
    
metadata
    any metadata is returned here. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](compare.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
