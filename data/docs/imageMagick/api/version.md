[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[GetMagickCopyright](version.html#GetMagickCopyright) • [GetMagickDelegates](version.html#GetMagickDelegates) • [GetMagickFeatures](version.html#GetMagickFeatures) • [GetMagickHomeURL](version.html#GetMagickHomeURL) • [GetMagickLicense](version.html#GetMagickLicense) • [GetMagickPackageName](version.html#GetMagickPackageName) • [GetMagickQuantumDepth](version.html#GetMagickQuantumDepth) • [GetMagickQuantumRange](version.html#GetMagickQuantumRange) • [GetMagickReleaseDate](version.html#GetMagickReleaseDate) • [GetMagickSignature](version.html#GetMagickSignature) • [GetMagickVersion](version.html#GetMagickVersion) • [ListMagickVersion](version.html#ListMagickVersion)

## [GetMagickCopyright](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickCopyright() returns the ImageMagick API copyright as a string.

The format of the GetMagickCopyright method is:
    
    
    const char *GetMagickCopyright(void)
    

## [GetMagickDelegates](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickDelegates() returns the ImageMagick delegate libraries.

The format of the GetMagickDelegates method is:
    
    
    const char *GetMagickDelegates(void)
    

No parameters are required.

## [GetMagickFeatures](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickFeatures() returns the ImageMagick features.

The format of the GetMagickFeatures method is:
    
    
    const char *GetMagickFeatures(void)
    

No parameters are required.

## [GetMagickHomeURL](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickHomeURL() returns the ImageMagick home URL.

The format of the GetMagickHomeURL method is:
    
    
    char *GetMagickHomeURL(void)
    

## [GetMagickLicense](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickLicense() returns the ImageMagick API license as a string.

The format of the GetMagickLicense method is:
    
    
    const char *GetMagickLicense(void)
    

## [GetMagickPackageName](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickPackageName() returns the ImageMagick package name.

The format of the GetMagickName method is:
    
    
    const char *GetMagickName(void)
    

No parameters are required.

## [GetMagickQuantumDepth](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickQuantumDepth() returns the ImageMagick quantum depth.

The format of the GetMagickQuantumDepth method is:
    
    
    const char *GetMagickQuantumDepth(size_t *depth)
    

A description of each parameter follows:

    
    

depth
    the quantum depth is returned as a number. 
    

## [GetMagickQuantumRange](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickQuantumRange() returns the ImageMagick quantum range.

The format of the GetMagickQuantumRange method is:
    
    
    const char *GetMagickQuantumRange(size_t *range)
    

A description of each parameter follows:

    
    

range
    the quantum range is returned as a number. 
    

## [GetMagickReleaseDate](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickReleaseDate() returns the ImageMagick release date.

The format of the GetMagickReleaseDate method is:
    
    
    const char *GetMagickReleaseDate(void)
    

No parameters are required.

## [GetMagickSignature](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickSignature() returns a signature that uniquely encodes the MagickCore libary version, quantum depth, HDRI status, OS word size, and endianness.

The format of the GetMagickSignature method is:
    
    
    unsigned int GetMagickSignature(const StringInfo *nonce)
    

A description of each parameter follows:

    
    

nonce
    arbitrary data. 
    

## [GetMagickVersion](http://www.imagemagick.org/api/MagickCore/version_8c.html)

GetMagickVersion() returns the ImageMagick API version as a string and as a number.

The format of the GetMagickVersion method is:
    
    
    const char *GetMagickVersion(size_t *version)
    

A description of each parameter follows:

    
    

version
    the ImageMagick version is returned as a number. 
    

## [ListMagickVersion](http://www.imagemagick.org/api/MagickCore/version_8c.html)

ListMagickVersion() identifies the ImageMagick version by printing its attributes to the file. Attributes include the copyright, features, and delegates.

The format of the ListMagickVersion method is:
    
    
    void ListMagickVersion(FILE *file)
    

A description of each parameter follows:

    
    

file
    the file, typically stdout. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](version.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
