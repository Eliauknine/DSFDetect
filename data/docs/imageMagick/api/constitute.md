[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ConstituteImage](constitute.html#ConstituteImage) • [PingImage](constitute.html#PingImage) • [PingImages](constitute.html#PingImages) • [ReadImage](constitute.html#ReadImage) • [ReadImages](constitute.html#ReadImages) • [WriteImage](constitute.html#WriteImage) • [WriteImages](constitute.html#WriteImages)

## [ConstituteImage](http://www.imagemagick.org/api/MagickCore/constitute_8c.html)

ConstituteImage() returns an image from the pixel data you supply. The pixel data must be in scanline order top-to-bottom. The data can be char, short int, int, float, or double. Float and double require the pixels to be normalized [0..1], otherwise [0..QuantumRange]. For example, to create a 640x480 image from unsigned red-green-blue character data, use:
    
    
    image = ConstituteImage(640,480,"RGB",CharPixel,pixels,&exception);
    

The format of the ConstituteImage method is:
    
    
    Image *ConstituteImage(const size_t columns,const size_t rows,
      const char *map,const StorageType storage,const void *pixels,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

columns
    width in pixels of the image. 
    
rows
    height in pixels of the image. 
    
map
     This string reflects the expected ordering of the pixel array. It can be any combination or order of R = red, G = green, B = blue, A = alpha (0 is transparent), O = opacity (0 is opaque), C = cyan, Y = yellow, M = magenta, K = black, I = intensity (for grayscale), P = pad. 
    
storage
    Define the data type of the pixels. Float and double types are expected to be normalized [0..1] otherwise [0..QuantumRange]. Choose from these types: CharPixel, DoublePixel, FloatPixel, IntegerPixel, LongPixel, QuantumPixel, or ShortPixel. 
    
pixels
    This array of values contain the pixel components as defined by map and type. You must preallocate this array where the expected length varies depending on the values of width, height, map, and type. 
    
exception
    return any errors or warnings in this structure. 
    

## [PingImage](http://www.imagemagick.org/api/MagickCore/constitute_8c.html)

PingImage() returns all the properties of an image or image sequence except for the pixels. It is much faster and consumes far less memory than ReadImage(). On failure, a NULL image is returned and exception describes the reason for the failure.

The format of the PingImage method is:
    
    
    Image *PingImage(const ImageInfo *image_info,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    Ping the image defined by the file or filename members of this structure. 
    
exception
    return any errors or warnings in this structure. 
    

## [PingImages](http://www.imagemagick.org/api/MagickCore/constitute_8c.html)

PingImages() pings one or more images and returns them as an image list.

The format of the PingImage method is:
    
    
    Image *PingImages(ImageInfo *image_info,const char *filename,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
filename
    the image filename. 
    
exception
    return any errors or warnings in this structure. 
    

## [ReadImage](http://www.imagemagick.org/api/MagickCore/constitute_8c.html)

ReadImage() reads an image or image sequence from a file or file handle. The method returns a NULL if there is a memory shortage or if the image cannot be read. On failure, a NULL image is returned and exception describes the reason for the failure.

The format of the ReadImage method is:
    
    
    Image *ReadImage(const ImageInfo *image_info,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    Read the image defined by the file or filename members of this structure. 
    
exception
    return any errors or warnings in this structure. 
    

## [ReadImages](http://www.imagemagick.org/api/MagickCore/constitute_8c.html)

ReadImages() reads one or more images and returns them as an image list.

The format of the ReadImage method is:
    
    
    Image *ReadImages(ImageInfo *image_info,const char *filename,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
filename
    the image filename. 
    
exception
    return any errors or warnings in this structure. 
    

## [WriteImage](http://www.imagemagick.org/api/MagickCore/constitute_8c.html)

WriteImage() writes an image or an image sequence to a file or file handle. If writing to a file is on disk, the name is defined by the filename member of the image structure. WriteImage() returns MagickFalse is there is a memory shortage or if the image cannot be written. Check the exception member of image to determine the cause for any failure.

The format of the WriteImage method is:
    
    
    MagickBooleanType WriteImage(const ImageInfo *image_info,Image *image,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [WriteImages](http://www.imagemagick.org/api/MagickCore/constitute_8c.html)

WriteImages() writes an image sequence into one or more files. While WriteImage() can write an image sequence, it is limited to writing the sequence into a single file using a format which supports multiple frames. WriteImages(), however, does not have this limitation, instead it generates multiple output files if necessary (or when requested). When ImageInfo's adjoin flag is set to MagickFalse, the file name is expected to include a printf-style formatting string for the frame number (e.g. "image02d.png").

The format of the WriteImages method is:
    
    
    MagickBooleanType WriteImages(const ImageInfo *image_info,Image *images,
      const char *filename,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
images
    the image list. 
    
filename
    the image filename. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](constitute.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
