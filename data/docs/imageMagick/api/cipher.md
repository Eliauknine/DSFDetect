[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireAESInfo](cipher.html#AcquireAESInfo) • [DestroyAESInfo](cipher.html#DestroyAESInfo) • [EncipherAESBlock](cipher.html#EncipherAESBlock) • [PasskeyDecipherImage](cipher.html#PasskeyDecipherImage) • [PasskeyEncipherImage](cipher.html#PasskeyEncipherImage) • [SetAESKey](cipher.html#SetAESKey) • [PasskeyDecipherImage](cipher.html#PasskeyDecipherImage) • [PasskeyEncipherImage](cipher.html#PasskeyEncipherImage)

## [AcquireAESInfo](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

AcquireAESInfo() allocate the AESInfo structure.

The format of the AcquireAESInfo method is:
    
    
    AESInfo *AcquireAESInfo(void)
    

## [DestroyAESInfo](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

DestroyAESInfo() zeros memory associated with the AESInfo structure.

The format of the DestroyAESInfo method is:
    
    
    AESInfo *DestroyAESInfo(AESInfo *aes_info)
    

A description of each parameter follows:

    
    

aes_info
    the cipher context. 
    

## [EncipherAESBlock](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

EncipherAESBlock() enciphers a single block of plaintext to produce a block of ciphertext.

The format of the EncipherAESBlock method is:
    
    
    void EncipherAES(AESInfo *aes_info,const unsigned char *plaintext,
      unsigned char *ciphertext)
    

A description of each parameter follows:

    
    

aes_info
    the cipher context. 
    
plaintext
    the plain text. 
    
ciphertext
    the cipher text. 
    

## [PasskeyDecipherImage](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

PasskeyDecipherImage() converts cipher pixels to plain pixels.

The format of the PasskeyDecipherImage method is:
    
    
    MagickBooleanType PasskeyDecipherImage(Image *image,
      const StringInfo *passkey,ExceptionInfo *exception)
    MagickBooleanType DecipherImage(Image *image,const char *passphrase,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
passphrase
    decipher cipher pixels with this passphrase. 
    
passkey
    decrypt cipher pixels with this passkey. 
    
exception
    return any errors or warnings in this structure. 
    

## [PasskeyEncipherImage](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

PasskeyEncipherImage() converts pixels to cipher-pixels.

The format of the PasskeyEncipherImage method is:
    
    
    MagickBooleanType PasskeyEncipherImage(Image *image,
      const StringInfo *passkey,ExceptionInfo *exception)
    MagickBooleanType EncipherImage(Image *image,const char *passphrase,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
passphrase
    encipher pixels with this passphrase. 
    
passkey
    decrypt cipher pixels with this passkey. 
    
exception
    return any errors or warnings in this structure. 
    

## [SetAESKey](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

SetAESKey() sets the key for the AES cipher. The key length is specified in bits. Valid values are 128, 192, or 256 requiring a key buffer length in bytes of 16, 24, and 32 respectively.

The format of the SetAESKey method is:
    
    
    SetAESKey(AESInfo *aes_info,const StringInfo *key)
    

A description of each parameter follows:

    
    

aes_info
    the cipher context. 
    
key
    the key. 
    

## [PasskeyDecipherImage](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

PasskeyDecipherImage() converts cipher pixels to plain pixels.

The format of the PasskeyDecipherImage method is:
    
    
    MagickBooleanType PasskeyDecipherImage(Image *image,
      const StringInfo *passkey,ExceptionInfo *exception)
    MagickBooleanType DecipherImage(Image *image,const char *passphrase,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image. 
    
passphrase
    decipher cipher pixels with this passphrase. 
    
passkey
    decrypt cipher pixels with this passkey. 
    
exception
    return any errors or warnings in this structure. 
    

## [PasskeyEncipherImage](http://www.imagemagick.org/api/MagickCore/cipher_8c.html)

PasskeyEncipherImage() converts pixels to cipher-pixels.

The format of the PasskeyEncipherImage method is:
    
    
    MagickBooleanType PasskeyEncipherImage(Image *image,
      const StringInfo *passkey,ExceptionInfo *exception)
    MagickBooleanType EncipherImage(Image *image,const char *passphrase,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

passphrase
    decipher cipher pixels with this passphrase. 
    
passkey
    decrypt cipher pixels with this passkey. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](cipher.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
