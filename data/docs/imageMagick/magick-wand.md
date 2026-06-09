[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

The [MagickWand API](http://nextgen.imagemagick.org/api/MagickWand/index.html) is the recommended interface between the C programming language and the ImageMagick image processing libraries. Unlike the [MagickCore](magick-core.html) C API, MagickWand uses only a few opaque types. Accessors are available to set or get important wand properties. A description of the MagickWand public methods are found here:

  * [Magick Wand Methods](api/magick-wand.html)
  * [Set or Get Magick Wand Properties](api/magick-property.html)
  * [Magick Wand Image Methods](api/magick-image.html)
  * [Pixel Iterator Methods](api/pixel-iterator.html)
  * [Pixel Wand Methods](api/pixel-wand.html)
  * [Image Vector Drawing](api/drawing-wand.html)
  * [Command-line Interface](api/mogrify.html)
  * [Wand View Methods](api/wand-view.html)
  * [Deprecated Methods](api/magick-deprecate.html)
  * [Error and Warning Codes](exception.html)



After you write your MagickWand program, compile it like this:
    
    
    cc -o wand wand.c `pkg-config --cflags --libs MagickWand`
    

Set the `PKG_CONFIG_PATH` environment variable if ImageMagick is not in your default system path:
    
    
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
    

Here is a example program that utilizes the MagickWand API to get you started, [wand.c](../source/wand.c). It reads an image, creates a thumbnail, and writes the result to disk.
    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <wand/MagickWand.h>
    
    int main(int argc,char **argv)
    {
    #define ThrowWandException(wand) \
    { \
      char \
        *description; \
     \
      ExceptionType \
        severity; \
     \
      description=MagickGetException(wand,&severity); \
      (void) fprintf(stderr,"%s %s %lu %s\n",GetMagickModule(),description); \
      description=(char *) MagickRelinquishMemory(description); \
      exit(-1); \
    }
    
      MagickBooleanType
        status;
    
      MagickWand
        *magick_wand;
    
      if (argc != 3)
        {
          (void) fprintf(stdout,"Usage: %s image thumbnail\n",argv[0]);
          exit(0);
        }
      /*
        Read an image.
      */
      MagickWandGenesis();
      magick_wand=NewMagickWand();
      status=MagickReadImage(magick_wand,argv[1]);
      if (status == MagickFalse)
        ThrowWandException(magick_wand);
      /*
        Turn the images into a thumbnail sequence.
      */
      MagickResetIterator(magick_wand);
      while (MagickNextImage(magick_wand) != MagickFalse)
        MagickResizeImage(magick_wand,106,80,LanczosFilter,1.0);
      /*
        Write the image then destroy it.
      */
      status=MagickWriteImages(magick_wand,argv[2],MagickTrue);
      if (status == MagickFalse)
        ThrowWandException(magick_wand);
      magick_wand=DestroyMagickWand(magick_wand);
      MagickWandTerminus();
      return(0);
    }
    

Here is another program that shows one way to get and set image pixels with the MagickWand API, [contrast.c](../source/contrast.c). It reads an image, applies sigmoidal non-linearity contrast control, and writes the result to disk.
    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <math.h>
    #include <wand/MagickWand.h>
    
    int main(int argc,char **argv)
    {
    #define QuantumScale  ((MagickRealType) 1.0/(MagickRealType) QuantumRange)
    #define SigmoidalContrast(x) \
      (QuantumRange*(1.0/(1+exp(10.0*(0.5-QuantumScale*x)))-0.0066928509)*1.0092503)
    #define ThrowWandException(wand) \
    { \
      char \
        *description; \
     \
      ExceptionType \
        severity; \
     \
      description=MagickGetException(wand,&severity); \
      (void) fprintf(stderr,"%s %s %lu %s\n",GetMagickModule(),description); \
      description=(char *) MagickRelinquishMemory(description); \
      exit(-1); \
    }
    
      long
        y;
    
      MagickBooleanType
        status;
    
      MagickPixelPacket
        pixel;
    
      MagickWand
        *contrast_wand,
        *image_wand;
    
      PixelIterator
        *contrast_iterator,
        *iterator;
    
      PixelWand
        **contrast_pixels,
        **pixels;
    
      register long
        x;
    
      unsigned long
        width;
    
      if (argc != 3)
        {
          (void) fprintf(stdout,"Usage: %s image sigmoidal-image\n",argv[0]);
          exit(0);
        }
      /*
        Read an image.
      */
      MagickWandGenesis();
      image_wand=NewMagickWand();
      status=MagickReadImage(image_wand,argv[1]);
      if (status == MagickFalse)
        ThrowWandException(image_wand);
      contrast_wand=CloneMagickWand(image_wand);
      /*
        Sigmoidal non-linearity contrast control.
      */
      iterator=NewPixelIterator(image_wand);
      contrast_iterator=NewPixelIterator(contrast_wand);
      if ((iterator == (PixelIterator *) NULL) ||
          (contrast_iterator == (PixelIterator *) NULL))
        ThrowWandException(image_wand);
      for (y=0; y < (long) MagickGetImageHeight(image_wand); y++)
      {
        pixels=PixelGetNextIteratorRow(iterator,&width);
        contrast_pixels=PixelGetNextIteratorRow(contrast_iterator,&width);
        if ((pixels == (PixelWand **) NULL) ||
            (contrast_pixels == (PixelWand **) NULL))
          break;
        for (x=0; x < (long) width; x++)
        {
          PixelGetMagickColor(pixels[x],&pixel);
          pixel.red=SigmoidalContrast(pixel.red);
          pixel.green=SigmoidalContrast(pixel.green);
          pixel.blue=SigmoidalContrast(pixel.blue);
          pixel.index=SigmoidalContrast(pixel.index);
          PixelSetMagickColor(contrast_pixels[x],&pixel);
        }
        (void) PixelSyncIterator(contrast_iterator);
      }
      if (y < (long) MagickGetImageHeight(image_wand))
        ThrowWandException(image_wand);
      contrast_iterator=DestroyPixelIterator(contrast_iterator);
      iterator=DestroyPixelIterator(iterator);
      image_wand=DestroyMagickWand(image_wand);
      /*
        Write the image then destroy it.
      */
      status=MagickWriteImages(contrast_wand,argv[2],MagickTrue);
      if (status == MagickFalse)
        ThrowWandException(image_wand);
      contrast_wand=DestroyMagickWand(contrast_wand);
      MagickWandTerminus();
      return(0);
    }
    

Now lets perform the same contrast enhancement while taking advantage of our dual or quad-core processing system by running the algorithm in parallel utilizing wand views. The [sigmoidal-contrast.c](../source/wand/sigmoidal-contrast.c) module reads an image, applies sigmoidal non-linearity contrast control, and writes the result to disk just like the previous contrast enhancement program, but now it does its work in parallel (assumes ImageMagick is built with OpenMP support).
    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <math.h>
    #include <wand/MagickWand.h>
    
    static MagickBooleanType SigmoidalContrast(WandView *pixel_view,
      const ssize_t y,const int id,void *context)
    {
    #define QuantumScale  ((MagickRealType) 1.0/(MagickRealType) QuantumRange)
    #define SigmoidalContrast(x) \
      (QuantumRange*(1.0/(1+exp(10.0*(0.5-QuantumScale*x)))-0.0066928509)*1.0092503)
    
      RectangleInfo
        extent;
    
      MagickPixelPacket
        pixel;
    
      PixelWand
        **pixels;
    
      register long
        x;
    
      extent=GetWandViewExtent(contrast_view);
      pixels=GetWandViewPixels(contrast_view);
      for (x=0; x < (long) (extent.width-extent.height); x++)
      {
        PixelGetMagickColor(pixels[x],&pixel);
        pixel.red=SigmoidalContrast(pixel.red);
        pixel.green=SigmoidalContrast(pixel.green);
        pixel.blue=SigmoidalContrast(pixel.blue);
        pixel.index=SigmoidalContrast(pixel.index);
        PixelSetMagickColor(contrast_pixels[x],&pixel);
      }
      return(MagickTrue);
    }
    
    int main(int argc,char **argv)
    {
    #define ThrowViewException(view) \
    { \
      description=GetWandViewException(view,&severity); \
      (void) fprintf(stderr,"%s %s %lu %s\n",GetMagickModule(),description); \
      description=(char *) MagickRelinquishMemory(description); \
      exit(-1); \
    }
    #define ThrowWandException(wand) \
    { \
      description=MagickGetException(wand,&severity); \
      (void) fprintf(stderr,"%s %s %lu %s\n",GetMagickModule(),description); \
      description=(char *) MagickRelinquishMemory(description); \
      exit(-1); \
    }
    
      char
        *description;
    
      ExceptionType
        severity;
    
      MagickBooleanType
        status;
    
      MagickPixelPacket
        pixel;
    
      MagickWand
        *contrast_wand;
    
      WandView
        *contrast_view;
    
      if (argc != 3)
        {
          (void) fprintf(stdout,"Usage: %s image sigmoidal-image\n",argv[0]);
          exit(0);
        }
      /*
        Read an image.
      */
      MagickWandGenesis();
      contrast_wand=NewMagickWand();
      status=MagickReadImage(contrast_wand,argv[1]);
      if (status == MagickFalse)
        ThrowWandException(contrast_wand);
      /*
        Sigmoidal non-linearity contrast control.
      */
      contrast_view=NewWandView(contrast_wand);
      if (contrast_view == (WandView *) NULL)
        ThrowWandException(contrast_wand);
      status=UpdateWandViewIterator(contrast_view,SigmoidalContrast,(void *) NULL);
      if (status == MagickFalse)
        ThrowWandException(contrast_wand);
      contrast_view=DestroyWandView(contrast_view);
      /*
        Write the image then destroy it.
      */
      status=MagickWriteImages(contrast_wand,argv[2],MagickTrue);
      if (status == MagickFalse)
        ThrowWandException(contrast_wand);
      contrast_wand=DestroyMagickWand(contrast_wand);
      MagickWandTerminus();
      return(0);
    }
    

[MagickWand Examples in C](http://members.shaw.ca/el.supremo/MagickWand/) illustrates how to use the ImageMagick MagickWand API. Each example is presented as a C function, complete with headers, so that it can be copied to a file and then included in your own C project.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](magick-wand.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
