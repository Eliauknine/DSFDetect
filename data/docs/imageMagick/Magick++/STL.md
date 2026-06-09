#  Magick++ STL Support  
  
Magick++ provides a set of [Standard Template Libary](http://www.sgi.com/tech/stl/) ([STL](http://www.sgi.com/tech/stl/) ) algorithms for operating across ranges of image frames in a container. It also provides a set of STL unary function objects to apply an operation on image frames in a container via an algorithm which uses unary function objects. A good example of a standard algorithm which is useful for processing containers of image frames is the STL _[for_each](http://www.sgi.com/tech/stl/for_each.html) _ algorithm which invokes a unary function object on a range of container elements. 

Magick++ uses a limited set of template argument types. The current template argument types are: 

[Container](http://www.sgi.com/tech/stl/Container.html)

> A container having the properties of a [ Back Insertion Sequence](http://www.sgi.com/tech/stl/BackInsertionSequence.html) . Sequences support forward iterators and Back Insertion Sequences support the additional abilty to append an element via push_back(). Common compatable container types are the STL <[ vector](http://www.sgi.com/tech/stl/Vector.html) > and <[list](http://www.sgi.com/tech/stl/List.html) > template containers. This template argument is usually used to represent an output container in which one or more image frames may be appended. Containers like STL <[vector](http://www.sgi.com/tech/stl/Vector.html) > which have a given default _capacity_ may need to have their _capacity_ adjusted via r _eserve()_ to a larger _capacity_ in order to support the expected final _size_ . Since Magick++ images are very small, it is likely that the default capacity of STL <[ vector](http://www.sgi.com/tech/stl/Vector.html) > is sufficient for most situations.

[InputIterator](http://www.sgi.com/tech/stl/InputIterator.html)

> An input iterator used to express a position in a container. These template arguments are typically used to represent a range of elements with f _irst__ representing the first element to be processed and _last__ representing the element to stop at. When processing the entire contents of a container, it is handy to know that STL containers usually provide the begin() and end() methods to return input interators which correspond with the first and last elements, respectively.

The following is an example of how frames from a GIF animation  "test_image_anim.gif" may be appended horizontally with the resulting image written to the file `appended_image.miff`:
    
    
    #include <list> 
    #include <Magick++.h> 
    using namespace std; 
    using namespace Magick;
    
    int main(int /*argc*/,char **/*argv*/) 
    { 
       list<Image> imageList; 
       readImages( &imageList, "test_image_anim.gif" );
    
       Image appended; 
       appendImages( &appended, imageList.begin(), imageList.end() ); 
       appended.write( "appended_image.miff" ); 
       return 0; 
    }
    

The available Magick++ specific STL algorithms for operating on sequences of image frames are shown in the following table:   


**Magick++ STL Algorithms For Image Sequences** **Algorithm** |  **Signature** |  **Description**  
---|---|---  
animateImages | [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_ | Animate a sequence of image frames. Image frames are displayed in succession, creating an animated effect. The animation options are taken from the first image frame. This feature is only supported under X11 at the moment.  
appendImages | [Image](Image++.html) *appendedImage_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_, bool stack_ = false | Append a sequence of image frames, writing the result to _appendedImage_._ All the input image frames must have the same width or height. Image frames of the same width are stacked top-to-bottom. Image frames of the same height are stacked left-to-right. If the _stack__ parameter is false, rectangular image frames are stacked left-to-right otherwise top-to-bottom.  
averageImages | [Image](Image++.html) *averagedImage_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_ | Average a sequence of image frames, writing the result to _averagedImage__. All the input image frames must be the same size in pixels.  
coalesceImages | [ Container](http://www.sgi.com/tech/stl/Container.html) *coalescedImages_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_  
| Create a coalesced image sequence obtained by "playing" the image sequence (observing page offsets and disposal methods) to create a new image sequence in which all frames are full size and completely rendered. Note that if the original image sequence relied on page offsets and disposal methods that the resulting sequence will be larger (perhaps much larger) then the original. This is useful for GIF animation sequences that have page offsets and disposal methods. The resuting image sequence is returned via _coalescedImages_._  
deconstructImages | [ Container](http://www.sgi.com/tech/stl/Container.html) *deconstructedImages_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_ | Break down an image sequence into constituent parts. This is useful for creating GIF or MNG animation sequences. The input sequence is specified by _first__ and _last__ , and the deconstructed images are returned via _deconstructedImages__.  
displayImages | [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_ | Display a sequence of image frames. Through use of a pop-up menu, image frames may be selected in succession. This feature is fully supported under X11 but may have only limited support in other environments.   
**Caution:** if an image format is is not compatable with the display visual (e.g. JPEG on a colormapped display) then the original image will be altered. Use a copy of the original if this is a problem.  
flattenImages | [Image](Image++.html) *flattendImage_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_ | Merge a sequence of image frames which represent image layers into a single composited representation. The _flattendImage__ parameter points to an existing Image to update with the flattened image. This function is useful for combining Photoshop layers into a single image.  
forwardFourierTransformImage | [ Container](http://www.sgi.com/tech/stl/Container.html) *fourierImages_, const Image &image_  |  Implements the discrete Fourier transform (DFT) of the image as a magnitude / phase image pair via _fourierImages__.  
forwardFourierTransformImage | [ Container](http://www.sgi.com/tech/stl/Container.html) *fourierImages_, const Image &image_, const bool magnitude_  |  Implements the discrete Fourier transform (DFT) of the image either as a magnitude / phase or real / imaginary image pair via _fourierImages__.  
mapImages | [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_, const [Image](Image++.html) & mapImage_, bool dither_, bool measureError_ = false | Replace the colors of a sequence of images with the closest color from a reference image. Set _dither__ to _true_ to enable dithering. Set _measureError__ to _true_ in order to evaluate quantization error.  
montageImages | [ Container](http://www.sgi.com/tech/stl/Container.html) *montageImages_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_, const [Montage](Montage.html) &montageOpts_ | Create a composite image by combining several separate image frames. Multiple frames may be generated in the output container _montageImages__ depending on the tile setting and the number of image frames montaged. Montage options are provided via the parameter _montageOpts__ . Options set in the first image frame ([ backgroundColor,](Image++.html#backgroundColor) [borderColor](Image++.html#borderColor) , [matteColor](Image++.html#matteColor) , [penColor,](Image++.html#penColor) [font,](Image++.html#font) and [fontPointsize](Image++.html#fontPointsize) ) are also used as options by _montageImages()._  
morphImages | [ Container](http://www.sgi.com/tech/stl/Container.html) *morphedImages_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_, size_t frames_ | Morph a seqence of image frames. This algorithm expands the number of image frames (output to the container _morphedImages_)_ by adding the number of intervening frames specified by _frames__ such that the original frames morph (blend) into each other when played as an animation.  
mosaicImages | [Image](Image++.html) *mosaicImage_, [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_ | Inlay a number of images to form a single coherent picture. The _mosicImage__ argument is updated with a mosaic constructed from the image sequence represented by _first__ through _last__ .  
quantizeImages | [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_, bool measureError_ = false | Quantize colors in images using current quantization settings. Set _measureError__ to _true_ in order to measure quantization error.  
readImages | [ Container](http://www.sgi.com/tech/stl/Container.html) *sequence_, const std::string &imageSpec_ | Read a sequence of image frames into existing container (appending to container _sequence__) with image names specified in the UTF-8 string _imageSpec__.  
[ Container](http://www.sgi.com/tech/stl/Container.html) *sequence_, const [Blob](Blob.html) &blob_ | Read a sequence of image frames into existing container (appending to container sequence_) from [Blob](Blob.html) blob_.  
writeImages | [ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_, const std::string &imageSpec_, bool adjoin_ = true | Write images in container to file specified by string _imageSpec__. Set _adjoin__ to false to write a set of image frames via a wildcard _imageSpec__(e.g. image%02d.miff).   
The wildcard must be one of `%0Nd, %0No, or %0Nx`.   
**Caution:** if an image format is selected which is capable of supporting fewer colors than the original image or quantization has been requested, the original image will be quantized to fewer colors. Use a copy of the original if this is a problem.  
[ InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) first_, [InputIterator](http://www.sgi.com/tech/stl/InputIterator.html) last_, [Blob](Blob.html) *blob_, bool adjoin_ = true | Write images in container to in-memory BLOB specified by [Blob](Blob.html) blob_. Set adjoin_ to false to write a set of image frames via a wildcard imageSpec_ (e.g. image%02d.miff).   
**Caution:** if an image format is selected which is capable of supporting fewer colors than the original image or quantization has been requested, the original image will be quantized to fewer colors. Use a copy of the original if this is a problem.  



In addition, we support these yet to be documented methods: `combineImages()`, `evaluateImages()`, `mergeImageLayers()`, `optimizeImageLayers()`, `optimizePlusImageLayers()`, and `separateImages()`.

  


###  Magick++ Unary Function Objects

Magick++ unary function objects inherit from the STL unary_function template class . The STL unary_function template class is of the form 
    
    
    unary_function<Arg, Result>

and expects that derived classes implement a method of the form: 
    
    
    Result operator()( Arg argument_);

which is invoked by algorithms using the function object. In the case of unary function objects defined by Magick++, the invoked function looks like: 
    
    
    void operator()( Image &image_);

with a typical implementation looking similar to: 
    
    
    void operator()( Image &image_ )   
    
        {   
    
          image_.contrast(
    _sharpen );   
    
        }

where _contrast_ is an Image method and __sharpen_ is an argument stored within the function object by its contructor. Since constructors may be polymorphic, a given function object may have several constructors and selects the appropriate Image method based on the arguments supplied. 

In essence, unary function objects (as provided by Magick++) simply provide the means to construct an object which caches arguments for later use by an algorithm designed for use with unary function objects. There is a unary function object corresponding each algorithm provided by the [ Image](Image++.html) class and there is a contructor available compatable with each synonymous method in the Image class. 

The unary function objects that Magick++ provides to support manipulating images are shown in the following table:   


**Magick++ Unary Function Objects For Image Manipulation** **Function Object** | **Constructor Signatures(s)** | **Description**  
---|---|---  
adaptiveThresholdImage  
| size_t width, size_t height, unsigned offset = 0  
| Apply adaptive thresholding to the image. Adaptive thresholding is useful if the ideal threshold level is not known in advance, or if the illumination gradient is not constant across the image. Adaptive thresholding works by evaulating the mean (average) of a pixel region (size specified by _width_ and _height_) and using the mean as the thresholding value. In order to remove residual noise from the background, the threshold may be adjusted by subtracting a constant _offset_ (default zero) from the mean to compute the threshold.  
  
addNoiseImage | [NoiseType](Enumerations.html#NoiseType) noiseType_ | Add noise to image with specified noise type.  
affineTransformImage  
| const DrawableAffine &affine_  
| Transform image by specified affine (or free transform) matrix.  
  
annotateImage | const std::string &text_, const [ Geometry](Geometry.html) &location_ | Annotate with text using specified text, bounding area, placement gravity, and rotation. If _boundingArea__ is invalid, then bounding area is entire image.  
std::string text_, const [Geometry](Geometry.html) &boundingArea_, [GravityType](Enumerations.html#GravityType) gravity_ | Annotate using specified text, bounding area, and placement gravity. If _boundingArea__ is invalid, then bounding area is entire image.  
const std::string &text_, const [ Geometry](Geometry.html) &boundingArea_, [GravityType](Enumerations.html#GravityType) gravity_, double degrees_, | Annotate with text using specified text, bounding area, placement gravity, and rotation. If _boundingArea__ is invalid, then bounding area is entire image.  
const std::string &text_, [ GravityType](Enumerations.html#GravityType) gravity_ | Annotate with text (bounding area is entire image) and placement gravity.  
blurImage | const double radius_ = 1, const double sigma_ = 0.5 | Blur image. The radius_ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The sigma_ parameter specifies the standard deviation of the Laplacian, in pixels.  
borderImage | const [Geometry](Geometry.html) &geometry_ = "6x6+0+0" | Border image (add border to image). The color of the border is specified by the _borderColor_ attribute.  
charcoalImage | const double radius_ = 1, const double sigma_ = 0.5 | Charcoal effect image (looks like charcoal sketch). The radius_ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The sigma_ parameter specifies the standard deviation of the Laplacian, in pixels.  
chopImage | const [Geometry](Geometry.html) &geometry_ | Chop image (remove vertical or horizontal subregion of image)  
colorizeImage | const size_t opacityRed_, const size_t opacityGreen_, const size_t opacityBlue_, const Color &penColor_ | Colorize image with pen color, using specified percent opacity for red, green, and blue quantums.  
const size_t opacity_, const [ Color](Color.html) &penColor_ | Colorize image with pen color, using specified percent opacity.  
commentImage | const std::string &comment_ | Comment image (add comment string to image). By default, each image is commented with its file name. Use this method to assign a specific comment to the image. Optionally you can include the image filename, type, width, height, or other image attributes by embedding [special format characters.](FormatCharacters.html)  
compositeImage | const [Image](Image++.html) &compositeImage_, ssize_t xOffset_, ssize_t yOffset_, [ CompositeOperator](Enumerations.html#CompositeOperator) compose_ = _InCompositeOp_ | Compose an image onto another at specified offset and using specified algorithm  
const [Image](Image++.html) &compositeImage_, const Geometry &offset_, [ CompositeOperator](Enumerations.html#CompositeOperator) compose_ = _InCompositeOp_  
condenseImage | void | Condense image (Re-run-length encode image in memory).  
contrastImage | size_t sharpen_ | Contrast image (enhance intensity differences in image)  
cropImage | const [Geometry](Geometry.html) &geometry_ | Crop image (subregion of original image)  
cycleColormap-   
Image | int amount_ | Cycle image colormap  
despeckleImage | void | Despeckle image (reduce speckle noise)  
drawImage | const [Drawable](Drawable.html) &drawable_ | Draw shape or text on image.  
const std::list<[Drawable](Drawable.html) > &drawable_ | Draw shapes or text on image using a set of Drawable objects contained in an STL list. Use of this method improves drawing performance and allows batching draw objects together in a list for repeated use.  
edgeImage | size_t radius_ = 0.0 | Edge image (hilight edges in image). The radius is the radius of the pixel neighborhood.. Specify a radius of zero for automatic radius selection.  
embossImage | const double radius_ = 1, const double sigma_ = 0.5 | Emboss image (hilight edges with 3D effect). The radius_ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The sigma_ parameter specifies the standard deviation of the Laplacian, in pixels.  
enhanceImage | void | Enhance image (minimize noise)  
equalizeImage | void | Equalize image (histogram equalization)  
flipImage | void | Flip image (reflect each scanline in the vertical direction)  
floodFill-   
ColorImage | ssize_t x_, ssize_t y_, const [ Color](Color.html) &fillColor_ | Flood-fill color across pixels that match the color of the target pixel and are neighbors of the target pixel. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const [Color](Color.html) &fillColor_  
ssize_t x_, ssize_t y_, const [ Color](Color.html) &fillColor_, const [Color](Color.html) &borderColor_ | Flood-fill color across pixels starting at target-pixel and stopping at pixels matching specified border color. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const [Color](Color.html) &fillColor_, const [Color](Color.html) &borderColor_  
floodFill-   
TextureImage | ssize_t x_, ssize_t y_, const [ Image](Image++.html) &texture_ | Flood-fill texture across pixels that match the color of the target pixel and are neighbors of the target pixel. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const Image &texture_  
ssize_t x_, ssize_t y_, const Image &texture_, const [Color](Color.html) &borderColor_ | Flood-fill texture across pixels starting at target-pixel and stopping at pixels matching specified border color. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const Image &texture_, const [Color](Color.html) &borderColor_  
flopImage | void | Flop image (reflect each scanline in the horizontal direction)  
frameImage | const [Geometry](Geometry.html) &geometry_ = "25x25+6+6" | Add decorative frame around image  
size_t width_, size_t height_, ssize_t x_, ssize_t y_, ssize_t innerBevel_ = 0, ssize_t outerBevel_ = 0  
gammaImage | double gamma_ | Gamma correct image (uniform red, green, and blue correction).  
double gammaRed_, double gammaGreen_, double gammaBlue_ | Gamma correct red, green, and blue channels of image.  
gaussianBlurImage | double width_, double sigma_ | Gaussian blur image. The number of neighbor pixels to be included in the convolution mask is specified by 'width_'. For example, a width of one gives a (standard) 3x3 convolution mask. The standard deviation of the gaussian bell curve is specified by 'sigma_'.  
implodeImage | double factor_ | Implode image (special effect)  
inverseFourierTransformImage | const [Image](Image++.html) &phaseImage_, const bool magnitude_ | implements the inverse discrete Fourier transform (DFT) of the image either as a magnitude / phase or real / imaginary image pair.  
labelImage | const string &label_ | Assign a label to an image. Use this option to assign a specific label to the image. Optionally you can include the image filename, type, width, height, or scene number in the label by embedding [special format characters.](FormatCharacters.html) If the first character of string is @, the image label is read from a file titled by the remaining characters in the string. When converting to Postscript, use this option to specify a header string to print above the image.  
levelImage  
| const double black_point, const double white_point, const double mid_point=1.0  
| Level image. Adjust the levels of the image by scaling the colors falling between specified white and black points to the full available quantum range. The parameters provided represent the black, mid (gamma), and white points. The black point specifies the darkest color in the image. Colors darker than the black point are set to zero. Mid point (gamma) specifies a gamma correction to apply to the image. White point specifies the lightest color in the image. Colors brighter than the white point are set to the maximum quantum value. The black and white point have the valid range 0 to QuantumRange while mid (gamma) has a useful range of 0 to ten.  
levelChannelImage  
| const Magick::ChannelType channel, const double black_point, const double white_point, const double mid_point=1.0  
| Level image channel. Adjust the levels of the image channel by scaling the values falling between specified white and black points to the full available quantum range. The parameters provided represent the black, mid (gamma), and white points. The black point specifies the darkest color in the image. Colors darker than the black point are set to zero. Mid point (gamma) specifies a gamma correction to apply to the image. White point specifies the lightest color in the image. Colors brighter than the white point are set to the maximum quantum value. The black and white point have the valid range 0 to QuantumRange while mid (gamma) has a useful range of 0 to ten.  
layerImage | [ChannelType](Enumerations.html#ChannelType) layer_ | Extract layer from image. Use this option to extract a particular layer from the image. _MatteLayer_ , for example, is useful for extracting the opacity values from an image.  
magnifyImage | void | Magnify image by integral size  
mapImage | const [Image](Image++.html) &mapImage_ , bool dither_ = false | Remap image colors with closest color from reference image. Set dither_ to _true_ in to apply Floyd/Steinberg error diffusion to the image. By default, color reduction chooses an optimal set of colors that best represent the original image. Alternatively, you can choose a particular set of colors from an image file with this option.  
matteFloodfill-   
Image | const [Color](Color.html) &target_, unsigned int matte_, ssize_t x_, ssize_t y_, [ PaintMethod](Enumerations.html#PaintMethod) method_ | Floodfill designated area with a matte value  
medianFilterImage | const double radius_ = 0.0 | Filter image by replacing each pixel component with the median color in a circular neighborhood  
minifyImage | void | Reduce image by integral size  
modulateImage | double brightness_, double saturation_, double hue_ | Modulate percent hue, saturation, and brightness of an image. Modulation of saturation and brightness is as a ratio of the current value (1.0 for no change). Modulation of hue is an absolute rotation of -180 degrees to +180 degrees from the current position corresponding to an argument range of 0 to 2.0 (1.0 for no change).  
negateImage | bool grayscale_ = false | Negate colors in image. Replace every pixel with its complementary color (white becomes black, yellow becomes blue, etc.). Set grayscale to only negate grayscale values in image.  
normalizeImage | void | Normalize image (increase contrast by normalizing the pixel values to span the full range of color values).  
oilPaintImage | size_t radius_ = 3 | Oilpaint image (image looks like oil painting)  
opacityImage | size_t opacity_ | Set or attenuate the opacity channel in the image. If the image pixels are opaque then they are set to the specified opacity value, otherwise they are blended with the supplied opacity value. The value of opacity_ ranges from 0 (completely opaque) to _QuantumRange_. The defines _OpaqueOpacity_ and _TransparentOpacity_ are available to specify completely opaque or completely transparent, respectively.  
opaqueImage | const [Color](Color.html) &opaqueColor_, const [Color](Color.html) &penColor_ | Change color of pixels matching opaqueColor_ to specified penColor_.  
quantizeImage | bool measureError_ = false | Quantize image (reduce number of colors). Set measureError_ to true in order to calculate error attributes.  
raiseImage | const [Geometry](Geometry.html) &geometry_ = "6x6+0+0", bool raisedFlag_ = false | Raise image (lighten or darken the edges of an image to give a 3-D raised or lowered effect)  
reduceNoise-   
Image | void | Reduce noise in image using a noise peak elimination filter.  
size_t order_  
rollImage | int columns_, ssize_t rows_ | Roll image (rolls image vertically and horizontally) by specified number of columnms and rows)  
rotateImage | double degrees_ | Rotate image counter-clockwise by specified number of degrees  
sampleImage | const [Geometry](Geometry.html) &geometry_ | Resize image by using pixel sampling algorithm  
scaleImage | const [Geometry](Geometry.html) &geometry_ | Resize image by using simple ratio algorithm  
segmentImage | double clusterThreshold_ = 1.0,   
double smoothingThreshold_ = 1.5 | Segment (coalesce similar image components) by analyzing the histograms of the color components and identifying units that are homogeneous with the fuzzy c-means technique. Also uses _quantizeColorSpace_ and _verbose_ image attributes. Specify _clusterThreshold__ , as the number of pixels each cluster must exceed the cluster threshold to be considered valid. _SmoothingThreshold__ eliminates noise in the second derivative of the histogram. As the value is increased, you can expect a smoother second derivative. The default is 1.5.  
shadeImage | double azimuth_ = 30, double elevation_ = 30,   
bool colorShading_ = false | Shade image using distant light source. Specify _azimuth__ and _elevation__ as the position of the light source. By default, the shading results as a grayscale image.. Set c _olorShading__ to _true_ to shade the red, green, and blue components of the image.  
sharpenImage | const double radius_ = 1, const double sigma_ = 0.5 | Sharpen pixels in image. The radius_ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The sigma_ parameter specifies the standard deviation of the Laplacian, in pixels.  
shaveImage | const [Geometry](Geometry.html) &geometry_ | Shave pixels from image edges.  
shearImage | double xShearAngle_, double yShearAngle_ | Shear image (create parallelogram by sliding image by X or Y axis). Shearing slides one edge of an image along the X or Y axis, creating a parallelogram. An X direction shear slides an edge along the X axis, while a Y direction shear slides an edge along the Y axis. The amount of the shear is controlled by a shear angle. For X direction shears, x degrees is measured relative to the Y axis, and similarly, for Y direction shears y degrees is measured relative to the X axis. Empty triangles left over from shearing the image are filled with the color defined as _borderColor_.  
solarizeImage | double factor_ | Solarize image (similar to effect seen when exposing a photographic film to light during the development process)  
spreadImage | size_t amount_ = 3 | Spread pixels randomly within image by specified amount  
steganoImage | const [Image](Image++.html) &watermark_ | Add a digital watermark to the image (based on second image)  
stereoImage | const [Image](Image++.html) &rightImage_ | Create an image which appears in stereo when viewed with red-blue glasses (Red image on left, blue on right)  
swirlImage | double degrees_ | Swirl image (image pixels are rotated by degrees)  
textureImage | const [Image](Image++.html) &texture_ | Layer a texture on image background  
thresholdImage | double threshold_ | Threshold image  
transformImage | const [Geometry](Geometry.html) &imageGeometry_ | Transform image based on image and crop geometries. Crop geometry is optional.  
const [Geometry](Geometry.html) &imageGeometry_, const [Geometry](Geometry.html) &cropGeometry_  
transparentImage | const [Color](Color.html) &color_ | Add matte image to image, setting pixels matching color to transparent.  
trimImage | void | Trim edges that are the background color from the image.  
waveImage | double amplitude_ = 25.0, double wavelength_ = 150.0 | Alter an image along a sine wave.  
zoomImage | const [Geometry](Geometry.html) &geometry_ | Zoom image to specified size.  



Function objects are available to set attributes on image frames which are equivalent to methods in the Image object. These function objects allow setting an option across a range of image frames using f` or_each()`. 

The following code is an example of how the color 'red' may be set to transparent in a GIF animation: 
    
    
    list<image> images; 
    readImages( &images, "animation.gif" ); 
    for_each ( images.begin(), images.end(), transparentImage( "red" )  ); 
    writeImages( images.begin(), images.end(), "animation.gif" );
    

The available function objects for setting image attributes are   


Image Attributes **Attribute** |  **Type** |  **Constructor Signature(s)** |  **Description**  
---|---|---|---  
adjoinImage | bool | bool flag_ | Join images into a single multi-image file.  
antiAliasImage | bool | bool flag_ | Control antialiasing of rendered Postscript and Postscript or TrueType fonts. Enabled by default.  
animation-   
DelayImage | size_t (0 to 65535) | size_t delay_ | Time in 1/100ths of a second (0 to 65535) which must expire before displaying the next image in an animated sequence. This option is useful for regulating the animation of a sequence of GIF images within Netscape.  
animation-   
IterationsImage | size_t | size_t iterations_ | Number of iterations to loop an animation (e.g. Netscape loop extension) for.  
background-   
ColorImage | [Color](Color.html) | const [Color](Color.html) &color_ | Image background color  
background-   
TextureImage | std::string | const string &texture_ | Image to use as background texture.  
borderColor-   
Image | [Color](Color.html) |  const [Color](Color.html) &color_ | Image border color  
boxColorImage | [Color](Color.html) | const [Color](Color.html) &boxColor_ | Base color that annotation text is rendered on.  
chroma-   
BluePrimaryImage | double x & y | double x_, double y_ | Chromaticity blue primary point (e.g. x=0.15, y=0.06)  
chroma-   
GreenPrimaryImage | double x & y | double x_, double y_ | Chromaticity green primary point (e.g. x=0.3, y=0.6)  
chroma-   
RedPrimaryImage | double x & y | double x_, double y_ | Chromaticity red primary point (e.g. x=0.64, y=0.33)  
chroma-   
WhitePointImage | double x & y | double x_, double y_ | Chromaticity white point (e.g. x=0.3127, y=0.329)  
colorFuzzImage | double | double fuzz_ | Colors within this distance are considered equal. A number of algorithms search for a target color. By default the color must be exact. Use this option to match colors that are close to the target color in RGB space.  
colorMapImage | [Color](Color.html) | size_t index_, const [Color](Color.html) &color_ | Color at color-pallet index.  
colorSpaceImage | [ColorspaceType](Enumerations.html#ColorspaceType) | [ColorspaceType](Enumerations.html#ColorspaceType) colorSpace_ | The colorspace (e.g. CMYK) used to represent the image pixel colors. Image pixels are always stored as RGB(A) except for the case of CMY(K).  
composeImage | [CompositeOperator](Enumerations.html#CompositeOperator) | [CompositeOperator](Enumerations.html#CompositeOperator) compose_ | Composition operator to be used when composition is implicitly used (such as for image flattening).  
compressType-   
Image | [CompressionType](Enumerations.html#CompressionType) | [CompressionType](Enumerations.html#CompressionType) compressType_ | Image compresion type. The default is the compression type of the specified image file.  
densityImage | [Geometry](Geometry.html) (default 72x72) | const [Geometry](Geometry.html) &density_ | Vertical and horizontal resolution in pixels of the image. This option specifies an image density when decoding a Postscript or Portable Document page. Often used with _psPageSize_.  
depthImage | size_t (8 or 16) | size_t depth_ | Image depth. Used to specify the bit depth when reading or writing raw images or thwn the output format supports multiple depths. Defaults to the quantum depth that ImageMagick is compiled with.  
endianImage | [EndianType](Enumerations.html#EndianType) | [EndianType](Enumerations.html#EndianType) endian_ | Specify (or obtain) endian option for formats which support it.  
fileNameImage | std::string | const std::string &fileName_ | Image file name.  
fillColorImage | Color | const Color &fillColor_ | Color to use when filling drawn objects  
filterTypeImage | [FilterTypes](Enumerations.html#FilterTypes) | [FilterTypes](Enumerations.html#FilterTypes) filterType_ | Filter to use when resizing image. The reduction filter employed has a sigificant effect on the time required to resize an image and the resulting quality. The default filter is _Lanczos_ which has been shown to produce good results when reducing images.  
fontImage | std::string | const std::string &font_ | Text rendering font. If the font is a fully qualified X server font name, the font is obtained from an X server. To use a TrueType font, precede the TrueType filename with an @. Otherwise, specify a Postscript font name (e.g. "helvetica").  
fontPointsize-   
Image | size_t | size_t pointSize_ | Text rendering font point size  
gifDispose-   
MethodImage | size_t   
{ 0 = Disposal not specified,   
1 = Do not dispose of graphic,   
3 = Overwrite graphic with background color,   
4 = Overwrite graphic with previous graphic. } | size_t disposeMethod_ | layer disposal method. This option is used to control how successive frames are rendered (how the preceding frame is disposed of) when creating a GIF animation.  
interlace-   
TypeImage | [InterlaceType](Enumerations.html#InterlaceType) | [InterlaceType](Enumerations.html#InterlaceType) interlace_ | The type of interlacing scheme (default _NoInterlace_ ). This option is used to specify the type of interlacing scheme for raw image formats such as RGB or YUV. _NoInterlace_ means do not interlace, _LineInterlace_ uses scanline interlacing, and _PlaneInterlace_ uses plane interlacing. _PartitionInterlace_ is like _PlaneInterlace_ except the different planes are saved to individual files (e.g. image.R, image.G, and image.B). Use _LineInterlace_ or _PlaneInterlace_ to create an interlaced GIF or progressive JPEG image.  
isValidImage | bool | bool isValid_ | Set image validity. Valid images become empty (inValid) if argument is false.  
labelImage | std::string | const std::string &label_ | Image label  
lineWidthImage | double | double lineWidth_ | Line width for drawing lines, circles, ellipses, etc. See [Drawable](Drawable.html) .  
magickImage | std::string |  const std::string &magick_ | Get image format (e.g. "GIF")  
matteImage | bool | bool matteFlag_ | True if the image has transparency. If set True, store matte channel if the image has one otherwise create an opaque one.  
matteColorImage | [Color](Color.html) | const [Color](Color.html) &matteColor_ | Image matte (frame) color  
monochrome-   
Image | bool | bool flag_ | Transform the image to black and white  
pageImage | [Geometry](Geometry.html#PostscriptPageSize) | const [Geometry](Geometry.html#PostscriptPageSize) &pageSize_ | Preferred size and location of an image canvas. Use this option to specify the dimensions and position of the Postscript page in dots per inch or a TEXT page in pixels. This option is typically used in concert with _[density](STL.html#density) _. Page may also be used to position a GIF image (such as for a scene in an animation)  
penColorImage | [Color](Color.html) | const [Color](Color.html) &penColor_ | Pen color to use when annotating on or drawing on image.  
penTextureImage | [Image](Image++.html) | const Image & penTexture_ | Texture image to paint with (similar to penColor).  
pixelColorImage | [Color](Color.html) | size_t x_, size_t y_, const [ Color](Color.html) &color_ | Get/set pixel color at location x & y.  
psPageSizeImage | [Geometry](Geometry.html#PostscriptPageSize) | const [Geometry](Geometry.html#PostscriptPageSize) &pageSize_ | Postscript page size. Use this option to specify the dimensions of the Postscript page in dots per inch or a TEXT page in pixels. This option is typically used in concert with _density_.  
qualityImage | size_t (0 to 100) | size_t quality_ | JPEG/MIFF/PNG compression level (default 75).  
quantize-   
ColorsImage | size_t | size_t colors_ | Preferred number of colors in the image. The actual number of colors in the image may be less than your request, but never more. Images with less unique colors than specified with this option will have any duplicate or unused colors removed.  
quantize-   
ColorSpaceImage | [ColorspaceType](Enumerations.html#ColorspaceType) | [ColorspaceType](Enumerations.html#ColorspaceType) colorSpace_ | Colorspace to quantize colors in (default RGB). Empirical evidence suggests that distances in color spaces such as YUV or YIQ correspond to perceptual color differences more closely than do distances in RGB space. These color spaces may give better results when color reducing an image.  
quantize-   
DitherImage | bool | bool flag_ | Apply Floyd/Steinberg error diffusion to the image. The basic strategy of dithering is to trade intensity resolution for spatial resolution by averaging the intensities of several neighboring pixels. Images which suffer from severe contouring when reducing colors can be improved with this option. The quantizeColors or monochrome option must be set for this option to take effect.  
quantize-   
TreeDepthImage | size_t (0 to 8) | size_t treeDepth_ | Depth of the quantization color classification tree. Values of 0 or 1 allow selection of the optimal tree depth for the color reduction algorithm. Values between 2 and 8 may be used to manually adjust the tree depth.  
rendering-   
IntentImage | [RenderingIntent](Enumerations.html#RenderingIntent) | [RenderingIntent](Enumerations.html#RenderingIntent) render_ | The type of rendering intent  
resolution-   
UnitsImage | [ResolutionType](Enumerations.html#ResolutionType) | [ResolutionType](Enumerations.html#ResolutionType) units_ | Units of image resolution  
sceneImage | size_t | size_t scene_ | Image scene number  
sizeImage | [Geometry](Geometry.html) | const [Geometry](Geometry.html) &geometry_ | Width and height of a raw image (an image which does not support width and height information). Size may also be used to affect the image size read from a multi-resolution format (e.g. Photo CD, JBIG, or JPEG.  
stripImage | void | strips an image of all profiles and comments.  
strokeColorImage | [Color](Color.html) | const [Color](Color.html) &strokeColor_ | Color to use when drawing object outlines  
subImageImage | size_t | size_t subImage_ | Subimage of an image sequence  
subRangeImage | size_t | size_t subRange_ | Number of images relative to the base image  
tileNameImage | std::string | const std::string &tileName_ | Tile name  
typeImage | [ImageType](Enumerations.html#ImageType) | [ImageType](Enumerations.html#ImageType) type_ | Image storage type.  
verboseImage | bool | bool verboseFlag_ | Print detailed information about the image  
viewImage | std::string | const std::string &view_ | FlashPix viewing parameters.  
x11DisplayImage | std::string (e.g. "hostname:0.0") | const std::string &display_ | X11 display to display to, obtain fonts from, or to capture image from  

  


###  Query Image Format Support

Magick++ provides the _coderInfoList()_ function to support obtaining information about the image formats supported by ImageMagick. Support for image formats in ImageMagick is provided by modules known as "coders". A user-provided container is updated based on a boolean truth-table match. The truth-table supports matching based on whether ImageMagick can read the format, write the format, or supports multiple frames for the format. A wildcard specifier is supported for any "don't care" field. The data obtained via coderInfoList() may be useful for preparing GUI dialog boxes or for deciding which output format to write based on support within the ImageMagick build.

The definition of coderInfoList is: 
    
    
    class CoderInfo 
      { 
      public:
    
        enum MatchType { 
          AnyMatch,  // match any coder 
          TrueMatch, // match coder if true 
          FalseMatch // match coder if false 
        };
    
        [ remaining CoderInfo methods ]
    
       }
    
      template <class Container > 
      void coderInfoList( Container *container_, 
                          CoderInfo::MatchType isReadable_   = CoderInfo::AnyMatch, 
                          CoderInfo::MatchType isWritable_   = CoderInfo::AnyMatch, 
                          CoderInfo::MatchType isMultiFrame_ = CoderInfo::AnyMatch 
                          );
    

The following example shows how to retrieve a list of all of the coders which support reading images and print the coder attributes (all listed formats will be readable): 
    
    
      list<CoderInfo> coderList; 
      coderInfoList( &coderList,           // Reference to output list 
                     CoderInfo::TrueMatch, // Match readable formats 
                     CoderInfo::AnyMatch,  // Don't care about writable formats 
                     CoderInfo::AnyMatch); // Don't care about multi-frame support 
      list<CoderInfo>::iterator entry = coderList.begin(); 
      while( entry != coderList.end() ) 
      { 
        cout << entry->name() << ": (" << entry->description() << ") : "; 
        cout << "Readable = "; 
        if ( entry->isReadable() ) 
          cout << "true"; 
        else 
          cout << "false"; 
        cout << ", "; 
        cout << "Writable = "; 
        if ( entry->isWritable() ) 
          cout << "true"; 
        else 
          cout << "false"; 
        cout << ", "; 
        cout << "Multiframe = "; 
        if ( entry->isMultiframe() ) 
          cout << "true"; 
        else 
          cout << "false"; 
        cout << endl;
        entry ++;
       } 
    

` }`

### Obtaining A Color Histogram

Magick++ provides the colorHistogram template function to retrieve a color histogram from an image. A color histogram provides a count of how many times each color occurs in the image. The histogram is written into a user-provided container, which (for example) could be a <vector> or a <map>.  When a <map> is used, the Color is used as the key so that quick lookups of usage counts for colors may be performed. Writing into a <map> may be slower than writing into a <vector> since the <map> sorts the entries (by color intensity) and checks for uniqueness. Each histogram entry is contained in type std::pair<Magick::Color,unsigned long> with the first member of the pair being a Color, and the second member of the pair being an 'unsigned long'. Use the <pair> "first" member to access the Color and the "second" member to access the number of times the color occurs in the image.

The template function declaration is as follows:  

    
    
    template <class Container >
    void colorHistogram( Container *histogram_, const Image image)
    

The following examples illustrate using both a <map> and a <vector> to retrieve the color histogram, and print out a formatted summary.  
  
Using <map>:  
  

    
    
      Image image("image.miff");
      map<Color,unsigned long> histogram;
      colorHistogram( &histogram, image );
      std::map<Color,unsigned long>::const_iterator p=histogram.begin();
      while (p != histogram.end())
        {
          cout << setw(10) << (int)p->second << ": ("
               << setw(quantum_width) << (int)p->first.redQuantum() << ","
               << setw(quantum_width) << (int)p->first.greenQuantum() << ","
               << setw(quantum_width) << (int)p->first.blueQuantum() << ")"
               << endl;
           p++;
        }
    

  
Using <vector>:  
  

    
    
      Image image("image.miff");
      std::vector<std::pair<Color,unsigned long> > histogram;
      colorHistogram( &histogram, image );
      std::vector<std::pair<Color,unsigned long> >::const_iterator p=histogram.begin();
      while (p != histogram.end())
        {
          cout << setw(10) << (int)p->second << ": ("
               << setw(quantum_width) << (int)p->first.redQuantum() << ","
               << setw(quantum_width) << (int)p->first.greenQuantum() << ","
               << setw(quantum_width) << (int)p->first.blueQuantum() << ")"
               << endl;
          p++;
        }
    
