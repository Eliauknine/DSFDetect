[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[SignatureImage](signature.html#SignatureImage)

## [SignatureImage](http://www.imagemagick.org/api/MagickCore/signature_8c.html)

SignatureImage() computes a message digest from an image pixel stream with an implementation of the NIST SHA-256 Message Digest algorithm. This signature uniquely identifies the image and is convenient for determining if an image has been modified or whether two images are identical.

The format of the SignatureImage method is:
    
    
    MagickBooleanType SignatureImage(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](signature.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
