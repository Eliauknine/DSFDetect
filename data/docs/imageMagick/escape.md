[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

There are copious amounts of extra data associated with images (metadata), beyond the actual image pixels. This metadata can be useful, either for display, or for various calculations, or in modifying the behavior of later image processing operations. You can utilize percent escapes in a number of options, for example in [-format](command-line-options.html#format_identify_) or in montage [-label](command-line-options.html#label), to print various properties and other settings associated with an image.

**Profile Data** | Such as EXIF: data, containing focal lengths, exposures, dates, and in come cases GPS locations.   
---|---  
**Attributes** | These are directly involved with image data, and more commonly modified as part of normal image processing. These include width, height, depth, image type (colorspace), timing delays, and background color. Most specific percent escapes is to access this information.   
**Properties** | These are stored as a table of free form strings, and are (if possible) saved with the image (especially in MIFF and PNG image file formats). These include: Labels, Captions, Comments.   
**Artifacts** | These are various operational (expert) settings that are saved for use by various operators, or by the user for future use. It is just a table of free-form strings. They are not saved with the image when written. See Artifacts and Options below for details.   
**Options** | Also operational (expert) settings that are saved for use by various operators, but are set globally for use by a whole image list (also not saved). See Artifacts and Options below.   
  
### Percent Escape Handling

If you request a percent escape such as `%[key]` the setting is looked for in the following order until the first match has been found...

  1. Handle special prefixes such as 'artifact:' 'option:' 'exif:', or 'fx:'. This includes and calculations and or globs of those prefixes such as 'exif:*' or 'artifact:*' (see below).
  2. If `key` contains a glob pattern (but no known prefix) search free-form properties table.
  3. If `key` is a special image 'attribute' name (see list above) return the associated or calculated image attribute.
  4. Search for setting as a free-form 'property'
  5. Search for setting as a free-form 'artifact'
  6. Search for setting as a free-form 'option'
  7. Replace escape with empty string, and perhaps produce a warning.



Remember, all long name forms of percent escapes are handled in a is case insensitive manner. 

**As of IM v6.8.0-5** you can now access the Artifact and Option free-form string tables directly, allowing you to override the above sequence, and avoid accessing an attribute or property of the same name.
    
    
    %[artifact:setting]
    %[option:setting]
    

### Single Letter Attribute Percent Escapes

Here are common single letter escapes (short form) is used to report the most common attributes and properties of an image, such as: the image filename filename, type, width, height. 

\n | newline  
---|---  
\r | carriage return  
< | less-than character.  
> | greater-than character.  
& | ampersand character.  
%% | a percent sign  
%b | file size of image read in  
%c | comment meta-data property  
%d | directory component of path  
%e | filename extension or suffix  
%f | filename (including suffix)  
%g | layer canvas page geometry (equivalent to "%Wx%H%X%Y")  
%h | current image height in pixels  
%i | image filename (note: becomes output filename for "info:")  
%k | CALCULATED: number of unique colors  
%l | label meta-data property  
%m | image file format (file magic)  
%n | number of images in current image sequence  
%o | output filename (used for delegates)  
%p | index of image in current image list  
%q | quantum depth (compile-time constant)  
%r | image class and colorspace  
%s | scene number (from input unless re-assigned)  
%t | filename without directory or extension (suffix)  
%u | unique temporary filename (used for delegates)  
%w | current width in pixels  
%x | x resolution (density)  
%y | y resolution (density)  
%z | image depth (as read in unless modified, image save depth)  
%A | image transparency channel enabled (true/false)  
%C | image compression type  
%D | image GIF dispose method  
%G | original image size (%wx%h; before any resizes)  
%H | page (canvas) height  
%M | Magick filename (original file exactly as given, including read mods)  
%O | page (canvas) offset ( = %X%Y )  
%P | page (canvas) size ( = %Wx%H )  
%Q | image compression quality ( 0 = default )  
%S | ?? scenes ??  
%T | image time delay (in centi-seconds)  
%U | image resolution units  
%W | page (canvas) width  
%X | page (canvas) x offset (including sign)  
%Y | page (canvas) y offset (including sign)  
%Z | unique filename (used for delegates)  
%@ | CALCULATED: trim bounding box (without actually trimming)  
%# | CALCULATED: 'signature' hash of image values  
  
Here is a sample command and its output for an image with filename `bird.miff` and whose width is 512 and height is 480.
    
    
    -> identify -format "%m:%f %wx%h" bird.miff
    MIFF:bird.miff 512x480
    

Note that all single letter percent escapes can also be used using long form (from IM version 6.7.6-9, see next). For example `%[f]` is equivalent to the `%f` short form. 

**WARNING** : short form percent escapes are NOT performed when the percent is after a number. For example, `10%x10` does not expand the `%x` as a percent escape. If you specifically want to expand the 'x', use the long form which overrides this special case. EG: `10%[x]10`. 

Also be warned that calculated attributes can take some time to generate, especially for large images.

### Long Form Attribute Percent Escapes

In addition to the above specific and calculated attributes are recognized when enclosed in braces (long form):

%[base] | base filename, no suffixes (as %t)  
---|---  
%[channels] | ??? channels in use - colorspace ???  
%[colorspace] | Colorspace of Image Data (excluding transparency)  
%[copyright] | ImageMagick Copyright String  
%[depth] | depth of image for write (as input unless changed)  
%[deskew:angle] | The deskew angle in degrees of rotation  
%[directory] | directory part of filename (as %d)  
%[distortion] | how well an image resembles a reference image ([-compare](command-line-options.html#compare))  
%[entropy] | CALCULATED: entropy of the image  
%[extension] | extension part of filename (as %e)  
%[gamma] | value of image gamma  
%[group] | ??? window group ???  
%[height] | original height of image (when it was read in)  
%[kurtosis] | CALCULATED: kurtosis statistic of image  
%[label] | label meta-data property  
%[magick] | coder used to read image (not the file suffix)  
%[max] | CALCULATED: maximum value statistic of image  
%[mean] | CALCULATED: average value statistic of image  
%[min] | CALCULATED: minimum value statistic of image  
%[name] | The original name of the image  
%[opaque] | CALCULATED: is image fully-opaque?  
%[orientation] | image orientation  
%[page] | Virtual canvas (page) geometry  
%[profile:icc] | ICC profile info  
%[profile:icm] | ICM profile info  
%[profiles] | list of any embedded profiles  
%[resolution.x] | X density (resolution) without units  
%[resolution.y] | Y density (resolution) without units  
%[scene] | original scene number of image in input file  
%[size] | original size of image (when it was read in)  
%[skewness] | CALCULATED: skewness statistic of image  
%[standard-deviation] | CALCULATED: standard deviation statistic of image  
%[type] | CALCULATED: image type  
%[unique] | unique temporary filename ???  
%[units] | image resolution units  
%[version] | Version Information of this running ImageMagick  
%[width] | original width of image (when it was read in)  
%[zero] | zero (unique filename for delegate use)  
  
### Properties

All other long forms of percent escapes (not single letter long form) are handled in a case insensitive manner. Such escapes will will attempt to look up that name specific data sources. 

The primary search space (if not a specific attribute listed above) is a free-form property string. Such strings are associated and saved with images, and are typically set using either the [-set](command-line-options.html#set) CLI option (or API equivalent), or from special convenience options (such as [-label](command-line-options.html#label), [-comment](command-line-options.html#comment), [-caption](command-line-options.html#caption)). 

These convenience options are globally saved (as 'global options' so thay can be set before images are read), and later are transfered to the property of individual images, only when they are read in. At that time any internal percent escape present is then handled. 

To change a property of an image already in memory, you need to use [-set](command-line-options.html#set). 

Note that properties, like attributes (and profiles), are saved with images when write, if the image file format allows. 

### Artifacts and Options

The previous percent escapes are associated with the primary Attributes and Properties. Which is the original and primary focus of such percent escapes. 

However there are many operational settings that are used by various ImageMagick operators that can be useful to set and later access. These consist of per-image Artifacts, and Global options (associated with a list of images, typically the current image list).

Note that the major difference between an artifact and a property is that artifacts, being an internal operational setting, is not saved with images (if such is possible). 

For example when you use `-define 'distort:viewport=100x100'` you are in fact generating a global option, which the [-distort](command-line-options.html#distort) operator will use to modify its behavior (distorted output image 'view'). 

An Option is essentually a Artifact that has been stored globally as part of a list of images (specifically a 'Wand' of images). As such they are identical, in that a Option, is simply a global Artifact for all the associated images. 

As such you can use `-set 'option:distort:viewport' '100x100'` to achieve the same result of setting a Artifact for the disort operation to use. 

**Internal Handling of a Global Option...**

The Core library ('MagickCore') does not generally directly understand Global Options. As such, continuing the previous example, the `DistortImages()` function only looks up an artifact to discover if a 'viewport' has been provided to it. 

How Global Options are used when a library function requests an Artifact is one of the key differences between IMv6 and IMv7.

In **ImageMagick version 6**... before each operator, any global Options are copied to per-image Artifacts, for every image in the current image list. This allows various operators to find its operational 'defines' or Artifacts. 

In **ImageMagick version 7**... sets a link back to the global options data, so that if a specific per-image Artifact is not found , then it will look for a equivalent global Option for that image list. directly. This saves coping these free-form options into artifacts repeatally, and means you can now separately define a global option for a list, and a individual overriding artifact for a specific image in that list. 

Note that many API's that do not use Wands (PerlMagick for example using arrays of images rather than a Wand). In these API's you will not have Global Options, only per-image Artifacts. 

In summery a Global Option, if available, is equivalent to a per-image Artifact. 

### Glob-Pattern Listing of Properties, Artifacts and Options

The setting can contain a glob pattern. As such you can now list all free-form string properties, artifacts, and options, (but not specific image attributes) using...
    
    
    convert ... \
       -print "__Properties__\n%[*]" \
       -print "__Artifacts__\n%[artifact:*]" \
       -print "__Options__\n%[option:*]" \
       ...
    

The format of glob patterns are very specific and as such is generally only used to list specific settings, such as when debugging, rather than being used for image processing use. 

### Calculated Percent Escape Prefixes

There are some special prefixes (before the first ':') which performs calculations based on the user provided string that follows that prefix. For example you can do a numerical calculation use `%[fx:...]` to evaluate the given [FX](fx.html) expressions:
    
    
    %[fx:expression]
    

Use `pixel:` to evaluate a pixel color as defined by the [FX](fx.html) expression:
    
    
    %[pixel:expression]
    

### Specific Profile Percent Escape Prefixes

You can also use the following special formatting syntax to print EXIF mage meta-data that was included in the image read in:
    
    
    %[EXIF:tag]
    

Choose tag from the following:
    
    
    *  (print all EXIF tags, in keyword=data format)
    !  (print all EXIF tags, in tag_number data format)
    #hhhh (print data for EXIF tag #hhhh)
    ImageWidth
    ImageLength
    BitsPerSample
    Compression
    PhotometricInterpretation
    FillOrder
    DocumentName
    ImageDescription
    Make
    Model
    StripOffsets
    Orientation
    SamplesPerPixel
    RowsPerStrip
    StripByteCounts
    XResolution
    YResolution
    PlanarConfiguration
    ResolutionUnit
    TransferFunction
    Software
    DateTime
    Artist
    WhitePoint
    PrimaryChromaticities
    TransferRange
    JPEGProc
    JPEGInterchangeFormat
    JPEGInterchangeFormatLength
    YCbCrCoefficients
    YCbCrSubSampling
    YCbCrPositioning
    ReferenceBlackWhite
    CFARepeatPatternDim
    CFAPattern
    BatteryLevel
    Copyright
    ExposureTime
    FNumber
    IPTC/NAA
    EXIFOffset
    InterColorProfile
    ExposureProgram
    SpectralSensitivity
    GPSInfo
    ISOSpeedRatings
    OECF
    EXIFVersion
    DateTimeOriginal
    DateTimeDigitized
    ComponentsConfiguration
    CompressedBitsPerPixel
    ShutterSpeedValue
    ApertureValue
    BrightnessValue
    ExposureBiasValue
    MaxApertureValue
    SubjectDistance
    MeteringMode
    LightSource
    Flash
    FocalLength
    MakerNote
    UserComment
    SubSecTime
    SubSecTimeOriginal
    SubSecTimeDigitized
    FlashPixVersion
    ColorSpace
    EXIFImageWidth
    EXIFImageLength
    InteroperabilityOffset
    FlashEnergy
    SpatialFrequencyResponse
    FocalPlaneXResolution
    FocalPlaneYResolution
    FocalPlaneResolutionUnit
    SubjectLocation
    ExposureIndex
    SensingMethod
    FileSource
    SceneType
    

  


Surround the format specification with quotation marks to prevent your shell from misinterpreting any spaces and square brackets.

The following special formatting syntax can be used to print IPTC information contained in the file:
    
    
    %[IPTC:dataset:record]
    

Select dataset and record from the following:
    
    
      Envelope Record
      1:00  Model Version
      1:05  Destination
      1:20  File Format
      1:22  File Format Version
      1:30  Service Identifier
      1:40  Envelope Number
      1:50  Product ID
      1:60  Envelope Priority
      1:70  Date Sent
      1:80  Time Sent
      1:90  Coded Character Set
      1:100  UNO (Unique Name of Object)
      1:120  ARM Identifier
      1:122  ARM Version
    
    Application Record
      2:00  Record Version
      2:03  Object Type Reference
      2:05  Object Name (Title)
      2:07  Edit Status
      2:08  Editorial Update
      2:10  Urgency
      2:12  Subject Reference
      2:15  Category
      2:20  Supplemental Category
      2:22  Fixture Identifier
      2:25  Keywords
      2:26  Content Location Code
      2:27  Content Location Name
      2:30  Release Date
      2:35  Release Time
      2:37  Expiration Date
      2:38  Expiration Time
      2:40  Special Instructions
      2:42  Action Advised
      2:45  Reference Service
      2:47  Reference Date
      2:50  Reference Number
      2:55  Date Created
      2:60  Time Created
      2:62  Digital Creation Date
      2:63  Digital Creation Time
      2:65  Originating Program
      2:70  Program Version
      2:75  Object Cycle
      2:80  By-Line (Author)
      2:85  By-Line Title (Author Position) [Not used in Photoshop 7]
      2:90  City
      2:92  Sub-Location
      2:95  Province/State
      2:100  Country/Primary Location Code
      2:101  Country/Primary Location Name
      2:103  Original Transmission Reference
      2:105  Headline
      2:110  Credit
      2:115  Source
      2:116  Copyright Notice
      2:118  Contact
      2:120  Caption/Abstract
      2:122  Caption Writer/Editor
      2:125  Rasterized Caption
      2:130  Image Type
      2:131  Image Orientation
      2:135  Language Identifier
      2:150  Audio Type
      2:151  Audio Sampling Rate
      2:152  Audio Sampling Resolution
      2:153  Audio Duration
      2:154  Audio Outcue
      2:200  ObjectData Preview File Format
      2:201  ObjectData Preview File Format Version
      2:202  ObjectData Preview Data
    
    Pre-ObjectData Descriptor Record
      7:10   Size Mode
      7:20   Max Subfile Size
      7:90   ObjectData Size Announced
      7:95   Maximum ObjectData Size
    
    ObjectData Record
      8:10   Subfile
    
    Post ObjectData Descriptor Record
      9:10   Confirmed ObjectData Size
    

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](escape.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
