[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireMagickResource](resource.html#AcquireMagickResource) • [AcquireUniqueFileResource](resource.html#AcquireUniqueFileResource) • [GetMagickResource](resource.html#GetMagickResource) • [GetMagickResourceLimit](resource.html#GetMagickResourceLimit) • [ListMagickResourceInfo](resource.html#ListMagickResourceInfo) • [RelinquishMagickResource](resource.html#RelinquishMagickResource) • [RelinquishUniqueFileResource](resource.html#RelinquishUniqueFileResource) • [SetMagickResourceLimit](resource.html#SetMagickResourceLimit)

## [AcquireMagickResource](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

AcquireMagickResource() acquires resources of the specified type. MagickFalse is returned if the specified resource is exhausted otherwise MagickTrue.

The format of the AcquireMagickResource() method is:
    
    
    MagickBooleanType AcquireMagickResource(const ResourceType type,
      const MagickSizeType size)
    

A description of each parameter follows:

    
    

type
    the type of resource. 
    
size
    the number of bytes needed from for this resource. 
    

## [AcquireUniqueFileResource](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

AcquireUniqueFileResource() returns a unique file name, and returns a file descriptor for the file open for reading and writing.

The format of the AcquireUniqueFileResource() method is:
    
    
    int AcquireUniqueFileResource(char *path)
    

A description of each parameter follows:

    
    

path
     Specifies a pointer to an array of characters. The unique path name is returned in this array. 
    

## [GetMagickResource](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

GetMagickResource() returns the specified resource.

The format of the GetMagickResource() method is:
    
    
    MagickSizeType GetMagickResource(const ResourceType type)
    

A description of each parameter follows:

    
    

type
    the type of resource. 
    

## [GetMagickResourceLimit](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

GetMagickResourceLimit() returns the specified resource limit.

The format of the GetMagickResourceLimit() method is:
    
    
    MagickSizeType GetMagickResourceLimit(const ResourceType type)
    

A description of each parameter follows:

    
    

type
    the type of resource. 
    

## [ListMagickResourceInfo](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

ListMagickResourceInfo() lists the resource info to a file.

The format of the ListMagickResourceInfo method is:
    
    
    MagickBooleanType ListMagickResourceInfo(FILE *file,
      ExceptionInfo *exception)
    

A description of each parameter follows.

file

An pointer to a FILE.

exception

return any errors or warnings in this structure.

## [RelinquishMagickResource](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

RelinquishMagickResource() relinquishes resources of the specified type.

The format of the RelinquishMagickResource() method is:
    
    
    void RelinquishMagickResource(const ResourceType type,
      const MagickSizeType size)
    

A description of each parameter follows:

    
    

type
    the type of resource. 
    
size
    the size of the resource. 
    

## [RelinquishUniqueFileResource](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

RelinquishUniqueFileResource() relinquishes a unique file resource.

The format of the RelinquishUniqueFileResource() method is:
    
    
    MagickBooleanType RelinquishUniqueFileResource(const char *path)
    

A description of each parameter follows:

    
    

name
    the name of the temporary resource. 
    

## [SetMagickResourceLimit](http://www.imagemagick.org/api/MagickCore/resource_8c.html)

SetMagickResourceLimit() sets the limit for a particular resource.

The format of the SetMagickResourceLimit() method is:
    
    
    MagickBooleanType SetMagickResourceLimit(const ResourceType type,
      const MagickSizeType limit)
    

A description of each parameter follows:

    
    

type
    the type of resource. 
    
limit
    the maximum limit for the resource. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](resource.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
