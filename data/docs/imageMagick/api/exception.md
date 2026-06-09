[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireExceptionInfo](exception.html#AcquireExceptionInfo) • [ClearMagickException](exception.html#ClearMagickException) • [CatchException](exception.html#CatchException) • [CloneExceptionInfo](exception.html#CloneExceptionInfo) • [DestroyExceptionInfo](exception.html#DestroyExceptionInfo) • [GetExceptionMessage](exception.html#GetExceptionMessage) • [GetLocaleExceptionMessage](exception.html#GetLocaleExceptionMessage) • [InheritException](exception.html#InheritException) • [InitializeExceptionInfo](exception.html#InitializeExceptionInfo) • [MagickError](exception.html#MagickError) • [MagickFatalError](exception.html#MagickFatalError) • [MagickWarning](exception.html#MagickWarning) • [SetErrorHandler](exception.html#SetErrorHandler) • [SetFatalErrorHandler](exception.html#SetFatalErrorHandler) • [SetWarningHandler](exception.html#SetWarningHandler) • [ThrowException](exception.html#ThrowException)

## [AcquireExceptionInfo](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

AcquireExceptionInfo() allocates the ExceptionInfo structure.

The format of the AcquireExceptionInfo method is:
    
    
    ExceptionInfo *AcquireExceptionInfo(void)
    

## [ClearMagickException](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

ClearMagickException() clears any exception that may not have been caught yet.

The format of the ClearMagickException method is:
    
    
    ClearMagickException(ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

exception
    the exception info. 
    

## [CatchException](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

CatchException() returns if no exceptions is found otherwise it reports the exception as a warning, error, or fatal depending on the severity.

The format of the CatchException method is:
    
    
    CatchException(ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

exception
    the exception info. 
    

## [CloneExceptionInfo](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

CloneExceptionInfo() clones the ExceptionInfo structure.

The format of the CloneExceptionInfo method is:
    
    
    ExceptionInfo *CloneException(ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

exception
    the exception info. 
    

## [DestroyExceptionInfo](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

DestroyExceptionInfo() deallocates memory associated with an exception.

The format of the DestroyExceptionInfo method is:
    
    
    ExceptionInfo *DestroyExceptionInfo(ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

exception
    the exception info. 
    

## [GetExceptionMessage](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

GetExceptionMessage() returns the error message defined by the specified error code.

The format of the GetExceptionMessage method is:
    
    
    char *GetExceptionMessage(const int error)
    

A description of each parameter follows:

    
    

error
    the error code. 
    

## [GetLocaleExceptionMessage](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

GetLocaleExceptionMessage() converts a enumerated exception severity and tag to a message in the current locale.

The format of the GetLocaleExceptionMessage method is:
    
    
    const char *GetLocaleExceptionMessage(const ExceptionType severity,
      const char *tag)
    

A description of each parameter follows:

    
    

severity
    the severity of the exception. 
    
tag
    the message tag. 
    

## [InheritException](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

InheritException() inherits an exception from a related exception.

The format of the InheritException method is:
    
    
    InheritException(ExceptionInfo *exception,const ExceptionInfo *relative)
    

A description of each parameter follows:

    
    

exception
    the exception info. 
    
relative
    the related exception info. 
    

## [InitializeExceptionInfo](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

InitializeExceptionInfo() initializes an exception to default values.

The format of the InitializeExceptionInfo method is:
    
    
    InitializeExceptionInfo(ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

exception
    the exception info. 
    

## [MagickError](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

MagickError() calls the exception handler methods with an error reason.

The format of the MagickError method is:
    
    
    void MagickError(const ExceptionType error,const char *reason,
      const char *description)
    

A description of each parameter follows:

    
    

exception
    Specifies the numeric error category. 
    
reason
    Specifies the reason to display before terminating the program. 
    
description
    Specifies any description to the reason. 
    

## [MagickFatalError](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

MagickFatalError() calls the fatal exception handler methods with an error reason.

The format of the MagickError method is:
    
    
    void MagickFatalError(const ExceptionType error,const char *reason,
      const char *description)
    

A description of each parameter follows:

    
    

exception
    Specifies the numeric error category. 
    
reason
    Specifies the reason to display before terminating the program. 
    
description
    Specifies any description to the reason. 
    

## [MagickWarning](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

MagickWarning() calls the warning handler methods with a warning reason.

The format of the MagickWarning method is:
    
    
    void MagickWarning(const ExceptionType warning,const char *reason,
      const char *description)
    

A description of each parameter follows:

    
    

warning
    the warning severity. 
    
reason
    Define the reason for the warning. 
    
description
    Describe the warning. 
    

## [SetErrorHandler](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

SetErrorHandler() sets the exception handler to the specified method and returns the previous exception handler.

The format of the SetErrorHandler method is:
    
    
    ErrorHandler SetErrorHandler(ErrorHandler handler)
    

A description of each parameter follows:

    
    

handler
    the method to handle errors. 
    

## [SetFatalErrorHandler](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

SetFatalErrorHandler() sets the fatal exception handler to the specified method and returns the previous fatal exception handler.

The format of the SetErrorHandler method is:
    
    
    ErrorHandler SetErrorHandler(ErrorHandler handler)
    

A description of each parameter follows:

    
    

handler
    the method to handle errors. 
    

## [SetWarningHandler](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

SetWarningHandler() sets the warning handler to the specified method and returns the previous warning handler.

The format of the SetWarningHandler method is:
    
    
    ErrorHandler SetWarningHandler(ErrorHandler handler)
    

A description of each parameter follows:

    
    

handler
    the method to handle warnings. 
    

## [ThrowException](http://www.imagemagick.org/api/MagickCore/exception_8c.html)

ThrowException() throws an exception with the specified severity code, reason, and optional description.

The format of the ThrowException method is:
    
    
    MagickBooleanType ThrowException(ExceptionInfo *exception,
      const ExceptionType severity,const char *reason,
      const char *description)
    

A description of each parameter follows:

    
    

exception
    the exception info. 
    
severity
    the severity of the exception. 
    
reason
    the reason for the exception. 
    
description
    the exception description. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](exception.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
