[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[SetImageProgressMonitor](monitor.html#SetImageProgressMonitor) • [SetImageInfoProgressMonitor](monitor.html#SetImageInfoProgressMonitor)

## [SetImageProgressMonitor](http://www.imagemagick.org/api/MagickCore/monitor_8c.html)

SetImageProgressMonitor() sets the image progress monitor to the specified method and returns the previous progress monitor if any. The progress monitor method looks like this:
    
    
        MagickBooleanType MagickProgressMonitor(const char *text,
    const MagickOffsetType offset,const MagickSizeType extent,
    void *client_data)
    

If the progress monitor returns MagickFalse, the current operation is interrupted.

The format of the SetImageProgressMonitor method is:
    
    
    MagickProgressMonitor SetImageProgressMonitor(Image *image,
      const MagickProgressMonitor progress_monitor,void *client_data)
    

A description of each parameter follows:

    
    

image
    the image. 
    
progress_monitor
    Specifies a pointer to a method to monitor progress of an image operation. 
    
client_data
    Specifies a pointer to any client data. 
    

## [SetImageInfoProgressMonitor](http://www.imagemagick.org/api/MagickCore/monitor_8c.html)

SetImageInfoProgressMonitor() sets the image_info progress monitor to the specified method and returns the previous progress monitor if any. The progress monitor method looks like this:
    
    
        MagickBooleanType MagickProgressMonitor(const char *text,
    const MagickOffsetType offset,const MagickSizeType extent,
    void *client_data)
    

If the progress monitor returns MagickFalse, the current operation is interrupted.

The format of the SetImageInfoProgressMonitor method is:
    
    
    MagickProgressMonitor SetImageInfoProgressMonitor(ImageInfo *image_info,
      const MagickProgressMonitor progress_monitor,void *client_data)
    

A description of each parameter follows:

    
    

image_info
    the image info. 
    
progress_monitor
    Specifies a pointer to a method to monitor progress of an image operation. 
    
client_data
    Specifies a pointer to any client data. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](monitor.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
