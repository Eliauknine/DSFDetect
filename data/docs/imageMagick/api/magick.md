[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireMagickInfo](magick.html#AcquireMagickInfo) • [GetMagickPrecision](magick.html#GetMagickPrecision) • [IsMagickCoreInstantiated](magick.html#IsMagickCoreInstantiated) • [MagickCoreGenesis](magick.html#MagickCoreGenesis) • [MagickCoreTerminus](magick.html#MagickCoreTerminus) • [SetMagickPrecision](magick.html#SetMagickPrecision)

## [AcquireMagickInfo](http://www.imagemagick.org/api/MagickCore/magick_8c.html)

AcquireMagickInfo() allocates a MagickInfo structure and initializes the members to default values.

The format of the AcquireMagickInfo method is:
    
    
    MagickInfo *AcquireMagickInfo(const char *module, const char *name,)
    

A description of each parameter follows:

    
    

module
    a character string that represents the module associated with the MagickInfo structure. 
    
name
    a character string that represents the image format associated with the MagickInfo structure. 
    
description
    a character string that represents the image format associated with the MagickInfo structure. 
    

## [GetMagickPrecision](http://www.imagemagick.org/api/MagickCore/magick_8c.html)

GetMagickPrecision() returns the maximum number of significant digits to be printed.

The format of the GetMagickPrecision method is:
    
    
    int GetMagickPrecision(void)
    

## [IsMagickCoreInstantiated](http://www.imagemagick.org/api/MagickCore/magick_8c.html)

IsMagickCoreInstantiated() returns MagickTrue if the ImageMagick environment is currently instantiated: MagickCoreGenesis() has been called but MagickDestroy() has not.

The format of the IsMagickCoreInstantiated method is:
    
    
    MagickBooleanType IsMagickCoreInstantiated(void)
    

## [MagickCoreGenesis](http://www.imagemagick.org/api/MagickCore/magick_8c.html)

MagickCoreGenesis() initializes the MagickCore environment.

The format of the MagickCoreGenesis function is:
    
    
    MagickCoreGenesis(const char *path,
      const MagickBooleanType establish_signal_handlers)
    

A description of each parameter follows:

    
    

path
    the execution path of the current ImageMagick client. 
    
establish_signal_handlers
    set to MagickTrue to use MagickCore's own signal handlers for common signals. 
    

## [MagickCoreTerminus](http://www.imagemagick.org/api/MagickCore/magick_8c.html)

MagickCoreTerminus() destroys the MagickCore environment.

The format of the MagickCoreTerminus function is:
    
    
    MagickCoreTerminus(void)
    

## [SetMagickPrecision](http://www.imagemagick.org/api/MagickCore/magick_8c.html)

SetMagickPrecision() sets the maximum number of significant digits to be printed.

An input argument of 0 returns the current precision setting.

A negative value forces the precision to reset to a default value according to the environment variable "MAGICK_PRECISION", the current 'policy' configuration setting, or the default value of '6', in that order.

The format of the SetMagickPrecision method is:
    
    
    int SetMagickPrecision(const int precision)
    

A description of each parameter follows:

    
    

precision
    set the maximum number of significant digits to be printed. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](magick.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
