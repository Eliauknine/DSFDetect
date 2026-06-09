# Enumerations

![>](right_triangle.png) **Contents**  
---  
  
  * [ChannelType](Enumerations.html#ChannelType)

  * [ClassType](Enumerations.html#ClassType)

  * [ColorspaceType](Enumerations.html#ColorspaceType)

  * [CompositeOperator](Enumerations.html#CompositeOperator)

  * [CompressionType](Enumerations.html#CompressionType)

  * [DecorationType](Enumerations.html#DecorationType)

  * [FillRule](Enumerations.html#FillRule)

  * [FilterTypes](Enumerations.html#FilterTypes)

  * [GravityType](Enumerations.html#GravityType)

  * [ImageType](Enumerations.html#ImageType)

  * [InterlaceType](Enumerations.html#InterlaceType)

  * [ChannelType](Enumerations.html#ChannelType)

  * [LineCap](Enumerations.html#LineCap)

  * [LineJoin](Enumerations.html#LineJoin)

  * [NoiseType](Enumerations.html#NoiseType)

  * [OrientationType](Enumerations.html#OrientationType)

  * [PaintMethod](Enumerations.html#PaintMethod)

  * [QuantumTypes](Enumerations.html#QuantumTypes)

  * [RenderingIntent](Enumerations.html#RenderingIntent)

  * [ResolutionType](Enumerations.html#ResolutionType)

  * [StorageType](Enumerations.html#StorageType)

  * [StretchType](Enumerations.html#StretchType)

  * [StyleType](Enumerations.html#StyleType)

  * [VirtualPixelMethod](Enumerations.html#VirtualPixelMethod)


![>](right_triangle.png) **ChannelType**  
---  
  
_ChannelType_ is used as an argument when doing color separations. Use _ChannelType_ when extracting a layer from an image. _MatteChannel_ is useful for extracting the opacity values from an image. Note that an image may be represented in RGB, RGBA, CMYK, or CMYKA, pixel formats and a channel may only be extracted if it is valid for the current pixel format.

**ChannelType**

**Enumeration** |  **Description**  
---|---  
UndefinedChannel |  Unset value.  
RedChannel |  Extract red channel (RGB images only)  
CyanChannel |  Extract cyan channel (CMYK images only)  
GreenChannel |  Extract green channel (RGB images only)  
MagentaChannel |  Extract magenta channel (CMYK images only)  
BlueChannel |  Extract blue channel (RGB images only)  
YellowChannel |  Extract yellow channel (CMYK images only)  
OpacityChannel |  Extract matte (opacity values) channel (CMYKA images only)  
BlackChannel |  Extract black channel (CMYK images only)  
MatteChannel |  Extract matte (opacity values) channel (RGB images only)  
  
  


![>](right_triangle.png) **ClassType**  
---  
  
_ClassType_ specifies the image storage class. 

**ClassType**

**Enumeration** |  **Description**  
---|---  
UndefinedClass |  Unset value.  
DirectClass |  Image is composed of pixels which represent literal color values.  
PseudoClass |  Image is composed of pixels which specify an index in a color palette.  
  
  


![>](right_triangle.png) **ColorspaceType**  
---  
  
The ColorspaceType enumeration is used to specify the colorspace that quantization (color reduction and mapping) is done under or to specify the colorspace when encoding an output image. Colorspaces are ways of describing colors to fit the requirements of a particular application (e.g. Television, offset printing, color monitors). Color reduction, by default, takes place in the _RGBColorspace_. Empirical evidence suggests that distances in color spaces such as _YUVColorspace_ or _YIQColorspace_ correspond to perceptual color differences more closely han do distances in RGB space. These color spaces may give better results when color reducing an image. Refer to _quantize_ for more details. 

When encoding an output image, the colorspaces _RGBColorspace_ , _CMYKColorspace_ , and _GRAYColorspace_ may be specified. The _CMYKColorspace_ option is only applicable when writing TIFF, JPEG, and Adobe Photoshop bitmap (PSD) files. 

**ColorspaceType**

**Enumeration** |  **Description**  
---|---  
UndefinedColorspace |  Unset value.  
CMYKColorspace |  Cyan-Magenta-Yellow-Black colorspace. CYMK is a subtractive color system used by printers and photographers for the rendering of colors with ink or emulsion, normally on a white surface.  
GRAYColorspace |  Grayscale colorspace  
HCLColorspace |   
LabColorspace |   
LCHabColorspace |   
LuvColorspace |   
OHTAColorspace |   
RGBColorspace |  Red-Green-Blue colorspace.  
sRGBColorspace |   
scRGBColorspace |   
TransparentColorspace |  The Transparent color space behaves uniquely in that it preserves the matte channel of the image if it exists.  
XYZColorspace |   
YCbCrColorspace |   
YCCColorspace |   
YIQColorspace |   
YPbPrColorspace |   
YUVColorspace |  Y-signal, U-signal, and V-signal colorspace. YUV is most widely used to encode color for use in television transmission.  
  
  


![>](right_triangle.png) **CompositeOperator**  
---  
  
_CompositeOperator_ is used to select the image composition algorithm used to compose a _composite image_ with an _image_. By default, each of the composite image pixels are replaced by the corresponding image tile pixel. Specify _CompositeOperator_ to select a different algorithm. 

**CompositeOperator**

**Enumeration** |  **Description**  
---|---  
UndefinedCompositeOp |  Unset value.  
OverCompositeOp |  The result is the union of the the two image shapes with the _composite image_ obscuring _image_ in the region of overlap.  
InCompositeOp |  The result is a simply _composite image_ cut by the shape of image. None of the image data of _image_ is included in the result.  
OutCompositeOp |  The resulting image is _composite image_ with the shape of _image_ cut out.  
AtopCompositeOp |  The result is the same shape as image _image_ , with _composite image_ obscuring _image_ there the image shapes overlap. Note that this differs from _OverCompositeOp_ because the portion of _composite image_ outside of _image_ 's shape does not appear in the result.  
XorCompositeOp |  The result is the image data from both c _omposite image_ and _image_ that is outside the overlap region. The overlap region will be blank.  
PlusCompositeOp |  The result is just the sum of the image data. Output values are cropped to 255 (no overflow). This operation is independent of the matte channels.  
MinusCompositeOp |  The result of _composite image_ - _image_ , with overflow cropped to zero. The matte chanel is ignored (set to 255, full coverage).  
AddCompositeOp |  The result of _composite image_ + _image_ , with overflow wrapping around (mod 256).  
SubtractCompositeOp |  The result of _composite image_ - _image_ , with underflow wrapping around (mod 256). The add and subtract operators can be used to perform reverible transformations.  
DifferenceCompositeOp |  The result of abs(c _omposite image_ - _image_). This is useful for comparing two very similar images.  
MultiplyCompositeOp |   
BumpmapCompositeOp |  The result _image_ shaded by _composite image._  
CopyCompositeOp |  The resulting _image_ is image replaced with c _omposite image_. Here the matte information is ignored.  
CopyRedCompositeOp |  The resulting image is the red layer in _image_ replaced with the red layer in _composite image_. The other layers are copied untouched.  
CopyGreenCompositeOp |  The resulting image is the green layer in _image_ replaced with the green layer in _composite image_. The other layers are copied untouched.  
CopyBlueCompositeOp |  The resulting image is the blue layer in _image_ replaced with the blue layer in _composite image_. The other layers are copied untouched.  
CopyOpacityCompositeOp |  The resulting image is the matte layer in _image_ replaced with the matte layer in _composite image_. The other layers are copied untouched.  The image compositor requires a matte, or alpha channel in the image for some operations. This extra channel usually defines a mask which represents a sort of a cookie-cutter for the image. This is the case when matte is 255 (full coverage) for pixels inside the shape, zero outside, and between zero and 255 on the boundary. For certain operations, if _image_ does not have a matte channel, it is initialized with 0 for any pixel matching in color to pixel location (0,0), otherwise 255 (to work properly _borderWidth_ must be 0).  
ClearCompositeOp |   
DissolveCompositeOp |   
DisplaceCompositeOp |   
ModulateCompositeOp |   
ThresholdCompositeOp |   
  
  


![>](right_triangle.png)**CompressionType**  
---  
  
_CompressionType_ is used to express the desired compression type when encoding an image. Be aware that most image types only support a sub-set of the available compression types. If the compression type specified is incompatable with the image, ImageMagick selects a compression type compatable with the image type. 

**CompressionType**

**Enumeration** |  **Description**  
---|---  
UndefinedCompression |  Unset value.  
NoCompression |  No compression  
BZipCompression |  BZip (Burrows-Wheeler block-sorting text compression algorithm and Huffman coding) as used by bzip2 utilities  
FaxCompression |  CCITT Group 3 FAX compression  
Group4Compression |  CCITT Group 4 FAX compression (used only for TIFF)  
JPEGCompression |  JPEG compression  
LZWCompression |  Lempel-Ziv-Welch (LZW) compression (caution, patented by Unisys)  
RunlengthEncodedCompression |  Run-Length encoded (RLE) compression  
ZipCompression |  Lempel-Ziv compression (LZ77) as used in PKZIP and GNU gzip.  
  
  


![>](right_triangle.png) **DecorationType**  
---  
  
The _DecorationType_ enumerations are used to specify line decorations of rendered text. 

**DecorationType**

**Enumeration** |  **Description**  
---|---  
NoDecoration |  No decoration  
UnderlineDecoration |  Underlined text  
OverlineDecoration |  Overlined text  
LineThroughDecoration |  Strike-through text  
  
  


![>](right_triangle.png)**EndianType**  
---  
  
The _EndianType_ enumerations are used to specify the endian option for formats which support it (e.g. TIFF). 

  


**EndianType**

**Enumeration** |  **Description**  
---|---  
UndefinedEndian |  Not defined (default)  
LSBEndian |  Little endian (like Intel X86 and DEC Alpha)  
MSBEndian |  Big endian (like Motorola 68K, Mac PowerPC, & SPARC)  
  
  


![>](right_triangle.png)**FillRule**  
---  
  
_FillRule_ specifies the algorithm which is to be used to determine what parts of the canvas are included inside the shape. See the documentation on SVG's [fill-rule](http://www.w3.org/TR/SVG/painting.html#FillRuleProperty) property for usage details. 

**FillRule**

UndefinedRule |  Fill rule not specified  
---|---  
EvenOddRule |  See SVG fill-rule _evenodd_ rule.  
NonZeroRule |  See SVG fill-rule _nonzero_ rule.  
  
  


![>](right_triangle.png)**FilterTypes**  
---  
  
_FilterTypes_ is used to adjust the filter algorithm used when resizing images. Different filters experience varying degrees of success with various images and can take sipngicantly different amounts of processing time. ImageMagick uses the _LanczosFilter_ by default since this filter has been shown to provide the best results for most images in a reasonable amount of time. Other filter types (e.g. _TriangleFilter_) may execute much faster but may show artifacts when the image is re-sized or around diagonal lines. The only way to be sure is to test the filter with sample images. 

**FilterTypes**

**Enumeration** |  **Description**  
---|---  
UndefinedFilter |  Unset value.  
PointFilter |  Point Filter  
BoxFilter |  Box Filter  
TriangleFilter |  Triangle Filter  
HermiteFilter |  Hermite Filter  
HanningFilter |  Hanning Filter  
HammingFilter |  Hamming Filter  
BlackmanFilter |  Blackman Filter  
GaussianFilter |  Gaussian Filter  
QuadraticFilter |  Quadratic Filter  
CubicFilter |  Cubic Filter  
CatromFilter |  Catrom Filter  
MitchellFilter |  Mitchell Filter  
LanczosFilter |  Lanczos Filter  
BesselFilter |  Bessel Filter  
SincFilter |  Sinc Filter  
  
  


![>](right_triangle.png)**GravityType**  
---  
  
_GravityType_ specifies positioning of an object (e.g. text, image) within a bounding region (e.g. an image). Gravity provides a convenient way to locate objects irrespective of the size of the bounding region, in other words, you don't need to provide absolute coordinates in order to position an object. A common default for gravity is _NorthWestGravity_. 

**GravityType**

**Enumeration** |  **Description**  
---|---  
ForgetGravity |  Don't use gravity.  
NorthWestGravity |  Position object at top-left of region.  
NorthGravity |  Postiion object at top-center of region  
NorthEastGravity |  Position object at top-right of region  
WestGravity |  Position object at left-center of region  
CenterGravity |  Position object at center of region  
EastGravity |  Position object at right-center of region  
SouthWestGravity |  Position object at left-bottom of region  
SouthGravity |  Position object at bottom-center of region  
SouthEastGravity |  Position object at bottom-right of region  
  
  


![>](right_triangle.png)**ImageType**  
---  
  
_ImageType_ indicates the type classification of the image. 

**ImageType**

**Enumeration** |  **Description**  
---|---  
UndefinedType |  Unset value.  
BilevelType |  Monochrome image  
GrayscaleType |  Grayscale image  
GrayscaleMatteType |  Grayscale image with opacity  
PaletteType |  Indexed color (palette) image  
PaletteMatteType |  Indexed color (palette) image with opacity  
TrueColorType |  Truecolor image  
TrueColorMatteType |  Truecolor image with opacity  
ColorSeparationType |  Cyan/Yellow/Magenta/Black (CYMK) image  
  
  


![>](right_triangle.png)**InterlaceType**  
---  
  
_InterlaceType_ specifies the ordering of the red, green, and blue pixel information in the image. Interlacing is usually used to make image information available to the user faster by taking advantage of the space vs time tradeoff. For example, interlacing allows images on the Web to be recognizable sooner and satellite images to accumulate/render with image resolution increasing over time. 

Use _LineInterlace_ or _PlaneInterlace_ to create an interlaced GIF or progressive JPEG image. 

**InterlaceType**

**Enumeration** |  **Description**  
---|---  
UndefinedInterlace |  Unset value.  
NoInterlace |  Don't interlace image (RGBRGBRGBRGBRGBRGB...)  
LineInterlace |  Use scanline interlacing (RRR...GGG...BBB...RRR...GGG...BBB...)  
PlaneInterlace |  Use plane interlacing (RRRRRR...GGGGGG...BBBBBB...)  
PartitionInterlace |  Similar to plane interlaing except that the different planes are saved to individual files (e.g. image.R, image.G, and image.B)  
  
  


![>](right_triangle.png)**ChannelType**  
---  
  
_ChannelType_ is used as an argument when doing color separations. Use _ChannelType_ when extracting a layer from an image. _MatteLayer_ is useful for extracting the opacity values from an image. 

**ChannelType**

**Enumeration** |  **Description**  
---|---  
UndefinedLayer |  Unset value.  
RedLayer |  Select red layer  
GreenLayer |  Select green layer  
BlueLayer |  Select blue layer  
MatteLayer |  Select matte (opacity values) layer  
  
  


![>](right_triangle.png)**LineCap**  
---  
  
The _LineCap_ enumerations specify shape to be used at the end of open subpaths when they are stroked. See SVG's '[stroke-linecap'](http://www.w3.org/TR/SVG/painting.html#StrokeLinecapProperty) for examples. 

**LineCap**

**Enumeration** |  **Description**  
---|---  
UndefinedCap |  Unset value.  
ButtCap |  Square ending.  
RoundCap |  Rounded ending (half-circle end with radius of 1/2 stroke width).  
SquareCap |  Square ending, extended by 1/2 the stroke width at end.  
  
  


![>](right_triangle.png)**LineJoin**  
---  
  
The _LineJoin_ enumerations specify the shape to be used at the corners of paths or basic shapes when they are stroked. See SVG's '[stroke-linejoin'](http://www.w3.org/TR/SVG/painting.html#StrokeLinejoinProperty) for examples. 

**ChannelType**

**Enumeration** |  **Description**  
---|---  
UndefinedJoin |  Unset value.  
MiterJoin |  Sharp-edged join  
RoundJoin |  Rounded-edged join  
BevelJoin |  Beveled-edged join  
  
  


![>](right_triangle.png)**NoiseType**  
---  
  
_NoiseType_ is used as an argument to select the type of noise to be added to the image. 

**NoiseType**

**Enumeration** |  **Description**  
---|---  
UniformNoise |  Uniform noise  
GaussianNoise |  Gaussian noise  
MultiplicativeGaussianNoise |  Multiplicative Gaussian noise  
ImpulseNoise |  Impulse noise  
LaplacianNoise |  Laplacian noise  
PoissonNoise |  Poisson noise  
  
  


![>](right_triangle.png)**OrientationType**  
---  
  
_OrientationType_ specifies the orientation of the image. Useful for when the image is produced via a different ordinate system, the camera was turned on its side, or the page was scanned sideways.

**OrientationType**

**Enumeration** |  **Scanline Direction** |  **Frame Direction**  
---|---|---  
UndefinedOrientation |  Unknown |  Unknown  
TopLeftOrientation |  Left to right |  Top to bottom  
TopRightOrientation |  Right to left |  Top to bottom  
BottomRightOrientation |  Right to left |  Bottom to top  
BottomLeftOrientation |  Left to right |  Bottom to top  
LeftTopOrientation |  Top to bottom |  Left to right  
RightTopOrientation |  Top to bottom |  Right to left  
RightBottomOrientation |  Bottom to top |  Right to left  
LeftBottomOrientation |  Bottom to top |  Left to right  
  
  


![>](right_triangle.png)**PaintMethod**  
---  
  
_PaintMethod_ specifies how pixel colors are to be replaced in the image. It is used to select the pixel-filling algorithm employed. 

**PaintMethod**

**Enumeration** |  **Description**  
---|---  
PointMethod |  Replace pixel color at point.  
ReplaceMethod |  Replace color for all image pixels matching color at point.  
FloodfillMethod |  Replace color for pixels surrounding point until encountering pixel that fails to match color at point.  
FillToBorderMethod |  Replace color for pixels surrounding point until encountering pixels matching border color.  
ResetMethod |  Replace colors for **all** pixels in image with pen color.  
  
  


![>](right_triangle.png)**QuantumTypes**  
---  
  
_QuantumTypes_ is used to indicate the source or destination format of entire pixels, or components of pixels ("Quantums") while they are being read, or written to, a pixel cache. The validity of these format specifications depends on whether the Image pixels are in RGB format, RGBA format, or CMYK format. The pixel Quantum size is determined by the Image depth (eight or sixteen bits). 

**RGB(A) Image Quantums**

**Enumeration** |  **Description**  
---|---  
IndexQuantum |  PseudoColor colormap indices (valid only for image with colormap)  
RedQuantum |  Red pixel Quantum  
GreenQuantum |  Green pixel Quantum  
BlueQuantum |  Blue pixel Quantum  
AlphaQuantum |  Alpha Quantum  
  
  


**CMY(K)(A) Image Quantum**

**Enumeration** |  **Description**  
---|---  
CyanQuantum |  Cyan pixel Quantum  
MagentaQuantum |  Magenta pixel Quantum  
YellowQuantum |  Yellow pixel Quantum  
BlackQuantum |  Black pixel Quantum  
AlphaQuantum |  Alpha Quantum  
  
  


**Grayscale Image Quantums**

**Enumeration** |  **Description**  
---|---  
GrayQuantum |  Gray pixel  
GrayOpacityQuantum |  Pixel opacity  
AlphaQuantum |  Alpha Quantum  
  
  


**Entire Pixels (Expressed in Byte Order)**

**Enumeration** |  **Description**  
---|---  
RGBQuantum |  RGB pixel (24 or 48 bits)  
RGBAQuantum |  RGBA pixel (32 or 64 bits)  
CMYKQuantum |  CMYK pixel (32 or 64 bits)  
CMYKAQuantum |  CMYKA pixel (40 or 80 bits)  
  
  


![>](right_triangle.png)**RenderingIntent**  
---  
  
Rendering intent is a concept defined by [ICC](http://www.color.org/) Spec ICC.1:1998-09, "File Format for Color Profiles". ImageMagick uses _RenderingIntent_ in order to support ICC Color Profiles. 

From the specification: "Rendering intent specifies the style of reproduction to be used during the evaluation of this profile in a sequence of profiles. It applies specifically to that profile in the sequence and not to the entire sequence. Typically, the user or application will set the rendering intent dynamically at runtime or embedding time."

**RenderingIntent**

**Enumeration** |  **Description**  
---|---  
UndefinedIntent |  Unset value.  
SaturationIntent |  A rendering intent that specifies the saturation of the pixels in the image is preserved perhaps at the expense of accuracy in hue and lightness.  
PerceptualIntent |  A rendering intent that specifies the full gamut of the image is compressed or expanded to fill the gamut of the destination device. Gray balance is preserved but colorimetric accuracy might not be preserved.  
AbsoluteIntent |  Absolute colorimetric  
RelativeIntent |  Relative colorimetric  
  
  


![>](right_triangle.png)**ResolutionType**  
---  
  
By default, ImageMagick defines resolutions in pixels per inch. _ResolutionType_ provides a means to adjust this. 

**ResolutionType**

**Enumeration** |  **Description**  
---|---  
UndefinedResolution |  Unset value.  
PixelsPerInchResolution |  Density specifications are specified in units of pixels per inch (english units).  
PixelsPerCentimeterResolution |  Density specifications are specified in units of pixels per centimeter (metric units).  
  
  


![>](right_triangle.png)**StorageType**  
---  
  
The _StorageType_ enumerations are used to specify the storage format of pixels in the source or destination pixel array. 

**StorageType**

**Enumeration** |  **Description**  
---|---  
CharPixel |  Character type  
ShortPixel |  Short type  
IntegerPixel |  Integer type  
FloatPixel |  Float type  
DoublePixel |  Double type  
  
  


![>](right_triangle.png)**StretchType**  
---  
  
The _StretchType_ enumerations are used to specify the relative width of a font to the regular width for the font family. If the width is not important, the _AnyStretch_ enumeration may be specified for a wildcard match. 

**StretchType**

**Enumeration** |  **Description**  
---|---  
AnyStretch |  Wildcard match for font stretch  
NormalStretch |  Normal width font  
UltraCondensedStretch |  Ultra-condensed (narrowest) font  
ExtraCondensedStretch |  Extra-condensed font  
CondensedStretch |  Condensed font  
SemiCondensedStretch |  Semi-Condensed font  
SemiExpandedStretch |  Semi-Expanded font  
ExpandedStretch |  Expanded font  
ExtraExpandedStretch |  Extra-Expanded font  
UltraExpandedStretch |  Ultra-expanded (widest) font  
  
  


![>](right_triangle.png)**StyleType**  
---  
  
The _StyleType_ enumerations are used to specify the style (e.g. Italic) of a font. If the style is not important, the _AnyStyle_ enumeration may be specified for a wildcard match. 

**StyleType**

**Enumeration** |  **Description**  
---|---  
AnyStyle |  Wildcard match for font style  
NormalStyle |  Normal font style  
ItalicStyle |  Italic font style  
ObliqueStyle |  Oblique font style  
  
  


![>](right_triangle.png)**VirtualPixelMethod**  
---  
  
The _VirtualPixelMethod_ enumerations are used to specify the virtual pixel method. 

  


**VirtualPixelMethod**

**Enumeration** |  **Description**  
---|---  
UndefinedVirtualPixelMethod |  Not defined  
BackgroundVirtualPixelMethod |  the area surrounding the image is the background color   
BlackVirtualPixelMethod |  the area surrounding the image is black  
CheckerTileVirtualPixelMethod |  alternate squares with image and background color   
DitherVirtualPixelMethod |  non-random 32x32 dithered pattern   
EdgeVirtualPixelMethod |  extend the edge pixel toward infinity   
GrayVirtualPixelMethod |  the area surrounding the image is gray   
HorizontalTileVirtualPixelMethod |  horizontally tile the image, background color above/below  
HorizontalTileEdgeVirtualPixelMethod |  horizontally tile the image and replicate the side edge pixels  
MirrorVirtualPixelMethod |  mirror tile the image   
RandomVirtualPixelMethod |  choose a random pixel from the image   
TileVirtualPixelMethod |  tile the image (default)   
TransparentVirtualPixelMethod |  the area surrounding the image is transparent blackness   
VerticalTileVirtualPixelMethod |  vertically tile the image, sides are background color   
VerticalTileEdgeVirtualPixelMethod |  vertically tile the image and replicate the side edge pixels   
WhiteVirtualPixelMethod |  the area surrounding the image is white 
