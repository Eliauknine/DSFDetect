# TIFFError

NAME  
SYNOPSIS  
DESCRIPTION  
RETURN VALUES  
SEE ALSO  


* * *

## NAME

|  |  TIFFError, TIFFSetErrorHandler − library error handling interface

## SYNOPSIS

|  |  **#include <tiffio.h>** **void TIFFError(const char ***_module_**, const char ***_fmt_**,** _..._**)** **#include <stdarg.h>** **typedef void (*TIFFErrorHandler)(const char ***_module_**, const char ***_fmt_**, va_list** _ap_**);  
TIFFErrorHandler TIFFSetErrorHandler(TIFFErrorHandler handler);**

## DESCRIPTION

|  |  _TIFFError_ invokes the library-wide error handling function to (normally) write an error message to the **stderr**. The _fmt_ parameter is a _printf_(3S) format string, and any number arguments can be supplied. The _module_ parameter, if non-zero, is printed before the message; it typically is used to identify the software module in which an error is detected. Applications that desire to capture control in the event of an error should use _TIFFSetErrorHandler_ to override the default error handler. A NULL (0) error handling function may be installed to suppress error messages.

## RETURN VALUES

|  |  _TIFFSetErrorHandler_ returns a reference to the previous error handling function.

## SEE ALSO

|  |  **TIFFWarning**(3TIFF), **libtiff**(3TIFF), **printf**(3) Libtiff library home page: **http://www.remotesensing.org/libtiff/**

* * *
