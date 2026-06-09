[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[MagickDeleteImageArtifact](magick-property.html#MagickDeleteImageArtifact) • [MagickDeleteImageProperty](magick-property.html#MagickDeleteImageProperty) • [MagickDeleteOption](magick-property.html#MagickDeleteOption) • [MagickGetAntialias](magick-property.html#MagickGetAntialias) • [MagickGetBackgroundColor](magick-property.html#MagickGetBackgroundColor) • [MagickGetColorspace](magick-property.html#MagickGetColorspace) • [MagickGetCompression](magick-property.html#MagickGetCompression) • [MagickGetCompressionQuality](magick-property.html#MagickGetCompressionQuality) • [MagickGetCopyright](magick-property.html#MagickGetCopyright) • [MagickGetFilename](magick-property.html#MagickGetFilename) • [MagickGetFont](magick-property.html#MagickGetFont) • [MagickGetFormat](magick-property.html#MagickGetFormat) • [MagickGetGravity](magick-property.html#MagickGetGravity) • [MagickGetHomeURL](magick-property.html#MagickGetHomeURL) • [MagickGetImageArtifact](magick-property.html#MagickGetImageArtifact) • [MagickGetImageArtifacts](magick-property.html#MagickGetImageArtifacts) • [MagickGetImageProfile](magick-property.html#MagickGetImageProfile) • [MagickGetImageProfiles](magick-property.html#MagickGetImageProfiles) • [MagickGetImageProperty](magick-property.html#MagickGetImageProperty) • [MagickGetImageProperties](magick-property.html#MagickGetImageProperties) • [MagickGetInterlaceScheme](magick-property.html#MagickGetInterlaceScheme) • [MagickGetInterpolateMethod](magick-property.html#MagickGetInterpolateMethod) • [MagickGetOption](magick-property.html#MagickGetOption) • [MagickGetOptions](magick-property.html#MagickGetOptions) • [MagickGetOrientation](magick-property.html#MagickGetOrientation) • [MagickGetPackageName](magick-property.html#MagickGetPackageName) • [MagickGetPage](magick-property.html#MagickGetPage) • [MagickGetPointsize](magick-property.html#MagickGetPointsize) • [MagickGetQuantumDepth](magick-property.html#MagickGetQuantumDepth) • [MagickGetQuantumRange](magick-property.html#MagickGetQuantumRange) • [MagickGetReleaseDate](magick-property.html#MagickGetReleaseDate) • [MagickGetResolution](magick-property.html#MagickGetResolution) • [MagickGetResource](magick-property.html#MagickGetResource) • [MagickGetResourceLimit](magick-property.html#MagickGetResourceLimit) • [MagickGetSamplingFactors](magick-property.html#MagickGetSamplingFactors) • [MagickGetSize](magick-property.html#MagickGetSize) • [MagickGetSizeOffset](magick-property.html#MagickGetSizeOffset) • [MagickGetType](magick-property.html#MagickGetType) • [MagickGetVersion](magick-property.html#MagickGetVersion) • [MagickProfileImage](magick-property.html#MagickProfileImage) • [MagickRemoveImageProfile](magick-property.html#MagickRemoveImageProfile) • [MagickSetAntialias](magick-property.html#MagickSetAntialias) • [MagickSetBackgroundColor](magick-property.html#MagickSetBackgroundColor) • [MagickSetColorspace](magick-property.html#MagickSetColorspace) • [MagickSetCompression](magick-property.html#MagickSetCompression) • [MagickSetCompressionQuality](magick-property.html#MagickSetCompressionQuality) • [MagickSetDepth](magick-property.html#MagickSetDepth) • [MagickSetExtract](magick-property.html#MagickSetExtract) • [MagickSetFilename](magick-property.html#MagickSetFilename) • [MagickSetFont](magick-property.html#MagickSetFont) • [MagickSetFormat](magick-property.html#MagickSetFormat) • [MagickSetGravity](magick-property.html#MagickSetGravity) • [MagickSetImageArtifact](magick-property.html#MagickSetImageArtifact) • [MagickSetImageProfile](magick-property.html#MagickSetImageProfile) • [MagickSetImageProperty](magick-property.html#MagickSetImageProperty) • [MagickSetInterlaceScheme](magick-property.html#MagickSetInterlaceScheme) • [MagickSetInterpolateMethod](magick-property.html#MagickSetInterpolateMethod) • [MagickSetOption](magick-property.html#MagickSetOption) • [MagickSetOrientation](magick-property.html#MagickSetOrientation) • [MagickSetPage](magick-property.html#MagickSetPage) • [MagickSetPassphrase](magick-property.html#MagickSetPassphrase) • [MagickSetPointsize](magick-property.html#MagickSetPointsize) • [MagickSetProgressMonitor](magick-property.html#MagickSetProgressMonitor) • [MagickSetResourceLimit](magick-property.html#MagickSetResourceLimit) • [MagickSetResolution](magick-property.html#MagickSetResolution) • [MagickSetSamplingFactors](magick-property.html#MagickSetSamplingFactors) • [MagickSetSize](magick-property.html#MagickSetSize) • [MagickSetSizeOffset](magick-property.html#MagickSetSizeOffset) • [MagickSetType](magick-property.html#MagickSetType)

## [MagickDeleteImageArtifact](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickDeleteImageArtifact() deletes a wand artifact.

The format of the MagickDeleteImageArtifact method is:
    
    
    MagickBooleanType MagickDeleteImageArtifact(MagickWand *wand,
      const char *artifact)
    

A description of each parameter follows:

    
    

image
    the image. 
    
artifact
    the image artifact. 
    

## [MagickDeleteImageProperty](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickDeleteImageProperty() deletes a wand property.

The format of the MagickDeleteImageProperty method is:
    
    
    MagickBooleanType MagickDeleteImageProperty(MagickWand *wand,
      const char *property)
    

A description of each parameter follows:

    
    

image
    the image. 
    
property
    the image property. 
    

## [MagickDeleteOption](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickDeleteOption() deletes a wand option.

The format of the MagickDeleteOption method is:
    
    
    MagickBooleanType MagickDeleteOption(MagickWand *wand,
      const char *option)
    

A description of each parameter follows:

    
    

image
    the image. 
    
option
    the image option. 
    

## [MagickGetAntialias](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetAntialias() returns the antialias property associated with the wand.

The format of the MagickGetAntialias method is:
    
    
    MagickBooleanType MagickGetAntialias(const MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetBackgroundColor](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetBackgroundColor() returns the wand background color.

The format of the MagickGetBackgroundColor method is:
    
    
    PixelWand *MagickGetBackgroundColor(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetColorspace](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetColorspace() gets the wand colorspace type.

The format of the MagickGetColorspace method is:
    
    
    ColorspaceType MagickGetColorspace(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetCompression](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetCompression() gets the wand compression type.

The format of the MagickGetCompression method is:
    
    
    CompressionType MagickGetCompression(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetCompressionQuality](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetCompressionQuality() gets the wand compression quality.

The format of the MagickGetCompressionQuality method is:
    
    
    size_t MagickGetCompressionQuality(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetCopyright](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetCopyright() returns the ImageMagick API copyright as a string constant.

The format of the MagickGetCopyright method is:
    
    
    const char *MagickGetCopyright(void)
    

## [MagickGetFilename](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetFilename() returns the filename associated with an image sequence.

The format of the MagickGetFilename method is:
    
    
    const char *MagickGetFilename(const MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetFont](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetFont() returns the font associated with the MagickWand.

The format of the MagickGetFont method is:
    
    
    char *MagickGetFont(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetFormat](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetFormat() returns the format of the magick wand.

The format of the MagickGetFormat method is:
    
    
    const char MagickGetFormat(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetGravity](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetGravity() gets the wand gravity.

The format of the MagickGetGravity method is:
    
    
    GravityType MagickGetGravity(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetHomeURL](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetHomeURL() returns the ImageMagick home URL.

The format of the MagickGetHomeURL method is:
    
    
    char *MagickGetHomeURL(void)
    

## [MagickGetImageArtifact](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetImageArtifact() returns a value associated with the specified artifact. Use MagickRelinquishMemory() to free the value when you are finished with it.

The format of the MagickGetImageArtifact method is:
    
    
    char *MagickGetImageArtifact(MagickWand *wand,const char *artifact)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
artifact
    the artifact. 
    

## [MagickGetImageArtifacts](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetImageArtifacts() returns all the artifact names that match the specified pattern associated with a wand. Use MagickGetImageProperty() to return the value of a particular artifact. Use MagickRelinquishMemory() to free the value when you are finished with it.

The format of the MagickGetImageArtifacts method is:
    
    
    char *MagickGetImageArtifacts(MagickWand *wand,
      const char *pattern,size_t *number_artifacts)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_artifacts
    the number artifacts associated with this wand. 
    

## [MagickGetImageProfile](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetImageProfile() returns the named image profile.

The format of the MagickGetImageProfile method is:
    
    
    unsigned char *MagickGetImageProfile(MagickWand *wand,const char *name,
      size_t *length)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
name
    Name of profile to return: ICC, IPTC, or generic profile. 
    
length
    the length of the profile. 
    

## [MagickGetImageProfiles](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetImageProfiles() returns all the profile names that match the specified pattern associated with a wand. Use MagickGetImageProfile() to return the value of a particular property. Use MagickRelinquishMemory() to free the value when you are finished with it.

The format of the MagickGetImageProfiles method is:
    
    
    char *MagickGetImageProfiles(MagickWand *wand,const char *pattern,
      size_t *number_profiles)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_profiles
    the number profiles associated with this wand. 
    

## [MagickGetImageProperty](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetImageProperty() returns a value associated with the specified property. Use MagickRelinquishMemory() to free the value when you are finished with it.

The format of the MagickGetImageProperty method is:
    
    
    char *MagickGetImageProperty(MagickWand *wand,const char *property)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
property
    the property. 
    

## [MagickGetImageProperties](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetImageProperties() returns all the property names that match the specified pattern associated with a wand. Use MagickGetImageProperty() to return the value of a particular property. Use MagickRelinquishMemory() to free the value when you are finished with it.

The format of the MagickGetImageProperties method is:
    
    
    char *MagickGetImageProperties(MagickWand *wand,
      const char *pattern,size_t *number_properties)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_properties
    the number properties associated with this wand. 
    

## [MagickGetInterlaceScheme](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetInterlaceScheme() gets the wand interlace scheme.

The format of the MagickGetInterlaceScheme method is:
    
    
    InterlaceType MagickGetInterlaceScheme(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetInterpolateMethod](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetInterpolateMethod() gets the wand compression.

The format of the MagickGetInterpolateMethod method is:
    
    
    PixelInterpolateMethod MagickGetInterpolateMethod(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetOption](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetOption() returns a value associated with a wand and the specified key. Use MagickRelinquishMemory() to free the value when you are finished with it.

The format of the MagickGetOption method is:
    
    
    char *MagickGetOption(MagickWand *wand,const char *key)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
key
    the key. 
    

## [MagickGetOptions](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetOptions() returns all the option names that match the specified pattern associated with a wand. Use MagickGetOption() to return the value of a particular option. Use MagickRelinquishMemory() to free the value when you are finished with it.

The format of the MagickGetOptions method is:
    
    
    char *MagickGetOptions(MagickWand *wand,const char *pattern,
      size_t *number_options)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_options
    the number options associated with this wand. 
    

## [MagickGetOrientation](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetOrientation() gets the wand orientation type.

The format of the MagickGetOrientation method is:
    
    
    OrientationType MagickGetOrientation(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetPackageName](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetPackageName() returns the ImageMagick package name as a string constant.

The format of the MagickGetPackageName method is:
    
    
    const char *MagickGetPackageName(void)
    

## [MagickGetPage](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetPage() returns the page geometry associated with the magick wand.

The format of the MagickGetPage method is:
    
    
    MagickBooleanType MagickGetPage(const MagickWand *wand,
      size_t *width,size_t *height,ssize_t *x,ssize_t *y)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
width
    the page width. 
    
height
    page height. 
    
x
    the page x-offset. 
    
y
    the page y-offset. 
    

## [MagickGetPointsize](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetPointsize() returns the font pointsize associated with the MagickWand.

The format of the MagickGetPointsize method is:
    
    
    double MagickGetPointsize(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetQuantumDepth](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetQuantumDepth() returns the ImageMagick quantum depth as a string constant.

The format of the MagickGetQuantumDepth method is:
    
    
    const char *MagickGetQuantumDepth(size_t *depth)
    

A description of each parameter follows:

    
    

depth
    the quantum depth is returned as a number. 
    

## [MagickGetQuantumRange](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetQuantumRange() returns the ImageMagick quantum range as a string constant.

The format of the MagickGetQuantumRange method is:
    
    
    const char *MagickGetQuantumRange(size_t *range)
    

A description of each parameter follows:

    
    

range
    the quantum range is returned as a number. 
    

## [MagickGetReleaseDate](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetReleaseDate() returns the ImageMagick release date as a string constant.

The format of the MagickGetReleaseDate method is:
    
    
    const char *MagickGetReleaseDate(void)
    

## [MagickGetResolution](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetResolution() gets the image X and Y resolution.

The format of the MagickGetResolution method is:
    
    
    MagickBooleanType MagickGetResolution(const MagickWand *wand,double *x,
      double *y)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
x
    the x-resolution. 
    
y
    the y-resolution. 
    

## [MagickGetResource](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetResource() returns the specified resource in megabytes.

The format of the MagickGetResource method is:
    
    
    MagickSizeType MagickGetResource(const ResourceType type)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetResourceLimit](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetResourceLimit() returns the specified resource limit in megabytes.

The format of the MagickGetResourceLimit method is:
    
    
    MagickSizeType MagickGetResourceLimit(const ResourceType type)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetSamplingFactors](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetSamplingFactors() gets the horizontal and vertical sampling factor.

The format of the MagickGetSamplingFactors method is:
    
    
    double *MagickGetSamplingFactor(MagickWand *wand,
      size_t *number_factors)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
number_factors
    the number of factors in the returned array. 
    

## [MagickGetSize](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetSize() returns the size associated with the magick wand.

The format of the MagickGetSize method is:
    
    
    MagickBooleanType MagickGetSize(const MagickWand *wand,
      size_t *columns,size_t *rows)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
columns
    the width in pixels. 
    
height
    the height in pixels. 
    

## [MagickGetSizeOffset](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetSizeOffset() returns the size offset associated with the magick wand.

The format of the MagickGetSizeOffset method is:
    
    
    MagickBooleanType MagickGetSizeOffset(const MagickWand *wand,
      ssize_t *offset)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
offset
    the image offset. 
    

## [MagickGetType](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetType() returns the wand type.

The format of the MagickGetType method is:
    
    
    ImageType MagickGetType(MagickWand *wand)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    

## [MagickGetVersion](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickGetVersion() returns the ImageMagick API version as a string constant and as a number.

The format of the MagickGetVersion method is:
    
    
    const char *MagickGetVersion(size_t *version)
    

A description of each parameter follows:

    
    

version
    the ImageMagick version is returned as a number. 
    

## [MagickProfileImage](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickProfileImage() adds or removes a ICC, IPTC, or generic profile from an image. If the profile is NULL, it is removed from the image otherwise added. Use a name of '*' and a profile of NULL to remove all profiles from the image.

The format of the MagickProfileImage method is:
    
    
    MagickBooleanType MagickProfileImage(MagickWand *wand,const char *name,
      const void *profile,const size_t length)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
name
    Name of profile to add or remove: ICC, IPTC, or generic profile. 
    
profile
    the profile. 
    
length
    the length of the profile. 
    

## [MagickRemoveImageProfile](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickRemoveImageProfile() removes the named image profile and returns it.

The format of the MagickRemoveImageProfile method is:
    
    
    unsigned char *MagickRemoveImageProfile(MagickWand *wand,
      const char *name,size_t *length)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
name
    Name of profile to return: ICC, IPTC, or generic profile. 
    
length
    the length of the profile. 
    

## [MagickSetAntialias](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetAntialias() sets the antialias propery of the wand.

The format of the MagickSetAntialias method is:
    
    
    MagickBooleanType MagickSetAntialias(MagickWand *wand,
      const MagickBooleanType antialias)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
antialias
    the antialias property. 
    

## [MagickSetBackgroundColor](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetBackgroundColor() sets the wand background color.

The format of the MagickSetBackgroundColor method is:
    
    
    MagickBooleanType MagickSetBackgroundColor(MagickWand *wand,
      const PixelWand *background)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
background
    the background pixel wand. 
    

## [MagickSetColorspace](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetColorspace() sets the wand colorspace type.

The format of the MagickSetColorspace method is:
    
    
    MagickBooleanType MagickSetColorspace(MagickWand *wand,
      const ColorspaceType colorspace)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
colorspace
    the wand colorspace. 
    

## [MagickSetCompression](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetCompression() sets the wand compression type.

The format of the MagickSetCompression method is:
    
    
    MagickBooleanType MagickSetCompression(MagickWand *wand,
      const CompressionType compression)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
compression
    the wand compression. 
    

## [MagickSetCompressionQuality](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetCompressionQuality() sets the wand compression quality.

The format of the MagickSetCompressionQuality method is:
    
    
    MagickBooleanType MagickSetCompressionQuality(MagickWand *wand,
      const size_t quality)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
quality
    the wand compression quality. 
    

## [MagickSetDepth](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetDepth() sets the wand pixel depth.

The format of the MagickSetDepth method is:
    
    
    MagickBooleanType MagickSetDepth(MagickWand *wand,
      const size_t depth)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
depth
    the wand pixel depth. 
    

## [MagickSetExtract](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetExtract() sets the extract geometry before you read or write an image file. Use it for inline cropping (e.g. 200x200+0+0) or resizing (e.g.200x200).

The format of the MagickSetExtract method is:
    
    
    MagickBooleanType MagickSetExtract(MagickWand *wand,
      const char *geometry)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
geometry
    the extract geometry. 
    

## [MagickSetFilename](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetFilename() sets the filename before you read or write an image file.

The format of the MagickSetFilename method is:
    
    
    MagickBooleanType MagickSetFilename(MagickWand *wand,
      const char *filename)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
filename
    the image filename. 
    

## [MagickSetFont](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetFont() sets the font associated with the MagickWand.

The format of the MagickSetFont method is:
    
    
    MagickBooleanType MagickSetFont(MagickWand *wand, const char *font)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
font
    the font 
    

## [MagickSetFormat](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetFormat() sets the format of the magick wand.

The format of the MagickSetFormat method is:
    
    
    MagickBooleanType MagickSetFormat(MagickWand *wand,const char *format)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
format
    the image format. 
    

## [MagickSetGravity](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetGravity() sets the gravity type.

The format of the MagickSetGravity type is:
    
    
    MagickBooleanType MagickSetGravity(MagickWand *wand,
      const GravityType type)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
type
    the gravity type. 
    

## [MagickSetImageArtifact](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetImageArtifact() associates a artifact with an image.

The format of the MagickSetImageArtifact method is:
    
    
    MagickBooleanType MagickSetImageArtifact(MagickWand *wand,
      const char *artifact,const char *value)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
artifact
    the artifact. 
    
value
    the value. 
    

## [MagickSetImageProfile](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetImageProfile() adds a named profile to the magick wand. If a profile with the same name already exists, it is replaced. This method differs from the MagickProfileImage() method in that it does not apply any CMS color profiles.

The format of the MagickSetImageProfile method is:
    
    
    MagickBooleanType MagickSetImageProfile(MagickWand *wand,
      const char *name,const void *profile,const size_t length)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
name
    Name of profile to add or remove: ICC, IPTC, or generic profile. 
    
profile
    the profile. 
    
length
    the length of the profile. 
    

## [MagickSetImageProperty](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetImageProperty() associates a property with an image.

The format of the MagickSetImageProperty method is:
    
    
    MagickBooleanType MagickSetImageProperty(MagickWand *wand,
      const char *property,const char *value)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
property
    the property. 
    
value
    the value. 
    

## [MagickSetInterlaceScheme](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetInterlaceScheme() sets the image compression.

The format of the MagickSetInterlaceScheme method is:
    
    
    MagickBooleanType MagickSetInterlaceScheme(MagickWand *wand,
      const InterlaceType interlace_scheme)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
interlace_scheme
    the image interlace scheme: NoInterlace, LineInterlace, PlaneInterlace, PartitionInterlace. 
    

## [MagickSetInterpolateMethod](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetInterpolateMethod() sets the interpolate pixel method.

The format of the MagickSetInterpolateMethod method is:
    
    
    MagickBooleanType MagickSetInterpolateMethod(MagickWand *wand,
      const InterpolateMethodPixel method)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
method
    the interpolate pixel method. 
    

## [MagickSetOption](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetOption() associates one or options with the wand (.e.g MagickSetOption(wand,"jpeg:perserve","yes")).

The format of the MagickSetOption method is:
    
    
    MagickBooleanType MagickSetOption(MagickWand *wand,const char *key,
      const char *value)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
key
     The key. 
    
value
     The value. 
    

## [MagickSetOrientation](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetOrientation() sets the wand orientation type.

The format of the MagickSetOrientation method is:
    
    
    MagickBooleanType MagickSetOrientation(MagickWand *wand,
      const OrientationType orientation)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
orientation
    the wand orientation. 
    

## [MagickSetPage](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetPage() sets the page geometry of the magick wand.

The format of the MagickSetPage method is:
    
    
    MagickBooleanType MagickSetPage(MagickWand *wand,
      const size_t width,const size_t height,const ssize_t x,
      const ssize_t y)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
width
    the page width. 
    
height
    the page height. 
    
x
    the page x-offset. 
    
y
    the page y-offset. 
    

## [MagickSetPassphrase](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetPassphrase() sets the passphrase.

The format of the MagickSetPassphrase method is:
    
    
    MagickBooleanType MagickSetPassphrase(MagickWand *wand,
      const char *passphrase)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
passphrase
    the passphrase. 
    

## [MagickSetPointsize](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetPointsize() sets the font pointsize associated with the MagickWand.

The format of the MagickSetPointsize method is:
    
    
    MagickBooleanType MagickSetPointsize(MagickWand *wand,
      const double pointsize)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
pointsize
    the size of the font 
    

## [MagickSetProgressMonitor](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetProgressMonitor() sets the wand progress monitor to the specified method and returns the previous progress monitor if any. The progress monitor method looks like this:
    
    
        MagickBooleanType MagickProgressMonitor(const char *text,
    const MagickOffsetType offset,const MagickSizeType span,
    void *client_data)
    

If the progress monitor returns MagickFalse, the current operation is interrupted.

The format of the MagickSetProgressMonitor method is:
    
    
    MagickProgressMonitor MagickSetProgressMonitor(MagickWand *wand
      const MagickProgressMonitor progress_monitor,void *client_data)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
progress_monitor
    Specifies a pointer to a method to monitor progress of an image operation. 
    
client_data
    Specifies a pointer to any client data. 
    

## [MagickSetResourceLimit](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetResourceLimit() sets the limit for a particular resource in megabytes.

The format of the MagickSetResourceLimit method is:
    
    
    MagickBooleanType MagickSetResourceLimit(const ResourceType type,
      const MagickSizeType limit)
    

A description of each parameter follows:

    
    

type
    the type of resource: AreaResource, MemoryResource, MapResource, DiskResource, FileResource. 
     o The maximum limit for the resource. 
    

## [MagickSetResolution](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetResolution() sets the image resolution.

The format of the MagickSetResolution method is:
    
    
    MagickBooleanType MagickSetResolution(MagickWand *wand,
      const double x_resolution,const double y_resolution)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
x_resolution
    the image x resolution. 
    
y_resolution
    the image y resolution. 
    

## [MagickSetSamplingFactors](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetSamplingFactors() sets the image sampling factors.

The format of the MagickSetSamplingFactors method is:
    
    
    MagickBooleanType MagickSetSamplingFactors(MagickWand *wand,
      const size_t number_factors,const double *sampling_factors)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
number_factoes
    the number of factors. 
    
sampling_factors
    An array of doubles representing the sampling factor for each color component (in RGB order). 
    

## [MagickSetSize](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetSize() sets the size of the magick wand. Set it before you read a raw image format such as RGB, GRAY, or CMYK.

The format of the MagickSetSize method is:
    
    
    MagickBooleanType MagickSetSize(MagickWand *wand,
      const size_t columns,const size_t rows)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
columns
    the width in pixels. 
    
rows
    the rows in pixels. 
    

## [MagickSetSizeOffset](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetSizeOffset() sets the size and offset of the magick wand. Set it before you read a raw image format such as RGB, GRAY, or CMYK.

The format of the MagickSetSizeOffset method is:
    
    
    MagickBooleanType MagickSetSizeOffset(MagickWand *wand,
      const size_t columns,const size_t rows,
      const ssize_t offset)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
columns
    the image width in pixels. 
    
rows
    the image rows in pixels. 
    
offset
    the image offset. 
    

## [MagickSetType](http://www.imagemagick.org/api/MagickWand/magick-property_8c.html)

MagickSetType() sets the image type attribute.

The format of the MagickSetType method is:
    
    
    MagickBooleanType MagickSetType(MagickWand *wand,
      const ImageType image_type)
    

A description of each parameter follows:

    
    

wand
    the magick wand. 
    
image_type
    the image type: UndefinedType, BilevelType, GrayscaleType, GrayscaleAlphaType, PaletteType, PaletteAlphaType, TrueColorType, TrueColorAlphaType, ColorSeparationType, ColorSeparationAlphaType, or OptimizeType. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](magick-property.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
