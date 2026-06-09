[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Build ImageMagickObject From Source](index.html#build)

The ImageMagickObject is a COM+ compatible component that can be invoked from any language capable of using COM objects. The intended use is for Windows Scripting Host VBS scripts and Visual Basic, but it is also available from to C++, ASP, and other languages like Delphi, Perl and PHP.

The ImageMagickObject COM+ component provides access to the [compare](compare.html), [convert](convert.html), [composite](composite.html), [mogrify](mogrify.html), [identify](identify.html), [montage](montage.html), and [stream](stream.html) tools, efficiently executing them as part of your process, rather than as external programs. The way you use it is exactly the same. You pass it a list of strings including filenames and various options and it does the job. In fact, you can take any existing batch scripts that use the command line tools and translate them into the equivalent calls to the COM+ object in a matter of minutes. Beyond that, there is also a way to pass in and retrieve images in memory in the form of standard smart arrays (byte arrays). Samples are provided, to show both the simple and more elaborate forms of access.

ImageMagick provides a statically-built ImageMagick object as part of its [Windows installation package](binary-releases.html#windows). When this package is installed, ImageMagickObject and its sample programs are installed to this path:
    
    
      c:\Program Files\ImageMagick-7.0.0-Q16\ImageMagickObject
    

The ImageMagickObject is registered if the checkbox, `Register ImageMagickObject`, is checked at install time.

To execute the sample program from the Windows Command Shell, type:
    
    
    cscript SimpleTest.vbs
    

Since the ImageMagick utility command line parsers are incorporated within ImageMagickObject, please refer to the [command-line tools](command-line-tools.html) discussion to learn how to use it. The sample VBS scripts show how the object should be called and used and have lots of comments.

C++ programmers should have a look at the `MagickCMD.cpp` command line utility for an example of how to call the object from C++. The object requires a variable size list of BSTR's to emulate the command line argc, argv style calling conventions of the COM component which is more complex in C++ then in VBS or VB.

MagickCMD is a C++ sample, but it also serves as a replacement for all the other command line utilities in most applications. Instead of using `convert xxxx yyyy` you can use `MagickCMD convert xxxx yyyy` instead. MagickCMD calls the COM object to accomplish the designated task. This small tight combination replaces the entire usual binary distribution in just a few mebibytes.

## Build ImageMagickObject From Source

The source code for ImageMagickObject is available from the ImageMagick [GIT](http://git.imagemagick.org/repos/ImageMagick) repository, or as part of the [Windows source](install-source.html#windows) distribution. Once the source code has been retrieved and extracted, the source for ImageMagickObject is the directory `ImageMagick\contrib\win32\ATL7ImageMagickObject`, however, ImageMagick itself must be built using the static-multithread (VisualStaticMT) build configuration. Building ImageMagickObject requires Microsoft Visual C++ 7.0 as delivered with Microsoft's Visual Studio .NET package. See the [Windows compilation instructions](install-source.html#windows) to get ImageMagick itself built before building the ImageMagick COM+ component.

Once the VisualStaticMT project has been built, build the ImageMagickObject with this procedure:
    
    
    cd ImageMagick/contrib/win32/ATL7/ImageMagickObject
    BuildImageMagickObject release
    

Here, we assume that the VisualStaticMT project has been built using the release setting for an optimized build. If the debug setting was used for a debug build, specify the argument `debug`; instead.

To register the DLL as a COM+ server, type
    
    
    regsvr32 /c /s ImageMagickObject.dll
    

To unregister the DLL, type
    
    
    regsvr32 /u /s ImageMagickObject.dll
    

Use MagickCMD to exercise ImageMagickObject to verify that it is working properly.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](ImageMagickObject.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
