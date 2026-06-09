# Magick::Geometry

Geometry provides a convenient means to specify a geometry argument. The object may be initialized from a C string or C++ string containing a geometry specification. It may also be initialized by more efficient parameterized constructors. 

### Geometry Specifications

Geometry specifications are in the form `"<width>x<height>{+-}<xoffset>{+-}<yoffset>"` (where _width_ , _height_ , _xoffset_ , and _yoffset_ are numbers) for specifying the size and placement location for an object. 

The _width_ and _height_ parts of the geometry specification are measured in pixels. The _xoffset_ and _yoffset_ parts are also measured in pixels and are used to specify the distance of the placement coordinate from the left and top and edges of the image, respectively. Both types of offsets are measured from the indicated edge of the object to the corresponding edge of the image. The X offset may be specified in the following ways: 

+_xoffset_ |  The left edge of the object is to be placed _xoffset_ pixels in from the _left edge_ of the image.  
---|---  
-_xoffset_ |  The left edge of the object is to be placed outside the image, _xoffset_ pixels out from the _left edge_ of the image.  
  
The Y offset has similar meanings: 

+_yoffset_ |  The top edge of the object is to be _yoffset_ pixels _below_ the _top edge_ of the image.  
---|---  
-_yoffset_ |  The top edge of the object is to be _yoffset_ pixels _above_ the _top edge_ of the image.  
  
Offsets must be given as pairs; in other words, in order to specify either _xoffset_ or _yoffset_ both must be present. 

### ImageMagick Extensions To Geometry Specifications

ImageMagick has added a number of qualifiers to the standard geometry string for use when resizing images. The form of an extended geometry string is "`<width>x<height>{+-}<xoffset>{+-}<yoffset>{%}{!}{<}{>}"`. Extended geometry strings should _only_ be used _when resizing an image_. Using an extended geometry string for other applications may cause the API call to fail. The available qualifiers are shown in the following table: 

**ImageMagick Geometry Qualifiers**

**Qualifier** |  **Description**  
---|---  
**%** |  Interpret width and height as a **percentage** of the current size.  
**!** |  Resize to width and height **exactly** , loosing original aspect ratio.  
**<** |  Resize only if the image is **smaller** than the geometry specification.  
**>** |  Resize only if the image is **greater** than the geometry specification.  
  
### Postscript Page Size Extension To Geometry Specifications

Any geometry string specification supplied to the Geometry constructor is considered to be a Postscript page size nickname if the first character is not numeric. The Geometry constructor converts these page size specifications into the equivalent numeric geometry string specification (preserving any offset component) prior to conversion to the internal object format. Postscript page size specifications are short-hand for the pixel geometry required to fill a page of that size. Since the 11x17 inch page size used in the US starts with a digit, it is not supported as a Postscript page size nickname. Instead, substitute the geometry specification "`792x1224>"` when 11x17 output is desired. 

An example of a Postscript page size specification is `"letter+43+43>"`. 

**Postscript Page Size Nicknames**

**Postscript Page Size Nickname** |  **Equivalent Extended Geometry Specification**  
---|---  
Ledger |  1224x792>  
Legal |  612x1008>  
Letter |  612x792>  
LetterSmall |  612x792>  
ArchE |  2592x3456>  
ArchD |  1728x2592>  
ArchC |  1296x1728>  
ArchB |  864x1296>  
ArchA |  648x864>  
A0 |  2380x3368>  
A1 |  1684x2380>  
A2 |  1190x1684>  
A3 |  842x1190>  
A4 |  595x842>  
A4Small |  595x842>  
A5 |  421x595>  
A6 |  297x421>  
A7 |  210x297>  
A8 |  148x210>  
A9 |  105x148>  
A10 |  74x105>  
B0 |  2836x4008>  
B1 |  2004x2836>  
B2 |  1418x2004>  
B3 |  1002x1418>  
B4 |  709x1002>  
B5 |  501x709>  
C0 |  2600x3677>  
C1 |  1837x2600>  
C2 |  1298x1837>  
C3 |  918x1298>  
C4 |  649x918>  
C5 |  459x649>  
C6 |  323x459>  
Flsa |  612x936>  
Flse |  612x936>  
HalfLetter |  396x612>  
  
### Geometry Methods

Geometry provides methods to initialize its value from strings, from a set of parameters, or via attributes. The methods available for use in Geometry are shown in the following table: 

**Geometry Methods**

**Method** |  **Return Type** |  **Signature(s)** |  **Description**  
---|---|---|---  
Geometry |  |  size_t width_, size_t height_, ssize_t xOff_ = 0, ssize_t yOff_ = 0, bool xNegative_ = false, bool yNegative_ = false |  Construct geometry via explicit parameters.  
const string geometry_ |  Construct geometry from C++ string  
const char * geometry_ |  Construct geometry from C string  
width |  void |  size_t width_ |  Width  
size_t |  void  
height |  void |  size_t height_ |  Height  
size_t |  void  
xOff |  void |  ssize_t xOff_ |  X offset from origin  
ssize_t |  void  
yOff |  void |  ssize_t yOff_ |  Y offset from origin  
size_t |  void  
xNegative |  void |  bool xNegative_ |  Sign of X offset negative? (X origin at right)  
bool |  void  
yNegative |  void |  bool yNegative_ |  Sign of Y offset negative? (Y origin at bottom)  
bool |  void  
percent |  void |  bool percent_ |  Width and height are expressed as percentages  
bool |  void  
aspect |  void |  bool aspect_ |  Resize without preserving aspect ratio (!)  
bool |  void  
greater |  void |  bool greater_ |  Resize if image is greater than size (>)  
bool |  void  
less |  void |  bool less_ |  Resize if image is less than size (<)  
bool |  void  
isValid |  void |  bool isValid_ |  Does object contain a valid geometry? May be set to _false_ in order to invalidate an existing geometry object.  
bool |  void  
operator = |  const Geometry& |  const string geometry_ |  Set geometry via C++ string  
operator = |  const Geometry& |  const char * geometry_ |  Set geometry via C string  
operator string |  string |  Geometry& |  Obtain C++ string representation of geometry  
  
In addition, we support these yet to be documented geometry flags: the fill area flag ('^') and the pixel area count limit flag ('@').

  
  

