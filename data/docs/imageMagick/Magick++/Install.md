# Installing Magick++

### General

In order to compile Magick++ you must have access to a standard C++ implementation. The author uses [gcc 3.4 (GNU C++)](http://gcc.gnu.org/index.html) which is available under UNIX and under the [Cygwin UNIX-emulation environment](http://www.cygwin.com/) for Windows. Standards compliant commercial C++ compilers should also work fine. Most modern C++ compilers for Microsoft Windows or the Mac should work (project files are provided for Microsoft Visual C++ 8.0).

It was decided that Magick++ will be around for the long-haul, so its API definition depends on valuable C++ features which should be common in all current and future C++ compilers. The compiler must support the following C++ standard features:

  * templates

  * static constructors

  * C++-style casts (e.g. static_cast)

  * bool type

  * string class (`<string>`)

  * exceptions (`<exception>`)

  * namespaces

  * Standard Template Library (STL) (e.g. `<list>`, `<vector>`)




The author has personally verified that Magick++ compiles and runs using the following compiler/platform combinations:

  


**Tested Configurations**

**Operating System** |  **Architecture** |  **Compiler**  
---|---|---  
SunOS 5.6, 5.7, 5.8 ("Solaris 2.6, 7, & 8) |  SPARC |  GCC 3.0.4  
SunOS 5.7 ("Solaris 7") |  SPARC |  Sun Workshop 5.0 C++  
SunOS 5.8 ("Solaris 8") |  SPARC |  Sun WorkShop 6 update 2 C++ 5.3  
FreeBSD 4.0 |  Intel Pentium II |  GCC 2.95  
Windows NT 4.0 SP6a |  Intel Pentium II |  Visual C++ 8.0 Standard Edition  
Windows XP |  Intel Pentium IV |  Visual C++ 8.0 Standard Edition Service Pack 5  
Windows '98 + [Cygwin](http://www.cygwin.com/) 1.3.10 |  Intel Pentium III |  GCC 2.95.3-5  
Windows NT 4.0 SP6a |  Intel Pentium II |  GCC 2.95.3-5  
Windows XP + [Cygwin](http://www.cygwin.com/) 1.3.10 |  Intel Pentium IV |  GCC 2.95.3-5  
  
Users of Magick++ have reported that the following configurations work with Magick++:

  


**Other Known Working Configurations**

**Operating System** |  **Architecture** |  **Compiler** |  **Reported By**  
---|---|---|---  
Red Hat Linux 8.0 |  i386 & alpha |  EGCS 1.1.2 |  Dr. Alexander Zimmermann <Alexander.Zimmermann@fmi.uni-passau.de>  
Red Hat Linux 7.0 |  i386 |  GCC 2.95.2 |  Dr. Alexander Zimmermann <Alexander.Zimmermann@fmi.uni-passau.de>  
Red Hat Linux 7.0 |  i386 |  GCC "2.96" snapshot |  ???  
Red Hat Linux 7.X |  i386 & alpha |  GCC 3.0 |  Dr. Alexander Zimmermann <Alexander.Zimmermann@fmi.uni-passau.de>  
SGI IRIX 6.2, 6.5 |  MIPS |  IRIX C++ 7.3.1.2m |  Albert Chin-A-Young <china@thewrittenword.com>  
SunOS 5.5.1 |  SPARC |  Sun WorkShop CC 5.0 |  Albert Chin-A-Young <china@thewrittenword.com>  
SunOS 5.6, 5.7, 5.8 |  SPARC |  Sun Forte CC 5.3 |  Albert Chin-A-Young <china@thewrittenword.com>  
HP-UX 11.00 |  PA-RISC |  HP-UX aCC A.03.30 |  Albert Chin-A-Young <china@thewrittenword.com>  
Mac OS 9 |  PowerPC |  CodeWarrior Professional Release 6 |  Leonard Rosenthol <leonardr@digapp.com>  
Mac OS X 10.1 "Darwin" |  PowerPC |  GCC 2.95.2 (apple gcc -926) |  Cristy  
  
Please let me know if you have successfully built and executed Magick++ using a different configuration so that I can add to the table of verified configurations.

* * *

### Unix/Linux

#### Building From Source

Magick++ is now built using the ImageMagick configure script and Makefiles. Please follow the installation instructions provided by its README.txt file. The following instructions pertain to the Magick++ specific configuration and build options.

To install ImageMagick plus Magick++ under Unix, installation should be similar to

`./configure [ --prefix=/prefix ]`  
`make`  
`make install`

The library is currently named similar to 'libMagick++.a' (and/or libMagick++.so.5.0.39) and is installed under prefix/lib while the headers are installed with Magick++.h being installed in prefix/include and the remaining headers in prefix/include/Magick++.

To influence the options the configure script chooses, you may specify 'make' option variables when running the configure script. For example, the command

> `./configure CXX=CC CXXFLAGS=-O2 LIBS=-lposix`

  
specifies additional options to the configure script. The following table shows the available options.

  


Environment Variables That Effect Configure

**Make Option Variable** |  **Description**  
---|---  
CXX |  Name of C++ compiler (e.g. 'CC -Xa') to use compiler 'CC -Xa'  
CXXFLAGS |  Compiler flags (e.g. '-g -O2') to compile with  
CPPFLAGS |  Include paths (-I/somedir) to look for header files  
LDFLAGS |  Library paths (-L/somedir) to look for libraries. Systems that support the notion of a library run-path may additionally require -R/somedir or '-rpath /somedir' in order to find shared libraries at run time.  
LIBS |  Extra libraries (-lsomelib) required to link  
  
#### Installing Linux RPMs

Linux RPMs of ImageMagick and Magick++ can be downloaded from [ftp://ftp.imagemagick.org/pub/ImageMagick/linux/](ftp://ftp.imagemagick.org/pub/ImageMagick/linux//).

* * *

### Windows '9X, NT, 2003, 2008, XP, & Windows 7

#### Visual C++

Windows NT through Windows Vista are supported by the ImageMagick source package for NT available in the 'win2k' subdirectory of the ImageMagick ftp site (and mirrors). The ImageMagick source package for NT provides sources to ImageMagick, Magick++, add-on libraries (e.g. JPEG), and a ready-made Visual C++ 8.0 build environment. Please read the configuration and build instructions in README.txt (under the heading "Windows Win2K/XP VISUAL C++ 8.0 COMPILATION") in order to build Magick++.

#### Cygwin & GCC

It is possible to build both ImageMagick and Magick++ under the Cygwin Unix-emulation environment for Windows NT. Obtain and install Cgywin from <http://www.cygwin.com/> . An X11R6 environment for Cygwin is available from <http://www.cygwin.com/xfree/> .To build using Cygwin and GCC, follow the instructions for building under Unix.
