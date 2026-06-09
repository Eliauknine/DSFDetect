[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Install from Unix Source](install-source.html#unix) • [Install from Windows Source](install-source.html#windows)

Chances are, ImageMagick is already installed on your computer if you are using some flavor of Unix, and its likely not installed if you are using some form of Windows. In either case, you can type the following to find out:
    
    
    identify -version
    

If the [identify](identify.html) program executes and identifies itself as ImageMagick, you may not need to install ImageMagick from source unless you want to add support for additional image formats or upgrade to a newer version. You also have the option of installing a pre-compiled [binary release](binary-releases.html). However, if you still want to install from source, choose a platform, [Unix](install-source.html#unix) or [Windows](install-source.html#windows). Before installing from source, you may want to review recent [changes](changelog.html) to the ImageMagick distribution.

The authoritative source code repository is <http://git.imagemagick.org/repos/ImageMagick>. We maintain a source code mirror at [GitHub](https://github.com/ImageMagick/ImageMagick). We test and deploy ImageMagick with [Travis CI](https://travis-ci.org/ImageMagick) and [AppVeyor](https://ci.appveyor.com/project/dlemstra/imagemagick-windows).

## Install from Unix Source

ImageMagick builds on a variety of Unix and Unix-like operating systems including Linux, Solaris, FreeBSD, Mac OS X, and others. A compiler is required and fortunately almost all modern Unix systems have one. Download [ImageMagick.tar.gz](http://www.imagemagick.org/download/ImageMagick.tar.gz) from [www.imagemagick.org](http://www.imagemagick.org/download) or a [mirrors](download.html) and verify its [message digest](http://www.imagemagick.org/download/digest.rdf).

Unpack the distribution with this command:
    
    
    tar xvzf ImageMagick.tar.gz
    

Next configure and compile ImageMagick:
    
    
     cd ImageMagick-7.0.0  
     ./configure  
     make

If ImageMagick configured and compiled without complaint, you are ready to install it on your system. Administrator privileges are required to install. To install, type
    
    
    sudo make install
    

You may need to configure the dynamic linker run-time bindings:
    
    
    sudo ldconfig /usr/local/lib
    

Finally, verify the ImageMagick install worked properly, type
    
    
    /usr/local/bin/convert logo: logo.gif
    

For a more comprehensive test, run the ImageMagick validation suite. Ghostscript is a prerequisite, otherwise the EPS, PS, and PDF tests will fail.
    
    
    make check
    

Congratulations, you have a working ImageMagick distribution and you are ready to use ImageMagick to [convert, compose, or edit](http://www.imagemagick.org/Usage/) your images or perhaps you'll want to use one of the [Application Program Interfaces](api.html) for C, C++, Perl, and others.

The above instructions will satisfy a great number of ImageMagick users, but we suspect a few will have additional questions or problems to consider. For example, what does one do if ImageMagick fails to configure or compile? Or what if you don't have administrator privileges and what if you don't want to install ImageMagick in the default `/../usr/local` folder? You will find the answer to these questions, and more, in [Advanced Unix Source Installation](advanced-unix-installation.html).

## Install from Windows Source

Building ImageMagick source for Windows requires a modern version of Microsoft Visual Studio IDE. Users have reported success with the Borland C++ compiler as well. If you don't have a compiler you can still install a self-installing [binary release](binary-releases.html).

Download [ImageMagick-windows.zip](http://www.imagemagick.org/download/windows/ImageMagick-windows.zip) from [www.imagemagick.org](http://www.imagemagick.org/download/windows) or a [mirrors](download.html) and verify its [message digest](http://www.imagemagick.org/download/windows/digest.rdf).

You can unpack the distribution with [WinZip](http://www.winzip.com) or type the following from any MS-DOS Command Prompt window:
    
    
    unzip ImageMagick-windows.zip
    

Next, launch your Visual Studio IDE and choose `Open->Project`. Select the configure workspace from the `ImageMagick-7.0.0/VisualMagick/configure` folder and press Open. Choose `Build->Build Solution` to compile the program and on completion run the program.

![\[configure\]](../images/configure.jpg)

Press `Next` and click on the multi-threaded static build. If you are using the Visual Studio 6.0 IDE, make sure no check is next to the Generate Visual Studio 7 format option. Now press, on `Next` twice and finally `Finish`. The configuration utility just created a workspace required to build ImageMagick from source. Choose `Open->Project` and select the VisualStaticMT workspace from the `ImageMagick-7.0.0/VisualMagick/` folder. Finally, choose `Build->Build Solution` to compile and build the ImageMagick distribution.

To verify ImageMagick is working properly, launch a MS-DOS Command Prompt window and type
    
    
     cd ImageMagick-7.0.0  
     convert logo: image.jpg

For a more comprehensive test, run the ImageMagick validation suite:
    
    
    validate
    

Congratulations, you have a working ImageMagick distribution under Windows and you are ready to use ImageMagick to [convert, compose, or edit](http://www.imagemagick.org/Usage/) your images or perhaps you'll want to use one of the [Application Program Interfaces](api.html) for C, C++, Perl, and others.

The above instructions will satisfy a great number of ImageMagick users, but we suspect a few will have additional questions or problems to consider. For example, what does one do if ImageMagick fails to configure or compile? Or what if you want to install ImageMagick in a place other than the `ImageMagick-7.0.0/VisualMagick/bin` folder? Or perhaps you want to build and install the [ImageMagickObject](ImageMagickObject.html) COM+ component. You will find the answer to these questions, and more, in [Advanced Windows Source Installation](advanced-windows-installation.html).

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](install-source.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
