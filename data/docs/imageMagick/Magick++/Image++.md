#  Magick::Image Class  
  
####  Quick Contents

  * [BLOBs](Image++.html#BLOBs)
  * [Constructors](Image++.html#Constructors)
  * [Image Manipulation Methods](Image++.html#Image%20Manipulation%20Methods)
  * [Image Attributes](Image++.html#Image%20Attributes)
  * [Low-Level Image Pixel Access](Image++.html#Raw%20Image%20Pixel%20Access)



Image is the primary object in Magick++ and represents a single image frame (see [design](ImageDesign.html) ). The [STL interface](STL.html) **must** be used to operate on image sequences or images (e.g. of format GIF, TIFF, MIFF, Postscript, & MNG) which are comprized of multiple image frames. Individual frames of a multi-frame image may be requested by adding array-style notation to the end of the file name (e.g. "animation.gif[3]" retrieves the fourth frame of a GIF animation. Various image manipulation operations may be applied to the image. Attributes may be set on the image to influence the operation of the manipulation operations. The [ Pixels](Pixels.html) class provides low-level access to image pixels. As a convenience, including `<Magick++.h>` is sufficient in order to use the complete Magick++ API. The Magick++ API is enclosed within the _Magick_ namespace so you must either add the prefix "` Magick::` " to each class/enumeration name or add the statement "` using namespace Magick;`" after including the `Magick++.h` header.

The preferred way to allocate Image objects is via automatic allocation (on the stack). There is no concern that allocating Image objects on the stack will excessively enlarge the stack since Magick++ allocates all large data objects (such as the actual image data) from the heap. Use of automatic allocation is preferred over explicit allocation (via _new_) since it is much less error prone and allows use of C++ scoping rules to avoid memory leaks. Use of automatic allocation allows Magick++ objects to be assigned and copied just like the C++ intrinsic data types (e.g. '_int_ '), leading to clear and easy to read code. Use of automatic allocation leads to naturally exception-safe code since if an exception is thrown, the object is automagically deallocated once the stack unwinds past the scope of the allocation (not the case for objects allocated via _new_ ). 

Image is very easy to use. For example, here is a the source to a program which reads an image, crops it, and writes it to a new file (the exception handling is optional but strongly recommended): 
    
    
    #include <Magick++.h> 
    #include <iostream> 
    using namespace std; 
    using namespace Magick; 
    int main(int argc,char **argv) 
    { 
      InitializeMagick(*argv);
    
      // Construct the image object. Seperating image construction from the 
      // the read operation ensures that a failure to read the image file 
      // doesn't render the image object useless. 
      Image image;
      try { 
        // Read a file into image object 
        image.read( "girl.gif" );
    
        // Crop the image to specified size (width, height, xOffset, yOffset)
        image.crop( Geometry(100,100, 100, 100) );
    
        // Write the image to a file 
        image.write( "x.gif" ); 
      } 
      catch( Exception &error_ ) 
        { 
          cout << "Caught exception: " << error_.what() << endl; 
          return 1; 
        } 
      return 0; 
    }
    

The following is the source to a program which illustrates the use of Magick++'s efficient reference-counted assignment and copy-constructor operations which minimize use of memory and eliminate unncessary copy operations (allowing Image objects to be efficiently assigned, and copied into containers). The program accomplishes the following: 

  1. Read master image.
  2. Assign master image to second image.
  3. Resize second image to the size 640x480.
  4. Assign master image to a third image.
  5. Resize third image to the size 800x600.
  6. Write the second image to a file.
  7. Write the third image to a file.


    
    
    #include <Magick++.h> 
    #include <iostream> 
    using namespace std; 
    using namespace Magick; 
    int main(int argc,char **argv) 
    { 
      InitializeMagick(*argv);
    
      Image master("horse.jpg"); 
      Image second = master; 
      second.resize("640x480"); 
      Image third = master; 
      third.resize("800x600"); 
      second.write("horse640x480.jpg"); 
      third.write("horse800x600.jpg"); 
      return 0; 
    }
    

During the entire operation, a maximum of three images exist in memory and the image data is never copied. 

The following is the source for another simple program which creates a 100 by 100 pixel white image with a red pixel in the center and writes it to a file: 
    
    
    #include <Magick++.h> 
    using namespace std; 
    using namespace Magick; 
    int main(int argc,char **argv) 
    { 
      InitializeMagick(*argv);
      Image image( "100x100", "white" ); 
      image.pixelColor( 49, 49, "red" ); 
      image.write( "red_pixel.png" ); 
      return 0; 
    }
    

If you wanted to change the color image to grayscale, you could add the lines: 
    
    
    image.quantizeColorSpace( GRAYColorspace ); 
    image.quantizeColors( 256 ); 
    image.quantize( );
    

or, more simply: 
    
    
     image.type( GrayscaleType );
    

prior to writing the image. 

###  BLOBs

While encoded images (e.g. JPEG) are most often written-to and read-from a disk file, encoded images may also reside in memory. Encoded images in memory are known as BLOBs (Binary Large OBjects) and may be represented using the [Blob](Blob.html) class. The encoded image may be initially placed in memory by reading it directly from a file, reading the image from a database, memory-mapped from a disk file, or could be written to memory by Magick++. Once the encoded image has been placed within a Blob, it may be read into a Magick++ Image via a [constructor](Image++.html#constructor_blob) or [read()](Image++.html#read) . Likewise, a Magick++ image may be written to a Blob via [ write()](Image++.html#write) . 

An example of using Image to write to a Blob follows:   

    
    
    #include >Magick++.h> 
    using namespace std; 
    using namespace Magick; 
    int main(int argc,char **argv) 
    { 
      InitializeMagick(*argv);
    
      // Read GIF file from disk 
      Image image( "giraffe.gif" );
      // Write to BLOB in JPEG format 
      Blob blob; 
      image.magick( "JPEG" ) // Set JPEG output format 
      image.write( &blob );
    
      [ Use BLOB data (in JPEG format) here ]
    
      return 0; 
    }
    

  
likewise, to read an image from a Blob, you could use one of the following examples: 

[ Entry condition for the following examples is that _data_ is pointer to encoded image data and _length_ represents the size of the data ] 
    
    
    Blob blob( data, length ); 
    Image image( blob );
    

or 
    
    
    Blob blob( data, length ); 
    Image image; 
    image.read( blob);
    

some images do not contain their size or format so the size and format must be specified in advance: 
    
    
    Blob blob( data, length ); 
    Image image; 
    image.size( "640x480") 
    image.magick( "RGBA" ); 
    image.read( blob);
    

###  Constructors

Image may be constructed in a number of ways. It may be constructed from a file, a URL, or an encoded image (e.g. JPEG) contained in an in-memory [ BLOB](Blob.html) . The available Image constructors are shown in the following table:   
  
**Image Constructors** **Signature** |  **Description**  
---|---  
const std::string &imageSpec_ | Construct Image by reading from file or URL specified by _imageSpec__. Use array notation (e.g. filename[9]) to select a specific scene from a multi-frame image.  
const Geometry &size_, const [ Color](Color.html) &color_ | Construct a blank image canvas of specified size and color  
const [Blob](Blob.html) &blob_ | Construct Image by reading from encoded image data contained in an in-memory [BLOB](Blob.html) . Depending on the constructor arguments, the Blob [size](Image++.html#size) , [depth](Image++.html#depth) , [magick](Image++.html#magick) (format) may also be specified. Some image formats require that size be specified. The default ImageMagick uses for depth depends on the compiled-in Quantum size (8 or 16). If ImageMagick's Quantum size does not match that of the image, the depth may need to be specified. ImageMagick can usually automagically detect the image's format. When a format can't be automagically detected, the format ([magick](Image++.html#magick) ) must be specified.  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size_  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size, size_t depth  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size, size_t depth_, const string &magick_  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size, const string &magick_  
const size_t width_,   
const size_t height_,   
std::string map_,   
const [ StorageType](Enumerations.html#StorageType) type_,   
const void *pixels_ | Construct a new Image based on an array of image pixels. The pixel data must be in scanline order top-to-bottom. The data can be character, short int, integer, float, or double. Float and double require the pixels to be normalized [0..1]. The other types are [0..MaxRGB]. For example, to create a 640x480 image from unsigned red-green-blue character data, use Image image( 640, 480, "RGB", 0, pixels ); The parameters are as follows:   
| width_ | Width in pixels of the image.  
---|---  
height_ | Height in pixels of the image.  
map_ | This character string can be any combination or order of R = red, G = green, B = blue, A = alpha, C = cyan, Y = yellow M = magenta, and K = black. The ordering reflects the order of the pixels in the supplied pixel array.  
type_ | [Pixel storage type](Enumerations.html#StorageType) (CharPixel, ShortPixel, IntegerPixel, FloatPixel, or DoublePixel)  
pixels_ | This array of values contain the pixel components as defined by the map_ and type_ parameters. The length of the arrays must equal the area specified by the width_ and height_ values and type_ parameters.  
  
###  Image Manipulation Methods

_Image_ supports access to all the single-image (versus image-list) manipulation operations provided by the ImageMagick library. If you must process a multi-image file (such as an animation), the [ STL interface](STL.html) , which provides a multi-image abstraction on top of _Image_ , must be used. 

Image manipulation methods are very easy to use. For example: 
    
    
    Image image; 
    image.read("myImage.tiff"); 
    image.addNoise(GaussianNoise); 
    image.write("myImage.tiff");
    

adds gaussian noise to the image file "myImage.tiff". 

The operations supported by Image are shown in the following table:   


**Image Image Manipulation Methods** **Method** | **Signature(s)** | **Description**  
---|---|---  
adaptiveThreshold  
| size_t width, size_t height, size_t offset = 0  
| Apply adaptive thresholding to the image. Adaptive thresholding is useful if the ideal threshold level is not known in advance, or if the illumination gradient is not constant across the image. Adaptive thresholding works by evaulating the mean (average) of a pixel region (size specified by _width_ and _height_) and using the mean as the thresholding value. In order to remove residual noise from the background, the threshold may be adjusted by subtracting a constant _offset_ (default zero) from the mean to compute the threshold.  
  
addNoise | [NoiseType](Enumerations.html#NoiseType) noiseType_ | Add noise to image with specified noise type.  
addNoiseChannel  
| const ChannelType channel_, const NoiseType noiseType_  
| Add noise to an image channel with the specified noise type. The channel_ parameter specifies the channel to add noise to. The noiseType_ parameter specifies the type of noise.  
  
affineTransform  
| const DrawableAffine &affine  
| Transform image by specified affine (or free transform) matrix.  
  
annotate | const std::string &text_, const [ Geometry](Geometry.html) &location_ | Annotate using specified text, and placement location  
string text_, const [Geometry](Geometry.html) &boundingArea_, [GravityType](Enumerations.html#GravityType) gravity_ | Annotate using specified text, bounding area, and placement gravity. If _boundingArea__ is invalid, then bounding area is entire image.  
const std::string &text_, const [ Geometry](Geometry.html) &boundingArea_, [GravityType](Enumerations.html#GravityType) gravity_, double degrees_, | Annotate with text using specified text, bounding area, placement gravity, and rotation. If _boundingArea__ is invalid, then bounding area is entire image.  
const std::string &text_, [ GravityType](Enumerations.html#GravityType) gravity_ | Annotate with text (bounding area is entire image) and placement gravity.  
blur | const double radius_ = 1, const double sigma_ = 0.5 | Blur image. The _radius__ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma__ parameter specifies the standard deviation of the Laplacian, in pixels.  
blurChannel  
| const ChannelType channel_, const double radius_ = 0.0, const double sigma_ = 1.0  
| Blur an image channel. The channel_ parameter specifies the channel to blur. The _radius__ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma__ parameter specifies the standard deviation of the Laplacian, in pixels.  
border | const [Geometry](Geometry.html) &geometry_ = "6x6+0+0" | Border image (add border to image). The color of the border is specified by the _borderColor_ attribute.  
cdl | const std::string &cdl_ | color correct with a color decision list. See <http://en.wikipedia.org/wiki/ASC_CDL> for details.  
channel | [ChannelType](Enumerations.html#ChannelType) layer_ | Extract channel from image. Use this option to extract a particular channel from the image. _MatteChannel_ for example, is useful for extracting the opacity values from an image.  
charcoal | const double radius_ = 1, const double sigma_ = 0.5 | Charcoal effect image (looks like charcoal sketch). The _radius__ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma__ parameter specifies the standard deviation of the Laplacian, in pixels.  
chop | const [Geometry](Geometry.html) &geometry_ | Chop image (remove vertical or horizontal subregion of image)  
colorize | const unsigned int opacityRed_, const unsigned int opacityGreen_, const unsigned int opacityBlue_, const Color &penColor_ | Colorize image with pen color, using specified percent opacity for red, green, and blue quantums.  
colorMatrix | const size_t order_, const double *color_matrix_ | apply color correction to the image.  
comment | const std::string &comment_ | Comment image (add comment string to image). By default, each image is commented with its file name. Use this method to assign a specific comment to the image. Optionally you can include the image filename, type, width, height, or other image attributes by embedding [special format characters.](FormatCharacters.html)  
compare  
| const Image &reference_  
| Compare current image with another image. Sets [meanErrorPerPixel](Image++.html#meanErrorPerPixel) , [normalizedMaxError](Image++.html#normalizedMaxError) , and [normalizedMeanError](Image++.html#normalizedMeanError) in the current image. False is returned if the images are identical. An ErrorOption exception is thrown if the reference image columns, rows, colorspace, or matte differ from the current image.  
  
composite | const [Image](Image++.html) &compositeImage_, ssize_t xOffset_, ssize_t yOffset_, [ CompositeOperator](Enumerations.html#CompositeOperator) compose_ = _InCompositeOp_ | Compose an image onto the current image at offset specified by _xOffset__ , _yOffset__ using the composition algorithm specified by _compose__.  
const [Image](Image++.html) &compositeImage_, const [Geometry](Geometry.html) &offset_, [CompositeOperator](Enumerations.html#CompositeOperator) compose_ = _InCompositeOp_ | Compose an image onto the current image at offset specified by _offset__ using the composition algorithm specified by _compose__ .  
const [Image](Image++.html) &compositeImage_, [GravityType](Enumerations.html#GravityType) gravity_, [CompositeOperator](Enumerations.html#CompositeOperator) compose_ = _InCompositeOp_ | Compose an image onto the current image with placement specified by _gravity__ using the composition algorithm specified by _compose__.  
contrast | size_t sharpen_ | Contrast image (enhance intensity differences in image)  
convolve | size_t order_, const double *kernel_ | Convolve image. Applies a user-specfied convolution to the image. The _order__ parameter represents the number of columns and rows in the filter kernel, and _kernel__ is a two-dimensional array of doubles representing the convolution kernel to apply.  
crop | const [Geometry](Geometry.html) &geometry_ | Crop image (subregion of original image)  
cycleColormap | int amount_ | Cycle image colormap  
despeckle | void | Despeckle image (reduce speckle noise)  
display | void | Display image on screen.   
**Caution:** if an image format is is not compatible with the display visual (e.g. JPEG on a colormapped display) then the original image will be altered. Use a copy of the original if this is a problem.  
distort | const DistortImageMethod method, const size_t number_arguments, const double *arguments, const bool bestfit = false  | Distort image. Applies a user-specfied distortion to the image.  
draw | const [Drawable](Drawable.html) &drawable_ | Draw shape or text on image.  
const std::list<[Drawable](Drawable.html) > &drawable_ | Draw shapes or text on image using a set of Drawable objects contained in an STL list. Use of this method improves drawing performance and allows batching draw objects together in a list for repeated use.  
edge | size_t radius_ = 0.0 | Edge image (hilight edges in image). The radius is the radius of the pixel neighborhood.. Specify a radius of zero for automatic radius selection.  
emboss | const double radius_ = 1, const double sigma_ = 0.5 | Emboss image (hilight edges with 3D effect). The _radius__ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma__ parameter specifies the standard deviation of the Laplacian, in pixels.  
enhance | void | Enhance image (minimize noise)  
equalize | void | Equalize image (histogram equalization)  
erase | void | Set all image pixels to the current background color.  
extent | const [ Geometry](Geometry.html) &geometry_ | extends the image as defined by the geometry, gravity, and image background color.  
const [Geometry](Geometry.html) &geometry_, const [Color](Color.html) &backgroundColor_  
const [ Geometry](Geometry.html) &geometry_, const [GravityType](Enumerations.html#GravityType) &gravity_ | extends the image as defined by the geometry, gravity, and image background color.  
const [Geometry](Geometry.html) &geometry_, const [Color](Color.html) &backgroundColor_, const [GravityType](Enumerations.html#GravityType) &gravity_  
flip | void | Flip image (reflect each scanline in the vertical direction)  
floodFill-   
Color | ssize_t x_, ssize_t y_, const [ Color](Color.html) &fillColor_ | Flood-fill color across pixels that match the color of the target pixel and are neighbors of the target pixel. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const [Color](Color.html) &fillColor_  
ssize_t x_, ssize_t y_, const [ Color](Color.html) &fillColor_, const [Color](Color.html) &borderColor_ | Flood-fill color across pixels starting at target-pixel and stopping at pixels matching specified border color. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const [Color](Color.html) &fillColor_, const [Color](Color.html) &borderColor_  
floodFillOpacity | const long x_, const long y_, const unsigned int opacity_, const PaintMethod method_ | Floodfill pixels matching color (within fuzz factor) of target pixel(x,y) with replacement opacity value using method.  
floodFill-   
Texture | ssize_t x_, ssize_t y_, const Image &texture_ | Flood-fill texture across pixels that match the color of the target pixel and are neighbors of the target pixel. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const Image &texture_  
ssize_t x_, ssize_t y_, const Image &texture_, const [Color](Color.html) &borderColor_ | Flood-fill texture across pixels starting at target-pixel and stopping at pixels matching specified border color. Uses current fuzz setting when determining color match.  
const [Geometry](Geometry.html) &point_, const Image &texture_, const [ Color](Color.html) &borderColor_  
flop | void | Flop image (reflect each scanline in the horizontal direction)  
frame | const [Geometry](Geometry.html) &geometry_ = "25x25+6+6" | Add decorative frame around image  
size_t width_, size_t height_, ssize_t x_, ssize_t y_, ssize_t innerBevel_ = 0, ssize_t outerBevel_ = 0  
fx | const std::string expression, const Magick::ChannelType channel | Fx image. Applies a mathematical expression to the image.  
gamma | double gamma_ | Gamma correct image (uniform red, green, and blue correction).  
double gammaRed_, double gammaGreen_, double gammaBlue_ | Gamma correct red, green, and blue channels of image.  
gaussianBlur | const double width_, const double sigma_ | Gaussian blur image. The number of neighbor pixels to be included in the convolution mask is specified by 'width_'. For example, a width of one gives a (standard) 3x3 convolution mask. The standard deviation of the gaussian bell curve is specified by 'sigma_'.  
gaussianBlurChannel  
| const ChannelType channel_, const double radius_ = 0.0, const double sigma_ = 1.0  
| Gaussian blur an image channel. The channel_ parameter specifies the channel to blur. The number of neighbor pixels to be included in the convolution mask is specified by 'width_'. For example, a width of one gives a (standard) 3x3 convolution mask. The standard deviation of the gaussian bell curve is specified by 'sigma_'.  
haldClut  
| const Image &reference_  
| apply a Hald color lookup table to the image.  
  
implode | const double factor_ | Implode image (special effect)  
inverseFourierTransform | const Image &phaseImage_, const bool magnitude_ | implements the inverse discrete Fourier transform (DFT) of the image either as a magnitude / phase or real / imaginary image pair.  
label | const string &label_ | Assign a label to an image. Use this option to assign a specific label to the image. Optionally you can include the image filename, type, width, height, or scene number in the label by embedding [ special format characters.](FormatCharacters.html) If the first character of string is @, the image label is read from a file titled by the remaining characters in the string. When converting to Postscript, use this option to specify a header string to print above the image.  
level  
| const double black_point, const double white_point, const double mid_point=1.0  
| Level image. Adjust the levels of the image by scaling the colors falling between specified white and black points to the full available quantum range. The parameters provided represent the black, mid (gamma), and white points. The black point specifies the darkest color in the image. Colors darker than the black point are set to zero. Mid point (gamma) specifies a gamma correction to apply to the image. White point specifies the lightest color in the image. Colors brighter than the white point are set to the maximum quantum value. The black and white point have the valid range 0 to MaxRGB while mid (gamma) has a useful range of 0 to ten.  
  
levelChannel  
| const ChannelType channel, const double black_point, const double white_point, const double mid_point=1.0  
| Level image channel. Adjust the levels of the image channel by scaling the values falling between specified white and black points to the full available quantum range. The parameters provided represent the black, mid (gamma), and white points. The black point specifies the darkest color in the image. Colors darker than the black point are set to zero. Mid point (gamma) specifies a gamma correction to apply to the image. White point specifies the lightest color in the image. Colors brighter than the white point are set to the maximum quantum value. The black and white point have the valid range 0 to MaxRGB while mid (gamma) has a useful range of 0 to ten.  
  
magnify | void | Magnify image by integral size  
map | const Image &mapImage_ , bool dither_ = false | Remap image colors with closest color from reference image. Set dither_ to _true_ in to apply Floyd/Steinberg error diffusion to the image. By default, color reduction chooses an optimal set of colors that best represent the original image. Alternatively, you can choose a particular set of colors from an image file with this option.  
matteFloodfill | const [Color](Color.html) &target_, const unsigned int opacity_, const ssize_t x_, const ssize_t y_, [PaintMethod](Enumerations.html#PaintMethod) method_ | Floodfill designated area with a replacement opacity value.  
medianFilter | const double radius_ = 0.0 | Filter image by replacing each pixel component with the median color in a circular neighborhood  
mergeLayers | [LayerMethod](Enumerations.html#LayerMethod) noiseType_ | handle multiple images forming a set of image layers or animation frames.  
minify | void | Reduce image by integral size  
modifyImage | void | Prepare to update image. Ensures that there is only one reference to the underlying image so that the underlying image may be safely modified without effecting previous generations of the image. Copies the underlying image to a new image if necessary.  
modulate | double brightness_, double saturation_, double hue_ | Modulate percent hue, saturation, and brightness of an image. Modulation of saturation and brightness is as a ratio of the current value (1.0 for no change). Modulation of hue is an absolute rotation of -180 degrees to +180 degrees from the current position corresponding to an argument range of 0 to 2.0 (1.0 for no change).  
motionBlur  
| const double radius_, const double sigma_, const double angle_  
| Motion blur image with specified blur factor. The radius_ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The sigma_ parameter specifies the standard deviation of the Laplacian, in pixels. The angle_ parameter specifies the angle the object appears to be comming from (zero degrees is from the right).  
  
negate | bool grayscale_ = false | Negate colors in image. Replace every pixel with its complementary color (white becomes black, yellow becomes blue, etc.). Set grayscale to only negate grayscale values in image.  
normalize | void | Normalize image (increase contrast by normalizing the pixel values to span the full range of color values).  
oilPaint | size_t radius_ = 3 | Oilpaint image (image looks like oil painting)  
opacity | unsigned int opacity_ | Set or attenuate the opacity channel in the image. If the image pixels are opaque then they are set to the specified opacity value, otherwise they are blended with the supplied opacity value. The value of opacity_ ranges from 0 (completely opaque) to _MaxRGB_ . The defines _OpaqueOpacity_ and _TransparentOpacity_ are available to specify completely opaque or completely transparent, respectively.  
opaque | const [Color](Color.html) &opaqueColor_, const [Color](Color.html) &penColor_ | Change color of pixels matching opaqueColor_ to specified penColor_.  
ping | const std::string &imageSpec_ | Ping is similar to read except only enough of the image is read to determine the image columns, rows, and filesize. The [columns](Image++.html#columns) , [rows](Image++.html#rows) , and [fileSize](Image++.html#fileSize) attributes are valid after invoking ping. The image data is not valid after calling ping.  
const Blob &blob_  
process  
| std::string name_, const ssize_t argc_, char **argv_  
| Execute the named process module, passing any arguments via an argument vector, with argc_ specifying the number of arguments in the vector, and argv_ passing the address of an array of null-terminated C strings which constitute the argument vector. An exception is thrown if the requested process module does not exist, fails to load, or fails during execution.  
  
quantize | bool measureError_ = false | Quantize image (reduce number of colors). Set measureError_ to true in order to calculate error attributes.  
raise | const [Geometry](Geometry.html) &geometry_ = "6x6+0+0", bool raisedFlag_ = false | Raise image (lighten or darken the edges of an image to give a 3-D raised or lowered effect)  
read | const string &imageSpec_ | Read image into current object  
const [Geometry](Geometry.html) &size_, const std::string &imageSpec_ | Read image of specified size into current object. This form is useful for images that do not specifiy their size or to specify a size hint for decoding an image. For example, when reading a Photo CD, JBIG, or JPEG image, a size request causes the library to return an image which is the next resolution greater or equal to the specified size. This may result in memory and time savings.  
const [Blob](Blob.html) &blob_ | Read encoded image of specified size from an in-memory [BLOB](Blob.html) into current object. Depending on the method arguments, the Blob size, depth, and format may also be specified. Some image formats require that size be specified. The default ImageMagick uses for depth depends on its Quantum size (8 or 16). If ImageMagick's Quantum size does not match that of the image, the depth may need to be specified. ImageMagick can usually automagically detect the image's format. When a format can't be automagically detected, the format must be specified.  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size_  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size_, size_t depth_  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size_, size_t depth_, const string &magick_  
const [Blob](Blob.html) &blob_, const [Geometry](Geometry.html) &size_, const string &magick_  
const size_t width_, const size_t height_, std::string map_, const StorageType type_, const void *pixels_ | Read image based on an array of image pixels. The pixel data must be in scanline order top-to-bottom. The data can be character, short int, integer, float, or double. Float and double require the pixels to be normalized [0..1]. The other types are [0..MaxRGB]. For example, to create a 640x480 image from unsigned red-green-blue character data, use image.read( 640, 480, "RGB", CharPixel, pixels ); The parameters are as follows:   
| width_ | Width in pixels of the image.  
---|---  
height_ | Height in pixels of the image.  
map_ | This character string can be any combination or order of R = red, G = green, B = blue, A = alpha, C = cyan, Y = yellow M = magenta, and K = black. The ordering reflects the order of the pixels in the supplied pixel array.  
type_ | Pixel storage type (CharPixel, ShortPixel, IntegerPixel, FloatPixel, or DoublePixel)  
pixels_ | This array of values contain the pixel components as defined by the map_ and type_ parameters. The length of the arrays must equal the area specified by the width_ and height_ values and type_ parameters.  
reduceNoise | const double order_ | reduce noise in image using a noise peak elimination filter.  
randomThreshold  
| const Geometry &thresholds_  
| Random threshold the image. Changes the value of individual pixels based on the intensity of each pixel compared to a random threshold. The result is a low-contrast, two color image. The thresholds_ argument is a geometry containing LOWxHIGH thresholds. If the string contains 2x2, 3x3, or 4x4, then an ordered dither of order 2, 3, or 4 will be performed instead. This is a very fast alternative to 'quantize' based dithering.  
  
randomThresholdChannel  
| const Geometry &thresholds_, const ChannelType channel_  
| Random threshold an image channel. Similar to [randomThreshold](Image++.html#randomThreshold)() but restricted to the specified channel.  
  
roll | int columns_, ssize_t rows_ | Roll image (rolls image vertically and horizontally) by specified number of columnms and rows)  
rotate | double degrees_ | Rotate image counter-clockwise by specified number of degrees.  
sample | const [Geometry](Geometry.html) &geometry_ | Resize image by using pixel sampling algorithm  
scale | const [Geometry](Geometry.html) &geometry_ | Resize image by using simple ratio algorithm  
segment | double clusterThreshold_ = 1.0,   
double smoothingThreshold_ = 1.5 | Segment (coalesce similar image components) by analyzing the histograms of the color components and identifying units that are homogeneous with the fuzzy c-means technique. Also uses _quantizeColorSpace_ and _verbose_ image attributes. Specify _clusterThreshold__ , as the number of pixels each cluster must exceed the cluster threshold to be considered valid. _SmoothingThreshold__ eliminates noise in the second derivative of the histogram. As the value is increased, you can expect a smoother second derivative. The default is 1.5.  
shade | double azimuth_ = 30, double elevation_ = 30,   
bool colorShading_ = false | Shade image using distant light source. Specify _azimuth__ and _elevation__ as the position of the light source. By default, the shading results as a grayscale image.. Set c _olorShading__ to _true_ to shade the red, green, and blue components of the image.  
shadow | const double percent_opacity = 80, const double sigma_ = 0.5, const ssize_t x_ = 0, const ssize_t y_ = 0 | simulate an image shadow  
sharpen | const double radius_ = 1, const double sigma_ = 0.5 | Sharpen pixels in image. The _radius__ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma__ parameter specifies the standard deviation of the Laplacian, in pixels.  
sharpenChannel  
| const ChannelType channel_, const double radius_ = 0.0, const double sigma_ = 1.0  
| Sharpen pixel quantums in an image channel The channel_ parameter specifies the channel to sharpen.. The _radius__ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma__ parameter specifies the standard deviation of the Laplacian, in pixels.  
shave | const Geometry &geometry_ | Shave pixels from image edges.  
shear | double xShearAngle_, double yShearAngle_ | Shear image (create parallelogram by sliding image by X or Y axis). Shearing slides one edge of an image along the X or Y axis, creating a parallelogram. An X direction shear slides an edge along the X axis, while a Y direction shear slides an edge along the Y axis. The amount of the shear is controlled by a shear angle. For X direction shears, x degrees is measured relative to the Y axis, and similarly, for Y direction shears y degrees is measured relative to the X axis. Empty triangles left over from shearing the image are filled with the color defined as _borderColor_.  
solarize | double factor_ = 50.0 | Solarize image (similar to effect seen when exposing a photographic film to light during the development process)  
splice | const [Geometry](Geometry.html) &geometry_ | splice the background color into the image  
spread | size_t amount_ = 3 | Spread pixels randomly within image by specified amount  
stegano | const Image &watermark_ | Add a digital watermark to the image (based on second image)  
sparseColor | const ChannelType channel, const SparseColorMethod method, const size_t number_arguments, const double *arguments  | Sparse color image, given a set of coordinates, interpolates the colors found at those coordinates, across the whole image, using various methods.  
statistics | ImageStatistics *statistics | Obtain image statistics. Statistics are normalized to the range of 0.0 to 1.0 and are output to the specified ImageStatistics structure. The structure includes members maximum, minimum, mean, standard_deviation, and variance for each of these channels: red, green, blue, and opacity (e.g. statistics->red.maximum).  
stereo | const Image &rightImage_ | Create an image which appears in stereo when viewed with red-blue glasses (Red image on left, blue on right)  
swirl | double degrees_ | Swirl image (image pixels are rotated by degrees)  
texture | const Image &texture_ | Layer a texture on pixels matching image background color.  
threshold | double threshold_ | Threshold image  
transform | const [Geometry](Geometry.html) &imageGeometry_ | Transform image based on image and crop geometries. Crop geometry is optional.  
const [Geometry](Geometry.html) &imageGeometry_, const [Geometry](Geometry.html) &cropGeometry_  
transparent | const [Color](Color.html) &color_ | Add matte image to image, setting pixels matching color to transparent.  
trim | void | Trim edges that are the background color from the image.  
unsharpmask | double radius_, double sigma_, double amount_, double threshold_ | Sharpen the image using the unsharp mask algorithm. The _radius_ _ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma_ _ parameter specifies the standard deviation of the Gaussian, in pixels. The _amount_ _ parameter specifies the percentage of the difference between the original and the blur image that is added back into the original. The _threshold_ _ parameter specifies the threshold in pixels needed to apply the diffence amount.  
unsharpmaskChannel  
| const ChannelType channel_, const double radius_, const double sigma_, const double amount_, const double threshold_  
| Sharpen an image channel using the unsharp mask algorithm. The channel_ parameter specifies the channel to sharpen. The _radius_ _ parameter specifies the radius of the Gaussian, in pixels, not counting the center pixel. The _sigma_ _ parameter specifies the standard deviation of the Gaussian, in pixels. The _amount_ _ parameter specifies the percentage of the difference between the original and the blur image that is added back into the original. The _threshold_ _ parameter specifies the threshold in pixels needed to apply the diffence amount.  
wave | double amplitude_ = 25.0, double wavelength_ = 150.0 | Alter an image along a sine wave.  
write | const string &imageSpec_ | Write image to a file using filename i _mageSpec__ .   
**Caution:** if an image format is selected which is capable of supporting fewer colors than the original image or quantization has been requested, the original image will be quantized to fewer colors. Use a copy of the original if this is a problem.  
[Blob](Blob.html) *blob_ | Write image to a in-memory [ BLOB](Blob.html) stored in _blob__. The _magick_ _ parameter specifies the image format to write (defaults to [magick](Image++.html#magick) ). The depth_ parameter species the image depth (defaults to [ depth](Image++.html#depth) ).   
**Caution:** if an image format is selected which is capable of supporting fewer colors than the original image or quantization has been requested, the original image will be quantized to fewer colors. Use a copy of the original if this is a problem.  
[Blob](Blob.html) *blob_, std::string &magick_  
[Blob](Blob.html) *blob_, std::string &magick_, size_t depth_  
const ssize_t x_, const ssize_t y_, const size_t columns_, const size_t rows_, const std::string &map_, const StorageType type_, void *pixels_ | Write pixel data into a buffer you supply. The data is saved either as char, short int, integer, float or double format in the order specified by the type_ parameter. For example, we want to extract scanline 1 of a 640x480 image as character data in red-green-blue order: image.write(0,0,640,1,"RGB",0,pixels); The parameters are as follows:   
| x_ | Horizontal ordinate of left-most coordinate of region to extract.  
---|---  
y_ | Vertical ordinate of top-most coordinate of region to extract.  
columns_ | Width in pixels of the region to extract.  
rows_ | Height in pixels of the region to extract.  
map_ | This character string can be any combination or order of R = red, G = green, B = blue, A = alpha, C = cyan, Y = yellow, M = magenta, and K = black. The ordering reflects the order of the pixels in the supplied pixel array.  
type_ | Pixel storage type (CharPixel, ShortPixel, IntegerPixel, FloatPixel, or DoublePixel)  
pixels_ | This array of values contain the pixel components as defined by the map_ and type_ parameters. The length of the arrays must equal the area specified by the width_ and height_ values and type_ parameters.  
resize | const [Geometry](Geometry.html) &geometry_ | Resize image to specified size.  
  
###  Image Attributes

Image attributes are set and obtained via methods in Image. Except for methods which accept pointer arguments (e.g. c`hromaBluePrimary)` all methods return attributes by value. 

Image attributes are easily used. For example, to set the resolution of the TIFF file "file.tiff" to 150 dots-per-inch (DPI) in both the horizontal and vertical directions, you can use the following example code: 
    
    
    string filename("file.tiff"); 
    Image image; 
    image.read(filename); 
    image.resolutionUnits(PixelsPerInchResolution); 
    image.density(Geometry(150,150));   // could also use image.density("150x150") 
    image.write(filename)
    

The supported image attributes and the method arguments required to obtain them are shown in the following table:   
Image Attributes **Function** |  **Type** |  **Get Signature** |  **Set Signature** |  **Description**  
---|---|---|---|---  
adjoin | bool | void | bool flag_ | Join images into a single multi-image file.  
antiAlias | bool | void | bool flag_ | Control antialiasing of rendered Postscript and Postscript or TrueType fonts. Enabled by default.  
animation-   
Delay | size_t (0 to 65535) | void | size_t delay_ | Time in 1/100ths of a second (0 to 65535) which must expire before displaying the next image in an animated sequence. This option is useful for regulating the animation of a sequence of GIF images within Netscape.  
animation-   
Iterations | size_t | void | size_t iterations_ | Number of iterations to loop an animation (e.g. Netscape loop extension) for.  
attribute  
| string  
| const std::string name_  
| const std::string name_, const std::string value_ | An arbitrary named image attribute. Any number of named attributes may be attached to the image. For example, the image comment is a named image attribute with the name "comment". EXIF tags are attached to the image as named attributes. Use the syntax "EXIF:<tag>" to request an EXIF tag similar to "EXIF:DateTime".  
  
background-   
Color | [Color](Color.html) | void | const [Color](Color.html) &color_ | Image background color  
background-   
Texture | string | void | const string &texture_ | Image file name to use as the background texture. Does not modify image pixels.  
baseColumns | size_t | void |  | Base image width (before transformations)  
baseFilename | string | void |  | Base image filename (before transformations)  
baseRows | size_t | void |  | Base image height (before transformations)  
borderColor | [Color](Color.html) | void |  const [Color](Color.html) &color_ | Image border color  
boundingBox | Geometry | void |  | Return smallest bounding box enclosing non-border pixels. The current fuzz value is used when discriminating between pixels. This is the crop bounding box used by crop(Geometry(0,0)).  
boxColor | [Color](Color.html) | void | const [Color](Color.html) &boxColor_ | Base color that annotation text is rendered on.  
cacheThreshold | size_t |  | const size_t | Pixel cache threshold in bytes. Once this threshold is exceeded, all subsequent pixels cache operations are to/from disk. This is a static method and the attribute it sets is shared by all Image objects.  
channelDepth  
| size_t   
| const ChannelType channel_  
| const ChannelType channel_, const size_t depth_  
| Channel modulus depth. The channel modulus depth represents the minimum number of bits required to support the channel without loss. Setting the channel's modulus depth modifies the channel (i.e. discards resolution) if the requested modulus depth is less than the current modulus depth, otherwise the channel is not altered. There is no attribute associated with the modulus depth so the current modulus depth is obtained by inspecting the pixels. As a result, the depth returned may be less than the most recently set channel depth. Subsequent image processing may result in increasing the channel depth.  
  
chroma-   
BluePrimary | double x & y | double *x_, double *y_ | double x_, double y_ | Chromaticity blue primary point (e.g. x=0.15, y=0.06)  
chroma-   
GreenPrimary | double x & y | double *x_, double *y_ | double x_, double y_ | Chromaticity green primary point (e.g. x=0.3, y=0.6)  
chroma-   
RedPrimary | double x & y | double *x_, double *y_ | double x_, double y_ | Chromaticity red primary point (e.g. x=0.64, y=0.33)  
chroma-   
WhitePoint | double x & y | double*x_, double *y_ | double x_, double y_ | Chromaticity white point (e.g. x=0.3127, y=0.329)  
classType | [ClassType](Enumerations.html#ClassType) | void |  [ClassType](Enumerations.html#ClassType) class_ | Image storage class. Note that conversion from a DirectClass image to a PseudoClass image may result in a loss of color due to the limited size of the palette (256 or 65535 colors).  
clipMask | Image | void | const Image &clipMask_ | Associate a clip mask image with the current image. The clip mask image must have the same dimensions as the current image or an exception is thrown. Clipping occurs wherever pixels are transparent in the clip mask image. Clipping Pass an invalid image to unset an existing clip mask.  
colorFuzz | double | void | double fuzz_ | Colors within this distance are considered equal. A number of algorithms search for a target color. By default the color must be exact. Use this option to match colors that are close to the target color in RGB space.  
colorMap | [Color](Color.html) | size_t index_ | size_t index_, const [ Color](Color.html) &color_ | Color at colormap index.  
colorMapSize  
| size_t  
| void  
| size_t entries_  
| Number of entries in the colormap. Setting the colormap size may extend or truncate the colormap. The maximum number of supported entries is specified by the _MaxColormapSize_ constant, and is dependent on the value of QuantumDepth when ImageMagick is compiled. An exception is thrown if more entries are requested than may be supported. Care should be taken when truncating the colormap to ensure that the image colormap indexes reference valid colormap entries.  
  
colorSpace | [ColorspaceType](Enumerations.html#ColorspaceType) colorSpace_ | void | [ColorspaceType](Enumerations.html#ColorspaceType) colorSpace_ | The colorspace (e.g. CMYK) used to represent the image pixel colors. Image pixels are always stored as RGB(A) except for the case of CMY(K).  
columns | size_t | void |  | Image width  
comment | string | void |  | Image comment  
compose | [CompositeOperator](Enumerations.html#CompositeOperator) | void | [CompositeOperator](Enumerations.html#CompositeOperator) compose_ | Composition operator to be used when composition is implicitly used (such as for image flattening).  
compress-   
Type | [CompressionType](Enumerations.html#CompressionType) | void | [CompressionType](Enumerations.html#CompressionType) compressType_ | Image compresion type. The default is the compression type of the specified image file.  
debug | bool | void | bool flag_ | Enable printing of internal debug messages from ImageMagick as it executes.  
defineValue  
| string  
| const std::string &magick_, const std::string &key_  
| const std::string &magick_, const std::string &key_,  const std::string &value_  
| Set or obtain a definition string to applied when encoding or decoding the specified format. The meanings of the definitions are format specific. The format is designated by the magick_ argument, the format-specific key is designated by key_, and the associated value is specified by value_. See the defineSet() method if the key must be removed entirely.  
  
defineSet  
| bool  
| const std::string &magick_, const std::string &key_  
| const std::string &magick_, const std::string &key_, bool flag_  
| Set or obtain a definition flag to applied when encoding or decoding the specified format.. Similar to the defineValue() method except that passing the flag_ value 'true' creates a value-less define with that format and key. Passing the flag_ value 'false' removes any existing matching definition. The method returns 'true' if a matching key exists, and 'false' if no matching key exists.  
  
density | [Geometry](Geometry.html) (default 72x72) | void | const [Geometry](Geometry.html) &density_ | Vertical and horizontal resolution in pixels of the image. This option specifies an image density when decoding a Postscript or Portable Document page. Often used with _psPageSize_.  
depth |  size_t (8-32) | void | size_t depth_ | Image depth. Used to specify the bit depth when reading or writing raw images or when the output format supports multiple depths. Defaults to the quantum depth that ImageMagick is compiled with.  
endian | [EndianType](Enumerations.html#EndianType) | void | [EndianType](Enumerations.html#EndianType) endian_ | Specify (or obtain) endian option for formats which support it.  
directory | string | void |  | Tile names from within an image montage  
file | FILE * | FILE * | FILE *file_ | Image file descriptor.  
fileName | string | void | const string &fileName_ | Image file name.  
fileSize | off_t | void |  | Number of bytes of the image on disk  
fillColor | Color | void | const Color &fillColor_ | Color to use when filling drawn objects  
fillPattern | Image | void | const Image &fillPattern_ | Pattern image to use when filling drawn objects.  
fillRule | [FillRule](Enumerations.html#FillRule) | void | const Magick::FillRule &fillRule_ | Rule to use when filling drawn objects.  
filterType | [FilterTypes](Enumerations.html#FilterTypes) | void | [FilterTypes](Enumerations.html#FilterTypes) filterType_ | Filter to use when resizing image. The reduction filter employed has a sigificant effect on the time required to resize an image and the resulting quality. The default filter is _Lanczos_ which has been shown to produce high quality results when reducing most images.  
font | string | void | const string &font_ | Text rendering font. If the font is a fully qualified X server font name, the font is obtained from an X server. To use a TrueType font, precede the TrueType filename with an @. Otherwise, specify a Postscript font name (e.g. "helvetica").  
fontPointsize | size_t | void | size_t pointSize_ | Text rendering font point size  
fontTypeMetrics | [TypeMetric](TypeMetric.html) | const std::string &text_, [ TypeMetric](TypeMetric.html) *metrics |  | Update metrics with font type metrics using specified _text_ , and current [font](Image++.html#font) and [fontPointSize](Image++.html#fontPointsize) settings.  
format | string | void |  | Long form image format description.  
gamma | double (typical range 0.8 to 2.3) | void |  | Gamma level of the image. The same color image displayed on two different workstations may look different due to differences in the display monitor. Use gamma correction to adjust for this color difference.  
geometry | [Geometry](Geometry.html) | void |  | Preferred size of the image when encoding.  
gifDispose-   
Method | size_t   
{ 0 = Disposal not specified,   
1 = Do not dispose of graphic,   
3 = Overwrite graphic with background color,   
4 = Overwrite graphic with previous graphic. } | void | size_t disposeMethod_ | GIF disposal method. This option is used to control how successive frames are rendered (how the preceding frame is disposed of) when creating a GIF animation.  
iccColorProfile | [Blob](Blob.html) | void | const [Blob](Blob.html) &colorProfile_ | ICC color profile. Supplied via a [ Blob](Blob.html) since Magick++/ and ImageMagick do not currently support formating this data structure directly. Specifications are available from the [ International Color Consortium](http://www.color.org/) for the format of ICC color profiles.  
interlace-   
Type | [InterlaceType](Enumerations.html#InterlaceType) | void | [InterlaceType](Enumerations.html#InterlaceType) interlace_ | The type of interlacing scheme (default _NoInterlace_ ). This option is used to specify the type of interlacing scheme for raw image formats such as RGB or YUV. _NoInterlace_ means do not interlace, _LineInterlace_ uses scanline interlacing, and _PlaneInterlace_ uses plane interlacing. _PartitionInterlace_ is like _PlaneInterlace_ except the different planes are saved to individual files (e.g. image.R, image.G, and image.B). Use _LineInterlace_ or _PlaneInterlace_ to create an interlaced GIF or progressive JPEG image.  
iptcProfile | [Blob](Blob.html) | void | const [Blob](Blob.html) & iptcProfile_ | IPTC profile. Supplied via a [ Blob](Blob.html) since Magick++ and ImageMagick do not currently support formating this data structure directly. Specifications are available from the [ International Press Telecommunications Council](http://www.iptc.org/) for IPTC profiles.  
label | string | void | const string &label_ | Image label  
magick | string | void |  const string &magick_ | Get image format (e.g. "GIF")  
matte | bool | void | bool matteFlag_ | True if the image has transparency. If set True, store matte channel if the image has one otherwise create an opaque one.  
matteColor | [Color](Color.html) | void | const [Color](Color.html) &matteColor_ | Image matte (frame) color  
meanError-   
PerPixel | double | void |  | The mean error per pixel computed when an image is color reduced. This parameter is only valid if verbose is set to true and the image has just been quantized.  
modulusDepth  
| size_t   
| void  
| size_t depth_  
| Image modulus depth (minimum number of bits required to support red/green/blue components without loss of accuracy). The pixel modulus depth may be decreased by supplying a value which is less than the current value, updating the pixels (reducing accuracy) to the new depth. The pixel modulus depth can not be increased over the current value using this method.  
  
monochrome | bool | void | bool flag_ | Transform the image to black and white  
montage-   
Geometry | [Geometry](Geometry.html) | void |  | Tile size and offset within an image montage. Only valid for montage images.  
normalized-   
MaxError | double | void |  | The normalized max error per pixel computed when an image is color reduced. This parameter is only valid if verbose is set to true and the image has just been quantized.  
normalized-   
MeanError | double | void |  | The normalized mean error per pixel computed when an image is color reduced. This parameter is only valid if verbose is set to true and the image has just been quantized.  
orientation  
| [OrientationType](Enumerations.html#OrientationType) | void  
| [OrientationType](Enumerations.html#OrientationType) orientation_ | Image orientation.  Supported by some file formats such as DPX and TIFF. Useful for turning the right way up.  
  
packets | size_t | void |  | The number of runlength-encoded packets in   
the image  
packetSize | size_t | void |  | The number of bytes in each pixel packet  
page | [Geometry](Geometry.html#PostscriptPageSize) | void | const [ Geometry](Geometry.html#PostscriptPageSize) &pageSize_ | Preferred size and location of an image canvas. Use this option to specify the dimensions and position of the Postscript page in dots per inch or a TEXT page in pixels. This option is typically used in concert with _[density](Image++.html#density) _. Page may also be used to position a GIF image (such as for a scene in an animation)  
pixelColor | [Color](Color.html) | ssize_t x_, ssize_t y_ | ssize_t x_, ssize_t y_, const [ Color](Color.html) &color_ | Get/set pixel color at location x & y.  
profile  
| [ Blob  
](Blob.html) | const std::string name_  
| const std::string name_, const Blob &colorProfile_  
| Get/set/remove  a named profile. Valid names include "*", "8BIM", "ICM", "IPTC", or a user/format-defined profile name.   
  
quality | size_t (0 to 100) | void | size_t quality_ | JPEG/MIFF/PNG compression level (default 75).  
quantize-   
Colors | size_t | void | size_t colors_ | Preferred number of colors in the image. The actual number of colors in the image may be less than your request, but never more. Images with less unique colors than specified with this option will have any duplicate or unused colors removed.  
quantize-   
ColorSpace | [ColorspaceType](Enumerations.html#ColorspaceType) | void | [ColorspaceType](Enumerations.html#ColorspaceType) colorSpace_ | Colorspace to quantize colors in (default RGB). Empirical evidence suggests that distances in color spaces such as YUV or YIQ correspond to perceptual color differences more closely than do distances in RGB space. These color spaces may give better results when color reducing an image.  
quantize-   
Dither | bool | void | bool flag_ | Apply Floyd/Steinberg error diffusion to the image. The basic strategy of dithering is to trade intensity resolution for spatial resolution by averaging the intensities of several neighboring pixels. Images which suffer from severe contouring when reducing colors can be improved with this option. The quantizeColors or monochrome option must be set for this option to take effect.  
quantize-   
TreeDepth | size_t | void | size_t treeDepth_ | Depth of the quantization color classification tree. Values of 0 or 1 allow selection of the optimal tree depth for the color reduction algorithm. Values between 2 and 8 may be used to manually adjust the tree depth.  
rendering-   
Intent | [RenderingIntent](Enumerations.html#RenderingIntent) | void | [RenderingIntent](Enumerations.html#RenderingIntent) render_ | The type of rendering intent  
resolution-   
Units | [ResolutionType](Enumerations.html#ResolutionType) | void | [ResolutionType](Enumerations.html#ResolutionType) units_ | Units of image resolution  
rows | size_t | void |  | The number of pixel rows in the image  
scene | size_t | void | size_t scene_ | Image scene number  
signature | string | bool force_ = false |  | Image MD5 signature. Set force_ to 'true' to force re-computation of signature.  
size | [Geometry](Geometry.html) | void | const [Geometry](Geometry.html) &geometry_ | Width and height of a raw image (an image which does not support width and height information). Size may also be used to affect the image size read from a multi-resolution format (e.g. Photo CD, JBIG, or JPEG.  
strip | void | strips an image of all profiles and comments.  
strokeAntiAlias | bool | void | bool flag_ | Enable or disable anti-aliasing when drawing object outlines.  
strokeColor | Color | void | const Color &strokeColor_ | Color to use when drawing object outlines  
strokeDashOffset | size_t | void | double strokeDashOffset_ | While drawing using a dash pattern, specify distance into the dash pattern to start the dash (default 0).  
strokeDashArray | const double* | void | const double* strokeDashArray_ | Specify the pattern of dashes and gaps used to stroke paths. The strokeDashArray represents a zero-terminated array of numbers that specify the lengths (in pixels) of alternating dashes and gaps in user units. If an odd number of values is provided, then the list of values is repeated to yield an even number of values. A typical strokeDashArray_ array might contain the members 5 3 2 0, where the zero value indicates the end of the pattern array.  
strokeLineCap | LineCap | void | LineCap lineCap_ | Specify the shape to be used at the corners of paths (or other vector shapes) when they are stroked. Values of LineJoin are UndefinedJoin, MiterJoin, RoundJoin, and BevelJoin.  
strokeLineJoin | LineJoin | void | LineJoin lineJoin_ | Specify the shape to be used at the corners of paths (or other vector shapes) when they are stroked. Values of LineJoin are UndefinedJoin, MiterJoin, RoundJoin, and BevelJoin.  
strokeMiterLimit | size_t | void | size_t miterLimit_ | Specify miter limit. When two line segments meet at a sharp angle and miter joins have been specified for 'lineJoin', it is possible for the miter to extend far beyond the thickness of the line stroking the path. The miterLimit' imposes a limit on the ratio of the miter length to the 'lineWidth'. The default value of this parameter is 4.  
strokeWidth | double | void | double strokeWidth_ | Stroke width for use when drawing vector objects (default one)  
strokePattern | Image | void | const Image &strokePattern_ | Pattern image to use while drawing object stroke (outlines).  
subImage | size_t | void | size_t subImage_ | Subimage of an image sequence  
subRange | size_t | void | size_t subRange_ | Number of images relative to the base image  
textEncoding  
| string  
| void  
| const std::string &encoding_  
| Specify the code set to use for text annotations. The only character encoding which may be specified at this time is "UTF-8" for representing [ Unicode ](http://www.unicode.org/) as a sequence of bytes. Specify an empty string to use the default ASCII encoding. Successful text annotation using Unicode may require fonts designed to support Unicode.  
  
tileName | string | void | const string &tileName_ | Tile name  
totalColors | size_t | void |  | Number of colors in the image  
type | [ImageType](Enumerations.html#ImageType) | void | [ ImageType](Enumerations.html#ImageType) | Image type.  
verbose | bool | void | bool verboseFlag_ | Print detailed information about the image  
view | string | void | const string &view_ | FlashPix viewing parameters.  
virtualPixelMethod | [VirtualPixelMethod](Enumerations.html#VirtualPixelMethod) | void | [VirtualPixelMethod](Enumerations.html#VirtualPixelMethod) virtualPixelMethod_ | Image virtual pixel method.  
x11Display | string (e.g. "hostname:0.0") | void | const string &display_ | X11 display to display to, obtain fonts from, or to capture image from  
xResolution | double | void |  | x resolution of the image  
yResolution | double | void |  | y resolution of the image  
  
###  Low-Level Image Pixel Access

Image pixels (of type _[PixelPacket](PixelPacket.html) _) may be accessed directly via the _Image Pixel Cache_ . The image pixel cache is a rectangular window into the actual image pixels (which may be in memory, memory-mapped from a disk file, or entirely on disk). Two interfaces exist to access the _Image Pixel Cache._ The interface described here (part of the _Image_ class) supports only one view at a time. See the _[Pixels](Pixels.html) _ class for a more abstract interface which supports simultaneous pixel views (up to the number of rows). As an analogy, the interface described here relates to the _[Pixels](Pixels.html) _ class as stdio's gets() relates to fgets(). The _[Pixels](Pixels.html) _class provides the more general form of the interface. 

Obtain existing image pixels via _getPixels()_. Create a new pixel region using _setPixels()._

In order to ensure that only the current generation of the image is modified, the Image's [modifyImage()](Image++.html#modifyImage) method should be invoked to reduce the reference count on the underlying image to one. If this is not done, then it is possible for a previous generation of the image to be modified due to the use of reference counting when copying or constructing an Image.  


Depending on the capabilities of the operating system, and the relationship of the window to the image, the pixel cache may be a copy of the pixels in the selected window, or it may be the actual image pixels. In any case calling _syncPixels()_ insures that the base image is updated with the contents of the modified pixel cache. The method _readPixels()_ supports copying foreign pixel data formats into the pixel cache according to the _QuantumTypes_. The method _writePixels()_ supports copying the pixels in the cache to a foreign pixel representation according to the format specified by _QuantumTypes_.

The pixel region is effectively a small image in which the pixels may be accessed, addressed, and updated, as shown in the following example:
    
    
    ![cache](Cache.png)
    Image image("cow.png"); 
    // Ensure that there are no other references to this image.
    image.modifyImage();
    // Set the image type to TrueColor DirectClass representation.
    image.type(TrueColorType);
    // Request pixel region with size 60x40, and top origin at 20x30 
    ssize_t columns = 60; 
    PixelPacket *pixel_cache = image.getPixels(20,30,columns,40); 
    // Set pixel at column 5, and row 10 in the pixel cache to red. 
    ssize_t column = 5; 
    ssize_t row = 10; 
    PixelPacket *pixel = pixel_cache+row*columns+column; 
    *pixel = Color("red"); 
    // Save changes to underlying image .
    image.syncPixels();
      // Save updated image to file.
    image.write("horse.png");
    

The image cache supports the following methods:   


Image Cache Methods **Method** |  **Returns** |  **Signature** |  **Description**  
---|---|---|---  
getConstPixels | const [PixelPacket](PixelPacket.html) * | const ssize_t x_, const ssize_t y_, const size_t columns_, const size_t rows_ | Transfers pixels from the image to the pixel cache as defined by the specified rectangular region. The returned pointer remains valid until the next getPixel, getConstPixels, or setPixels call and should never be deallocated by the user.  
getConstIndexes | const IndexPacket* | void | Returns a pointer to the Image pixel indexes corresponding to a previous getPixel, getConstPixels, or setPixels call.  The returned pointer remains valid until the next getPixel, getConstPixels, or setPixels call and should never be deallocated by the user. Only valid for PseudoClass images or CMYKA images. The pixel indexes represent an array of type IndexPacket, with each entry corresponding to an x,y pixel position. For PseudoClass images, the entry's value is the offset into the colormap (see [colorMap](Image++.html#colorMap) ) for that pixel. For CMYKA images, the indexes are used to contain the alpha channel.  
getIndexes | IndexPacket* | void | Returns a pointer to the Image pixel indexes corresponding to the pixel region requested by the last [getConstPixels](Image++.html#getConstPixels) , [getPixels](Image++.html#getPixels) , or [setPixels](Image++.html#setPixels) call. The returned pointer remains valid until the next getPixel, getConstPixels, or setPixels call and should never be deallocated by the user. Only valid for PseudoClass images or CMYKA images. The pixel indexes represent an array of type IndexPacket, with each entry corresponding to a pixel x,y position. For PseudoClass images, the entry's value is the offset into the colormap (see [colorMap](Image++.html#colorMap) ) for that pixel. For CMYKA images, the indexes are used to contain the alpha channel.  
getPixels | [PixelPacket](PixelPacket.html) * | const ssize_t x_, const ssize_t y_, const size_t columns_, const size_t rows_ | Transfers pixels from the image to the pixel cache as defined by the specified rectangular region. Modified pixels may be subsequently transferred back to the image via syncPixels. The returned pointer remains valid until the next getPixel, getConstPixels, or setPixels call and should never be deallocated by the user.  
setPixels | [PixelPacket](PixelPacket.html) * | const ssize_t x_, const ssize_t y_, const size_t columns_, const size_t rows_ | Allocates a pixel cache region to store image pixels as defined by the region rectangle. This area is subsequently transferred from the pixel cache to the image via syncPixels. The returned pointer remains valid until the next getPixel, getConstPixels, or setPixels call and should never be deallocated by the user.  
syncPixels | void | void | Transfers the image cache pixels to the image.  
readPixels | void | [QuantumTypes](Enumerations.html#QuantumTypes) quantum_, unsigned char *source_, | Transfers one or more pixel components from a buffer or file into the image pixel cache of an image. ReadPixels is typically used to support image decoders. The region transferred corresponds to the region set by a preceding setPixels call.  
writePixels | void | [QuantumTypes](Enumerations.html#QuantumTypes) quantum_, unsigned char *destination_ | Transfers one or more pixel components from the image pixel cache to a buffer or file. WritePixels is typically used to support image encoders. The region transferred corresponds to the region set by a preceding getPixels or getConstPixels call.
