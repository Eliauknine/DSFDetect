# ![](images/cramps.gif) Building the Software Distribution

  * Building on a UNIX system.
  * Building on a Macintosh system with MPW.
  * Building on a Macintosh system with CodeWarrior.
  * Building on an MS-DOS or Windows system.
  * Building on MS-DOS with the DJGPP v2 compiler.
  * Building on a VMS system.
  * Building on an Acorn RISC OS system.
  * Building the Software on Other Systems

  
This chapter contains step-by-step instructions on how to configure and build the TIFF software distribution. The software is most easily built on a UNIX system, but with a little bit of work it can easily be built and used on other non-UNIX platforms. 

* * *

## Building on a UNIX System

To build the software on a UNIX system you need to first run the configure shell script that is located in the top level of the source directory. This script probes the target system for necessary tools and functions and constructs a build environment in which the software may be compiled. Once configuration is done, you simply run `make` (or `gmake`) to build the software and then `make install` to do the installation; for example: 
    
    
    hyla% **cd tiff-v3.4beta099**
    hyla% **./configure**
        _...lots of messages..._
    hyla% **make**
        _...lots of messages..._
    hyla# **make install**
    

Supplied makefiles are depend on GNU `make` utility, so you will need the one. Depending on your installation **make** command may invoke standard system `make` and **gmake** invoke GNU make. In this case you should use former. If you don't have `make` at all, but only `gmake`, you should export environment variable `MAKE=gmake` before **./configure**. 

In general, the software is designed such that the following should be ``_make-able_ '' in each directory:
    
    
    make [all]      build stuff
    make install    build&install stuff
    make clean      remove .o files, executables and cruft
    make distclean  remove everything, that can be recreated
    

Note that after running "`make distclean`" the `configure` script must be run again to create the Makefiles and other make-related files. 

* * *

### Build Trees

There are two schemes for configuring and building the software. If you intend to build the software for only one target system, you can configure the software so that it is built in the same directories as the source code. 
    
    
    hyla% **cd tiff-v3.4beta099**
    hyla% **ls**
    COPYRIGHT       VERSION         config.sub      dist            man
    Makefile.in     config.guess    configure       html            port
    README          config.site     contrib         libtiff         tools
    hyla% **./configure**
    

Otherwise, you can configure a build tree that is parallel to the source tree hierarchy but which contains only configured files and files created during the build procedure.
    
    
    hyla% **cd tiff-v3.4beta099**
    hyla% **mkdir obj obj/mycpu**
    hyla% **cd obj/mycpu**
    hyla% **../../configure**
    

This second scheme is useful for: 

  * building multiple targets from a single source tree
  * building from a read-only source tree (e.g. if you receive the distribution on CD-ROM)



* * *

### Configuration Options

The configuration process is critical to the proper compilation, installation, and operation of the software. The configure script runs a series of tests to decide whether or not the target system supports required functionality and, if it does not, whether it can emulate or workaround the missing functions. This procedure is fairly complicated and, due to the nonstandard nature of most UNIX systems, prone to error. The first time that you configure the software for use you should check the output from the configure script and look for anything that does not make sense for your system. 

A second function of the configure script is to set the default configuration parameters for the software. Of particular note are the directories where the software is to be installed. By default the software is installed in the **/usr/local** hierarchy. To change this behaviour the appropriate parameters can be specified on the command line to configure. Run **./configure --help** to get a list of possible options. Installation related options are shown below.
    
    
    
    Installation directories:
      --prefix=PREFIX         install architecture-independent files in PREFIX
                              [/usr/local]
      --exec-prefix=EPREFIX   install architecture-dependent files in EPREFIX
                              [PREFIX]
    
    By default, `make install' will install all the files in
    `/usr/local/bin', `/usr/local/lib' etc.  You can specify
    an installation prefix other than `/usr/local' using `--prefix',
    for instance `--prefix=$HOME'.
    
    For better control, use the options below.
    
    Fine tuning of the installation directories:
      --bindir=DIR           user executables [EPREFIX/bin]
      --sbindir=DIR          system admin executables [EPREFIX/sbin]
      --libexecdir=DIR       program executables [EPREFIX/libexec]
      --datadir=DIR          read-only architecture-independent data [PREFIX/share]
      --sysconfdir=DIR       read-only single-machine data [PREFIX/etc]
      --sharedstatedir=DIR   modifiable architecture-independent data [PREFIX/com]
      --localstatedir=DIR    modifiable single-machine data [PREFIX/var]
      --libdir=DIR           object code libraries [EPREFIX/lib]
      --includedir=DIR       C header files [PREFIX/include]
      --oldincludedir=DIR    C header files for non-gcc [/usr/include]
      --infodir=DIR          info documentation [PREFIX/info]
      --mandir=DIR           man documentation [PREFIX/man]
    
    Program names:
      --program-prefix=PREFIX            prepend PREFIX to installed program names
      --program-suffix=SUFFIX            append SUFFIX to installed program names
      --program-transform-name=PROGRAM   run sed PROGRAM on installed program names
    
    

* * *

### Configuring Optional Packages/Support

The TIFF software comes with several packages that are installed only as needed, or only if specifically configured at the time the configure script is run. Packages can be configured via the **configure** script commandline parameters. 

_Static/Shared Objects Support_
    `--enable-shared[=PKGS]    build shared libraries [default=yes]  
