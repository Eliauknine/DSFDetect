# CODEC

NAME  
SYNOPSIS  
DESCRIPTION  
DIAGNOSTICS  
SEE ALSO  


* * *

## NAME

|  |  TIFFFindCODEC, TIFFRegisterCODEC, TIFFUnRegisterCODEC, TIFFIsCODECConfigured − codec-related utility routines

## SYNOPSIS

|  |  **#include <tiffio.h>** **const TIFFCodec* TIFFFindCODEC(uint16** _scheme_**);  
TIFFCodec* TIFFRegisterCODEC(uint16** _scheme_**, const char ***_method_**, TIFFInitMethod** _init_**);  
void TIFFUnRegisterCODEC(TIFFCodec ***_codec_**);  
int TIFFIsCODECConfigured(uint16** _scheme_**);**

## DESCRIPTION

|  |  _libtiff_ supports a variety of compression schemes implemented by software _codecs_. Each codec adheres to a modular interface that provides for the decoding and encoding of image data; as well as some other methods for initialization, setup, cleanup, and the control of default strip and tile sizes. Codecs are identified by the associated value of the TIFF _Compression_ tag; e.g. 5 for LZW compression. The _TIFFRegisterCODEC_ routine can be used to augment or override the set of codecs available to an application. If the specified _scheme_ already has a registered codec then it is _overridden_ and any images with data encoded with this compression scheme will be decoded using the supplied coded. _TIFFIsCODECConfigured_ returns 1 if the codec is configured and working. Otherwise 0 will be returned.

## DIAGNOSTICS

|  |  **No space to register compression scheme %s**. _TIFFRegisterCODEC_ was unable to allocate memory for the data structures needed to register a codec. **Cannot remove compression scheme %s; not registered**. _TIFFUnRegisterCODEC_ did not locate the specified codec in the table of registered compression schemes.

## SEE ALSO

|  |  **libtiff**(3TIFF) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
