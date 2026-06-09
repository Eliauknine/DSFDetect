[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Documentation](magick++.html#documentation) • [Obtaining Magick++](magick++.html#get) • [Installation](magick++.html#install) • [Reporting Bugs](magick++.html#bugs)

[Magick++ API](api/Magick++/index.html) is the object-oriented C++ API to the [ImageMagick](http://www.imagemagick.org/) image-processing library.

Magick++ supports an object model which is inspired by [PerlMagick](http://www.imagemagick.org/www/perl-magick.html). Images support implicit reference counting so that copy constructors and assignment incur almost no cost. The cost of actually copying an image (if necessary) is done just before modification and this copy is managed automagically by Magick++. De-referenced copies are automagically deleted. The image objects support value (rather than pointer) semantics so it is trivial to support multiple generations of an image in memory at one time. 

Magick++ provides integrated support for the [Standard Template Library](http://www.sgi.com/tech/stl/) (STL) so that the powerful containers available (e.g. [deque](http://www.sgi.com/tech/stl/Deque.html), [vector](http://www.sgi.com/tech/stl/Vector.html), [list](http://www.sgi.com/tech/stl/List.html), and [map](http://www.sgi.com/tech/stl/Map.html)) can be used to write programs similar to those possible with PERL & PerlMagick. STL-compatible template versions of ImageMagick's list-style operations are provided so that operations may be performed on multiple images stored in STL containers. 

## Documentation

Detailed [documentation](api/magick++-classes.html) is provided for all Magick++ classes, class methods, and template functions which comprise the API. See a [ Gentle Introduction to Magick++](http://www.imagemagick.org/Magick++/tutorial/Magick++_tutorial.pdf) for an introductory tutorial to Magick++. We include the [source](http://www.imagemagick.org/Magick++/tutorial/Magick++_tutorial.odt) if you want to correct, enhance, or expand the tutorial.

## Obtaining Magick++

Magick++ is included as part of [ImageMagick](../index.html) source releases and may be retrieved via [ftp](http://www.imagemagick.org/www/download.html) or [GIT](http://git.imagemagick.org/repos/ImageMagick/Magick++). 

## Installation

Once you have the Magick++ sources available, follow these detailed [installation instructions](../Magick++/Install.html) for UNIX and Windows. 

## Usage

A helper script named `Magick++-config` is installed under Unix which assists with recalling compilation options required to compile and link programs which use Magick++. For example, the following command compiles and links the source file `demo.cpp` to produce the executable `demo` (notice that quotes are backward quotes): 
    
    
    c++ `Magick++-config --cxxflags --cppflags` -O2 -o demo demo.cpp \
      `Magick++-config --ldflags --libs`
    

Set the `PKG_CONFIG_PATH` environment variable if ImageMagick is not in your default system path:
    
    
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
    

Windows users may get started by manually editing a project file for one of the Magick++ demo programs. 

Note, under Windows (and possibly the Mac) it may be necessary to initialize the ImageMagick library prior to using the Magick++ library. This initialization is performed by passing the path to the ImageMagick DLLs (assumed to be in the same directory as your program) to the InitializeMagick() function call. This is commonly performed by providing the path to your program (argv[0]) as shown in the following example: 
    
    
    int main( int argc, char ** argv) {
      InitializeMagick(*argv);
      ...
    

This initialization step is not required under Unix, Linux, Cygwin, or any other operating environment that supports the notion of installing ImageMagick in a known location. 

Here is a example program that utilizes the Magick++ API to get you started, [magick++.cpp](../source/magick++.cpp). It reads an image, crops it, and writes it to disk in the PNG image format.
    
    
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
        image.read( "logo:" );
    
        // Crop the image to specified size (width, height, xOffset, yOffset)
        image.crop( Geometry(100,100, 100, 100) );
    
        // Write the image to a file 
        image.write( "logo.png" ); 
      } 
      catch( Exception &error_ ) 
        { 
          cout << "Caught exception: " << error_.what() << endl; 
          return 1; 
        } 
      return 0; 
    }
    

## Reporting Bugs

Questions regarding usage should be directed to or to report any bugs go to [Magick++ bug tracking forum](http://www.imagemagick.org/discourse-server/viewforum.html?f=23). 

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](magick++.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