--enable-static[=PKGS]    build static libraries [default=yes]`

These options control whether or not to configure the software to build a shared and static binaries for the TIFF library. Use of shared libraries can significantly reduce the disk space needed for users of the TIFF software. If shared libarries are not used then the code is statically linked into each application that uses it. By default both types of binaries is configured.

`--enable-rpath    Enable runtime linker paths (-R libtool option)`

Add library directories (see other options below) to the TIFF library run-time linker path.

_JPEG Support_
    `--disable-jpeg    disable IJG JPEG library usage (required for JPEG compression, enabled by default) --with-jpeg-include-dir=DIR    location of IJG JPEG library headers --with-jpeg-lib-dir=DIR    location of IJG JPEG library binary)`
    The `JPEG` package enables support for the handling of TIFF images with JPEG-encoded data. Support for JPEG-encoded data requires the Independent JPEG Group (IJG) `libjpeg` distribution; this software is available at [ftp.uu.net:/graphics/jpeg/](ftp://ftp.uu.net/graphics/jpeg/). **configure** script automatically tries to search the working IJG JPEG installation. If it fails to find library, JPEG support will be automatically disabled.If you want specify the exact paths to library binary and headers, use above switches for that.
_ZIP Support_
    The `ZIP` support enables support for the handling of TIFF images with deflate-encoded data. Support for deflate-encoded data requires the freely available `zlib` distribution written by Jean-loup Gailly and Mark Adler; this software is available at [ftp.uu.net:/pub/archiving/zip/zlib/](ftp://ftp.uu.net/pub/archiving/zip/zlib/) (or try [quest.jpl.nasa.gov:/beta/zlib/](ftp://quest.jpl.nasa.gov/beta/zlib/)). If ZIP support is enabled the `DIRS_LIBINC` and `DIR_GZLIB` parameters should also be set (see below). By default this package is not configured.

* * *

### A Sample Configuration Session

This section shows a sample configuration session and describes the work done. The session is shown indented in a `fixed width font` with user-supplied input in a `**bold font**`. Comments are shown in a normal or _italic_ font. This session was collected on a 486 machine running BSDI 1.1. 
    
    
    
    wullbrandt% **mkdir tiff**
    wullbrandt% **cd tiff**
    wullbrandt% **ln -s /hosts/oxford/usr/people/sam/tiff src**
    
    

A build tree separate from the source tree is used here. In fact, in this case the distribution is accessed from a read-only NFS-mounted filesystem. 
    
    
    
    wullbrandt% **src/configure**
    Configuring TIFF Software v3.4beta015.
    
    Reading site-wide parameters from ../tiff-v3.4beta015/config.site.
    Reading local parameters from config.local.
    Gosh, aren't you lucky to have a i386-unknown-bsdi1.1 system!
    
    

Note that configure announces the distribution version and the deduced target configuration (`i386-unknown-bsdi1.1` here). 
    
    
    
    Using /usr/local/bin/gcc for a C compiler (set CC to override).
    Looks like /usr/local/bin/gcc supports the -g option.
    Using " -g" for C compiler options.
    
    

configure checked the normal shell search path for potential ANSI C compilers. The compiler is selected according to it properly compiling a small ANSI C test program. A specific compiler may be requested by setting the `CC` environment variable to the appropriate pathname, by supplying the parameter on the command line, e.g. `-with-CC=gcc`, or by setting `CC` in a configuration file. 

![](images/info.gif) _Note that an ANSI C compiler is required to build the software. If a C compiler requires options to enable ANSI C compilation, they can be specified with the` ENVOPTS` parameter._

Once a compiler is selected configure checks to see if the compiler accepts a -g option to enable the generation of debugging symbols, and if the compiler includes an ANSI C preprocessor.
    
    
    
    Using /usr/ucb/make to configure the software.
    
    

Next various system-specific libraries that may or may not be needed are checked for (none are needed in this case). If your system requires a library that is not automatically included it can be specified by setting the `MACHDEPLIBS` parameter. 

_Creating port.h._ The **port.h** file is included by all the C code in the library (but not the tools). It includes definitions for functions and type definitions that are missing from system include files, `#defines` to enable or disable system-specific functionality, and other odds and ends.
    
    
    
    Creating libtiff/port.h with necessary definitions.
    ... using LSB2MSB bit order for your i386 cpu
    ... using big-endian byte order for your i386 cpu
    ... configure use of mmap for memory-mapped files
    ... O_RDONLY is in <fcntl.h>
    ... using double for promoted floating point parameters
    ... enabling use of inline functions
    Done creating libtiff/port.h.
    
    

