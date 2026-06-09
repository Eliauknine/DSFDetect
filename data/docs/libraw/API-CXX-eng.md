LibRaw C++ API


## LibRaw Objects


     The main LibRaw object (class) is created either without parameters or with flags determining the object behavior.
    

```

#include "libraw/libraw.h"
...

   LibRaw ImageProcessor(unsigned int flags=0);
...
    
```

Flags (several flags are combined via operator |, i.e., bitwise OR):

LIBRAW_OPTIONS_NO_MEMERR_CALLBACK: do not set the standard
out-of-memory error handler (standard handler outputs the error report in stderr);
LIBRAW_OPTIONS_NO_DATAERR_CALLBACK: do not set the standard
file read error handler (standard handler outputs the error report in stderr).


    Three groups of methods are used for image processing
    

Data loading from the RAW file
Postprocessing functions emulating the dcraw behavior
File output functions emulating the dcraw behavior.


      The results of processing are placed in the imgdata field of type libraw_data_t; the same data set contains fields that control the postprocessing
and output.
    


## Returned Values


      All LibRaw API functions return an integer number in accordance with the
return code convention. Please read the descriptions of 
this convention and LibRaw behavior
in cases of fatal errors.
    


## Methods Loading Data from a File



### int LibRaw::open_datastream(LibRaw_abstract_datastream *stream)

Opens a datastream with RAW data, reads metadata (EXIF) from it, and fills the following structures:
    

imgdata.idata (libraw_iparams_t),
imgdata.sizes (libraw_image_sizes_t),
imgdata.color (libraw_colordata_t),
imgdata.other (libraw_imgother_t), and 
imgdata.thumbnail (libraw_thumbnail_t).

The function returns an integer number in accordance with the return
code convention: positive if any system call has returned an error, negative
  (from the  LibRaw error list) if there has been an error
situation within LibRaw.
    
Before file opening, recycle() is always called; hence, if several images
are processed in the batch mode, there is no need to call recycle() at the end of each processing cycle.
    
Input data: pointer to object, derived from LibRaw_abstract_datastream class.
      This object should be initialized and ready to read. This object should be destroyed in calling application
      after use.
    


### int LibRaw::open_file(const char *filename[,INT64 bigfile_size])


      Creates an LibRaw_file_datastream object, calls 
      open_datastream(). If succeed, sets internal flag which signals
      to destroy internal datastream object on recycle(). On failure,
      just created file_datastream destroyed immediately.
    

      Second optional parameter bigfile_size controls background I/O interface used for file operations. For
      files smaller than bigfile_size the LibRaw_file_datastream will be used and the LibRaw_bigfile_datastream otherwise.
    The function returns an integer number in accordance with the 
      return code convention: positive if any system call has returned an error, negative
      (from the  LibRaw error list) if there has been an error
      situation within LibRaw.
    


### int LibRaw::open_buffer(void *buffer, size_t bufsize)


      Created an LibRaw_buffer_datastream object, calls 
      open_datastream(). If succeed, sets internal flag which signals
      to destroy internal datastream object on recycle(). On failure,
      just created file_datastream destroyed immediately.
    
The function returns an integer number in accordance with the 
      return code convention: positive if any system call has returned an error, negative
      (from the  LibRaw error list) if there has been an error
      situation within LibRaw.
    


###  int LibRaw::unpack(void)


      Unpacks the RAW files of the image, calculates the black level (not for all formats). The results are placed in imgdata.image.
    

 Data reading is sometimes (not frequently) affected by settings made in imgdata.params (libraw_output_params_t); see API notes for details.
    
The function returns an integer number in accordance with the return code
convention: positive if any system call has returned an error, negative (from the
      LibRaw error list) if there has been an error
situation within LibRaw.
    


### int LibRaw::unpack_thumb(void)


 Reads (or unpacks) the image preview (thumbnail), placing the result into the imgdata.thumbnail.thumb buffer.
 JPEG previews are placed into this buffer without any changes (with the header etc.). Other preview
formats are placed into the buffer in the form of the unpacked bitmap image (three components, 8 bits per component).
 The thumbnail format is written to the imgdata.thumbnail.tformat field; for the possible values, see
description of constants and data structures.

    
The function returns an integer number in accordance with the return code
convention: positive if any system call has returned an error, negative (from the
LibRaw error list) if there has been an error situation within
LibRaw.
    


## Auxiliary Functions


### Library version check



