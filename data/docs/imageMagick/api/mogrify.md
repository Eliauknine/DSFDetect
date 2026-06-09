[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[MagickCommandGenesis](mogrify.html#MagickCommandGenesis)

## [MagickCommandGenesis](http://www.imagemagick.org/api/MagickWand/mogrify_8c.html)

MagickCommandGenesis() applies image processing options to an image as prescribed by command line options.

It wiil look for special options like "-debug", "-bench", and "-distribute-cache" that needs to be applied even before the main processing begins, and may completely overrule normal command processing. Such 'Genesis' Options can only be given on the CLI, (not in a script) and are typically ignored (as they have been handled) if seen later.

The format of the MagickCommandGenesis method is:
    
    
    MagickBooleanType MagickCommandGenesis(ImageInfo *image_info,
      MagickCommand command,int argc,char **argv,char **metadata,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
command
    Choose from ConvertImageCommand, IdentifyImageCommand, MogrifyImageCommand, CompositeImageCommand, CompareImagesCommand, ConjureImageCommand, StreamImageCommand, ImportImageCommand, DisplayImageCommand, or AnimateImageCommand. 
    
argc
    Specifies a pointer to an integer describing the number of elements in the argument vector. 
    
argv
    Specifies a pointer to a text array containing the command line arguments. 
    
metadata
    any metadata is returned here. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](mogrify.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
