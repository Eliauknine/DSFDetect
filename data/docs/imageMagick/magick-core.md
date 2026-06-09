[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

The [MagickCore API](http://nextgen.imagemagick.org/api/MagickCore/index.html) is a low-level interface between the C programming language and the ImageMagick image processing libraries and is recommended for wizard-level programmers only. Unlike the [MagickWand](magick-wand.html) C API which uses only a few opaque types and accessors, with MagickCore you almost exlusively access the structure members directly. A description of the MagickCore public methods are found here:

  * [Initialize or Destroy the ImageMagick Environment](api/magick.html)
  * [Constitute an Image](api/constitute.html)
  * [Composite an Image](api/composite.html)
  * [Image Methods](api/image.html)
  * [Image Channel Methods](api/channel.html)
  * [Count the Colors in an Image](api/color.html)
  * [Colormap Methods](api/colormap.html)
  * [Colorspace Methods](api/colorspace.html)
  * [Image Distortions](api/distort.html)
  * [Dealing with Image Layers](api/layer.html)
  * [Dealing with Image Profiles](api/profile.html)
  * [Reduce the Number of Unique Colors in an Image](api/quantize.html)
  * [Image Histograms](api/histogram.html)
  * [Segment an Image with Thresholding Fuzzy c-Means](api/segment.html)
  * [Resize an Image](api/resize.html)
  * [Transform an Image](api/transform.html)
  * [Shear or Rotate an Image by an Arbitrary Angle](api/shear.html)
  * [Enhance an Image](api/enhance.html)
  * [Add an Effect](api/effect.html)
  * [Morphological Erosions, Dilations, Openings, and Closings](api/morphology.html)
  * [Add a Special Effect](api/fx.html)
  * [Decorate an Image](api/decorate.html)
  * [Get/Set an Image Attribute](api/attribute.html)
  * [Get/Set Image Properties](api/property.html)
  * [Get Image Statistics](api/statistic.html)
  * [Get Image Features](api/feature.html)
  * [Annotate an Image](api/annotate.html)
  * [Paint on an Image](api/paint.html)
  * [Draw on an Image](api/draw.html)
  * [Create an Image Thumbnail](api/montage.html)
  * [Compute the discrete Fourier transform (DFT)](api/fourier.html)
  * [Compare an Image to a Reconstructed Image](api/compare.html)
  * [Interactively Display and Edit an Image](api/display.html)
  * [Interactively Animate an Image Sequence](api/animate.html)
  * [Convert to and from Cipher Pixels](api/cipher.html)
  * [Working with Image Lists](api/list.html)
  * [Image View Methods](api/image-view.html)
  * [Get or Set Image Pixels](api/cache.html)
  * [Working with Cache Views](api/cache-view.html)
  * [The Pixel FIFO](api/stream.html)
  * [Read or Write Binary Large OBjects](api/blob.html)
  * [Loadable Modules](api/module.html)
  * [Compute a Message Digest for an Image](api/signature.html)
  * [The Image Registry](api/registry.html)
  * [Dealing with Exceptions](api/exception.html)
  * [Memory Allocation](api/memory.html)
  * [Monitor or Limit Resource Consumption](api/resource.html)
  * [Monitor the Progress of an Image Operation](api/monitor.html)
  * [Get the Version and Copyrights](api/version.html)
  * [Mime Methods](api/mime.html)
  * [Deprecated Methods](api/deprecate.html)
  * [Error and Warning Codes](exception.html)



After you write your MagickCore program, compile it like this:
    
    
    cc -o core core.c `pkg-config --cflags --libs MagickCore`
    

Note, if your instance of ImageMagick does not support modules but does include support for the WMF image format, you'll need to link with the [MagickWand](magick-wand.html) library instead (since it is a dependency of the WMF image format):
    
    
    cc -o core core.c `pkg-config --cflags --libs MagickWand`
    

Set the `PKG_CONFIG_PATH` environment variable if ImageMagick is not in your default system path:
    
    
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
    

Here is a example program that utilizes the MagickCore API to get you started, [core.c](../source/core.c). It reads a GIF image, creates a thumbnail, and writes it to disk in the PNG image format.
    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <time.h>
    #include <magick/MagickCore.h>
    
    int main(int argc,char **argv)
    {
      ExceptionInfo
        *exception;
    
      Image
        *image,
        *images,
        *resize_image,
        *thumbnails;
    
      ImageInfo
        *image_info;
    
      if (argc != 3)
        {
          (void) fprintf(stdout,"Usage: %s image thumbnail\n",argv[0]);
          exit(0);
        }
      /*
        Initialize the image info structure and read an image.
      */
      MagickCoreGenesis(*argv,MagickTrue);
      exception=AcquireExceptionInfo();
      image_info=CloneImageInfo((ImageInfo *) NULL);
      (void) strcpy(image_info->filename,argv[1]);
      images=ReadImage(image_info,exception);
      if (exception->severity != UndefinedException)
        CatchException(exception);
      if (images == (Image *) NULL)
        exit(1);
      /*
        Convert the image to a thumbnail.
      */
      thumbnails=NewImageList();
      while ((image=RemoveFirstImageFromList(&images)) != (Image *) NULL)
      {
        resize_image=ResizeImage(image,106,80,LanczosFilter,1.0,exception);
        if (resize_image == (Image *) NULL)
          MagickError(exception->severity,exception->reason,exception->description);
        (void) AppendImageToList(&thumbnails,resize_image);
        DestroyImage(image);
      }
      /*
        Write the image thumbnail.
      */
      (void) strcpy(thumbnails->filename,argv[2]);
      WriteImage(image_info,thumbnails);
      /*
        Destroy the image thumbnail and exit.
      */
      thumbnails=DestroyImageList(thumbnails);
      image_info=DestroyImageInfo(image_info);
      exception=DestroyExceptionInfo(exception);
      MagickCoreTerminus();
      return(0);
    }

Now lets perform the same contrast enhancement while taking advantage of our dual or quad-core processing system by running the algorithm in parallel utilizing wand views. The [sigmoidal-contrast.c](../source/core/sigmoidal-contrast.c) module reads an image, applies sigmoidal non-linearity contrast control, and writes the result to disk just like the previous contrast enhancement program, but now it does its work in parallel (assumes ImageMagick is built with OpenMP support).
    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <math.h>
    #include <magick/MagickCore.h>
    
    static MagickBooleanType SigmoidalContrast(ImageView *contrast_view,
      const ssize_t y,const int id,void *context)
    {
    #define QuantumScale  ((MagickRealType) 1.0/(MagickRealType) QuantumRange)
    #define SigmoidalContrast(x) \
      (QuantumRange*(1.0/(1+exp(10.0*(0.5-QuantumScale*x)))-0.0066928509)*1.0092503)
    
      RectangleInfo
        extent;
    
      register IndexPacket
        *indexes;
    
      register PixelPacket
        *pixels;
    
      register ssize_t
        x;
    
      extent=GetImageViewExtent(contrast_view);
      pixels=GetImageViewAuthenticPixels(contrast_view);
      for (x=0; x < (ssize_t) (extent.width-extent.x); x++)
      {
        SetPixelRed(pixels,RoundToQuantum(SigmoidalContrast(GetPixelRed(pixels)));
        SetPixelGreen(pixels,RoundToQuantum(SigmoidalContrast(GetPixelGreen(pixels)));
        SetPixelBlue(pixels,RoundToQuantum(SigmoidalContrast(GetPixelBlue(pixels)));
        SetPixelOpacity(pixels,RoundToQuantum(SigmoidalContrast(GetPixelOpacity(pixels)));
        pixels++;
      }
      indexes=GetImageViewAuthenticIndexes(contrast_view);
      if (indexes != (IndexPacket *) NULL)
        for (x=0; x < (ssize_t) (extent.width-extent.x); x++)
          SetPixelIndex(indexes+x,RoundToQuantum(SigmoidalContrast(GetPixelIndex(indexes+x))));
      return(MagickTrue);
    }
    
    int main(int argc,char **argv)
    {
    #define ThrowImageException(image) \
    { \
     \
      CatchException(exception); \
      if (contrast_image != (Image *) NULL) \
        contrast_image=DestroyImage(contrast_image); \
      exit(-1); \
    }
    #define ThrowViewException(view) \
    { \
      char \
        *description; \
     \
      ExceptionType \
        severity; \
     \
      description=GetImageViewException(view,&severity); \
      (void) fprintf(stderr,"%s %s %lu %s\n",GetMagickModule(),description); \
      description=DestroyString(description); \
      exit(-1); \
    }
    
      ExceptionInfo
        *exception;
    
      Image
        *contrast_image;
    
      ImageInfo
        *image_info;
    
      ImageView
        *contrast_view;
    
      MagickBooleanType
        status;
    
      if (argc != 3)
        {
          (void) fprintf(stdout,"Usage: %s image sigmoidal-image\n",argv[0]);
          exit(0);
        }
      /*
        Read an image.
      */
      MagickCoreGenesis(*argv,MagickTrue);
      image_info=AcquireImageInfo();
      (void) CopyMagickString(image_info->filename,argv[1],MaxTextExtent);
      exception=AcquireExceptionInfo();
      contrast_image=ReadImage(image_info,exception);
      if (contrast_image == (Image *) NULL)
        ThrowImageException(contrast_image);
      /*
        Sigmoidal non-linearity contrast control.
      */
      contrast_view=NewImageView(contrast_image);
      if (contrast_view == (ImageView *) NULL)
        ThrowImageException(contrast_image);
      status=UpdateImageViewIterator(contrast_view,SigmoidalContrast,(void *) NULL);
      if (status == MagickFalse)
        ThrowImageException(contrast_image);
      contrast_view=DestroyImageView(contrast_view);
      /*
        Write the image then destroy it.
      */
      status=WriteImages(image_info,contrast_image,argv[2],exception);
      if (status == MagickFalse)
        ThrowImageException(contrast_image);
      contrast_image=DestroyImage(contrast_image);
      exception=DestroyExceptionInfo(exception);
      image_info=DestroyImageInfo(image_info);
      MagickCoreTerminus();
      return(0);
    }

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](magick-core.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
