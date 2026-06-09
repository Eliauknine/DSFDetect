[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[Encipher an Image](cipher.html#encipher) • [Decipher an Image](cipher.html#decipher) • [Encipher and Decipher Caveats](cipher.html#caveats)

Most images, by design, are made to be viewed often and by many people. Web images, for example, may be viewed hundreds of times a day by a multitude of vistors. However, in some cases, you may want to keep a particular image private so that only you or perhaps a select group of your friends or web visitors can view it. ImageMagick permits you to scramble your images such that unless someone knows your passphrase, they will be unable to view the original content.

You could use an [enciphering](http://www.wizards-toolkit.org/www/encipher.html) utility to scramble your image but they typically scramble the entire file making it unrecognizable as an image format. With ImageMagick, only the pixels are scrambled. The scrambled image continues to be recognized as an image and will even display in your web page. However, the content appears as gibberish, nothing like the original content.

## Encipher an Image

Use the [-encipher](command-line-options.html#encipher) option to scramble your image so that it is unrecognizable. The option requires a filename that contains your passphrase. In this example we scramble an image and save it in the PNG format:
    
    
    convert rose.jpg -encipher passphrase.txt rose.png
    

Here we encipher an image using another image as the passphrase:
    
    
    convert rose.jpg -encipher smiley.gif rose.png
    

## Decipher an Image

Use the [-decipher](command-line-options.html#decipher) option to unscramble your image so that it is recognizable once again. The option requires a filename that contains your passphrase. In this example we unscramble an image and save it in the JPEG format:
    
    
    convert rose.png -decipher passphrase.txt rose.jpg
    

## Encipher and Decipher Caveats

Some formats do not support enciphered pixels-- the JPEG or GIF format, for example. To ensure your image format is supported, encipher a test image and verify you can restore its original content before you encipher any additional images in that format.

The image format may only support 8-bit and RGB (TrueColor). As such you may like to include the options "-depth 8 -type TrueColor" before the output filename.

The passphrase can be any combinations of letters and symbols. It should be a minimum of 12 character combinations to help ensure your image remains private. Also make sure your passphrase file permissions prevent others from reading it otherwise unintended users may be able to view the original image content.

You can only restore the original image content if you know your passphrase. If you lose or forget it, your original image content is lost forever.

ImageMagick only scrambles the image pixels. The image metadata remains untouched and readable by anyone with access to the image file.

ImageMagick uses the [AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) cipher in Counter mode. We use the the first half of your passphrase to derive the nonce. The second half is the cipher key. When used correctly, AES-CTR provides a high level of confidentiality. To avoid information leaks, you must use a fresh passphrase for each image your encrypt.

Currently only ImageMagick can restore your enciphered image content. We use a standard cipher and mode so other vendors are could support enciphered image content.

Some small practical examples of image enciphering can be found in IM Examples [Encrypting Image Data](http://www.imagemagick.org/Usage/transform/#encipher). 

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](cipher.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
