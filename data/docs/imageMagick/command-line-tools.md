[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

ImageMagick includes a number of command-line utilities for manipulating images. Most of you are probably accustomed to editing images one at a time with a graphical user interface (GUI) with such programs as [gimp](http://www.gimp.org) or [Photoshop](http://www.adobe.com). However, a GUI is not always convenient. Suppose you want to process an image dynamically from a web script or you want to apply the same operations to many images or repeat a specific operation at different times to the same or different image. For these types of operations, the command-line image processing utility is appropriate.

The ImageMagick [command-line](command-line-processing.html) tools exit with a status of 0 if the command line arguments have a proper syntax and no problems are encountered. Expect a descriptive message and an exit status of 1 if any exception occurs such as improper syntax, a problem reading or writing an image, or any other problem that prevents the command from completing successfully.

Here is a short description for each command-line tool. Click on the program name to get details about the program usage and a list of command-line options that alters how the program behaves. If you are just getting acquainted with ImageMagick, start with the [magick](command-line-tools.html#magick) program. Be sure to peruse Anthony Thyssen's tutorial on how to use ImageMagick utilities to [create, edit, compose, or convert](http://www.imagemagick.org/Usage/) images from the command-line.

[animate](animate.html)
    animate an image sequence on any X server.
[compare](compare.html)
    mathematically and visually annotate the difference between an image and its reconstruction.
[composite](composite.html)
    overlap one image over another.
[conjure](conjure.html)
    interpret and execute scripts written in the Magick Scripting Language (MSL).
[convert](convert.html)
    convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more.
[display](display.html)
    display an image or image sequence on any X server.
[identify](identify.html)
    describe the format and characteristics of one or more image files.
[import](import.html)
    save any visible window on an X server and outputs it as an image file. You can capture a single window, the entire screen, or any rectangular portion of the screen.
[magick](magick.html)
    convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more.
[magick-script](magick-script.html)
    use this scripting language convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more.
[mogrify](mogrify.html)
    resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more. Mogrify overwrites the original image file, whereas, [convert](convert.html) writes to a different image file.
[montage](montage.html)
    create a composite image by combining several separate images. The images are tiled on the composite image optionally adorned with a border, frame, image name, and more.
[stream](stream.html)
    a lightweight tool to stream one or more pixel components of the image or portion of the image to your choice of storage formats. It writes the pixel components as they are read from the input image a row at a time making `stream` desirable when working with large images or when you require raw pixel components.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](command-line-tools.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
