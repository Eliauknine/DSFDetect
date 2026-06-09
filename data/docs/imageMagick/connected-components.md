[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

Connected-component labeling (alternatively connected-component analysis, blob extraction, region labeling, blob discovery, or region extraction) uniquely labels connected components in an image. The labeling process scans the image, pixel-by-pixel from top-left to bottom-right, in order to identify connected pixel regions, i.e. regions of adjacent pixels which share the same set of intensity values. For example, let's find the objects in this image:

[![purse](../images/objects.gif)](../images/objects.gif) 


To identify the objects in this image, use this command:
    
    
    convert objects.gif -connected-components 4 -auto-level -depth 8 objects.png
    

The detected objects are uniquely labeled. Use auto leveling to visualize the detected objects:

[![Objects](../images/objects.png)](../images/objects.png) 


Object statistics is useful to review. To display them, use this command:
    
    
    convert objects.gif -define connected-components:verbose=true -connected-components 4 objects.png
    

Five objects were detected in the source image with these statistics:
    
    
    Objects (id: bounding-box centroid area mean-color):
      0: 256x171+0+0 119.2,80.8 33117 srgb(0,0,0)
      2: 120x135+104+18 159.5,106.5 8690 srgb(255,255,255)
      3: 50x36+129+44 154.2,63.4 1529 srgb(0,0,0)
      4: 21x23+0+45 8.8,55.9 409 srgb(255,255,255)
      1: 4x10+252+0 253.9,4.1 31 srgb(255,255,255)
    

Use `-connected-components 8` to visit 8 neighbors rather than 4. By default, neighbor colors must be exact to be part of a unique object. Use the [-fuzz](command-line-options.html#fuzz) option to include pixels as part of an object that are close in color.

You might want to eliminate small objects by merging them with their larger neighbors. If so, use this command:
    
    
    convert objects.gif -define connected-components:area-threshold=410 -connected-components 4 \
      -auto-level objects.jpg
    

Here are the expected results. Notice, how the small objects are now merged with the background.

[![Objects](../images/objects.jpg)](../images/objects.jpg) 


Notice how two of the objects were merged leaving three remaining objects:
    
    
    Objects (id: bounding-box centroid area mean-color):
      0: 256x171+0+0 118.0,80.4 33557 srgb(0,0,0)
      2: 120x135+104+18 159.5,106.5 8690 srgb(255,255,255)
      3: 50x36+129+44 154.2,63.4 1529 srgb(0,0,0)
    

By default, the labeled image is grayscale. You can instead replace the object color in the labeled image with the mean-color from the source image. Simply add this setting, `-define connected-components:mean-color=true`, to your command line.

You may want to remove certain objects by making them transparent. Use `-define connected-components:remove=_list-of-ids_` (e.g. -define connected-components:remove=2,4-5). Or use `-define connected-components:keep=_list-of-ids_` to keep these objects and make all others transparent.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](connected-components.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
