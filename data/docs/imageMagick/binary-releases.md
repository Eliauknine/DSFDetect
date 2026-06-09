[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Unix Binary Release](binary-releases.html#unix) • [Mac OS X Binary Release](binary-releases.html#macosx) • [iOS Binary Release](binary-releases.html#iOS) • [Windows Binary Release](binary-releases.html#windows)

You can install ImageMagick from [source](install-source.html). However, if you don't have a proper development environment or if you're anxious to get started, download a ready-to-run [Unix](binary-releases.html#unix) or [Windows](binary-releases.html#windows) executable. Before you download, you may want to review recent [changes](changelog.html) to the ImageMagick distribution.

## Unix Binary Release

These are the Unix variations that we support. If your system is not on the list, try installing from [source](install-source.html). Although ImageMagick runs fine on a single core computer, it automagically runs in parallel on dual and quad-core systems reducing run times considerably.

Version | HTTP | FTP | Description  
---|---|---|---  
ImageMagick-7.0.0-0.x86_64.rpm | [download](http://www.imagemagick.org/download/linux/CentOS/x86_64/ImageMagick-7.0.0-0.x86_64.rpm) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/linux/CentOS/x86_64/ImageMagick-7.0.0-0.x86_64.rpm) | Redhat / CentOS 7.1 x86_64 RPM  
ImageMagick-7.0.0-0.i386.rpm | [download](http://www.imagemagick.org/download/linux/CentOS/i386/ImageMagick-7.0.0-0.i386.rpm) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/linux/CentOS/i386/ImageMagick-7.0.0-0.i386.rpm) | Redhat / CentOS 5.11 i386 RPM  
ImageMagick RPM's | [download](http://www.imagemagick.org/download/linux/CentOS) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/linux/CentOS) | Development, Perl, C++, and documentation RPM's.  
ImageMagick-i386-pc-solaris2.11.tar.gz | [download](http://www.imagemagick.org/download/binaries/ImageMagick-i386-pc-solaris2.11.tar.gz) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-i386-pc-solaris2.11.tar.gz) | Solaris Sparc 2.11  
ImageMagick-i686-pc-cygwin.tar.gz | [download](http://www.imagemagick.org/download/binaries/ImageMagick-i686-pc-cygwin.tar.gz) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-i686-pc-cygwin.tar.gz) | Cygwin  
ImageMagick-i686-pc-mingw32.tar.gz | [download](http://www.imagemagick.org/download/binaries/ImageMagick-i686-pc-mingw32.tar.gz) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-i686-pc-mingw32.tar.gz) | MinGW  
  
Verify its [message digest](http://www.imagemagick.org/download/binaries/digest.rdf).

ImageMagick RPM's are self-installing. Simply type the following command and you're ready to start using ImageMagick:
    
    
     rpm -Uvh ImageMagick-7.0.0-0.i386.rpm

For other systems, create (or choose) a directory to install the package into and change to that directory, for example:
    
    
    cd $HOME
    

Next, extract the contents of the package. For example:
    
    
    tar xvzf ImageMagick.tar.gz
    

Set the `MAGICK_HOME` environment variable to the path where you extracted the ImageMagick files. For example:
    
    
     export MAGICK_HOME="$HOME/ImageMagick-7.0.0"

If the `bin` subdirectory of the extracted package is not already in your executable search path, add it to your `PATH` environment variable. For example:
    
    
    export PATH="$MAGICK_HOME/bin:$PATH
    

On Linux and Solaris machines add `$MAGICK_HOME/lib` to the `LD_LIBRARY_PATH` environment variable:
    
    
    LD_LIBRARY_PATH="${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$MAGICK_HOME/lib
    export LD_LIBRARY_PATH
    

Finally, to verify ImageMagick is working properly, type the following on the command line:
    
    
    convert logo: logo.gif
    identify logo.gif
    display logo.gif
    

Congratulations, you have a working ImageMagick distribution under Unix or Linux and you are ready to use ImageMagick to [convert, compose, or edit](http://www.imagemagick.org/Usage/) your images or perhaps you'll want to use one of the [Application Program Interfaces](api.html) for C, C++, Perl, and others.

## Mac OS X Binary Release

We recommend [MacPorts](http://www.macports.org) which custom builds ImageMagick in your environment (some users prefer [Homebrew](http://brew.sh)). Download MacPorts and type:
    
    
    sudo port install ImageMagick
    

The `port` command downloads ImageMagick and many of its delegate libraries (e.g. JPEG, PNG, Freetype, etc.) and configures, builds, and installs ImageMagick automagically. Alternatively, you can download the ImageMagick Mac OS X distribution we provide:

Version | HTTP | FTP | Description  
---|---|---|---  
ImageMagick-x86_64-apple-darwin15.2.0.tar.gz | [download](http://www.imagemagick.org/download/binaries/ImageMagick-x86_64-apple-darwin15.2.0.tar.gz) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-x86_64-apple-darwin15.2.0.tar.gz) | Mac OS X El Capitan  
  
Verify its [message digest](http://www.imagemagick.org/download/binaries/digest.rdf).

Create (or choose) a directory to install the package into and change to that directory, for example:
    
    
    cd $HOME
    

Next, extract the contents of the package. For example:
    
    
    tar xvzf ImageMagick-x86_64-apple-darwin15.2.0.tar.gz
    

Set the `MAGICK_HOME` environment variable to the path where you extracted the ImageMagick files. For example:
    
    
     export MAGICK_HOME="$HOME/ImageMagick-7.0.0"

If the `bin` subdirectory of the extracted package is not already in your executable search path, add it to your `PATH` environment variable. For example:
    
    
    export PATH="$MAGICK_HOME/bin:$PATH"
    

Set the `DYLD_LIBRARY_PATH` environment variable:
    
    
    export DYLD_LIBRARY_PATH="$MAGICK_HOME/lib/"
    

Finally, to verify ImageMagick is working properly, type the following on the command line:
    
    
    convert logo: logo.gif
    identify logo.gif
    display logo.gif
    

**Note** , the [display](display.html) program requires the X11 server available on your Mac OS X installation DVD. Once that is installed, you will also need to `export DISPLAY=:0`.

The best way to deal with all the exports is to put them at the end of your .profile file

Congratulations, you have a working ImageMagick distribution under Mac OS X and you are ready to use ImageMagick to [convert, compose, or edit](http://www.imagemagick.org/Usage/) your images or perhaps you'll want to use one of the [Application Program Interfaces](api.html) for C, C++, Perl, and others.

## iOS Binary Release

[~Claudio](http://www.cloudgoessocial.net/2011/03/21/im-xcode4-ios4-3/) provides iOS builds of ImageMagick.

#### Download iOS Distribution

You can download the iOS distribution directly from ImageMagick's [repository](http://www.imagemagick.org/download/iOS).

There are always 2 packages for the compiled ImageMagick:

  * iOSMagick-VERSION-libs.zip
  * iOSMagick-VERSION.zip



The first one includes headers and compiled libraries that have been used to compile ImageMagick. Most users would need this one.

#### ImageMagick compiling script for iOS OS and iOS Simulator

To run the script:
    
    
    ./imagemagick_compile.sh VERSION
    

where VERSION is the version of ImageMagick you want to compile (i.e.: 7.0.0-0, svn, ...)

This script compiles ImageMagick as a static library to be included in iOS projects and adds support for

  * png
  * jpeg
  * tiff



Upon successful compilation a folder called `IMPORT_ME` is created on your `~/Desktop`. You can import it into your XCode project.

##### XCode project settings

After including everything into XCode please also make sure to have these settings (Build tab of the project information):

  * Other Linker Flags: -lMagickCore-Q16 -lMagickWand-Q16 -ljpeg -lpng -lbz2 -lz
  * Header Search Paths: $(SRCROOT) - make it Recursive
  * Library Search Paths: $(SRCROOT) - make it Recursive



On the lower left click on the small-wheel and select: Add User-Defined Setting

  * Key: OTHER_CFLAGS
  * Value: -Dmacintosh=1



##### Sample project

A [sample project ](http://www.cloudgoessocial.net/im_iphone/IM_Test.zip) is available for download. It is not updated too often, but it does give an idea of all the settings and some ways to play around with ImageMagick in an iOS application.

## Windows Binary Release

ImageMagick runs on Windows 8 (x86 & x64), Windows 7 (x86 & x64), Windows Server 2012, Windows XP (x86) with Service Pack 3, Windows Vista (x86 & x64) with Service Pack 2, Windows Server 2003 (x86 & x64) with Service Pack 2 (verify MSXML6 is present), Windows Server 2003 R2 (x86 & x64), Windows Server 2008 (x86 & x64) with Service Pack 2, and Windows Server 2008 R2 (x64).

The amount of memory can be an important factor, especially if you intend to work on large images. A minimum of 512 MB of RAM is recommended, but the more RAM the better. Although ImageMagick runs well on a single core computer, it automagically runs in parallel on multi-core systems reducing run times considerably.

The Windows version of ImageMagick is self-installing. Simply click on the appropriate version below and it will launch itself and ask you a few installation questions. Versions with Q8 in the name are 8 bits-per-pixel component (e.g. 8-bit red, 8-bit green, etc.), whereas, Q16 in the filename are 16 bits-per-pixel component. A Q16 version permits you to read or write 16-bit images without losing precision but requires twice as much resources as the Q8 version. Versions with dll in the filename include ImageMagick libraries as [dynamic link libraries](http://www.answers.com/topic/dll). Unless you have a Windows 32-bit OS, we recommend this version of ImageMagick for 64-bit Windows:

Version | HTTP | FTP | Description  
---|---|---|---  
ImageMagick-7.0.0-0-Q16-x64-dll.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-x64-dll.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-x64-dll.exe) | Win64 dynamic at 16 bits-per-pixel component  
  
Or choose from these alternate Windows binary distributions:

Version | HTTP | FTP | Description  
---|---|---|---  
ImageMagick-7.0.0-0-Q16-x64-static.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-x64-static.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-x64-static.exe) | Win64 static at 16 bits-per-pixel component  
ImageMagick-7.0.0-0-Q8-x64-dll.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q8-x64-dll.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q8-x64-dll.exe) | Win64 dynamic at 8 bits-per-pixel component  
ImageMagick-7.0.0-0-Q8-x64-static.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q8-x64-static.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q8-x64-static.exe) | Win64 static at 8 bits-per-pixel component  
ImageMagick-7.0.0-0-Q16-HDRI-x64-dll.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x64-dll.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x64-dll.exe) | Win64 dynamic at 16 bits-per-pixel component with [high dynamic-range imaging](high-dynamic-range.html) enabled  
ImageMagick-7.0.0-0-Q16-HDRI-x64-static.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x64-static.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x64-static.exe) | Win64 static at 16 bits-per-pixel component with [high dynamic-range imaging](high-dynamic-range.html) enabled  
ImageMagick-7.0.0-0-Q16-x86-dll.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-x86-dll.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-x86-dll.exe) | Win32 dynamic at 16 bits-per-pixel component  
ImageMagick-7.0.0-0-Q16-x86-static.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-x86-static.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-x86-static.exe) | Win32 static at 16 bits-per-pixel component  
ImageMagick-7.0.0-0-Q8-x86-dll.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q8-x86-dll.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q8-x86-dll.exe) | Win32 dynamic at 8 bits-per-pixel component  
ImageMagick-7.0.0-0-Q8-x86-static.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q8-x86-static.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q8-x86-static.exe) | Win32 static at 8 bits-per-pixel component  
ImageMagick-7.0.0-0-Q16-HDRI-x86-dll.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x86-dll.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x86-dll.exe) | Win32 dynamic at 16 bits-per-pixel component with [high dynamic-range imaging](high-dynamic-range.html) enabled  
ImageMagick-7.0.0-0-Q16-HDRI-x86-static.exe | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x86-static.exe) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-Q16-HDRI-x86-static.exe) | Win32 static at 16 bits-per-pixel component with [high dynamic-range imaging](high-dynamic-range.html) enabled  
ImageMagick-7.0.0-0-portable-Q16-x86.zip | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-portable-Q16-x86.zip) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-portable-Q16-x86.zip) | Portable Win32 static at 16 bits-per-pixel component. Just copy to your host and run (no installer, no Windows registry entries).  
ImageMagick-7.0.0-0-portable-Q16-x64.zip | [download](http://www.imagemagick.org/download/binaries/ImageMagick-7.0.0-0-portable-Q16-x64.zip) | [download](ftp://ftp.imagemagick.org/pub/ImageMagick/binaries/ImageMagick-7.0.0-0-portable-Q16-x64.zip) | Portable Win64 static at 16 bits-per-pixel component. Just copy to your host and run (no installer, no Windows registry entries).  
  
Verify its [message digest](http://www.imagemagick.org/download/binaries/digest.rdf).

To verify ImageMagick is working properly, type the following in an Command Prompt window:
    
    
    convert logo: logo.gif
    identify logo.gif
    imdisplay
    

If you have any problems, you likely need `vcomp120.dll`. To install it, download [Visual C++ 2013 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=40784).

Note, use a double quote (`"`) rather than a single quote (`'`) for the ImageMagick command line under Windows:
    
    
    convert "e:/myimages/image.png" "e:/myimages/image.jpg"
    

Use two double quotes for VBScript scripts:
    
    
    Set objShell = wscript.createobject("wscript.shell")
    objShell.Exec("convert ""e:/myimages/image.png"" ""e:/myimages/image.jpg""")
    

Congratulations, you have a working ImageMagick distribution under Windows and you are ready to use ImageMagick to [convert, compose, or edit](http://www.imagemagick.org/Usage/) your images or perhaps you'll want to use one of the [Application Program Interfaces](api.html) for C, C++, Perl, and others.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](binary-releases.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
