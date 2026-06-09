[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Configuration Files](resources.html#configure) • [Modules](resources.html#modules) • [Fonts](resources.html#fonts) • [Environment Variables](resources.html#environment)

ImageMagick depends on a number of external resources including configuration files, loadable modules, fonts, and environment variables.

## Configuration Files

ImageMagick depends on a number of external configuration files detailed here:

[coder.xml](../source/coder.xml)
    Associate an image format with the specified coder module. ImageMagick has a number of coder modules to support the reading and/or writing of an image format (e.g. JPEG). Some coder modules support more than one associated image format and the mapping between an associated format and its respective coder module is defined in this configuration file. For example, the PNG coder module not only supports the PNG image format, but the JNG and MNG formats as well. 
[colors.xml](../source/colors.xml)
    Associate a color name with its red, green, blue, and alpha intensities. A number of command line options require a [color parameter](color.html). It is often convenient to refer to a color by name (e.g. white) rather than by hex value (e.g. #fff). This file maps a color name to its equivalent red, green, blue, and alpha intensities (e.g. for white, red = 255, green = 255, blue = 255, and alpha = 0). 
[configure.xml](../source/configure.xml)
    Set ImageMagick build parameters and system-wide environment variables (e.g. MAGICK_TEMPORARY_PATH). As ImageMagick is built, a number of build parameters are saved to this configuration file. They include the version, release date, dependent delegate libraries, and quantum depth among others. 
[delegates.xml](../source/delegates.xml)
    Associate delegate programs with certain image formats. ImageMagick relies on a number of delegate programs to support certain image formats such as [ufraw-batch](http://ufraw.sourceforge.net/) to read raw camera formats or [Ghostscript](http://www.cs.wisc.edu/~ghost/) to read Postscript images. Use this configuration file to map an input or output format to an external delegate program. 
[english.xml](../source/english.xml)
    Associate message tags with English translations.
[francais.xml](../source/francais.xml)
    Associate message tags with French translations. 
[locale.xml](../source/locale.xml)
    Associate message tags with a translation for your locale. ImageMagick has a number of informational, warning, and error messages that are represented as tags. Tags are short descriptions of a message such as FileNotFound or MemoryAllocationFailed. This configuration file lists locales that have a translation for each tag recognized by ImageMagick. Currently only English and French translations are available in the `english.xml` and `francais.xml` configuration files. 
[log.xml](../source/log.xml)
    Configure logging parameters. ImageMagick is capable of spewing copious amounts of informational or debugging statements. Use this file to configure how the information will appear in a log message and where you want the logging messages posted. 
[magic.xml](../source/magic.xml)
    Associate an image format with a unique identifier. Many image formats have identifiers that uniquely identify a particular image format. For example, the GIF image format always begins with `GIF8` as the first 4 characters of the image. ImageMagick uses this information to quickly determine the type of image it is dealing with when it reads an image. 
[mime.xml](../source/mime.xml)
    Associate an internet media type with a unique identifier. Many files and data streams have identifiers that uniquely identify a particular internet media type. For example, files in the "Corel Draw drawing" format (mime type="application/vnd.corel-draw") are associated with the filename pattern `*.cdr`, and also have an initial string of the characters "CDRXvrsn". ImageMagick uses combinations of this information, when available, to attempt to quickly determine the internet media type of a file or data stream. 
[policy.xml](../source/policy.xml)
    Configure ImageMagick policies. By default any coder, delegate, filter, or file path is permitted. Use a policy to deny access to, for example, the MPEG video delegate, or permit reading images from a file system but deny writing to that same file system. Or use the resource policy to set resource limits. Policies are useful for multi-user servers that want to limit the overall impact ImageMagick has on the system. For example, to limit the maximum image size in memory to 100MB: 
    
    
    <policy domain="resource" name="area" value="100MB"/>
    

Any image larger than this area limit is cached to disk rather than memory. Use `width` to limit the maximum width of an image in pixels. Exceed this limit and an exception is thrown and processing stops. 
    
    
    <policy domain="resource" name="width" value="100MP"/>
    

To limit the elapsed time of any ImageMagick command to 5 minutes, use this policy: 
    
    
    <policy domain="resource" name="time" value="300"/>
    

Define arguments for the memory, map, area, and disk resources with SI prefixes (.e.g 100MB). In addition, resource policies are maximums for each instance of ImageMagick (e.g. policy memory limit 1GB, the `-limit 2GB` option exceeds policy maximum so memory limit is 1GB). 
[quantization-table.xml](../source/quantization-table.xml)
    Custom JPEG quantization tables. Activate with `-define:q-table=quantization-table.xml`.
[thresholds.xml](../source/thresholds.xml)
    Set threshold maps for ordered posterized dither.
[type.xml](../source/type.xml)
    Configure fonts. Define the font name, family, foundry, style, format, metrics, and glyphs for any font you want to use within ImageMagick. 
[type-ghostscript.xml](../source/type-ghostscript.xml)
    Configure [Ghostscript](http://www.cs.wisc.edu/~ghost/) fonts. The Ghostscript package includes a number of [fonts](https://sourceforge.net/projects/gs-fonts/) that can be accessed with ImageMagick. 
[type-windows.xml](../source/type-windows.xml)
    Associate names with Windows font glyphs.

Under Unix and Linux, ImageMagick searches for each of the configuration files listed above by looking in the locations given below, in order, and loads them if found:
    
    
    $MAGICK_CONFIGURE_PATH
    $PREFIX/etc/ImageMagick-7 
    $PREFIX/share/ImageMagick-7 
    $XDG_CACHE_HOME/ImageMagick
    $HOME/.config/ImageMagick
    <client path>/etc/ImageMagick
    

The environmental variable $PREFIX is the default install path (e.g. `/usr/local`). The client path is the execution path of your ImageMagick client (e.g. `/usr/local`) .

For the Unix or Linux pre-compiled uninstalled binary distributions, the configuration load order is:
    
    
    $MAGICK_CONFIGURE_PATH
    $MAGICK_HOME/etc/ImageMagick-7 
    $MAGICK_HOME/share/ImageMagick-7 
    $PREFIX/share/ImageMagick-7 
    $XDG_CACHE_HOME/ImageMagick
    $HOME/.config/ImageMagick/
    <client path>/etc/ImageMagick
    <current directory>
    

Under Windows, ImageMagick searches for these configuration files in the following order, and loads them if found:
    
    
    $MAGICK_CONFIGURE_PATH
    <windows registry>
    $PREFIX/config
    $USERPROFILE/.config/ImageMagick
    <client path>
    

Above, $PREFIX is the default install path, typically `c:\\\Program Files\\\ImageMagick-7.0.0`.

For an uninstalled Windows installation, the configuration load order is:
    
    
    $MAGICK_CONFIGURE_PATH
    $MAGICK_HOME
    $USERPROFILE/.config/ImageMagick
    client path
    <current directory>
    

If a configuration file cannot not be found, ImageMagick relies on built-in default values.

## Modules

#### Coders

An image coder (i.e. encoder / decoder) is responsible for registering, optionally classifying, optionally reading, optionally writing, and unregistering one image format (e.g. PNG, GIF, JPEG, etc.). ImageMagick searches for coders in the following order and it uses the first match found:
    
    
    $MAGICK_HOME/lib/ImageMagick-7.0.0/modules-Q16/coders
    <client path>/../lib/ImageMagick-7.0.0/modules-Q16/coders
    $MAGICK_HOME/lib/ImageMagick-7.0.0/modules-Q16/coders
    $MAGICK_HOME/share/ImageMagick-7.0.0/modules-Q16/coders
    $XDG_CACHE_HOME/ImageMagick
    $HOME/.config/ImageMagick
    <client path>/lib/ImageMagick-7.0.0/modules-Q16/coders
    

#### Filters

ImageMagick provides a convenient mechanism for adding your own custom image processing algorithms. ImageMagick searches for filters in the following order and it uses the first match found:
    
    
    $MAGICK_HOME/lib/ImageMagick-7.0.0/modules-Q16/filters
    <client path>/../lib/ImageMagick-7.0.0/modules-Q16/filters
    $MAGICK_HOME/lib/ImageMagick-7.0.0/modules-Q16/filters
    $MAGICK_HOME/share/ImageMagick-7.0.0/modules-Q16/filters
    $XDG_CACHE_HOME/ImageMagick
    $HOME/.config/ImageMagick
    <client path>/lib/ImageMagick-7.0.0/modules-Q16/filters
    

## Fonts

ImageMagick is able to load raw TrueType and Postscript font files. It searches for the font configuration file, [type.xml](resources.html#type.xml), in the following order, and loads them if found:
    
    
    $MAGICK_CONFIGURE_PATH
    $MAGICK_HOME/etc/ImageMagick/-7.0.0$MAGICK_HOME/share/ImageMagick-7.0.0$XDG_CACHE_HOME/ImageMagick
    $HOME/.config/ImageMagick
    <client path>/etc/ImageMagick
    $MAGICK_FONT_PATH
    

## Environment Variables

Environment variables recognized by ImageMagick include:

HOME | Set path to search for configuration files in `$HOME/.config/ImageMagick` if the directory exists.  
---|---  
LD_LIBRARY_PATH | Set path to the ImageMagick shareable libraries and other dependent libraries.  
MAGICK_AREA_LIMIT | Set the maximum width * height of an image that can reside in the pixel cache memory. Images that exceed the area limit are cached to disk (see [MAGICK_DISK_LIMIT](resources.html#disk-limit)) and optionally memory-mapped.  
MAGICK_CODER_FILTER_PATH | Set search path to use when searching for filter process modules (invoked via [-process](command-line-options.html#process)). This path permits the user to extend ImageMagick's image processing functionality by adding loadable modules to a preferred location rather than copying them into the ImageMagick installation directory. The formatting of the search path is similar to operating system search paths (i.e. colon delimited for Unix, and semi-colon delimited for Microsoft Windows). This user specified search path is searched before trying the [default search path](resources.html#modules).  
MAGICK_CODER_MODULE_PATH | Set path where ImageMagick can locate its coder modules. This path permits the user to arbitrarily extend the image formats supported by ImageMagick by adding loadable coder modules from an preferred location rather than copying them into the ImageMagick installation directory. The formatting of the search path is similar to operating system search paths (i.e. colon delimited for Unix, and semi-colon delimited for Microsoft Windows). This user specified search path is searched before trying the [default search path](resources.html#modules).  
MAGICK_CONFIGURE_PATH | Set path where ImageMagick can locate its configuration files. Use this search path to search for configuration (.xml) files. The formatting of the search path is similar to operating system search paths (i.e. colon delimited for Unix, and semi-colon delimited for Microsoft Windows). This user specified search path is searched before trying the [default search path](resources.html#configure).  
MAGICK_DEBUG | Set debug options. See [-debug](command-line-options.html#debug) for a description of debugging options.  
MAGICK_DISK_LIMIT | Set maximum amount of disk space in bytes permitted for use by the pixel cache. When this limit is exceeded, the pixel cache is not be created and an error message is returned.  
MAGICK_ERRORMODE | Set the process error mode (Windows only). A typical use might be a value of 1 to prevent error mode dialogs from displaying a message box and hanging the application.  
MAGICK_FILE_LIMIT | Set maximum number of open pixel cache files. When this limit is exceeded, any subsequent pixels cached to disk are closed and reopened on demand. This behavior permits a large number of images to be accessed simultaneously on disk, but with a speed penalty due to repeated open/close calls.  
MAGICK_FONT_PATH | Set path ImageMagick searches for TrueType and Postscript Type1 font files. This path is only consulted if a particular font file is not found in the current directory.  
MAGICK_HEIGHT_LIMIT | Set the maximum height of an image.  
MAGICK_HOME | Set the path at the top of ImageMagick installation directory. This path is consulted by uninstalled builds of ImageMagick which do not have their location hard-coded or set by an installer.  
MAGICK_MAP_LIMIT | Set maximum amount of memory map in bytes to allocate for the pixel cache. When this limit is exceeded, the image pixels are cached to disk (see MAGICK_DISK_LIMIT).  
MAGICK_MEMORY_LIMIT | Set maximum amount of memory in bytes to allocate for the pixel cache from the heap. When this limit is exceeded, the image pixels are cached to memory-mapped disk (see [MAGICK_MAP_LIMIT](resources.html#map-limit)).  
MAGICK_OCL_DEVICE | Set to `off` to disable hardware acceleration of certain accelerated algorithms (e.g. blur, convolve, etc.).  
MAGICK_PRECISION | Set the maximum number of significant digits to be printed.  
MAGICK_SHRED_PASSES | If you want to keep the temporary files ImageMagick creates private, overwrite them with zeros or random data before they are removed. On the first pass, the file is zeroed. For subsequent passes, random data is written.  
MAGICK_SYNCHRONIZE | Set to "true" to ensure all image data is fully flushed and synchronized to disk. There is a performance penalty, however, the benefits include ensuring a valid image file in the event of a system crash and early reporting if there is not enough disk space for the image pixel cache.  
MAGICK_TEMPORARY_PATH | Set path to store temporary files.  
MAGICK_THREAD_LIMIT | Set maximum parallel threads. Many ImageMagick algorithms run in parallel on multi-processor systems. Use this environment variable to set the maximum number of threads that are permitted to run in parallel.  
MAGICK_THROTTLE | Periodically yield the CPU for at least the time specified in milliseconds.  
MAGICK_TIME_LIMIT | Set maximum time in seconds. When this limit is exceeded, an exception is thrown and processing stops.  
MAGICK_WIDTH_LIMIT | Set the maximum width of an image.  
  
Define arguments for the `MAGICK_AREA_LIMIT`, `MAGICK_DISK_LIMIT`, `MAGICK_MAP_LIMIT`, and `MAGICK_MEMORY_LIMIT` environment variables with SI prefixes (.e.g `100MB`). `MAGICK_WIDTH_LIMIT` and `MAGICK_HEIGHT_LIMIT` accepts pixel suffixes such as MP for mega-pixels (e.g. 100MP).

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](resources.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
