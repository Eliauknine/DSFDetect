[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireMimeCache](mime.html#AcquireMimeCache) • [GetMimeInfoList](mime.html#GetMimeInfoList) • [GetMimeList](mime.html#GetMimeList) • [GetMimeDescription](mime.html#GetMimeDescription) • [GetMimeType](mime.html#GetMimeType) • [ListMimeInfo](mime.html#ListMimeInfo)

## [AcquireMimeCache](http://www.imagemagick.org/api/MagickCore/mime_8c.html)

AcquireMimeCache() caches one or more magic configurations which provides a mapping between magic attributes and a magic name.

The format of the AcquireMimeCache method is:
    
    
    LinkedListInfo *AcquireMimeCache(const char *filename,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

filename
    the font file name. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetMimeInfoList](http://www.imagemagick.org/api/MagickCore/mime_8c.html)

GetMimeInfoList() returns any image aliases that match the specified pattern.

The magic of the GetMimeInfoList function is:
    
    
    const MimeInfo **GetMimeInfoList(const char *pattern,
      size_t *number_aliases,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_aliases
     This integer returns the number of magics in the list. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetMimeList](http://www.imagemagick.org/api/MagickCore/mime_8c.html)

GetMimeList() returns any image format alias that matches the specified pattern.

The format of the GetMimeList function is:
    
    
    char **GetMimeList(const char *pattern,size_t *number_aliases,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_aliases
     This integer returns the number of image format aliases in the list. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetMimeDescription](http://www.imagemagick.org/api/MagickCore/mime_8c.html)

GetMimeDescription() returns the mime type description.

The format of the GetMimeDescription method is:
    
    
    const char *GetMimeDescription(const MimeInfo *mime_info)
    

A description of each parameter follows:

    
    

mime_info
     The magic info. 
    

## [GetMimeType](http://www.imagemagick.org/api/MagickCore/mime_8c.html)

GetMimeType() returns the mime type.

The format of the GetMimeType method is:
    
    
    const char *GetMimeType(const MimeInfo *mime_info)
    

A description of each parameter follows:

    
    

mime_info
     The magic info. 
    

## [ListMimeInfo](http://www.imagemagick.org/api/MagickCore/mime_8c.html)

ListMimeInfo() lists the magic info to a file.

The format of the ListMimeInfo method is:
    
    
    MagickBooleanType ListMimeInfo(FILE *file,ExceptionInfo *exception)
    

A description of each parameter follows.

file

An pointer to a FILE.

exception

return any errors or warnings in this structure.

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](mime.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
