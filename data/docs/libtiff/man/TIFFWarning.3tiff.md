# TIFFWarning

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
SEE ALSO  


* * *

## NAME

|  |  TIFFWarning, TIFFSetWarningHandler − library warning interface

## SYNOPSIS

|  |  **#include <tiffio.h>** **void TIFFWarning(const char ***_module_**, const char ***_fmt_**,** _..._**)** **#include <stdargh.h>** **typedef void (*TIFFWarningHandler)(const char ***_module_**, const char ***_fmt_**, va_list** _ap_**);** **TIFFWarningHandler TIFFSetWarningHandler(TIFFWarningHandler** _handler_**);**

## DESCRIPTION

|  |  _TIFFWarning_ invokes the library-wide warning handler function to (normally) write a warning message to the **stderr**. The _fmt_ parameter is a _printf_(3S) format string, and any number arguments can be supplied. The _module_ parameter is interpreted as a string that, if non-zero, should be printed before the message; it typically is used to identify the software module in which a warning is detected. Applications that desire to capture control in the event of a warning should use _TIFFSetWarningHandler_ to override the default warning handler. A NULL (0) warning handler function may be installed to suppress error messages.

## RETURN VALUES

|  |  _TIFFSetWarningHandler_ returns a reference to the previous error handling function.

## SEE ALSO

|  |  **TIFFError**(3TIFF), **libtiff**(3TIFF), **printf**(3) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