This file can take a long time to create so configure generates the file only when it is needed, either because the file does not exist or because a different target or compiler is to be used. Note that running "`make distclean`" in the top-level directory of the build tree will remove the **port.h** file (along with all the other files generated by configure). 

_Selecting emulated library functions._ Certain library functions used by the tools are not present on all systems and can be emulated using other system functionality. configure checks for the presence of such functions and if they are missing, will configure emulation code from the **port** directory to use instead. Building the TIFF software on unsupported systems may require adding to the code to the **port** directory.
    
    
    
    Checking system libraries for functionality to emulate.
    Done checking system libraries.
    
    

If a routine must be emulated and configure does not automatically check for it, the routine name can be specified using the `PORTFUNCS` parameter. To add emulation support for a new function `foo`, create a file **port/foo.c** that contains the emulation code and then set `PORTFUNCS=foo` in a configuration file or modify the configure script to automatically check for the missing function. 
    
    
    
    Checking for Dynamic Shared Object (DSO) support.
    Done checking for DSO support.
    
    

If the `DSO` package is enabled (`DSO=auto` or `DSO=yes`), then configure will verify the system and compiler are capable of constructing SVR4-style DSO's in the expected way. Note that while a system may support DSO's the compiler may not be capable of generating the required position-independent code and/or the compiler may not pass the needed options through to the loader. 

_Selecting utility programs._ configure locates various system utility programs that are used during installation of the software.
    
    
    
    Selecting programs used during installation.
    Looks like mv supports the -f option to force a move.
    Looks like /bin/ln supports the -s option to create a symbolic link.
    Done selecting programs.
    
    

_Selecting default configuration parameters._ The remainder of the work done by configure involves setting up configuration parameters that control the placement and setup of files during the installation procedure.
    
    
    
    Selecting default TIFF configuration parameters.
    
    Looks like manual pages go in /usr/contrib/man.
    Looks like manual pages should be installed with bsd-nroff-gzip-0.gz.
    
    TIFF configuration parameters are:
    
    [ 1] Directory for tools:               /usr/contrib/bin
    [ 2] Directory for libraries:           /usr/contrib/lib
    [ 3] Directory for include files:       /usr/contrib/include
    [ 4] Directory for manual pages:        /usr/contrib/man
    [ 5] Manual page installation scheme:   bsd-nroff-gzip-0.gz
    
    Are these ok [yes]? 
    
    

At this point you can interactively modify any of the displayed parameters. Hitting a carriage return or typing `yes` will accept the current parameters. Typing one of the number displayed along the left hand side causes configure to prompt for a new value of the specified parameter. Typing anything else causes configure to prompt for a new value _for each parameter_. In general hitting carriage return will accept the current value and typing anything that is unacceptable will cause a help message to be displayed. A description of each of the configuration parameters is given below. 

Once acceptable parameters are setup configure will generate all the files that depend on these parameters. Note that certain files may or may not be created based on the configuration of optional packages and/or the functions supported by target system.
    
    
    
    Creating Makefile from ../tiff-v3.4beta015/Makefile.in
    Creating libtiff/Makefile from ../tiff-v3.4beta015/libtiff/Makefile.in
    Creating man/Makefile from ../tiff-v3.4beta015/man/Makefile.in
    Creating tools/Makefile from ../tiff-v3.4beta015/tools/Makefile.in
    Creating port/install.sh from ../tiff-v3.4beta015/port/install.sh.in
    Done.
    
    

* * *

### Shared Library Support

