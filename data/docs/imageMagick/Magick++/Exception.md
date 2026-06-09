# Magick::Exception Classes  
  
_Exception_ represents the base class of objects thrown when Magick++reports an error. Magick++ throws C++ exceptions synchronous with the operation where the error occurred. This allows errors to be trapped within the enclosing code (perhaps the code to process a single image) while allowing the code to be written with a simple coding style.

A try/catch block should be placed around any sequence of operations which can be considered an important body of work. For example, if your program processes lists of images and some of these images may be defective, by placing the try/catch block around the entire sequence of code that processes one image (including instantiating the image object), you can minimize the overhead of error checking while ensuring that all objects created to deal with that object are safely destroyed (C++ exceptions unroll the stack until the enclosing try block, destroying any created objects). 

The pseudo code for the main loop of your program may look like: 

using namespace std; for infile in list { try { // Construct an image instance first so that we don't have to worry // about object construction failure due to a minor warning exception // being thrown. Magick::Image image; try { // Try reading image file image.read(infile); } catch( Magick::WarningCoder &warning ) { // Process coder warning while loading file (e.g. TIFF warning) // Maybe the user will be interested in these warnings (or not). // If a warning is produced while loading an image, the image // can normally still be used (but not if the warning was about // something important!) cerr << "Coder Warning: " << warning.what() << endl; } catch( Magick::Warning &warning ) { // Handle any other Magick++ warning. cerr << "Warning: " << warning.what() << endl; } catch( Magick::ErrorFileOpen &error ) { // Process Magick++ file open error cerr << "Error: " << error.what() << endl; continue; // Try next image. } try { image.rotate(90); image.write("outfile"); } catch ( MagickExeption & error) { // Handle problem while rotating or writing outfile. cerr << "Caught Magick++ exception: " << error.what() << endl; } } catch( std::exception & error ) { // Process any other exceptions derived from standard C++ exception cerr << "Caught C++ STD exception: " << error.what() << endl; } catch( ... ) { // Process *any* exception (last-ditch effort). There is not a lot // you can do here other to retry the operation that failed, or exit } } 

The desired location and number of try/catch blocks in your program depends how sophisticated its error handling must be. Very simple programs may use just one try/catch block.

The _Exception_ class is derived from the C++ standard exception class. This means that it contains a C++ string containing additional information about the error (e.g to display to the user). Obtain access to this string via the what() method. For example: 
    
    
    catch( Exception & error_ ) 
        { 
          cout << "Caught exception: " << error_.what() << endl; 
        }
    

The classes _Warning_ and _Error_ derive from the _Exception_ class. Exceptions derived from _Warning_ are thrown to represent non-fatal errors which may effect the completeness or quality of the result (e.g. one image provided as an argument to montage is defective). In most cases, a _Warning_ exception may be ignored by catching it immediately, processing it (e.g. printing a diagnostic) and continuing on. Exceptions derived from _Error_ are thrown to represent fatal errors that can not produce a valid result (e.g. attempting to read a file which does not exist). 

The specific derived exception classes are shown in the following tables: 

**Warning Sub-Classes**

**Warning** |  **Warning Description**  
---|---  
WarningUndefined |  Unspecified warning type.  
WarningBlob |  NOT CURRENTLY USED  
WarningCache |  NOT CURRENTLY USED  
WarningCoder |  Warnings issued by some coders.  
WarningConfigure |  NOT CURRENTLY USED  
WarningCorruptImage |  Warning issued when an image is determined to be corrupt.  
WarningDelegate |  Warnings reported by the delegate (interface to external programs) subsystem.  
WarningDraw |  Warnings reported by the rendering subsystem.  
WarningFileOpen |  Warning reported when The image file could not be opened (permission problem, wrong file type, or does not exist).  
WarningImage |  NOT CURRENTLY USED  
WarningMissingDelegate |  NOT CURRENTLY USED  
WarningModule |  NOT CURRENTLY USED  
WarningMonitor |  NOT CURRENTLY USED  
WarningOption |  Warning reported when an option is malformed or out of range.  
WarningRegistry |  NOT CURRENTLY USED  
WarningResourceLimit |  Warning reported when a program resource is exhausted (e.g. not enough memory).  
WarningStream |  NOT CURRENTLY USED  
WarningType |  NOT CURRENTLY USED  
WarningXServer |  Warnings reported by the X11 subsystem.  



  


**Error Sub-Classes**

**Error** |  **Error Description**  
---|---  
ErrorUndefined |  Unspecified error type.  
ErrorBlob |  Error reported by BLOB I/O subsystem.  
ErrorCache |  Error reported by the pixel cache subsystem.  
ErrorCoder |  Error reported by coders (image format support).  
ErrorConfigure |  Errors reported while loading configuration files.  
ErrorCorruptImage |  Error reported when the image file is corrupt.  
ErrorDelegate |  Errors reported by the delegate (interface to external programs) subsystem.  
ErrorDraw |  Error reported while drawing on image.  
ErrorFileOpen |  Error reported when the image file can not be opened.  
ErrorImage |  Errors reported while drawing.  
ErrorMissingDelegate |  Error reported when an add-on library or program is necessary in order to support the requested operation.  
ErrorModule |  Errors reported by the module loader subsystem.  
ErrorMonitor |  NOT CURRENTLY USED  
ErrorOption |  Error reported when an option is malformed or out of range.  
ErrorRegistry |  Errors reported by the image/BLOB registry subsystem.  
ErrorResourceLimit |  Error reported when a program resource is exhausted (e.g. not enough memory).  
ErrorStream |  Errors reported by the pixel stream subsystem.  
ErrorType |  Errors reported by the type (font) rendering subsystem.  
ErrorXServer |  Errors reported by the X11 subsystem.  



  
  

