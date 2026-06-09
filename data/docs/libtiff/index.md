# LibTIFF - TIFF Library and Utilities

* * *

Home Page | <http://www.remotesensing.org/libtiff/>  
---|---  
Home Page Mirror | <http://libtiff.maptools.org/>  
Latest Stable Release | [v3.8.2](v3.8.2.html)  
Latest Development Release | [v4.0.0alpha](v4.0.0.html)  
Master Download Site | [ftp.remotesensing.org](ftp://ftp.remotesensing.org/pub/libtiff), directory pub/libtiff  
Mirror Download Site | <http://libtiff.maptools.org/dl/>  
Windows Binaries | [GnuWin32 Project](http://gnuwin32.sourceforge.net/packages/libtiff.htm)  
Mailing List | [tiff@lists.maptools.org](mailto:tiff@lists.maptools.org), [Subscription](http://lists.maptools.org/mailman/listinfo/tiff/), [Archive](http://www.awaresystems.be/imaging/tiff/tml.html). Please, read the [TIFF FAQ](http://www.awaresystems.be/imaging/tiff/faq.html) before asking questions.  
Anonymous CVS | `export CVSROOT=:pserver:cvsanon@cvs.maptools.org:/cvs/maptools/cvsroot  
cvs login`  
(use empty password)  
`cvs checkout -r branch-3-9 libtiff  
` to get stable libtiff branch, or  
`cvs checkout libtiff`  
to get bleeding edge development version of libtiff from CVS HEAD.  
  
* * *

This software provides support for the _Tag Image File Format_ (TIFF), a widely used format for storing image data. The latest version of the TIFF specification is [available on-line](document.html) in several different formats. 

Included in this software distribution is a library, libtiff, for reading and writing TIFF, a small collection of tools for doing simple manipulations of TIFF images, and documentation on the library and tools. Libtiff is a portable software, it was built and tested on various systems: UNIX flavors (Linux, BSD, Solaris, MacOS X), Windows, OpenVMS. It should be possible to port libtiff and additional tools on other OSes. 

The library, along with associated tool programs, should handle most of your needs for reading and writing TIFF images on 32- and 64-bit machines. This software can also be used on older 16-bit systems though it may require some effort and you may need to leave out some of the compression support. 

The software was originally authored and maintained by Sam Leffler. While he keeps a fatherly eye on the mailing list, he is no longer responsible for day to day maintenance. 

Questions should be sent to the TIFF mailing list: [tiff@lists.maptools.org](mailto:tiff@lists.maptools.org), with a subscription interface at <http://lists.maptools.org/mailman/listinfo/tiff>. 

The persons responsible for putting up this site and putting together versions >= 3.5.1 are [Frank Warmerdam](http://pobox.com/~warmerdam), [Andrey Kiselev](mailto:dron@ak4719.spb.edu) and Mike Welles. 

The following sections are included in this documentation: 

  * [TIFF 6.0 specification coverage](support.html)
  * [Using the TIFF Library](libtiff.html)
  * [Modifying the TIFF Library](internals.html) and [Adding New Tags](addingtags.html)
  * [TIFF tools overview](tools.html)
  * [Contributed software](contrib.html)
  * [TIFF documentation](document.html)
  * [Building the software distribution](build.html)
  * [Bugs, Bugzilla, and the TIFF mailing list](bugs.html)
  * [Test images](images.html)
  * [Acknowledgements and copyright issues](misc.html)
  * [Man Pages](man/index.html)



**BigTIFF News**

  * [BigTIFF project proposal](BigTIFFProposal.html)
  * [Press release: Currently extending LibTiff](bigtiffpr.html)



* * *

Last updated $Date$. 
