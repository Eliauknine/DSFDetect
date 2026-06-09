[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[The XShearImage](shear.html#The XShearImage) • [DeskewImage](shear.html#DeskewImage) • [IntegralRotateImage](shear.html#IntegralRotateImage) • [ShearImage](shear.html#ShearImage) • [ShearRotateImage](shear.html#ShearRotateImage)

## [The XShearImage](http://www.imagemagick.org/api/MagickCore/shear_8c.html)

The XShearImage() and YShearImage() methods are based on the paper "A Fast Algorithm for General Raster Rotatation" by Alan W. Paeth, Graphics Interface '86 (Vancouver). ShearRotateImage() is adapted from a similar method based on the Paeth paper written by Michael Halle of the Spatial Imaging Group, MIT Media Lab.

## [DeskewImage](http://www.imagemagick.org/api/MagickCore/shear_8c.html)

DeskewImage() removes skew from the image. Skew is an artifact that occurs in scanned images because of the camera being misaligned, imperfections in the scanning or surface, or simply because the paper was not placed completely flat when scanned.

The result will be auto-croped if the artifact "deskew:auto-crop" is defined, while the amount the image is to be deskewed, in degrees is also saved as the artifact "deskew:angle".

If the artifact "deskew:auto-crop" is given the image will be automatically cropped of the excess background. The value is the border width of all pixels around the edge that will be used to determine an average border color for the automatic trim.

The format of the DeskewImage method is:
    
    
    Image *DeskewImage(const Image *image,const double threshold,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
threshold
    separate background from foreground. 
    
exception
    return any errors or warnings in this structure. 
    

## [IntegralRotateImage](http://www.imagemagick.org/api/MagickCore/shear_8c.html)

IntegralRotateImage() rotates the image an integral of 90 degrees. It allocates the memory necessary for the new Image structure and returns a pointer to the rotated image.

The format of the IntegralRotateImage method is:
    
    
    Image *IntegralRotateImage(const Image *image,size_t rotations,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

rotations

Specifies the number of 90 degree rotations.

## [ShearImage](http://www.imagemagick.org/api/MagickCore/shear_8c.html)

ShearImage() creates a new image that is a shear_image copy of an existing one. Shearing slides one edge of an image along the X or Y axis, creating a parallelogram. An X direction shear slides an edge along the X axis, while a Y direction shear slides an edge along the Y axis. The amount of the shear is controlled by a shear angle. For X direction shears, x_shear is measured relative to the Y axis, and similarly, for Y direction shears y_shear is measured relative to the X axis. Empty triangles left over from shearing the image are filled with the background color defined by member 'background_color' of the image.. ShearImage() allocates the memory necessary for the new Image structure and returns a pointer to the new image.

ShearImage() is based on the paper "A Fast Algorithm for General Raster Rotatation" by Alan W. Paeth.

The format of the ShearImage method is:
    
    
    Image *ShearImage(const Image *image,const double x_shear,
      const double y_shear,ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

x_shear, y_shear

Specifies the number of degrees to shear the image.

exception

return any errors or warnings in this structure.

## [ShearRotateImage](http://www.imagemagick.org/api/MagickCore/shear_8c.html)

ShearRotateImage() creates a new image that is a rotated copy of an existing one. Positive angles rotate counter-clockwise (right-hand rule), while negative angles rotate clockwise. Rotated images are usually larger than the originals and have 'empty' triangular corners. X axis. Empty triangles left over from shearing the image are filled with the background color defined by member 'background_color' of the image. ShearRotateImage allocates the memory necessary for the new Image structure and returns a pointer to the new image.

ShearRotateImage() is based on the paper "A Fast Algorithm for General Raster Rotatation" by Alan W. Paeth. ShearRotateImage is adapted from a similar method based on the Paeth paper written by Michael Halle of the Spatial Imaging Group, MIT Media Lab.

The format of the ShearRotateImage method is:
    
    
    Image *ShearRotateImage(const Image *image,const double degrees,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

the image.

degrees

Specifies the number of degrees to rotate the image.

exception

return any errors or warnings in this structure.

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](shear.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
