[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

2016-01-30 7.0.0-0 Fahad-Alsaidi & ShamsaHamed
* Add support for languages that require complex text layout (reference https://github.com/ImageMagick/ImageMagick/pull/88).
2012-04-27 7.0.0-0 Anthony thyssen <A.Thyssen@griffith...>
* Allow the use of set and escapes when no images in memory (unless you attempt to access per-image meta-data) Currently does not include %[fx:...] and %[pixel:...]
2012-10-05 7.0.0-0 Anthony thyssen <A.Thyssen@griffith...>
* Rather than replicate 'options' into 'artifacts' make a link from image to image_info and lookup a global option if no artifact is defined.
2012-09-11 7.0.0-0 Nicolas Robidoux <nicolas.robidoux@gmail...>
* sigmoidal-contrast:
* Remove unnecessary initial ClampToQuantum.
2012-09-10 7.0.0-0 Nicolas Robidoux <nicolas.robidoux@gmail...>
* sigmoidal-contrast:
* Direct computation, without LUT;
* Fix re-declaration of i (at the top, and inside a conditional).
2012-09-04 7.0.0-0 Nicolas Robidoux <nicolas.robidoux@gmail...>
* Add tanh/atanh clone of legacy sigmoidal map (faster & more accurate).
2012-08-08 7.0.0-0 Nicolas Robidoux <nicolas.robidoux@gmail...>
* Add final ClampToQuantum in sigmoidal colormap loop.
* Remove OpenMP calls from colormap update loops.
2011-08-01 7.0.0-0 Cristy <quetzlzacatenango@image...>
* New version 7.0.0-0.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](changelog.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
