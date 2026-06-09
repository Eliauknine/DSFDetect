[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[BlobToImage](blob.html#BlobToImage) • [FileToImage](blob.html#FileToImage) • [GetBlobProperties](blob.html#GetBlobProperties) • [ImageToBlob](blob.html#ImageToBlob) • [ImageToFile](blob.html#ImageToFile) • [ImagesToBlob](blob.html#ImagesToBlob) • [InjectImageBlob](blob.html#InjectImageBlob)

## [BlobToImage](http://www.imagemagick.org/api/MagickCore/blob_8c.html)

BlobToImage() implements direct to memory image formats. It returns the blob as an image.

The format of the BlobToImage method is:
    
    
    Image *BlobToImage(const ImageInfo *image_info,const void *blob,
      const size_t length,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
blob
    the address of a character stream in one of the image formats understood by ImageMagick. 
    
length
    This size_t integer reflects the length in bytes of the blob. 
    
exception
    return any errors or warnings in this structure. 
    

## [FileToImage](http://www.imagemagick.org/api/MagickCore/blob_8c.html)

FileToImage() write the contents of a file to an image.

The format of the FileToImage method is:
    
    
    MagickBooleanType FileToImage(Image *,const char *filename)
    

A description of each parameter follows:

    
    

image
    the image. 
    
filename
    the filename. 
    

## [GetBlobProperties](http://www.imagemagick.org/api/MagickCore/blob_8c.html)

GetBlobProperties() returns information about an image blob.

The format of the GetBlobProperties method is:
    
    
    const struct stat *GetBlobProperties(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [ImageToBlob](http://www.imagemagick.org/api/MagickCore/blob_8c.html)

ImageToBlob() implements direct to memory image formats. It returns the image as a formatted blob and its length. The magick member of the Image structure determines the format of the returned blob (GIF, JPEG, PNG, etc.). This method is the equivalent of WriteImage(), but writes the formatted "file" to a memory buffer rather than to an actual file.

The format of the ImageToBlob method is:
    
    
    void *ImageToBlob(const ImageInfo *image_info,Image *image,
      size_t *length,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
image
    the image. 
    
length
    return the actual length of the blob. 
    
exception
    return any errors or warnings in this structure. 
    

## [ImageToFile](http://www.imagemagick.org/api/MagickCore/blob_8c.html)

ImageToFile() writes an image to a file. It returns MagickFalse if an error occurs otherwise MagickTrue.

The format of the ImageToFile method is:
    
    
     MagickBooleanType ImageToFile(Image *image,char *filename,
       ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
filename
    Write the image to this file. 
    
exception
    return any errors or warnings in this structure. 
    

## [ImagesToBlob](http://www.imagemagick.org/api/MagickCore/blob_8c.html)

ImagesToBlob() implements direct to memory image formats. It returns the image sequence as a blob and its length. The magick member of the ImageInfo structure determines the format of the returned blob (GIF, JPEG, PNG, etc.)

Note, some image formats do not permit multiple images to the same image stream (e.g. JPEG). in this instance, just the first image of the sequence is returned as a blob.

The format of the ImagesToBlob method is:
    
    
    void *ImagesToBlob(const ImageInfo *image_info,Image *images,
      size_t *length,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
images
    the image list. 
    
length
    return the actual length of the blob. 
    
exception
    return any errors or warnings in this structure. 
    

## [InjectImageBlob](http://www.imagemagick.org/api/MagickCore/blob_8c.html)

InjectImageBlob() injects the image with a copy of itself in the specified format (e.g. inject JPEG into a PDF image).

The format of the InjectImageBlob method is:
    
    
    MagickBooleanType InjectImageBlob(const ImageInfo *image_info,
      Image *image,Image *inject_image,const char *format,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info.. 
    
image
    the image. 
    
inject_image
    inject into the image stream. 
    
format
    the image format. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](blob.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