#### const char* LibRaw::version()


      Returns string representation of LibRaw version in MAJOR.MINOR.PATCH-Status format (i.e. 0.6.0-Alpha2
      or 0.6.1-Release).
    


#### int LibRaw::versionNumber()


      Returns integer representation of LibRaw version. During LibRaw development, the version number is always
      increase .
    


#### bool LIBRAW_CHECK_VERSION(major,minor,patch)


      Macro for version check in caller applications. Returns 'true' if current library version is greater or equal to
      set in macro parameters. This macro executes at runtime (not at compile time) and may be used for checking
      version of dynamically loaded LibRaw (from DLL/shared library).
    

### List of supported RAW formats (cameras)



#### int LibRaw::cameraCount()


      Returns count of cameras supported.
    


#### const char** LibRaw::cameraList()


      Returns list of supported cameras. Latest item of list is set to NULL (for easy printing).
    


### const char* LibRaw::unpack_function_name()


      Returns function name of file unpacking function. Intended only for LibRaw test suite designers to use in test
      coverage evaluation.
    


#### void LibRaw::subtract_black()


      This call will subtract black level values from RAW data (for suitable RAW data).
      colordata.channel_maximum and
      colordata.maximum and black level data (colordata.black and colordata.cblack) will be adjusted
      too.  
    

      This call should be used if you postprocess RAW data by your own code. LibRaw 
      postprocessing functions will call subtract_black() by oneself.
    


### void LibRaw::add_masked_borders_to_bitmap


      This call rebuilds imgdata.image bitmap and makes full bitmap, contains both image data (active 
      pixels) and 'black border' (masked pixels). If no masked pixels data present, then this call does nothing.
      Function call changes data fields sizes.width,sizes.height,sizes.iwidth,sizes.iheight to full image
      size (i.e. raw_width/raw_height).
      This call does nothing:
      

for images containing more than one color component per pixel (full-color DNG,
        already demosaiced files: Canon sRAW, Sinar 4-shot etc).
for images, unpacked with half resolution (one of parameters set in options: half_mode, wavelet denoising
        threshold, aberration fixing data).
      

The function returns an integer number in accordance with the return code
        convention: positive if any system call has returned an error, negative (from the
      LibRaw error list) if there has been an error situation within
      LibRaw. 
    


###  int LibRaw:: rotate_fuji_raw()


      This function rotates non-interpolated RAW bitmap from FujiCCD sensors into 45-degree-rotated position,
      compatible with old LibRaw versions (prior to LibRaw 0.7). This call is intended for applications,
      which works with non-interpolated/non-demosaiced RAW data itself. If 
      dcraw_process/dcraw_document_mode_processing calls are used, these call make the rotation internally.
    
The function returns an integer number in accordance with the return code
        convention: positive if any system call has returned an error, negative (from the
      LibRaw error list) if there has been an error situation within
      LibRaw. 
    


### void LibRaw::recycle(void)

Frees the allocated data of LibRaw instance, enabling one to process the next file using
the same processor. Repeated calls of recycle() are quite possible and do not conflict with anything. 
    


### LibRaw::~LibRaw()

Destructor, which consists in calling recycle().


### const char* LibRaw::strprogress(enum LibRaw_progress code)

Converts progress stage code to description string (in English).


### const char* LibRaw::strerror(int errorcode)

Analog of strerror(3) function: outputs the text descriptions of LibRaw error codes (in English).


### Setting Error Notification Functions


      In process of RAW conversion LibRaw can call user-setted callback. This callback can be used for:
    

Dynamic status update (progress bar and so on).
Cancel of processing (for example, user pressed Cancel button).

Also, work of the library may cause two types of exceptional situations that require notification of the calling application:
    

Memory shortage
Data read error.


 An application may set its own callbacks that will be called in the cases mentioned above to notify the user (or the calling program).
    


#### Progress indication/processing termination


```

        typedef int (*progress_callback)(void *callback_data,enum LibRaw_progress stage, int iteration, int expected);
        void LibRaw::set_progress_handler(progress_callback func,void *callback_data);
    
```


      LibRaw user can set own callback which will be called 10-50 times during RAW postprocessing
       by dcraw_process()/dcraw_document_mode_processing();
    

      This callback may terminate current image processing by returning of non-zero value. In such case all processing
      will be cancelled immediately and all resources will be returned to system by recycle() call.
      Current call of dcraw_process()/dcraw_document_mode_processing() will return error code
      LIBRAW_CANCELLED_BY_CALLBACK.
      

      Callback parameters:
      

