# Magick::Montage Class  
  
A montage is a single image which is composed of thumbnail images composed in a uniform grid. The size of the montage image is determined by the size of the individual thumbnails and the number of rows and columns in the grid.

The following illustration shows a montage consisting of three columns and two rows of thumbnails rendered on a gray background:

![](montage-sample-framed.jpg)

Montages may be either "plain" (undecorated thumbnails) or "framed" (decorated thumbnails). In order to more easily understand the options supplied to [_MontageImages()_](STL.html#montageImages), montage options are supplied by two different classes: [_Magick::Montage_](Montage.html#Magick::Montage) and [_Magick::MontageFramed_](Montage.html#Magick::MontageFramed).

### Plain Montages

_Magick::Montage_ is the base class to provide montage options and provides methods to set all options required to render simple (unframed) montages. See [_Magick::MontageFramed_](Montage.html#Magick::MontageFramed)if you would like to create a framed montage.

Unframed thumbnails consist of four components: the thumbnail image, the thumbnail border, an optional thumbnail shadow, and an optional thumbnail label area.

![](thumbnail-anatomy-plain.jpg)

**Montage Methods**

**Method** |  **Return Type** |  **Signature(s)** |  **Description**  
---|---|---|---  
Montage |  |  void |  Default constructor  
backgroundColor |  void |  const [Color](Color.html) &backgroundColor_ |  Specifies the background color that thumbnails are imaged upon.  
[Color](Color.html) |  void  
compose |  void |  [CompositeOperator](Enumerations.html#CompositeOperator) compose_ |  Specifies the image composition algorithm for thumbnails. This controls the algorithm by which the thumbnail image is placed on the background. Use of OverCompositeOp is recommended for use with images that have transparency. This option may have negative side-effects for images without transparency.  
[CompositeOperator](Enumerations.html#CompositeOperator) |  void  
fileName |  void |  std::string fileName_ |  Specifies the image filename to be used for the generated montage images. To handle the case were multiple montage images are generated, a printf-style format may be embedded within the filename. For example, a filename specification of image%02d.miff names the montage images as image00.miff, image01.miff, etc.  
std::string |  void  
fill |  void |  const [Color](Color.html) &pen_ |  Specifies the fill color to use for the label text.  
[Color](Color.html) |  void  
font |  void |  std::string font_ |  Specifies the thumbnail label font.  
std::string |  void  
geometry |  void |  const [Geometry](Geometry.html) &geometry_ |  Specifies the size of the generated thumbnail.  
[Geometry](Geometry.html) |  void  
gravity |  void |  [GravityType](Enumerations.html#GravityType) gravity_ |  Specifies the thumbnail positioning within the specified geometry area. If the thumbnail is smaller in any dimension than the geometry, then it is placed according to this specification.  
[GravityType](Enumerations.html) |  void  
label |  void |  std::string label_ |  Specifies the format used for the image label. Special [format characters](FormatCharacters.html) may be embedded in the format string to include information about the image.  
std::string |  void  
penColor |  void |  const [Color](Color.html) &pen_ |  Specifies the pen color to use for the label text (same as _fill_).  
[Color](Color.html) |  void  
pointSize |  void |  size_t pointSize_ |  Specifies the thumbnail label font size.  
size_t |  void  
shadow |  void |  bool shadow_ |  Enable/disable drop-shadow on thumbnails.  
bool |  void  
stroke |  void |  const [Color](Color.html) &pen_ |  Specifies the stroke color to use for the label text .  
[Color](Color.html) |  void  
texture |  void |  std::string texture_ |  Specifies a texture image to use as montage background. The built-in textures "`granite:`" and "`plasma:`" are available. A texture is the same as a background image.  
std::string |  void  
tile |  void |  const [Geometry](Geometry.html) &tile_ |  Specifies the maximum number of montage columns and rows in the montage. The montage is built by filling out all cells in a row before advancing to the next row. Once the montage has reached the maximum number of columns and rows, a new montage image is started.  
[Geometry](Geometry.html) |  void  
transparentColor |  void |  const [Color](Color.html) &transparentColor_ |  Specifies a montage color to set transparent. This option can be set the same as the background color in order for the thumbnails to appear without a background when rendered on an HTML page. For best effect, ensure that the transparent color selected does not occur in the rendered thumbnail colors.  
[Color](Color.html) |  void  



### Framed Montages

_Magick::MontageFramed_ provides the means to specify montage options when it is desired to have decorative frames around the image thumbnails. _MontageFramed_ inherits from _Montage_ and therefore provides all the methods of _Montage_ as well as those shown in the table "MontageFramed Methods".

Framed thumbnails consist of four components: the thumbnail image, the thumbnail frame, the thumbnail border, an optional thumbnail shadow, and an optional thumbnail label area.

![](thumbnail-anatomy-framed.jpg)

**MontageFramed Methods**

**Method** |  **Return Type** |  **Signature(s)** |  **Description**  
---|---|---|---  
MontageFramed |  |  void |  Default constructor (enable frame via _frameGeometry_).  
borderColor |  void |  const [Color](Color.html) &borderColor_ |  Specifies the background color within the thumbnail frame.  
[Color](Color.html) |  void  
borderWidth |  void |  size_t borderWidth_ |  Specifies the border (in pixels) to place between a thumbnail and its surrounding frame. This option only takes effect if thumbnail frames are enabled (via _frameGeometry_) and the thumbnail geometry specification doesn't also specify the thumbnail border width.  
size_t |  void  
frameGeometry |  void |  const [Geometry](Geometry.html) &frame_ |  Specifies the geometry specification for frame to place around thumbnail. If this parameter is not specified, then the montage is unframed.  
[Geometry](Geometry.html) |  void  
matteColor |  void |  const [Color](Color.html) &matteColor_ |  Specifies the thumbnail frame color.  
[Color](Color.html) |  void  