It is desirable to make the TIFF library be a shared object on systems that have support for shared libraries. Unfortunately the rules to use to build a shared library vary between operating systems and even compilers. The distributed software includes support for building a shared version of the library on a number of different systems. This support is split between rules in the file **libtiff/Makefile.in** that construct the shared library and checks done by the `configure` script to verify that the expected rules are supported by compilation tools for the target system. 

To add new support for building a shared library both these files must be updated. In the configure script search for the section where the autoconfiguration setting of the `DSO` parameter is handled and add a new case for the target system that sets the `DSOSUF`, `DSOLD`, `DSOOPTS`, and `LIBCOPTS` options as appropriate for the system. `DSOSUF` specifies the filename suffix used for the shared library (e.g. ``.so'' for Dynamic Shared Objects on most SVR4-based systems). `DSOLD` specifies the program to use to build the shared library from a compiled object file; typically ``${LD}'' though on some systems it is better to use the C compiler directly so system-dependent options and libraries are automatically supplied. `DSOOPTS` are options that must be specified to `DSOLD` when building the shared library. `LIBCOPTS` are options to pass to the C compiler when constructing a relocatable object file to include in a shared library; e.g. ``-K PIC'' on a Sun system. The `DSO` parameter must also be set to a unique label that identifies the target system and compilation tools. This label is used to select a target in **libtiff/Makefile.in** to do the actual work in building the shared library. Finally, to complete support for the shared library added the appropriate rules to **libtiff/Makefile.in** under the target specified in the `configure` script. 

* * *

## Building the Software under Windows 95/98/NT/2000 with MS VC++

With Microsoft Visual C++ installed, and properly configured for commandline use (you will likely need to source VCVARS32.BAT in AUTOEXEC.bAT or somewhere similar) you should be able to use the provided `makefile.vc`. 

