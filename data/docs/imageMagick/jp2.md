[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

ImageMagick's JPEG-2000 image formats, JP2 and JPC, accept a plethora of encoding options as detailed below. As an example, suppose you are interested in these options:

  * code blocks are 64 samples in width and 32 samples in height
  * no multicomponent transform
  * 4 resolution levels for each component
  * compression is lossy at 64:1



Use this command to convert a JPEG-2000 image to the PNG image format:
    
    
    convert wizard.jp2 wizard.png
    

Let's convert a JPEG image to a lossless JPEG-2000 image:
    
    
    convert wizard.jpg -quality 0 wizard.jp2
    

Here we extract an area from the image:
    
    
    convert 'wizard.jp2[640x480+0+0]' wizard.png
    

Extract a particular tile from the image:
    
    
    convert 'wizard.jp2[2]' wizard.png
    

Specify a subsampling factor:
    
    
    convert wizard.png -colorspace YUV -sampling-factor 2,2 wizard.jp2
    

Save a tiled JPEG-2000 image:
    
    
    convert wizard.png 'wizard.png[512x512]'
    

Write a digital Cinema 4K profile compliant codestream:
    
    
    convert wizard.png -resize 4096x2160! -depth 12 wizard.jp2
    

Here is a complete list of JPEG-2000 decoding options:

jp2:layer-number=x | set the maximum number of quality layers to decode.  
---|---  
jp2:reduce-factor=x | set the number of highest resolution levels to be discarded.  
  
Here is a complete list of JPEG-2000 encoding options:

jp2:number-resolutions=x
    number of resolutions to encode.  
jp2:quality=x,x,... | set the quality layer PSNR, given in dB. The order is from left to right in ascending order. The default is a single lossless quality layer.  
jp2:rate=x,x,... | the compression ratio values. Each value is a factor of compression, thus 20 means 20 times compressed. The order is from left to right in descending order. A final lossless quality layer is signified by the value 1. The default is a single lossless quality layer.  
jp2:progression-order=x | choose from LRCP, RLCP, RPCL, PCRL or CPRL.  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](jp2.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
