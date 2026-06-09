[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[ClearPixelWand](pixel-wand.html#ClearPixelWand) • [ClonePixelWand](pixel-wand.html#ClonePixelWand) • [ClonePixelWands](pixel-wand.html#ClonePixelWands) • [DestroyPixelWand](pixel-wand.html#DestroyPixelWand) • [DestroyPixelWands](pixel-wand.html#DestroyPixelWands) • [IsPixelWandSimilar](pixel-wand.html#IsPixelWandSimilar) • [IsPixelWand](pixel-wand.html#IsPixelWand) • [NewPixelWand](pixel-wand.html#NewPixelWand) • [NewPixelWands](pixel-wand.html#NewPixelWands) • [PixelClearException](pixel-wand.html#PixelClearException) • [PixelGetAlpha](pixel-wand.html#PixelGetAlpha) • [PixelGetAlphaQuantum](pixel-wand.html#PixelGetAlphaQuantum) • [PixelGetBlack](pixel-wand.html#PixelGetBlack) • [PixelGetBlackQuantum](pixel-wand.html#PixelGetBlackQuantum) • [PixelGetBlue](pixel-wand.html#PixelGetBlue) • [PixelGetBlueQuantum](pixel-wand.html#PixelGetBlueQuantum) • [PixelGetColorAsString](pixel-wand.html#PixelGetColorAsString) • [PixelGetColorAsNormalizedString](pixel-wand.html#PixelGetColorAsNormalizedString) • [PixelGetColorCount](pixel-wand.html#PixelGetColorCount) • [PixelGetCyan](pixel-wand.html#PixelGetCyan) • [PixelGetCyanQuantum](pixel-wand.html#PixelGetCyanQuantum) • [PixelGetException](pixel-wand.html#PixelGetException) • [PixelGetExceptionType](pixel-wand.html#PixelGetExceptionType) • [PixelGetFuzz](pixel-wand.html#PixelGetFuzz) • [PixelGetGreen](pixel-wand.html#PixelGetGreen) • [PixelGetGreenQuantum](pixel-wand.html#PixelGetGreenQuantum) • [PixelGetHSL](pixel-wand.html#PixelGetHSL) • [PixelGetIndex](pixel-wand.html#PixelGetIndex) • [PixelGetMagenta](pixel-wand.html#PixelGetMagenta) • [PixelGetMagentaQuantum](pixel-wand.html#PixelGetMagentaQuantum) • [PixelGetMagickColor](pixel-wand.html#PixelGetMagickColor) • [PixelGetPixel](pixel-wand.html#PixelGetPixel) • [PixelGetQuantumPacket](pixel-wand.html#PixelGetQuantumPacket) • [PixelGetQuantumPixel](pixel-wand.html#PixelGetQuantumPixel) • [PixelGetRed](pixel-wand.html#PixelGetRed) • [PixelGetRedQuantum](pixel-wand.html#PixelGetRedQuantum) • [PixelGetYellow](pixel-wand.html#PixelGetYellow) • [PixelGetYellowQuantum](pixel-wand.html#PixelGetYellowQuantum) • [PixelSetAlpha](pixel-wand.html#PixelSetAlpha) • [PixelSetAlphaQuantum](pixel-wand.html#PixelSetAlphaQuantum) • [PixelSetBlack](pixel-wand.html#PixelSetBlack) • [PixelSetBlackQuantum](pixel-wand.html#PixelSetBlackQuantum) • [PixelSetBlue](pixel-wand.html#PixelSetBlue) • [PixelSetBlueQuantum](pixel-wand.html#PixelSetBlueQuantum) • [PixelSetColor](pixel-wand.html#PixelSetColor) • [PixelSetColorCount](pixel-wand.html#PixelSetColorCount) • [PixelSetColorFromWand](pixel-wand.html#PixelSetColorFromWand) • [PixelSetCyan](pixel-wand.html#PixelSetCyan) • [PixelSetCyanQuantum](pixel-wand.html#PixelSetCyanQuantum) • [PixelSetFuzz](pixel-wand.html#PixelSetFuzz) • [PixelSetGreen](pixel-wand.html#PixelSetGreen) • [PixelSetGreenQuantum](pixel-wand.html#PixelSetGreenQuantum) • [PixelSetHSL](pixel-wand.html#PixelSetHSL) • [PixelSetIndex](pixel-wand.html#PixelSetIndex) • [PixelSetMagenta](pixel-wand.html#PixelSetMagenta) • [PixelSetMagentaQuantum](pixel-wand.html#PixelSetMagentaQuantum) • [PixelSetPixelColor](pixel-wand.html#PixelSetPixelColor) • [PixelSetQuantumPixel](pixel-wand.html#PixelSetQuantumPixel) • [PixelSetRed](pixel-wand.html#PixelSetRed) • [PixelSetRedQuantum](pixel-wand.html#PixelSetRedQuantum) • [PixelSetYellow](pixel-wand.html#PixelSetYellow) • [PixelSetYellowQuantum](pixel-wand.html#PixelSetYellowQuantum)

## [ClearPixelWand](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

ClearPixelWand() clears resources associated with the wand.

The format of the ClearPixelWand method is:
    
    
    void ClearPixelWand(PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [ClonePixelWand](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

ClonePixelWand() makes an exact copy of the specified wand.

The format of the ClonePixelWand method is:
    
    
    PixelWand *ClonePixelWand(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [ClonePixelWands](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

ClonePixelWands() makes an exact copy of the specified wands.

The format of the ClonePixelWands method is:
    
    
    PixelWand **ClonePixelWands(const PixelWand **wands,
      const size_t number_wands)
    

A description of each parameter follows:

    
    

wands
    the magick wands. 
    
number_wands
    the number of wands. 
    

## [DestroyPixelWand](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

DestroyPixelWand() deallocates resources associated with a PixelWand.

The format of the DestroyPixelWand method is:
    
    
    PixelWand *DestroyPixelWand(PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [DestroyPixelWands](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

DestroyPixelWands() deallocates resources associated with an array of pixel wands.

The format of the DestroyPixelWands method is:
    
    
    PixelWand **DestroyPixelWands(PixelWand **wand,
      const size_t number_wands)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
number_wands
    the number of wands. 
    

## [IsPixelWandSimilar](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

IsPixelWandSimilar() returns MagickTrue if the distance between two colors is less than the specified distance.

The format of the IsPixelWandSimilar method is:
    
    
    MagickBooleanType IsPixelWandSimilar(PixelWand *p,PixelWand *q,
      const double fuzz)
    

A description of each parameter follows:

    
    

p
    the pixel wand. 
    
q
    the pixel wand. 
    
fuzz
    any two colors that are less than or equal to this distance squared are consider similar. 
    

## [IsPixelWand](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

IsPixelWand() returns MagickTrue if the wand is verified as a pixel wand.

The format of the IsPixelWand method is:
    
    
    MagickBooleanType IsPixelWand(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [NewPixelWand](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

NewPixelWand() returns a new pixel wand.

The format of the NewPixelWand method is:
    
    
    PixelWand *NewPixelWand(void)
    

## [NewPixelWands](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

NewPixelWands() returns an array of pixel wands.

The format of the NewPixelWands method is:
    
    
    PixelWand **NewPixelWands(const size_t number_wands)
    

A description of each parameter follows:

    
    

number_wands
    the number of wands. 
    

## [PixelClearException](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelClearException() clear any exceptions associated with the iterator.

The format of the PixelClearException method is:
    
    
    MagickBooleanType PixelClearException(PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetAlpha](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetAlpha() returns the normalized alpha value of the pixel wand.

The format of the PixelGetAlpha method is:
    
    
    double PixelGetAlpha(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetAlphaQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetAlphaQuantum() returns the alpha value of the pixel wand.

The format of the PixelGetAlphaQuantum method is:
    
    
    Quantum PixelGetAlphaQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetBlack](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetBlack() returns the normalized black color of the pixel wand.

The format of the PixelGetBlack method is:
    
    
    double PixelGetBlack(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetBlackQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetBlackQuantum() returns the black color of the pixel wand.

The format of the PixelGetBlackQuantum method is:
    
    
    Quantum PixelGetBlackQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetBlue](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetBlue() returns the normalized blue color of the pixel wand.

The format of the PixelGetBlue method is:
    
    
    double PixelGetBlue(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetBlueQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetBlueQuantum() returns the blue color of the pixel wand.

The format of the PixelGetBlueQuantum method is:
    
    
    Quantum PixelGetBlueQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetColorAsString](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetColorAsString() returnsd the color of the pixel wand as a string.

The format of the PixelGetColorAsString method is:
    
    
    char *PixelGetColorAsString(PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetColorAsNormalizedString](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetColorAsNormalizedString() returns the normalized color of the pixel wand as a string.

The format of the PixelGetColorAsNormalizedString method is:
    
    
    char *PixelGetColorAsNormalizedString(PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetColorCount](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetColorCount() returns the color count associated with this color.

The format of the PixelGetColorCount method is:
    
    
    size_t PixelGetColorCount(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetCyan](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetCyan() returns the normalized cyan color of the pixel wand.

The format of the PixelGetCyan method is:
    
    
    double PixelGetCyan(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetCyanQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetCyanQuantum() returns the cyan color of the pixel wand.

The format of the PixelGetCyanQuantum method is:
    
    
    Quantum PixelGetCyanQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetException](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetException() returns the severity, reason, and description of any error that occurs when using other methods in this API.

The format of the PixelGetException method is:
    
    
    char *PixelGetException(const PixelWand *wand,ExceptionType *severity)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
severity
    the severity of the error is returned here. 
    

## [PixelGetExceptionType](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetExceptionType() the exception type associated with the wand. If no exception has occurred, UndefinedExceptionType is returned.

The format of the PixelGetExceptionType method is:
    
    
    ExceptionType PixelGetExceptionType(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [PixelGetFuzz](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetFuzz() returns the normalized fuzz value of the pixel wand.

The format of the PixelGetFuzz method is:
    
    
    double PixelGetFuzz(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetGreen](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetGreen() returns the normalized green color of the pixel wand.

The format of the PixelGetGreen method is:
    
    
    double PixelGetGreen(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetGreenQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetGreenQuantum() returns the green color of the pixel wand.

The format of the PixelGetGreenQuantum method is:
    
    
    Quantum PixelGetGreenQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetHSL](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetHSL() returns the normalized HSL color of the pixel wand.

The format of the PixelGetHSL method is:
    
    
    void PixelGetHSL(const PixelWand *wand,double *hue,double *saturation,
      double *lightness)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
hue,saturation,lightness
    Return the pixel hue, saturation, and brightness. 
    

## [PixelGetIndex](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetIndex() returns the colormap index from the pixel wand.

The format of the PixelGetIndex method is:
    
    
    Quantum PixelGetIndex(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetMagenta](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetMagenta() returns the normalized magenta color of the pixel wand.

The format of the PixelGetMagenta method is:
    
    
    double PixelGetMagenta(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetMagentaQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetMagentaQuantum() returns the magenta color of the pixel wand.

The format of the PixelGetMagentaQuantum method is:
    
    
    Quantum PixelGetMagentaQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetMagickColor](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetMagickColor() gets the magick color of the pixel wand.

The format of the PixelGetMagickColor method is:
    
    
    void PixelGetMagickColor(PixelWand *wand,PixelInfo *color)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
color
     The pixel wand color is returned here. 
    

## [PixelGetPixel](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetPixel() returns the pixel wand pixel.

The format of the PixelGetPixel method is:
    
    
    PixelInfo PixelGetPixel(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetQuantumPacket](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetQuantumPacket() gets the packet of the pixel wand as a PixelInfo.

The format of the PixelGetQuantumPacket method is:
    
    
    void PixelGetQuantumPacket(PixelWand *wand,PixelInfo *packet)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
packet
     The pixel wand packet is returned here. 
    

## [PixelGetQuantumPixel](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetQuantumPixel() gets the pixel of the pixel wand as a PixelInfo.

The format of the PixelGetQuantumPixel method is:
    
    
    void PixelGetQuantumPixel(const Image *image,const PixelWand *wand,
      Quantum *pixel)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
pixel
     The pixel wand pixel is returned here. 
    

## [PixelGetRed](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetRed() returns the normalized red color of the pixel wand.

The format of the PixelGetRed method is:
    
    
    double PixelGetRed(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetRedQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetRedQuantum() returns the red color of the pixel wand.

The format of the PixelGetRedQuantum method is:
    
    
    Quantum PixelGetRedQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetYellow](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetYellow() returns the normalized yellow color of the pixel wand.

The format of the PixelGetYellow method is:
    
    
    double PixelGetYellow(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelGetYellowQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelGetYellowQuantum() returns the yellow color of the pixel wand.

The format of the PixelGetYellowQuantum method is:
    
    
    Quantum PixelGetYellowQuantum(const PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    

## [PixelSetAlpha](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetAlpha() sets the normalized alpha value of the pixel wand.

The format of the PixelSetAlpha method is:
    
    
    void PixelSetAlpha(PixelWand *wand,const double alpha)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
alpha
    the level of transparency: 1.0 is fully opaque and 0.0 is fully transparent. 
    

## [PixelSetAlphaQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetAlphaQuantum() sets the alpha value of the pixel wand.

The format of the PixelSetAlphaQuantum method is:
    
    
    void PixelSetAlphaQuantum(PixelWand *wand,const Quantum alpha)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
alpha
    the alpha value. 
    

## [PixelSetBlack](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetBlack() sets the normalized black color of the pixel wand.

The format of the PixelSetBlack method is:
    
    
    void PixelSetBlack(PixelWand *wand,const double black)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
black
    the black color. 
    

## [PixelSetBlackQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetBlackQuantum() sets the black color of the pixel wand.

The format of the PixelSetBlackQuantum method is:
    
    
    void PixelSetBlackQuantum(PixelWand *wand,const Quantum black)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
black
    the black color. 
    

## [PixelSetBlue](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetBlue() sets the normalized blue color of the pixel wand.

The format of the PixelSetBlue method is:
    
    
    void PixelSetBlue(PixelWand *wand,const double blue)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
blue
    the blue color. 
    

## [PixelSetBlueQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetBlueQuantum() sets the blue color of the pixel wand.

The format of the PixelSetBlueQuantum method is:
    
    
    void PixelSetBlueQuantum(PixelWand *wand,const Quantum blue)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
blue
    the blue color. 
    

## [PixelSetColor](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetColor() sets the color of the pixel wand with a string (e.g. "blue", "#0000ff", "rgb(0,0,255)", "cmyk(100,100,100,10)", etc.).

The format of the PixelSetColor method is:
    
    
    MagickBooleanType PixelSetColor(PixelWand *wand,const char *color)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
color
    the pixel wand color. 
    

## [PixelSetColorCount](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetColorCount() sets the color count of the pixel wand.

The format of the PixelSetColorCount method is:
    
    
    void PixelSetColorCount(PixelWand *wand,const size_t count)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
count
    the number of this particular color. 
    

## [PixelSetColorFromWand](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetColorFromWand() sets the color of the pixel wand.

The format of the PixelSetColorFromWand method is:
    
    
    void PixelSetColorFromWand(PixelWand *wand,const PixelWand *color)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
color
    set the pixel wand color here. 
    

## [PixelSetCyan](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetCyan() sets the normalized cyan color of the pixel wand.

The format of the PixelSetCyan method is:
    
    
    void PixelSetCyan(PixelWand *wand,const double cyan)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
cyan
    the cyan color. 
    

## [PixelSetCyanQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetCyanQuantum() sets the cyan color of the pixel wand.

The format of the PixelSetCyanQuantum method is:
    
    
    void PixelSetCyanQuantum(PixelWand *wand,const Quantum cyan)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
cyan
    the cyan color. 
    

## [PixelSetFuzz](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetFuzz() sets the fuzz value of the pixel wand.

The format of the PixelSetFuzz method is:
    
    
    void PixelSetFuzz(PixelWand *wand,const double fuzz)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
fuzz
    the fuzz value. 
    

## [PixelSetGreen](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetGreen() sets the normalized green color of the pixel wand.

The format of the PixelSetGreen method is:
    
    
    void PixelSetGreen(PixelWand *wand,const double green)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
green
    the green color. 
    

## [PixelSetGreenQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetGreenQuantum() sets the green color of the pixel wand.

The format of the PixelSetGreenQuantum method is:
    
    
    void PixelSetGreenQuantum(PixelWand *wand,const Quantum green)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
green
    the green color. 
    

## [PixelSetHSL](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetHSL() sets the normalized HSL color of the pixel wand.

The format of the PixelSetHSL method is:
    
    
    void PixelSetHSL(PixelWand *wand,const double hue,
      const double saturation,const double lightness)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
hue,saturation,lightness
    Return the pixel hue, saturation, and brightness. 
    

## [PixelSetIndex](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetIndex() sets the colormap index of the pixel wand.

The format of the PixelSetIndex method is:
    
    
    void PixelSetIndex(PixelWand *wand,const Quantum index)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
index
    the colormap index. 
    

## [PixelSetMagenta](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetMagenta() sets the normalized magenta color of the pixel wand.

The format of the PixelSetMagenta method is:
    
    
    void PixelSetMagenta(PixelWand *wand,const double magenta)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
magenta
    the magenta color. 
    

## [PixelSetMagentaQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetMagentaQuantum() sets the magenta color of the pixel wand.

The format of the PixelSetMagentaQuantum method is:
    
    
    void PixelSetMagentaQuantum(PixelWand *wand,
      const Quantum magenta)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
magenta
    the green magenta. 
    

## [PixelSetPixelColor](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetPixelColor() sets the color of the pixel wand.

The format of the PixelSetPixelColor method is:
    
    
    void PixelSetPixelColor(PixelWand *wand,const PixelInfo *color)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
color
    the pixel wand color. 
    

## [PixelSetQuantumPixel](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetQuantumPixel() sets the pixel of the pixel wand.

The format of the PixelSetQuantumPixel method is:
    
    
    void PixelSetQuantumPixel(const Image *image,const Quantum *pixel,
      PixelWand *wand)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
pixel
    the pixel wand pixel. 
    

## [PixelSetRed](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetRed() sets the normalized red color of the pixel wand.

The format of the PixelSetRed method is:
    
    
    void PixelSetRed(PixelWand *wand,const double red)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
red
    the red color. 
    

## [PixelSetRedQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetRedQuantum() sets the red color of the pixel wand.

The format of the PixelSetRedQuantum method is:
    
    
    void PixelSetRedQuantum(PixelWand *wand,const Quantum red)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
red
    the red color. 
    

## [PixelSetYellow](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetYellow() sets the normalized yellow color of the pixel wand.

The format of the PixelSetYellow method is:
    
    
    void PixelSetYellow(PixelWand *wand,const double yellow)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
yellow
    the yellow color. 
    

## [PixelSetYellowQuantum](http://www.imagemagick.org/api/MagickWand/pixel-wand_8c.html)

PixelSetYellowQuantum() sets the yellow color of the pixel wand.

The format of the PixelSetYellowQuantum method is:
    
    
    void PixelSetYellowQuantum(PixelWand *wand,const Quantum yellow)
    

A description of each parameter follows:

    
    

wand
    the pixel wand. 
    
yellow
    the yellow color. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](pixel-wand.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
