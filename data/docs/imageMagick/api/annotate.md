[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AnnotateImage](annotate.html#AnnotateImage) • [FormatMagickCaption](annotate.html#FormatMagickCaption) • [GetMultilineTypeMetrics](annotate.html#GetMultilineTypeMetrics) • [GetTypeMetrics](annotate.html#GetTypeMetrics)

## [AnnotateImage](http://www.imagemagick.org/api/MagickCore/annotate_8c.html)

AnnotateImage() annotates an image with text. Optionally you can include any of the following bits of information about the image by embedding the appropriate special characters:
    
    
        \n   newline
        \r   carriage return
        <    less-than character.
        >    greater-than character.
        &    ampersand character.
     a percent sign
        b   file size of image read in
        c   comment meta-data property
        d   directory component of path
        e   filename extension or suffix
        f   filename (including suffix)
        g   layer canvas page geometry   (equivalent to "WxHXY")
        h   current image height in pixels
        i   image filename (note: becomes output filename for "info:")
        k   CALCULATED: number of unique colors
        l   label meta-data property
        m   image file format (file magic)
        n   number of images in current image sequence
        o   output filename  (used for delegates)
        p   index of image in current image list
        q   quantum depth (compile-time constant)
        r   image class and colorspace
        s   scene number (from input unless re-assigned)
        t   filename without directory or extension (suffix)
        u   unique temporary filename (used for delegates)
        w   current width in pixels
        x   x resolution (density)
        y   y resolution (density)
        z   image depth (as read in unless modified, image save depth)
        A   image transparency channel enabled (true/false)
        C   image compression type
        D   image GIF dispose method
        G   original image size (wxh; before any resizes)
        H   page (canvas) height
        M   Magick filename (original file exactly as given,  including read mods)
        O   page (canvas) offset ( = XY )
        P   page (canvas) size ( = WxH )
        Q   image compression quality ( 0 = default )
        S   ?? scenes ??
        T   image time delay (in centi-seconds)
        U   image resolution units
        W   page (canvas) width
        X   page (canvas) x offset (including sign)
        Y   page (canvas) y offset (including sign)
        Z   unique filename (used for delegates)
        @   CALCULATED: trim bounding box (without actually trimming)
        #   CALCULATED: 'signature' hash of image values
    

The format of the AnnotateImage method is:
    
    
    MagickBooleanType AnnotateImage(Image *image,DrawInfo *draw_info,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
exception
    return any errors or warnings in this structure. 
    

## [FormatMagickCaption](http://www.imagemagick.org/api/MagickCore/annotate_8c.html)

FormatMagickCaption() formats a caption so that it fits within the image width. It returns the number of lines in the formatted caption.

The format of the FormatMagickCaption method is:
    
    
    ssize_t FormatMagickCaption(Image *image,DrawInfo *draw_info,
      const MagickBooleanType split,TypeMetric *metrics,char **caption,
      ExceptionInfo *exception)
    

A description of each parameter follows.

image

The image.

draw_info

the draw info.

split

when no convenient line breaks-- insert newline.

metrics

Return the font metrics in this structure.

caption

the caption.

exception

return any errors or warnings in this structure.

## [GetMultilineTypeMetrics](http://www.imagemagick.org/api/MagickCore/annotate_8c.html)

GetMultilineTypeMetrics() returns the following information for the specified font and text:
    
    
        character width
        character height
        ascender
        descender
        text width
        text height
        maximum horizontal advance
        bounds: x1
        bounds: y1
        bounds: x2
        bounds: y2
        origin: x
        origin: y
        underline position
        underline thickness
    

This method is like GetTypeMetrics() but it returns the maximum text width and height for multiple lines of text.

The format of the GetMultilineTypeMetrics method is:
    
    
    MagickBooleanType GetMultilineTypeMetrics(Image *image,
      const DrawInfo *draw_info,TypeMetric *metrics,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
metrics
    Return the font metrics in this structure. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetTypeMetrics](http://www.imagemagick.org/api/MagickCore/annotate_8c.html)

GetTypeMetrics() returns the following information for the specified font and text:
    
    
        character width
        character height
        ascender
        descender
        text width
        text height
        maximum horizontal advance
        bounds: x1
        bounds: y1
        bounds: x2
        bounds: y2
        origin: x
        origin: y
        underline position
        underline thickness
    

The format of the GetTypeMetrics method is:
    
    
    MagickBooleanType GetTypeMetrics(Image *image,const DrawInfo *draw_info,
      TypeMetric *metrics,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
draw_info
    the draw info. 
    
metrics
    Return the font metrics in this structure. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](annotate.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
