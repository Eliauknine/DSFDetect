[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[CoalesceImages](layer.html#CoalesceImages) • [DisposeImages](layer.html#DisposeImages) • [CompareImagesLayers](layer.html#CompareImagesLayers) • [OptimizeImageLayers](layer.html#OptimizeImageLayers) • [OptimizeImagePlusLayers](layer.html#OptimizeImagePlusLayers) • [OptimizeImageTransparency](layer.html#OptimizeImageTransparency) • [RemoveDuplicateLayers](layer.html#RemoveDuplicateLayers) • [RemoveZeroDelayLayers](layer.html#RemoveZeroDelayLayers) • [CompositeLayers](layer.html#CompositeLayers) • [MergeImageLayers](layer.html#MergeImageLayers)

## [CoalesceImages](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

CoalesceImages() composites a set of images while respecting any page offsets and disposal methods. GIF, MIFF, and MNG animation sequences typically start with an image background and each subsequent image varies in size and offset. A new image sequence is returned with all images the same size as the first images virtual canvas and composited with the next image in the sequence.

The format of the CoalesceImages method is:
    
    
    Image *CoalesceImages(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image sequence. 
    
exception
    return any errors or warnings in this structure. 
    

## [DisposeImages](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

DisposeImages() returns the coalesced frames of a GIF animation as it would appear after the GIF dispose method of that frame has been applied. That is it returned the appearance of each frame before the next is overlaid.

The format of the DisposeImages method is:
    
    
    Image *DisposeImages(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
exception
    return any errors or warnings in this structure. 
    

## [CompareImagesLayers](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

CompareImagesLayers() compares each image with the next in a sequence and returns the minimum bounding region of all the pixel differences (of the LayerMethod specified) it discovers.

Images do NOT have to be the same size, though it is best that all the images are 'coalesced' (images are all the same size, on a flattened canvas, so as to represent exactly how an specific frame should look).

No GIF dispose methods are applied, so GIF animations must be coalesced before applying this image operator to find differences to them.

The format of the CompareImagesLayers method is:
    
    
    Image *CompareImagesLayers(const Image *images,
      const LayerMethod method,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
method
    the layers type to compare images with. Must be one of... CompareAnyLayer, CompareClearLayer, CompareOverlayLayer. 
    
exception
    return any errors or warnings in this structure. 
    

## [OptimizeImageLayers](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

OptimizeImageLayers() compares each image the GIF disposed forms of the previous image in the sequence. From this it attempts to select the smallest cropped image to replace each frame, while preserving the results of the GIF animation.

The format of the OptimizeImageLayers method is:
    
    
    Image *OptimizeImageLayers(const Image *image,
             ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [OptimizeImagePlusLayers](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

OptimizeImagePlusLayers() is exactly as OptimizeImageLayers(), but may also add or even remove extra frames in the animation, if it improves the total number of pixels in the resulting GIF animation.

The format of the OptimizePlusImageLayers method is:
    
    
    Image *OptimizePlusImageLayers(const Image *image,
             ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
exception
    return any errors or warnings in this structure. 
    

## [OptimizeImageTransparency](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

OptimizeImageTransparency() takes a frame optimized GIF animation, and compares the overlayed pixels against the disposal image resulting from all the previous frames in the animation. Any pixel that does not change the disposal image (and thus does not effect the outcome of an overlay) is made transparent.

WARNING: This modifies the current images directly, rather than generate a new image sequence.

The format of the OptimizeImageTransperency method is:
    
    
    void OptimizeImageTransperency(Image *image,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image sequence 
    
exception
    return any errors or warnings in this structure. 
    

## [RemoveDuplicateLayers](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

RemoveDuplicateLayers() removes any image that is exactly the same as the next image in the given image list. Image size and virtual canvas offset must also match, though not the virtual canvas size itself.

No check is made with regards to image disposal setting, though it is the dispose setting of later image that is kept. Also any time delays are also added together. As such coalesced image animations should still produce the same result, though with duplicte frames merged into a single frame.

The format of the RemoveDuplicateLayers method is:
    
    
    void RemoveDuplicateLayers(Image **image, ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image list 
    
exception
    return any errors or warnings in this structure. 
    

## [RemoveZeroDelayLayers](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

RemoveZeroDelayLayers() removes any image that as a zero delay time. Such images generally represent intermediate or partial updates in GIF animations used for file optimization. They are not ment to be displayed to users of the animation. Viewable images in an animation should have a time delay of 3 or more centi-seconds (hundredths of a second).

However if all the frames have a zero time delay, then either the animation is as yet incomplete, or it is not a GIF animation. This a non-sensible situation, so no image will be removed and a 'Zero Time Animation' warning (exception) given.

No warning will be given if no image was removed because all images had an appropriate non-zero time delay set.

Due to the special requirements of GIF disposal handling, GIF animations should be coalesced first, before calling this function, though that is not a requirement.

The format of the RemoveZeroDelayLayers method is:
    
    
    void RemoveZeroDelayLayers(Image **image, ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image list 
    
exception
    return any errors or warnings in this structure. 
    

## [CompositeLayers](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

CompositeLayers() compose the source image sequence over the destination image sequence, starting with the current image in both lists.

Each layer from the two image lists are composted together until the end of one of the image lists is reached. The offset of each composition is also adjusted to match the virtual canvas offsets of each layer. As such the given offset is relative to the virtual canvas, and not the actual image.

Composition uses given x and y offsets, as the 'origin' location of the source images virtual canvas (not the real image) allowing you to compose a list of 'layer images' into the destiantioni images. This makes it well sutiable for directly composing 'Clears Frame Animations' or 'Coaleased Animations' onto a static or other 'Coaleased Animation' destination image list. GIF disposal handling is not looked at.

Special case:- If one of the image sequences is the last image (just a single image remaining), that image is repeatally composed with all the images in the other image list. Either the source or destination lists may be the single image, for this situation.

In the case of a single destination image (or last image given), that image will ve cloned to match the number of images remaining in the source image list.

This is equivelent to the "-layer Composite" Shell API operator.

The format of the CompositeLayers method is:
    
    
    void CompositeLayers(Image *destination, const CompositeOperator
    compose, Image *source, const ssize_t x_offset, const ssize_t y_offset,
    ExceptionInfo *exception);
    

A description of each parameter follows:

    
    

destination
    the destination images and results 
    
source
    source image(s) for the layer composition 
    
compose, x_offset, y_offset
     arguments passed on to CompositeImages() 
    
exception
    return any errors or warnings in this structure. 
    

## [MergeImageLayers](http://www.imagemagick.org/api/MagickCore/layer_8c.html)

MergeImageLayers() composes all the image layers from the current given image onward to produce a single image of the merged layers.

The inital canvas's size depends on the given LayerMethod, and is initialized using the first images background color. The images are then compositied onto that image in sequence using the given composition that has been assigned to each individual image.

The format of the MergeImageLayers is:
    
    
    Image *MergeImageLayers(const Image *image,
      const LayerMethod method, ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image list to be composited together 
    
method
    the method of selecting the size of the initial canvas. 
     MergeLayer: Merge all layers onto a canvas just large enough to hold all the actual images. The virtual canvas of the first image is preserved but otherwise ignored. 
     FlattenLayer: Use the virtual canvas size of first image. Images which fall outside this canvas is clipped. This can be used to 'fill out' a given virtual canvas. 
     MosaicLayer: Start with the virtual canvas of the first image, enlarging left and right edges to contain all images. Images with negative offsets will be clipped. 
     TrimBoundsLayer: Determine the overall bounds of all the image layers just as in "MergeLayer", then adjust the the canvas and offsets to be relative to those bounds, without overlaying the images. 
     WARNING: a new image is not returned, the original image sequence page data is modified instead. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](layer.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
