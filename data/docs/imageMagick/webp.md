[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

ImageMagick's WebP image format accepts a plethora of encoding options as detailed below. As an example, suppose you are interested in these options:

  * quality of 50
  * lossless compression



Use this command:
    
    
    convert wizard.png -quality 50 -define webp:lossless=true wizard.webp
    

Here is a complete list of WebP encoding options:

alpha-compression=value | encode the alpha plane: 0 = none, 1 = compressed.  
---|---  
alpha-filtering=value | predictive filtering method for alpha plane: 0=none, 1=fast, 2=best.  
alpha-quality=value | the compression value for alpha compression between 0 and 100. Lossless compression of alpha is achieved using a value of 100, while the lower values result in a lossy compression. The default is 100.  
auto-filter=true, false | when enabled, the algorithm spends additional time optimizing the filtering strength to reach a well-balanced quality.  
emulate-jpeg-size=true, false | return a similar compression to that of JPEG but with less degradation.  
filter-sharpness=value | filter sharpness.  
filter-strength=value | the strength of the deblocking filter, between 0 (no filtering) and 100 (maximum filtering). A value of 0 turns off any filtering. Higher values increase the strength of the filtering process applied after decoding the image. The higher the value, the smoother the image appears. Typical values are usually in the range of 20 to 50.  
filter-type=value | filter type: 0 = simple, 1 = strong  
image-hint=default, photo, picture, graph | the hint about the image type.  
lossless=true, false | encode the image without any loss.  
low-memory=true, false | reduce memory usage.  
method=value | the compression method to use. It controls the trade off between encoding speed and the compressed file size and quality. Possible values range from 0 to 6. Default value is 4. When higher values are utilized, the encoder spends more time inspecting additional encoding possibilities and decide on the quality gain. Lower value might result in faster processing time at the expense of larger file size and lower compression quality.  
preprocessing=value | Choose from: 0=none, 1=segment-smooth, 2=pseudo-random dithering.  
partitions=value | progressive decoding: choose 0 to 3.  
partition-limit=value | Choose 0 for no quality degradation and 100 for maximum degradation.  
pass=value | maximum number of passes to target compression size or PSNR.  
segment=value | Choose from 1 to 4, the maximum numbher of segments to use.  
show-compressed=true, false  
sns-strength=value | the amplitude of the spatial noise shaping. Spatial noise shaping (SNS) refers to a general collection of built-in algorithms used to decide which area of the picture should use relatively less bits, and where else to better transfer these bits. The possible range goes from 0 (algorithm is off) to 100 (the maximal effect). The default value is 80.   
target-size=value | a target size (in bytes) to try and reach for the compressed output. The compressor makes several passes of partial encoding in order to get as close as possible to this target.  
target-psnr=value | desired minimal distortion.  
thread-level=value | enable multi-threaded encoding.  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](webp.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
