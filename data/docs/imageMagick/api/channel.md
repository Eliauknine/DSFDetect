[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ChannelFxImage](channel.html#ChannelFxImage) • [CombineImages](channel.html#CombineImages) • [GetImageAlphaChannel](channel.html#GetImageAlphaChannel) • [SeparateImage](channel.html#SeparateImage) • [SeparateImages](channel.html#SeparateImages) • [SetImageAlphaChannel](channel.html#SetImageAlphaChannel)

## [ChannelFxImage](http://www.imagemagick.org/api/MagickCore/channel_8c.html)

ChannelFxImage() applies a channel expression to the specified image. The expression consists of one or more channels, either mnemonic or numeric (e.g. red, 1), separated by actions as follows:

    
     <=> exchange two channels (e.g. red<=>blue) => copy one channel to another channel (e.g. red=>green) = assign a constant value to a channel (e.g. red=50) , write new image channels in the specified order (e.g. red, green) | add a new output image for the next set of channel operations ; move to the next input image for the source of channel data 
     For example, to create 3 grayscale images from the red, green, and blue channels of an image, use: 
    
    
        -channel-fx "red; green; blue"
    

A channel without an operation symbol implies separate (i.e, semicolon). 
     The format of the ChannelFxImage method is: 
    
    
    Image *ChannelFxImage(const Image *image,const char *expression,
      ExceptionInfo *exception)
    

A description of each parameter follows: 
    
    

image
    the image. 
    
expression
    A channel expression. 
    
exception
    return any errors or warnings in this structure. 
    

## [CombineImages](http://www.imagemagick.org/api/MagickCore/channel_8c.html)

CombineImages() combines one or more images into a single image. The grayscale value of the pixels of each image in the sequence is assigned in order to the specified channels of the combined image. The typical ordering would be image 1 => Red, 2 => Green, 3 => Blue, etc.

The format of the CombineImages method is:
    
    
    Image *CombineImages(const Image *images,const ColorspaceType colorspace,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
colorspace
    the image colorspace. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetImageAlphaChannel](http://www.imagemagick.org/api/MagickCore/channel_8c.html)

GetImageAlphaChannel() returns MagickFalse if the image alpha channel is not activated. That is, the image is RGB rather than RGBA or CMYK rather than CMYKA.

The format of the GetImageAlphaChannel method is:
    
    
    MagickBooleanType GetImageAlphaChannel(const Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [SeparateImage](http://www.imagemagick.org/api/MagickCore/channel_8c.html)

SeparateImage() separates a channel from the image and returns it as a grayscale image.

The format of the SeparateImage method is:
    
    
    Image *SeparateImage(const Image *image,const ChannelType channel,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
channel
    the image channel. 
    
exception
    return any errors or warnings in this structure. 
    

## [SeparateImages](http://www.imagemagick.org/api/MagickCore/channel_8c.html)

SeparateImages() returns a separate grayscale image for each channel specified.

The format of the SeparateImages method is:
    
    
    Image *SeparateImages(const Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetImageAlphaChannel](http://www.imagemagick.org/api/MagickCore/channel_8c.html)

SetImageAlphaChannel() activates, deactivates, resets, or sets the alpha channel.

The format of the SetImageAlphaChannel method is:
    
    
    MagickBooleanType SetImageAlphaChannel(Image *image,
      const AlphaChannelOption alpha_type,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
alpha_type
     The alpha channel type: ActivateAlphaChannel, AssociateAlphaChannel, CopyAlphaChannel, DeactivateAlphaChannel, DisassociateAlphaChannel, ExtractAlphaChannel, OffAlphaChannel, OnAlphaChannel, OpaqueAlphaChannel, SetAlphaChannel, ShapeAlphaChannel, and TransparentAlphaChannel. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](channel.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