**void *callback_data**
: void*-pointer, passed as 2nd argument to set_progress_handler(). This pointer should be used to pass
        additional data to callback (i.e. thread local data and so on).

**enum LibRaw_progress stage**
: Current processing stage. This number can be converted to string by call toLibRaw::strprogress. Not all processing stages are covered by callback calls.

**int iteration**
: Iteration number within current stage (from 0 to expected-1).

**int expected**
: Expected number of iterations on current stage.


    Callback should return value of: 0 for continue processing and non-zero for immediate cancel of processing.
    

      If LibRaw compiled with OpenMP support, iteration parameter may not always increase within one stage. Out of
      order callback calls are possible.
    

      Callback code sample:

```

int my_progress_callback(void *data,enum LibRaw_progress p,int iteration, int expected)
{
    char *passed_string = (char *data);
    printf("Callback: %s  pass %d of %d, data passed: %s\n",libraw_strprogress(p),iteration,expected,passed_string);
    if(timeout || key_pressed )
        return 1; // cancel processing immediately
    else
        return 0; // can continue
}


```



#### Out-of-Memory Notifier


```

        typedef void (* memory_callback)(void *callback_data,const char *file, const char *where);
        void LibRaw::set_memerror_handler(memory_callback func,void *callback_data);
    
```

The user may set his or her own function called in the case of memory shortage. It is a void function
receiving two string parameters:
    

void *callback_data - void*-pointer, passed as 2nd argument to set_progress_handler(). This pointer
        should be used to pass         additional data to callback (i.e. thread local data and so on).
file is the name of the RAW file whose processing evoked the out-of-memory error.
        This name can be NULL if underlying data input layer does not know the name. So, if calling
        application sets own callback, this callback should work with NULL file name.
      
where is the name of the function where memory shortage occurred.

The callback function is intended for information purposes: it notifies the user
or the program code that processing is impossible.
If the user does not set his or her own handler, the standard one (output of error message in stderr) will be used.
One can set the null handler by passing NULL to set_memerror_handler; then no notifier
function will be called. The same effect can be achieved by creating a LibRaw object with the LIBRAW_OPTIONS_NO_MEMERR_CALLBACK
flag in the contructor.
    
In the case of memory shortage, processing of the current file is terminated and a notifier is called; all
allocated resources are freed, and recycle() is performed. The current call will return
LIBRAW_UNSUFFICIENT_MEMORY. 
      
At an attempt to continue data processing, all subsequent calls will return LIBRAW_OUT_OF_ORDER_CALL. 
Processing of a new file may be started in the usual way, by calling LibRaw::open_file().
    


#### File Read Error Notifier


```

        typedef void (*data_callback)(void *callback_data,const char *file, const int offset);
        void LibRaw::set_dataerror_handler(data_callback func, void *callback_data); 
    
```


      The user can define his or her own function to be called in the case of error in the input data. It is a void function receiving
two parameters:
    

void *callback_data - void*-pointer, passed as 2nd argument to set_progress_handler(). This pointer
        should be used to pass         additional data to callback (i.e. thread local data and so on).
file is the name of the RAW file whose processing evoked the file read error.
        This name can be NULL if underlying data input layer does not know the name. So, if calling
        application sets own callback, this callback should work with NULL file name.
      
offset is -1 at end-of-file (if LibRaw expects more data) or a positive number equal to
the file position (bytes from file beginning) where the unpacking error occurred.

The callback function is intended for information purposes: it notifies the user
or the program code that processing is impossible.
If the user does not set his or her own handler, the standard one (output of error message in stderr) will be used.
One can set the null handler by passing NULL to set_memerror_handler; then no notifier
function will be called. The same effect can be achieved by creating a LibRaw object with the LIBRAW_OPTIONS_NO_DATAERR_CALLBACK
flag in the contructor. 
In the case of error in the input data, processing of the current file is terminated and a notifier is called; all
allocated resources are freed, and recycle() is performed. The current call will return
LIBRAW_IO_ERROR. 
      
At an attempt to continue data processing, all subsequent calls will return LIBRAW_OUT_OF_ORDER_CALL. 
Processing of a new file may be started in the usual way, by calling LibRaw::open_file().
    


## Data Postprocessing: Emulation of dcraw Behavior


Instead of writing one's own Bayer pattern postprocessing, one can use the dcraw functions, which are called
after the calls of open_file() + unpack() /+ unpack_thumb()/
    


### Parameter Setting