The source package is delivered using Unix line termination conventions, which work with MSVC but do not work with Windows 'notepad'. If you use unzip from the [Info-Zip](http://www.info-zip.org/pub/infozip/) package, you can extract the files using Windows normal line termination conventions with a command similar to:
    
    
      unzip -aa -a tiff-3.7.4.zip
    

By default libtiff expects that a pre-built zlib and jpeg library are provided by the user. If this is not the case, then you may edit libtiff\tiffconf.h using a text editor (e.g. notepad) and comment out the entries for JPEG_SUPPORT, PIXARLOG_SUPPORT, and ZIP_SUPPORT. Ignore the comment at the top of the file which says that it has no influence on the build, because the statement is not true for Windows. However, by taking this approach, libtiff will not be able to open some TIFF files.

To build using the provided makefile.vc you may use:
    
    
      C:\tiff-3.7.4> nmake /f makefile.vc clean
      C:\tiff-3.7.4> nmake /f makefile.vc
    
        or (the hard way)
    
      C:\tiff-3.7.4> cd port
      C:\tiff-3.7.4\port> nmake /f makefile.vc clean
      C:\tiff-3.7.4\port> nmake /f makefile.vc
      C:\tiff-3.7.4> cd ../libtiff
      C:\tiff-3.7.4\libtiff> nmake /f makefile.vc clean
      C:\tiff-3.7.4\libtiff> nmake /f makefile.vc
      C:\tiff-3.7.4\libtiff> cd ..\tools
      C:\tiff-3.7.4\tools> nmake /f makefile.vc clean
      C:\tiff-3.7.4\tools> nmake /f makefile.vc
    

This will build the library file `libtiff\libtiff\libtiff.lib`. This can be used in Win32 programs. You may want to adjust the build options before start compiling. All parameters contained in the `nmake.opt` file.This is a plain text file you can open with your favorite text editor.

The makefile also builds a DLL (libtiff.dll) with an associated import library (libtiff_i.lib). Any builds using libtiff will need to include the LIBTIFF\LIBTIFF directory in the include path.

The `libtiff\tools\makefile.vc` should build .exe's for all the standard TIFF tool programs.

* * *

## Building the Software under MS/DOS with the DJGPP v2 compiler

[_From the file**contrib/dosdjgpp/README**._] 

The directory **contrib/dosdjgpp** contains the files necessary to build the library and tools with the DJGPP v2 compiler under MSDOS.

All you have to do is copy the files in the directory into the respective directories and run make. If you want, you can use the **conf.bat** script to do that for you, make sure that the file is stored with MSDOS text EOL-convention (CR/LF), otherwise the **command.com** will not do anything.

Note that you probably will not be able to build the library with the v1.x versions of djgpp, due to two problems. First, the top makefile calls a sub-make for each directory and you are likely to run out of memory, since each recursive invocation of a djgpp v1.x program requires about 130k, to avoid that, you can enter the directories manually and call make (well, there are only two dirs). The 2nd problem is that djgpp 1.x doesn't call the coff2exe (stubify) program when creating an executable. This means that all programs compiled are not converted to exe and consequently are not available for calling directly. For the tools directory, you can just call coff2exe for each program after make finishes, but in the libtiff directory, a few programs are created during the make process that have to be called for make to continue (e.g. mkg3states). Make will probably report an error at each such stage. To fix that, either add a coff2exe call before each program is called or call coff2exe manually and rerun make (there 2-3 such programs). 

* * *

## Building the Software on a Macintosh with MPW

The directory **contrib/mac-mpw** contains support for compiling the library and tools under the MPW Shell on a Macintosh system. This support was contributed by Niles Ritter ([ndr@tazboy.jpl.nasa.gov](mailto:ndr@tazboy.jpl.nasa.gov)). 

[_From the file**contrib/mac-mpw/README**._]

This directory contains all of the utilities and makefile source to build the LIBTIFF library and tools from the MPW Shell. The file BUILD.mpw in this directory is an executable script which uses all of these files to create the MPW makefiles and run them.

The <file>.make files are not MPW makefiles as such, but are when run through the "mactrans" program, which turns the ascii "%nn" metacharacters into the standard weird MPW make characters.

This translation trick is necessary to protect the files when they are put into unix tarfiles, which tend to mangle the special characters. 

* * *

## Building the Software on a Macintosh with CodeWarrior

The directory **contrib/mac-cw** contains support for compiling the library and tools with MetroWerks CodeWarrior 6.1 on a Macintosh system. This support was contributed by Niles Ritter ([ndr@tazboy.jpl.nasa.gov](mailto:ndr@tazboy.jpl.nasa.gov)). 

[_From the file**contrib/mac-cw/README**._] In this directory you will find a Makefile.script Applescript file, which should be run in order to build the libtiff code using MetroWerks CodeWarrior. Refer to the "metrowerks.note" instructions on building the library for 68k and PowerPC native code, as well as building some of the libtiff tools, which are rather unix-like, but at least give an example of how to link everything together. 

* * *

## Building the Software on a VMS System

The VMS port was done by Karsten Spang ([krs@kampsax.dk](mailto:krs@kampsax.dk)), who also "sort of" maintains it. The VMS specific files are not in the main directories. Instead they are placed under `[.CONTRIB.VMS...]` in the distribution tree. Installation: It is assumed that you have unpacked the tar file into a VMS directory tree, in this text called DISK:[TIFF]. 

  1. Move the VMS specific files to their proper directories. 
    
        $ SET DEFAULT DISK:[TIFF.CONTRIB.VMS]
    $ RENAME [.LIBTIFF]*.* [-.-.LIBTIFF]
    $ RENAME [.TOOLS]*.* [-.-.TOOLS]
    

  2. Compile the library. 
    
        $ SET DEFAULT DISK:[TIFF.LIBTIFF]
    $ @MAKEVMS
    

  3. Compile the tools. 
    
        $ SET DEFAULT DISK:[TIFF.TOOLS]
    $ @MAKEVMS
    

  4. Define the programs. 
    
        $ DEFINE TIFFSHR DISK:[TIFF.LIBTIFF]TIFFSHR
    $ FAX2PS    :==$DISK:[TIFF.TOOLS]FAX2PS
    $ FAX2TIFF  :==$DISK:[TIFF.TOOLS]FAX2TIFF
    $ GIF2TIFF  :==$DISK:[TIFF.TOOLS]GIF2TIFF
    $ PAL2RGB   :==$DISK:[TIFF.TOOLS]PAL2RGB
    $ PPM2TIFF  :==$DISK:[TIFF.TOOLS]PPM2TIFF
    $ RAS2TIFF  :==$DISK:[TIFF.TOOLS]RAS2TIFF
    $ RGB2YCBCR :==$DISK:[TIFF.TOOLS]RGB2YCBCR
    $ THUMBNAIL :==$DISK:[TIFF.TOOLS]THUMBNAIL
    $ TIFF2BW   :==$DISK:[TIFF.TOOLS]TIFF2BW
    $ TIFF2PS   :==$DISK:[TIFF.TOOLS]TIFF2PS
    $ TIFFCMP   :==$DISK:[TIFF.TOOLS]TIFFCMP
    $ TIFFCP    :==$DISK:[TIFF.TOOLS]TIFFCP
    $ TIFFDITHER:==$DISK:[TIFF.TOOLS]TIFFDITHER
    $ TIFFDUMP  :==$DISK:[TIFF.TOOLS]TIFFDUMP
    $ TIFFINFO  :==$DISK:[TIFF.TOOLS]TIFFINFO
    $ TIFFMEDIAN:==$DISK:[TIFF.TOOLS]TIFFMEDIAN
    $ TIFFSPLIT :==$DISK:[TIFF.TOOLS]TIFFSPLIT
    $ YCBCR     :==$DISK:[TIFF.TOOLS]YCBCR
    


You will want to add these lines to your `LOGIN.COM` file, after changing the name of the directory that you have used on your machine. 

This release has been tested on OpenVMS/VAX 5.5-2, using VAX C 3.2. A previous release was tested under OpenVMS/AXP ?.? using DEC C ?.?, it is believed that this release as well works on AXP. The code contains some GNU C specific things. This does *not* imply, however, that the VAX/GCC configuration has been tested, *it has not*.

The command procedures (`MAKEVMS.COM`) for building the library and tools, is believed to choose the correct options for the VAX and AXP cases automatically.

On the AXP, IEEE floating point is used by default. If you want VAX floating point, remove the `/FLOAT=IEEE_FLOAT` qualifier, and change `HAVE_IEEEFP=1` to `HAVE_IEEEFP=0` in the `MAKEVMS.COM` files in both the **libtiff** and **tools** directories.

### Compiling your own program on a VMS system:

When compiling a source file in which you `"#include <tiffio.h>"`, use the following command 
    
    
        $ CC/INCLUDE=DISK:[TIFF.LIBTIFF]
    

This ensures that the header file is found. On the AXP, also add `/FLOAT=IEEE_FLOAT` (if used when building the library). 

### Linking your own program to the TIFF library on a VMS system:

You can link to the library in two ways: Either using the shareable library, or using the object library. On the VAX these possibilities are: 

  1. Using the shareable TIFF library. 
    
        $ LINK MY_PROGRAM,DISK:[TIFF.LIBTIFF]TIFF/OPTIONS,SYS$INPUT:/OPTIONS
        SYS$SHARE:VAXCRTL/SHAREABLE
    

  2. Using the TIFF object library. 
    
        $ LINK MY_PROGRAM, -
        DISK:[TIFF.LIBTIFF]TIFF/LIBRARY/INCLUDE=(TIF_FAX3SM,TIF_CODEC), -
        SYS$INPUT:/OPTIONS
        SYS$SHARE:VAXCRTL/SHAREABLE
    


On AXP (and possibly also using DEC C on VAX) the corresponding commands are 
  1. Using the shareable TIFF library. 
    
        $ LINK MY_PROGRAM,DISK:[TIFF.LIBTIFF]TIFF/OPTIONS
    

  2. Using the TIFF object library. 
    
        $ LINK MY_PROGRAM,DISK:[TIFF.LIBTIFF]TIFF/LIBRARY
    


Method 1 uses the shortest link time and smallest `.EXE` files, but it requires that `TIFFSHR` is defined as above at link time and **at run time**. Using the compilation procedure above, the tools are linked in this way. 

Method 2 gives somewhat longer link time and larger `.EXE` files, but does not require `TIFFSHR` to be defined. This method is recommended if you want to run your program on another machine, and for some reason don't want to have the library on that machine. If you plan to have more than one program (including the tools) on the machine, it is recommended that you copy the library to the other machine and use method 1. 

* * *

## Building the Software on an Acorn RISC OS system

The directory **contrib/acorn** contains support for compiling the library under Acorn C/C++ under Acorn's RISC OS 3.10 or above. Subsequent pathnames will use the Acorn format: The full-stop or period character is a pathname delimeter, and the slash character is not interpreted; the reverse position from Unix. Thus "libtiff/tif_acorn.c" becomes "libtiff.tif_acorn/c". 

This support was contributed by Peter Greenham. ([peter@enlarion.demon.co.uk](mailto:peter@enlarion.demon.co.uk)).

### Installing LibTIFF:

LIBTIFF uses several files which have names longer than the normal RISC OS maximum of ten characters. This complicates matters. Maybe one day Acorn will address the problem and implement long filenames properly. Until then this gets messy, especially as I'm trying to do this with obeyfiles and not have to include binaries in this distribution.

First of all, ensure you have Truncate configured on (type `*Configure Truncate On`)

Although it is, of course, preferable to have long filenames, LIBTIFF can be installed with short filenames, and it will compile and link without problems. However, _getting_ it there is more problematic. **contrib.acorn.install** is an installation obeyfile which will create a normal Acorn-style library from the source (ie: with c, h and o folders etc.), but needs the distribution library to have been unpacked into a location which is capable of supporting long filenames, even if only temporarily.

My recommendation, until Acorn address this problem properly, is to use Jason Tribbeck's [ LongFilenames](ftp://ftp.demon.co.uk/pub/mirrors/hensa/micros/arch/riscos/c/c020/longfiles.arc), or any other working system that gives you long filenames, like a nearby NFS server for instance.

If you are using Longfilenames, even if only temporarily to install LIBTIFF, unpack the TAR into a RAMDisc which has been longfilenamed (ie: `*addlongfs ram`) and then install from there to the hard disk. Unfortunately Longfilenames seems a bit unhappy about copying a bunch of long-named files across the same filing system, but is happy going between systems. You'll need to create a ramdisk of about 2Mb.

Now you can run the installation script I've supplied (in contrib.acorn), which will automate the process of installing LIBTIFF as an Acorn-style library. The syntax is as follows:

`install <source_dir> <dest_dir>`

Install will then create <dest_dir> and put the library in there. For example, having used LongFilenames on the RAMDisk and unpacked the library into there, you can then type:

`Obey RAM::RamDisc0.$.contrib.acorn.install RAM::RamDisc0.$ ADFS::4.$.LIBTIFF`

It doesn't matter if the destination location can cope with long filenames or not. The filenames will be truncated if necessary (*Configure Truncate On if you get errors) and all will be well.

### Compiling LibTIFF:

Once the LibTIFF folder has been created and the files put inside, making the library should be just a matter of running '**SetVars** ' to set the appropriate system variables, then running '**Makefile** '.

**OSLib**

[OSLib](ftp://ftp.acorn.co.uk/pub/riscos/releases/oslib/oslib.arc) is a comprehensive API for RISC OS machines, written by Jonathan Coxhead of Acorn Computers (although OSLib is not an official Acorn product). Using the OSLib SWI veneers produces code which is more compact and more efficient than code written using _kernel_swi or _swi. The Acorn port of LibTIFF can take advantage of this if present. Edit the Makefile and go to the Static dependencies section. The first entry is:
    
    
    # Static dependencies:
    @.o.tif_acorn:   @.c.tif_acorn
            cc $(ccflags) -o @.o.tif_acorn @.c.tif_acorn 
    

Change the cc line to:
    
    
            cc $(ccflags) -DINCLUDE_OSLIB -o @.o.tif_acorn @.c.tif_acorn 
    

Remember, however, that OSLib is only _recommended_ for efficiency's sake. It is not required. 

* * *

## Building the Software on Other Systems

This section contains information that might be useful if you are working on a non-UNIX system that is not directly supported. All library-related files described below are located in the **libtiff** directory. 

The library requires two files that are generated _on-the-fly_. The file **tif_fax3sm.c** has the state tables for the Group 3 and Group 4 decoders. This file is generated by the `mkg3states` program on a UNIX system; for example,
    
    
    
    cd libtiff
    cc -o mkg3states mkg3states.c
    rm -f tif_fax3sm.c
    ./mkg3states -c const tif_fax3sm.c
    
    

The `-c` option can be used to control whether or not the resutling tables are generated with a `const` declaration. The `-s` option can be used to specify a C storage class for the table declarations. The `-b` option can be used to force data values to be explicitly bracketed with ``{}'' (apparently needed for some MS-Windows compilers); otherwise the structures are emitted in as compact a format as possible. Consult the source code for this program if you have questions. 

The second file required to build the library, **version.h** , contains the version information returned by the `TIFFGetVersion` routine. This file is built on most systems using the `mkversion` program and the contents of the `VERSION` and `tiff.alpha` files; for example,
    
    
    cd libtiff
    cc -o mkversion mkversion.c
    rm -f version.h
    ./mkversion -v ../VERSION -a ../dist/tiff.alpha version.h
    

Otherwise, when building the library on a non-UNIX system be sure to consult the files **tiffcomp.h** and **tiffconf.h**. The former contains system compatibility definitions while the latter is provided so that the software configuration can be controlled on systems that do not support the make facility for building the software.

Systems without a 32-bit compiler may not be able to handle some of the codecs in the library; especially the Group 3 and 4 decoder. If you encounter problems try disabling support for a particular codec; consult the [documentation](internals.html#Config).

Programs in the tools directory are written to assume an ANSI C compilation environment. There may be a few POSIX'isms as well. The code in the **port** directory is provided to emulate routines that may be missing on some systems. On UNIX systems the `configure` script automatically figures out which routines are not present on a system and enables the use of the equivalent emulation routines from the **port** directory. It may be necessary to manually do this work on a non-UNIX system. 

* * *

## Checking out the Software

Assuming you have working versions of `tiffgt` and `tiffsv`, you can just use them to view any of the sample images available for testing (see the [section on obtaining the test images](images.html)). Otherwise, you can do a cursory check of the library with the `tiffcp` and `tiffcmp` programs. For example,
    
    
    tiffcp -lzw cramps.tif x.tif
    tiffcmp cramps.tif x.tif
    

(`tiffcmp` should be silent if the files compare correctly). 

* * *

## Table of Contents

The following files makup the core library: 
    
    
    libtiff/tiff.h                  TIFF spec definitions
    libtiff/tiffcomp.h              non-UNIX OS-compatibility definitions
    libtiff/tiffconf.h              non-UNIX configuration definitions
    libtiff/tiffio.h                public TIFF library definitions
    libtiff/tiffiop.h               private TIFF library definitions
    libtiff/t4.h                    CCITT Group 3/4 code tables+definitions
    libtiff/tif_dir.h               private defs for TIFF directory handling
    libtiff/tif_fax3.h              CCITT Group 3/4-related definitions
    libtiff/tif_predict.h           private defs for Predictor tag support
    libtiff/uvcode.h                LogL/LogLuv codec-specific definitions
    libtiff/version.h               version string (generated by Makefile)
    
    libtiff/tif_acorn.c             Acorn-related OS support
    libtiff/tif_apple.c             Apple-related OS support
    libtiff/tif_atari.c             Atari-related OS support
    libtiff/tif_aux.c               auxilary directory-related functions
    libtiff/tif_close.c             close an open TIFF file
    libtiff/tif_codec.c             configuration table of builtin codecs
    libtiff/tif_compress.c          compression scheme support
    libtiff/tif_dir.c               directory tag interface code
    libtiff/tif_dirinfo.c           directory known tag support code
    libtiff/tif_dirread.c           directory reading code
    libtiff/tif_dirwrite.c          directory writing code
    libtiff/tif_dumpmode.c          "no" compression codec
    libtiff/tif_error.c             library error handler
    libtiff/tif_fax3.c              CCITT Group 3 and 4 codec
    libtiff/tif_fax3sm.c            G3/G4 state tables (generated by mkg3states)
    libtiff/tif_flush.c             i/o and directory state flushing
    libtiff/tif_getimage.c          TIFFRGBAImage support
    libtiff/tif_jpeg.c              JPEG codec (interface to the IJG distribution)
    libtiff/tif_luv.c               SGI LogL/LogLuv codec
    libtiff/tif_lzw.c               LZW codec
    libtiff/tif_msdos.c             MSDOS-related OS support
    libtiff/tif_next.c              NeXT 2-bit scheme codec (decoding only)
    libtiff/tif_open.c              open and simply query code
    libtiff/tif_packbits.c          Packbits codec
    libtiff/tif_pixarlog.c          Pixar codec
    libtiff/tif_predict.c           Predictor tag support
    libtiff/tif_print.c             directory printing support
    libtiff/tif_read.c              image data reading support
    libtiff/tif_strip.c             some strip-related code
    libtiff/tif_swab.c              byte and bit swapping support
    libtiff/tif_thunder.c           Thunderscan codec (decoding only)
    libtiff/tif_tile.c              some tile-related code
    libtiff/tif_unix.c              UNIX-related OS support
    libtiff/tif_version.c           library version support
    libtiff/tif_vms.c               VMS-related OS support
    libtiff/tif_warning.c           library warning handler
    libtiff/tif_win3.c              Windows-3.1-related OS support
    libtiff/tif_win32.c             Win32 (95/98/NT) related OS support
    libtiff/tif_write.c             image data writing support
    libtiff/tif_zip.c               Deflate codec
    
    libtiff/mkg3states.c            program to generate G3/G4 decoder state tables
    libtiff/mkspans.c               program to generate black-white span tables
    libtiff/mkversion.c             program to generate libtiff/version.h.
    

* * *

Last updated: $Date$ 
