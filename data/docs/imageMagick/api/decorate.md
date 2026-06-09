[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[BorderImage](decorate.html#BorderImage) • [FrameImage](decorate.html#FrameImage) • [RaiseImage](decorate.html#RaiseImage)

## [BorderImage](http://www.imagemagick.org/api/MagickCore/decorate_8c.html)

BorderImage() surrounds the image with a border of the color defined by the bordercolor member of the image structure. The width and height of the border are defined by the corresponding members of the border_info structure.

The format of the BorderImage method is:
    
    
    Image *BorderImage(const Image *image,const RectangleInfo *border_info,
      const CompositeOperator compose,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
border_info
     define the width and height of the border. 
    
compose
     the composite operator. 
    
exception
    return any errors or warnings in this structure. 
    

## [FrameImage](http://www.imagemagick.org/api/MagickCore/decorate_8c.html)

FrameImage() adds a simulated three-dimensional border around the image. The color of the border is defined by the alpha_color member of image. Members width and height of frame_info specify the border width of the vertical and horizontal sides of the frame. Members inner and outer indicate the width of the inner and outer shadows of the frame.

The format of the FrameImage method is:
    
    
    Image *FrameImage(const Image *image,const FrameInfo *frame_info,
      const CompositeOperator compose,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
frame_info
    Define the width and height of the frame and its bevels. 
    
compose
    the composite operator. 
    
exception
    return any errors or warnings in this structure. 
    

## [RaiseImage](http://www.imagemagick.org/api/MagickCore/decorate_8c.html)

RaiseImage() creates a simulated three-dimensional button-like effect by lightening and darkening the edges of the image. Members width and height of raise_info define the width of the vertical and horizontal edge of the effect.

The format of the RaiseImage method is:
    
    
    MagickBooleanType RaiseImage(const Image *image,
      const RectangleInfo *raise_info,const MagickBooleanType raise,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
raise_info
    Define the width and height of the raise area. 
    
raise
    A value other than zero creates a 3-D raise effect, otherwise it has a lowered effect. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](decorate.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
