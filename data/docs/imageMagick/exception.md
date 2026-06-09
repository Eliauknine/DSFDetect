[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

ImageMagick returns a status of 0 whenever a command or algorithm successfully complete without complaint. A warning code generally is typically just a notice that something unusual occurred but the command or algorithm still completed and most likely the results are still usable. An error means the command or algorithm could not complete as expected and any results are unreliable. A fatal error means the command or algorithm could not complete and the process exits prematurely and no results are returned.

ImageMagick Error and Warning Codes Domain | Description | Warning | Error | Fatal Error  
---|---|---|---|---  
Success | the command or algorithm completed successfully without complaint | 0 | 0 | 0  
Resource Limit | a program resource is exhausted (e.g. not enough memory) | 300 | 400 | 700  
Type | A font is unavailable; a substitution may have occurred | 305 | 405 | 705  
Option | a command-line option was malformed | 310 | 410 | 710  
Delegate | an ImageMagick _delegate_ failed to complete | 315 | 415 | 715  
Missing Delegate | the image type can not be read or written because the appropriate _Delegate_ is missing | 320 | 420 | 720  
Corrupt Image | the image file may be corrupt | 325 | 425 | 725  
FileOpen | the image file could not be opened for reading or writing | 330 | 430 | 730  
Blob | a binary large object could not be allocated, read, or written | 335 | 435 | 735  
Stream | there was a problem reading or writing from a stream | 340 | 440 | 740  
Cache | pixels could not be read or written to the pixel cache | 345 | 445 | 745  
Coder | there was a problem with an image coder | 350 | 450 | 750  
Module | there was a problem with an image module | 355 | 455 | 755  
Draw | a drawing operation failed | 360 | 460 | 760  
Image | the operation could not complete due to an incompatible image | 365 | 465 | 765  
Wand | there was a problem specific to the MagickWand API | 370 | 470 | 770  
Random | there is a problem generating a true or pseudo-random number | 375 | 475 | 775  
XServer | an X resource is unavailable | 380 | 480 | 780  
Monitor | there was a problem activating the progress monitor | 385 | 485 | 785  
Registry | there was a problem getting or setting the registry | 390 | 490 | 790  
Configure | there was a problem getting a configuration file | 395 | 495 | 795  
Policy | a policy denies access to a delegate, coder, filter, path, or resource. | 399 | 499 | 799  
  
[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](exception.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
