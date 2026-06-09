[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[DefineImageRegistry](registry.html#DefineImageRegistry) • [DeleteImageRegistry](registry.html#DeleteImageRegistry) • [GetImageRegistry](registry.html#GetImageRegistry) • [GetNextImageRegistry](registry.html#GetNextImageRegistry) • [RegistryComponentTerminus](registry.html#RegistryComponentTerminus) • [RemoveImageRegistry](registry.html#RemoveImageRegistry) • [ResetImageRegistryIterator](registry.html#ResetImageRegistryIterator) • [SetImageRegistry](registry.html#SetImageRegistry)

## [DefineImageRegistry](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

DefineImageRegistry() associates a key/value pair with the image registry.

The format of the DefineImageRegistry method is:
    
    
    MagickBooleanType DefineImageRegistry(const RegistryType type,
      const char *option,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

type
    the type. 
    
option
    the option. 
    
exception
    the exception. 
    

## [DeleteImageRegistry](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

DeleteImageRegistry() deletes a key from the image registry.

The format of the DeleteImageRegistry method is:
    
    
    MagickBooleanType DeleteImageRegistry(const char *key)
    

A description of each parameter follows:

    
    

key
    the registry. 
    

## [GetImageRegistry](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

GetImageRegistry() returns a value associated with an image registry key.

The format of the GetImageRegistry method is:
    
    
    void *GetImageRegistry(const RegistryType type,const char *key,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

type
    the type. 
    
key
    the key. 
    
exception
    the exception. 
    

## [GetNextImageRegistry](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

GetNextImageRegistry() gets the next image registry value.

The format of the GetNextImageRegistry method is:
    
    
    char *GetNextImageRegistry(void)
    

## [RegistryComponentTerminus](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

RegistryComponentTerminus() destroys the registry component.

The format of the DestroyDefines method is:
    
    
    void RegistryComponentTerminus(void)
    

## [RemoveImageRegistry](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

RemoveImageRegistry() removes a key from the image registry and returns its value.

The format of the RemoveImageRegistry method is:
    
    
    void *RemoveImageRegistry(const char *key)
    

A description of each parameter follows:

    
    

key
    the registry. 
    

## [ResetImageRegistryIterator](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

ResetImageRegistryIterator() resets the registry iterator. Use it in conjunction with GetNextImageRegistry() to iterate over all the values in the image registry.

The format of the ResetImageRegistryIterator method is:
    
    
    ResetImageRegistryIterator(void)
    

## [SetImageRegistry](http://www.imagemagick.org/api/MagickCore/registry_8c.html)

SetImageRegistry() associates a value with an image registry key.

The format of the SetImageRegistry method is:
    
    
    MagickBooleanType SetImageRegistry(const RegistryType type,
      const char *key,const void *value,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

type
    the type. 
    
key
    the key. 
    
value
    the value. 
    
exception
    the exception. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](registry.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
