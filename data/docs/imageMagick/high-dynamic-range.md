[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

High dynamic-range imaging (HDRI) permits a far greater dynamic range of exposures (i.e. a large difference between light and dark areas) than standard digital imaging techniques. HDRI accurately represents the wide range of intensity levels found in real scenes ranging from the brightest direct sunlight to the deepest darkest shadows. The HDR imaging approach includes:

  * render/capture floating-point color space
  * encompass the entire perceivable gamut (extend values outside [0,1] range)
  * post-process in extended color space
  * apply tone-mapping for specific display



## Enabling HDRI in ImageMagick

By default, image pixels in ImageMagick are stored as unsigned values that range from 0 to the quantum depth, which is typically 16-bits (Q16). With HDRI enabled, the pixels are stored in a floating-point representation and can include negative values as well as values that exceed the quantum depth. A majority of digital image formats do not support HDRI, and for those images any pixels outside the quantum range are clamped before they are stored.

The most promising HDR image format is EXR. You must have the [OpenEXR](http://www.openexr.org) delegate library installed to read or write this format. Other HDR formats include TIFF 48-bit integer and 96-bit float formats, HDR, PFM, and ImageMagick's own MIFF format.

To enable the HDRI version of ImageMagick, use this Unix/Linux command:
    
    
    ./configure --enable-hdri
    

Under Windows, set the `MAGICKCORE_HDRI_SUPPORT` definition in the `magick-baseconfig.h` configuration file and build.

To verify HDRI is properly configured, look for "HDRI" as a feature:
    
    
    identify -version
    Features: HDRI
    

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](high-dynamic-range.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