Virtually all parameters that can be set through the dcraw command line are specified by assigning values to
fields of the LibRaw::imgdata.params structure. The type of this structure is libraw_output_params_t;
all fields are listed and described in sufficient detail in the description
of data structures.
    


### int LibRaw::adjust_sizes_info_only(void)


      The function calculates the correct size of the output image (imgdata.sizes.iwidth and imgdata.sizes.iheight) for the
            following cases: 
      

Files from Fuji cameras (with a 45-degree rotation)
Files from cameras with non-square pixels
Images shot by a rotated camera.


      In the aforementioned cases, the function changes the fields of the image output size; note that
this change cannot be repeated again.
    

      The function should be used for information purposes; it is incompatible with dcraw_document_mode_processing() and dcraw_process() calls. 
    


### int LibRaw::dcraw_document_mode_processing(void)


     The function emulates dcraw -D: no interpolation, white balance, and color conversion. 
It is called after calling LibRaw::unpack();
    
The function returns an integer number in accordance with the error
code convention: positive if any system call has returned an error, negative (from the
LibRaw error list) if there has been an error situation within
LibRaw.
    


### int LibRaw::dcraw_process(void)


      The function emulates the postprocessing capabilities available in dcraw.
      Called after calling LibRaw::unpack();
    
The entire functionality of dcraw (set via the field values in imgdata.params) is supported, except for
      

Dark frame subtraction
Work with bad pixels.

The function is intended solely for demonstration and testing purposes; it is assumed that its source code
will be used in most real applications as the reference material concerning the order of RAW data processing. 
    
The function returns an integer number in accordance with the error
code convention: positive if any system call has returned an error, negative (from the
LibRaw error list) if there has been an error situation within
LibRaw.
    


## Data Output to Files: Emulation of dcraw Behavior

In spite of the abundance of libraries for file output in any formats, LibRaw includes calls that emulate
the file output provided by dcraw. This is done primarily for easier verification of library work: the resultant
files must be binary identical.
    


### int LibRaw::dcraw_ppm_tiff_writer(const char *outfile)


     The function outputs the postprocessing results to a file in the PPM/PGM or TIFF format (the format is set via 
      imgdata.params.output_tiff). The results are binary identical to those provided by dcraw.
    
The function returns an integer number in accordance with the error
code convention: positive if any system call has returned an error, negative (from the
LibRaw error list) if there has been an error situation within
LibRaw.
    


### int LibRaw::dcraw_thumb_writer(const char *thumbfile)

Writes the thumbnail to a file in the PPM format for bitmap thumbnails and in the JPEG format for JPEG thumbnails, i.e.,
in the format completely identical to the results provided by dcraw.
    
The function returns an integer number in accordance with the error
code convention: positive if any system call has returned an error, negative (from the
LibRaw error list) if there has been an error situation within
LibRaw.
    


## Copying unpacked data into memory buffer


      There is two function calls for store unpacked data into memory buffer (after using dcraw_process() and so on):
      
dcraw_make_mem_image - store processed image data into allocated buffer;
        
dcraw_make_mem_thumb -  store extracted thumbnail into buffer as JPEG-file image (for most cameras)
        or as RGB-bitmap.
      

    For usage primer see samples/mem_image.c sample.
    


### libraw_processed_image_t *dcraw_make_mem_image(int *errorcode=NULL) - store unpacked and processed image into
      memory buffer as RGB-bitmap


      This function allocates memory buffer and stores unpacked-preprocessed image into this buffer. Function returns
      allocated structure libraw_processed_image_t with
      filled fields. Always returns data as RGB bitmap  (i.e. type field is equal to LIBRAW_IMAGE_BITMAP).
    

      
      dcraw_process() or dcraw_document_mode_processing() should be called before dcraw_make_mem_image();
    

      Returns NULL in case of an error. If caller has passed not-NULL value as errorcode parameter, than *errorcode
      will be set to error code according to error code convention.
    
NOTE! Memory, allocated for return value will not be fried at destructor or LibRaw::recycle
      calls. Caller of dcraw_make_mem_image should free this memory by call to LibRaw::dcraw_clear_mem(). 
    


### libraw_processed_image_t *dcraw_make_mem_thumb(int *errorcode=NULL) - store unpacked thumbnail into memory buffer


      This function allocates memory buffer and stores thumbnail data in it. Function returns allocated
      structure libraw_processed_image_t with
      filled fields. For most RAW images allocated structure will contains JPEG image (i.e. type
      field is equal to  LIBRAW_IMAGE_JPEG). For some cameras with RGB-bitmap thumbnail (Kodak SLRs) 
      returned structure contains RGB bitmap (type field is equal to  LIBRAW_IMAGE_JPEG, see structure
      description for details).
    

      unpack_thumb() should be called before dcraw_make_mem_thumb();
    

      Returns NULL in case of an error. If caller has passed not-NULL value as errorcode parameter, than *errorcode
      will be set to error code according to ñ error code convention.
    
