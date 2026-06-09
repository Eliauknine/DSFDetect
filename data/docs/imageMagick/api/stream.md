[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[StreamImageCommand](stream.html#StreamImageCommand)

## [StreamImageCommand](http://www.imagemagick.org/api/MagickWand/stream_8c.html)

StreamImageCommand() is a lightweight method designed to extract pixels from large image files to a raw format using a minimum of system resources. The entire image or any regular portion of the image can be extracted.

The format of the StreamImageCommand method is:
    
    
    MagickBooleanType StreamImageCommand(ImageInfo *image_info,int argc,
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

[Back to top](stream.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
