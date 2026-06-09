[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireColorCache](color.html#AcquireColorCache) • [GetColorInfoList](color.html#GetColorInfoList) • [GetColorList](color.html#GetColorList) • [ListColorInfo](color.html#ListColorInfo) • [QueryColorname](color.html#QueryColorname)

## [AcquireColorCache](http://www.imagemagick.org/api/MagickCore/color_8c.html)

AcquireColorCache() caches one or more color configurations which provides a mapping between color attributes and a color name.

The format of the AcquireColorCache method is:
    
    
    LinkedListInfo *AcquireColorCache(const char *filename,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

filename
    the font file name. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetColorInfoList](http://www.imagemagick.org/api/MagickCore/color_8c.html)

GetColorInfoList() returns any colors that match the specified pattern.

The format of the GetColorInfoList function is:
    
    
    const ColorInfo **GetColorInfoList(const char *pattern,
      size_t *number_colors,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_colors
     This integer returns the number of colors in the list. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetColorList](http://www.imagemagick.org/api/MagickCore/color_8c.html)

GetColorList() returns any colors that match the specified pattern.

The format of the GetColorList function is:
    
    
    char **GetColorList(const char *pattern,size_t *number_colors,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_colors
     This integer returns the number of colors in the list. 
    
exception
    return any errors or warnings in this structure. 
    

## [ListColorInfo](http://www.imagemagick.org/api/MagickCore/color_8c.html)

ListColorInfo() lists color names to the specified file. Color names are a convenience. Rather than defining a color by its red, green, and blue intensities just use a color name such as white, blue, or yellow.

The format of the ListColorInfo method is:
    
    
    MagickBooleanType ListColorInfo(FILE *file,ExceptionInfo *exception)
    

A description of each parameter follows.

file

List color names to this file handle.

exception

return any errors or warnings in this structure.

## [QueryColorname](http://www.imagemagick.org/api/MagickCore/color_8c.html)

QueryColorname() returns a named color for the given color intensity. If an exact match is not found, a hex value is returned instead. For example an intensity of rgb:(0,0,0) returns black whereas rgb:(223,223,223) returns #dfdfdf.

UPDATE: the 'image' argument is no longer needed as all information should have been preset using GetPixelInfo().

The format of the QueryColorname method is:
    
    
    MagickBooleanType QueryColorname(const Image *image,
      const PixelInfo *color,const ComplianceType compliance,char *name,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image. (not used! - color gets settings from GetPixelInfo()

color

the color intensities.

Compliance

Adhere to this color standard: SVG, X11, or XPM.

name

Return the color name or hex value.

exception

return any errors or warnings in this structure.

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](color.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