NOTE! Memory, allocated for return value will not be fried at destructor or LibRaw::recycle
      calls. Caller of dcraw_make_mem_image should free this memory by call to LibRaw::dcraw_clear_mem(). 
    

### void LibRaw::dcraw_clear_mem(libraw_processed_image_t *)


      This function will free the memory allocated by dcraw_make_mem_image or dcraw_make_mem_thumb.
      

      This is static class member, so call syntax should be LibRaw::dcraw_clear_mem(...).
    

      This call translates directly to free() system function, but it is better to use dcraw_clear_mem because
      LibRaw (DLL) may be compiled with memory manager other than in calling application.
    


## Input layer abstraction



### class LibRaw_abstract_datastream - abstract RAW read interface


      LibRaw reads RAW-data by calling (virtual) methods of C++ object derived from 
      LibRaw_abstract_datastream. This C++ class does not implement any read, but defines interface to be
      called. Call to base class methods always results in error.
    


#### LibRaw_abstract_datastream class methods


Object verification


**virtual int         valid()**
: Checks input datastream validity. Returns 1 on valid stream and 0 if datastream was created on non-valid
        input parameters (wrong filename for file stream and so on).

**virtual int         read(void * ptr,size_t size, size_t nmemb)**
: Similar to fread(ptr,size,nmemb,file).

**virtual int         seek(off_t o, int whence)**
: Similar to fseek(file,o,whence).

**virtual int         tell(**
: Similar to ftell(file).

**virtual int         get_char()**
: Similar to getc(file)/fgetc(file).

**virtual char*       gets(char *s, int n)**
: Similar to fgets(s,n,file).

**virtual int         eof()**
: Similar to feof(file).

**virtual int         scanf_one(const char *fmt, void *val)**
: Simplified variant of fscanf(file,fmt,val): format string is always contains one argument to read. So,
        variable args call is not needed and only one pointer to data passed.

**virtual const char* fname()**
: Returns name of opened file if datastream object knows it (for example,LibRaw_file_datastreamused). Filename used in:error notofocation callbacks;generation of filename of JPEG-file with metadata when needed (i.e. cameras with 'Diag RAW hack').

**virtual int         subfile_open(const char *fn)**
: This call temporary switches input to filefn. Returns 0 on success and error code on error.The function used to read metadata from external JPEG file (on cameras with "Diag RAW hack").This call is not implemented forLibRaw_buffer_datastream, so
        external JPEG processing is not possible when buffer datastream used.This functon should be implemented in real input class, base class call always return error.Working implementation sample can be found inLibRaw_file_datastreamimplementation inlibraw/libraw_datastream.hfile.

**virtual void subfile_close()**
: This call switches input stream from temporary open file back to main data stream.

**virtual int		tempbuffer_open(void  *buf, size_t size)**
: This call temporary switches input toLibRaw_buffer_datastreamobject,
        created frombuf.This method is needed for Sony encrypted metadata parser.This call implemented in base class (LibRaw_abstract_datastream), there is no need to
          reimplement in in derived classes.Possible activity of temporary datastream requires very accurate programming when implementing
          datastreams derived from baseLibRaw_abstract_datastream. Seebelowfor more details.

**virtual void	tempbuffer_close()**
: This call switch input back from temporary datastream to main stream. This call implemented
        in baseLibRaw_abstract_datastreamclass.

**LibRaw_file_datastream(const char *fname)**
: This constructor createsLibRaw_file_datastreamobject from filefname.Unfortunately, C++ constructor cannot return an error. So if bad filename passed (e.g. nonexistent file)
        object is created as non-valid (valid() call returns zero).

**LibRaw_bigfile_datastream(const char *fname)**
: This constructor createsLibRaw_bigfile_datastreamobject from filefname.Unfortunately, C++ constructor cannot return an error. So if bad filename passed (e.g. nonexistent file)
        object is created as non-valid (valid() call returns zero).

**LibRaw_buffer_datastream(void *buffer, size_t bsize)**
: This constructor creates datastream object frombufferwith sizebsize.It is not possibly to verify the pointer passed, so buffer address is checked against 0 and -1 only.



