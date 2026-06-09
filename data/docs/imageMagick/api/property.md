[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[CloneImageProperties](property.html#CloneImageProperties) • [DefineImageProperty](property.html#DefineImageProperty) • [DeleteImageProperty](property.html#DeleteImageProperty) • [DestroyImageProperties](property.html#DestroyImageProperties) • [FormatImageProperty](property.html#FormatImageProperty) • [GetImageProperty](property.html#GetImageProperty) • [GetNextImageProperty](property.html#GetNextImageProperty) • [InterpretImageProperties](property.html#InterpretImageProperties) • [(void) LogMagickEvent(TraceEvent,GetMagickModule](property.html#\(void\) LogMagickEvent\(TraceEvent,GetMagickModule) • [RemoveImageProperty](property.html#RemoveImageProperty) • [ResetImagePropertyIterator](property.html#ResetImagePropertyIterator) • [SetImageProperty](property.html#SetImageProperty)

## [CloneImageProperties](http://www.imagemagick.org/api/MagickCore/property_8c.html)

CloneImageProperties() clones all the image properties to another image.

The format of the CloneImageProperties method is:
    
    
    MagickBooleanType CloneImageProperties(Image *image,
      const Image *clone_image)
    

A description of each parameter follows:

    
    

image
    the image. 
    
clone_image
    the clone image. 
    

## [DefineImageProperty](http://www.imagemagick.org/api/MagickCore/property_8c.html)

DefineImageProperty() associates an assignment string of the form "key=value" with an artifact or options. It is equivelent to SetImageProperty()

The format of the DefineImageProperty method is:
    
    
    MagickBooleanType DefineImageProperty(Image *image,const char *property,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
property
    the image property. 
    
exception
    return any errors or warnings in this structure. 
    

## [DeleteImageProperty](http://www.imagemagick.org/api/MagickCore/property_8c.html)

DeleteImageProperty() deletes an image property.

The format of the DeleteImageProperty method is:
    
    
    MagickBooleanType DeleteImageProperty(Image *image,const char *property)
    

A description of each parameter follows:

    
    

image
    the image. 
    
property
    the image property. 
    

## [DestroyImageProperties](http://www.imagemagick.org/api/MagickCore/property_8c.html)

DestroyImageProperties() destroys all properties and associated memory attached to the given image.

The format of the DestroyDefines method is:
    
    
    void DestroyImageProperties(Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [FormatImageProperty](http://www.imagemagick.org/api/MagickCore/property_8c.html)

FormatImageProperty() permits formatted property/value pairs to be saved as an image property.

The format of the FormatImageProperty method is:
    
    
    MagickBooleanType FormatImageProperty(Image *image,const char *property,
      const char *format,...)
    

A description of each parameter follows.

image

The image.

property

The attribute property.

format

A string describing the format to use to write the remaining arguments.

## [GetImageProperty](http://www.imagemagick.org/api/MagickCore/property_8c.html)

GetImageProperty() gets a value associated with an image property.

This includes, profile prefixes, such as "exif:", "iptc:" and "8bim:" It does not handle non-prifile prefixes, such as "fx:", "option:", or "artifact:".

The returned string is stored as a properity of the same name for faster lookup later. It should NOT be freed by the caller.

The format of the GetImageProperty method is:
    
    
    const char *GetImageProperty(const Image *image,const char *key,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
key
    the key. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetNextImageProperty](http://www.imagemagick.org/api/MagickCore/property_8c.html)

GetNextImageProperty() gets the next free-form string property name.

The format of the GetNextImageProperty method is:
    
    
    char *GetNextImageProperty(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [InterpretImageProperties](http://www.imagemagick.org/api/MagickCore/property_8c.html)

InterpretImageProperties() replaces any embedded formatting characters with the appropriate image property and returns the interpreted text.

This searches for and replaces \n \r \ replaced by newline, return, and percent resp. &lt; &gt; &amp; replaced by '<', '>', '&' resp. replaced by percent

x [x] where 'x' is a single letter properity, case sensitive). [type:name] where 'type' a is special and known prefix. [name] where 'name' is a specifically known attribute, calculated value, or a per-image property string name, or a per-image 'artifact' (as generated from a global option). It may contain ':' as long as the prefix is not special.

Single letter substitutions will only happen if the character before the percent is NOT a number. But braced substitutions will always be performed. This prevents the typical usage of percent in a interpreted geometry argument from being substituted when the percent is a geometry flag.

If 'glob-expresions' ('*' or '?' characters) is used for 'name' it may be used as a search pattern to print multiple lines of "name=value\n" pairs of the associacted set of properties.

The returned string must be freed using DestoryString() by the caller.

The format of the InterpretImageProperties method is:
    
    
    char *InterpretImageProperties(ImageInfo *image_info,
      Image *image,const char *embed_text,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. (required) 
    
image
    the image. (optional) 
    
embed_text
    the address of a character string containing the embedded formatting characters. 
    
exception
    return any errors or warnings in this structure. 
    

## [(void) LogMagickEvent(TraceEvent,GetMagickModule](http://www.imagemagick.org/api/MagickCore/property_8c.html)

(void) LogMagickEvent(TraceEvent,GetMagickModule(),"s",image->filename); else if( image_info != (ImageInfo *) NULL && image_info->debug != MagickFalse) (void) LogMagickEvent(TraceEvent,GetMagickModule(),"s","no-image");

if (embed_text == (const char *) NULL) return(ConstantString("")); p=embed_text;

if (*p == '\0') return(ConstantString(""));

if ((*p == '@') && (IsPathAccessible(p+1) != MagickFalse)) { /* handle a '@' replace string from file */ interpret_text=FileToString(p+1,~0UL,exception); if (interpret_text != (char *) NULL) return(interpret_text); }

/* Translate any embedded format characters. 

## [RemoveImageProperty](http://www.imagemagick.org/api/MagickCore/property_8c.html)

RemoveImageProperty() removes a property from the image and returns its value.

In this case the ConstantString() value returned should be freed by the caller when finished.

The format of the RemoveImageProperty method is:
    
    
    char *RemoveImageProperty(Image *image,const char *property)
    

A description of each parameter follows:

    
    

image
    the image. 
    
property
    the image property. 
    

## [ResetImagePropertyIterator](http://www.imagemagick.org/api/MagickCore/property_8c.html)

ResetImagePropertyIterator() resets the image properties iterator. Use it in conjunction with GetNextImageProperty() to iterate over all the values associated with an image property.

The format of the ResetImagePropertyIterator method is:
    
    
    ResetImagePropertyIterator(Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [SetImageProperty](http://www.imagemagick.org/api/MagickCore/property_8c.html)

SetImageProperty() saves the given string value either to specific known attribute or to a freeform property string.

Attempting to set a property that is normally calculated will produce an exception.

The format of the SetImageProperty method is:
    
    
    MagickBooleanType SetImageProperty(Image *image,const char *property,
      const char *value,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
property
    the image property. 
    
values
    the image property values. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](property.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
