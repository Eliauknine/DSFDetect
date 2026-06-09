


LibRaw: General Notes on API



[back to Index]

# LibRaw: General Notes on API


## LibRaw Versions

Since version 0.9, there is only one LibRaw variants. Older versions have three separate editions (normal,
      -Lite and -Commercial versions).
    


## Error Code Conventions and Error Handling


     The following conventions concern the returned errors: 
    

All functions that can return an error code have integer type of return data.
If there is no error, the return value is 0 (LIBRAW_SUCCESS).
If an error has happened in a system call, the return value is errno 
(a positive number), which can be analyzed using strerror() or similar means.
All LibRaw's own error codes are negative; each of these errors belongs to one of two types:
        

**Non-fatal errors**
: Non-fatal errors do not forbid execution of other functions in the processing succession
     (e.g.,unpack_thumb()can easily return the code corresponding to "preview is absent"
     but this does not prevent further call ofunpack().

**Fatal errors**
: In the case of fatal errors (memory shortage, input data error, data unpacking failure), the current stage of processing
            is terminated and all allocated resouces are freed.If an attempt to continue processing is made, all subsequent API calls will return the LIBRAW_OUT_OF_ORDER_CALL error.At the same time, the LibRaw instance in which a fatal error has occurred can process the next RAW
            files in the usual way (by callingopen_file()(or other input methods),  thenunpack(),
            etc.).


The macro LIBRAW_FATAL_ERROR(error code) checks if an error is fatal or not.
The error codes are listed and deciphered here.



## Nonstandard Situations That Are Not Errors

If the program has encountered a nonstandard situation that does not prevent retrieval of some data
     from a file, it sends a signal by setting the corresponding bit in imgdata.process_warnings. 
     The possible types of warnings are listed and deciphered here.
      


## Input Layer Abstraction


      LibRaw uses objects derived from 
      LibRaw_abstract_datastream for data input.
      Semantics of these objects is similar to 'file with arbitrary seek' object: both read and seek
      operations are used. 
    

      Some RAW formats requires temporary switch to another data stream created on top on memory buffer for metadata
      read. Methods for doing so are implemented in base class 
      LibRaw_abstract_datastream by internal data field substream.
      Look into source code of  LibRaw_file_datastream class 
      in  libraw/libraw_datastream.h file for more details.
      
      When implementing own datastream classes, you need to take substream into account and pass control to
      methods of this field if it is active (not NULL).
    

      If datastream implementaton knows name of input file, it should provide fname() call. This name will be used
      in error callbacks and in guessing name of JPEG file with metadata
      (for RAW files with external metadata).
    

      For external metadata support input class should implement
      subfile_open()/subfile_close() methods.
      возврашают код ошибки.
      
      Sample of these methods implementation may be found in 
      LibRaw_file_datastream class (look into 
      libraw/libraw_datastream.h file for details).
    


## Thread safety


      Thread safety is ensured if a LibRaw object is created and used within one thread. At the same time, the number
      of threads (each with its own LibRaw object) is not limited in any way (except by memory requirements).
      

      If a LibRaw object is created in one execution thread and used in another, external synchronization is
      necessary. 
    

      There is two libraries under  Unix enviroment (Linux/FreeBSD/MacOS): libraw_r.a (thread-safe) and libraw.a
      (single-threaded, slightly faster).
      

      Thread-safe library version stores intermediate unpacker data into LibRaw class data. So, several copies of
      LibRaw, working in parallel, is possible.
    

      Not thread-safe library uses global variable for intermediate data store which is faster but not reenterant.
      This library may be used in multi-threaded apps, but only if exactly one LibRaw class copy exists in program.
    

      Windows version is similar to multi-threaded Unix one.
    


## The Use of C++


      Exception situations within LibRaw are handled using the C++ exception mechanism. All exceptions are caught inside
   the library functions and should not penetrate outside. 
    

      Memory is allocated/freed using functions malloc(calloc)/free rather than new/delete.
    

    No specific libraries (STL, Boost, smart pointers) are used. 

    If C API is used, references to C++ calls new/delete still remain, and so linking with libstdc++(Unix)/....(Windows) is necessary. 
    


## Parameters of the LibRaw::imgdata.params Structure Affecting the Behavior of open_file/unpack/unpack_thumb


      Most data fields of structure LibRaw::imgdata.params affect only  data
        postprocessing,  but there are some exceptions, which have been inherited by the current version of LibRaw
      from/ dcraw source texts (these dependences will be gradually removed).
       

**imgdata.params.use_camera_matrix and imgdata.params.use_camera_wb**
: These fields affect loading of RAW data for cameras with a color matrix.Attention!If parameterimgdata.params.use_camera_matrixis not set by the user, it is copied fromimgdata.params.use_camera_wbat the stage of file opening.

**imgdata.params.user_flip**
: If this parameter is greater than or equal to zero, assignmentimgdata.sizes.flip = imgdata.params.user_flipis
     performed at theopen_file()stage.

**imgdata.params.shot_select**
: This parameter makes it possible to select the number of the extracted image for data formats in which storage
    of several RAW images in one data file is possible.

**imgdata.params.half_size**
: Affects RAW data loading for Phase One and Sinar backs. Also, it this parameter is set then image bitmap
        will be reduced by half in each dimension. In later case, all 4 components of bitmap will be filled during
        data extraction phase.

**imgdata.params.threshold, imgdata.params.aber**
: If these parameters used, then half-sized bitmap will be used for data unpacking. See above for details.

**imgdata.params.filtering_mode**
: Affects RAW data loading for cameras with black level subtraction/de-banding during RAW read phase:
        Canon A600, A5, CRW/CR2; cameras with LJPEG-compression (some Nikon, Kodak and Hasselblad cameras).

**imgdata.params.use_camera_wb**
: Affects loading of white balance matrix for Leaf backs.

**imgdata.params.document_mode**
: Does not affect data reading in the current version of LibRaw. In dcraw, this parameter affects the thumbnail data for certain Kodak cameras.




## RAW-data filtration


      During RAW unpacking and post-process stages LibRaw can filter RAW data:
    

Black level subtraction (required if not already done by camera firmware).
Zero pixels removal (averaging with nearest pixel values).
Tone curve operations on RAW-data.


      Current LibRaw version allows tuning of filtration process by setting imgdata.params.filtering_mode
      option to one of enum LibRaw_filtering vales:
      

Dcraw-compatible filtration. This mode is default for old LibRaw versions compatibility. This mode
        is not recommended for new applications.
One or several (or all) filtering stages can be turned off. This mode recommended for
        RAW analysers and advanced data filtration made by calling program (this programs may 
        calculate black level by analyzing masked frame data.
Automatic selection of best filtration  avaliable in LibRaw (e.g. camera/model specific
        routines). This mode is recommended for most applications.
        



## Masked pixels storage


      Some of RAW images contains data for not-active ("black","masked") pixels. For some of these formats
      LibRaw can extract these pixels values and store it in 
      imgdata.masked_pixels data structure. 
      These values can be explored for:
    

Black level calculation (with banding suppression on some cameras).
Noise level calculation, e.g. per-channel noise. This is useful for cameras with per-channel
        amplification.

Masked pixel data avaliable only for bayer-pattern data (one component per pixel) and only for cameras
      with masked frame. Masked pixels extraction for other color models (Canon sRAW, Kodak YRGB, Sinar 4-shot
      files) will possibly be added in future LibRaw versions.

      LibRaw provides interface for merging active pixel data and masked pixels into one bitmap:
      add_masked_borders_to_bitmap().
      This call is useful for RAW analyzers.
    


## Memory Usage



### Stack Usage


      An instance of the LibRaw class has its own size about 100 Kb; if constructions like LibRaw
        imageProcessor;  are used, this memory is stack-allocated. 
    

      Methods of class LibRaw (and C API calls) may allocate up to 130-140 Kb of data on the stack (to place auto
      variables) during their work. 
    
Thus, the work of one LibRaw instance may require about 250 Kb of stack memory. This is not a problem for most
      contemporary architectures.  However, when working in a multithreaded environment, one should not forget to
      allocate a sufficient amount of memory for the thread stack. 
    
In the case of dynamic allocation (LibRaw *iProcessor = new LibRaw;), the requirements to stack
      memory will decrease by 100 Kb, which is the size of a class instance). If C API is
      used, the LibRaw instance is allocated dynamically.
    


### Dynamic Memory Management

LibRaw keeps record of all allocated dynamic memory blocks; in the case of an exceptional situation (fatal
      error), they are all freed. The code for keeping this record is fairly primitive and not designed to consider
      allocation of many blocks (in the normal situation, allocation takes place from 2 to 6 times during file
      processing); this fact should be taken into account by developers trying to add new methods to LibRaw.
     


### Dynamic Memory Usage

LibRaw uses dynamic memory

for the decoded image;
for the decoded thumbnail;
for the ICC profile retrieved from the RAW file (if available);
for temporary data at the stage of RAW file unpacking;
for temporary data at the stage of postprocessing and result output;
for reading of the RAW source file (only under Win32).



#### Memory for the Decoded Image


      To simplify further processing, memory for the extracted RAW data is allocated with a fourfold (for Bayer sensor
      cameras) excess: for each pixel, four 16-bit components are available (three of them will be zero after
      RAW unpacking). Thus, one can perform debayer and other postprocessing actions directly in the same buffer as
      the one used for data extraction, but the required amount of memory becomes four times higher. 
Hence, the size of memory for the image buffer is 6-10 times greater than the size of the source RAW
        file. It is quite likely that allocation of this buffer in next versions of LibRaw will be more
        economical, under the condition that postprocessing calls inherited from dcraw will not be used..
    
The buffer for the decoded image is allocated upon calling unpack() and
      freed upon calling recycle().
    


#### Memory for the Decoded Thumbnail


      Memory for the thumbmail is allocated upon calling unpack_thumb() and freed upon
      calling recycle(). The size of the allocated buffer is precisely adjusted to the thumbnail size,
     i.e., up to several Mb. 
    


#### Memory for the Decoded ICC Profile


      Memory for the ICC profile is allocated upon calling  unpack_profile() and freed upon
      calling recycle(). The size of the allocated buffer is precisely adjusted to the ICC profile size,
     i.e., up to several hundred Kb. 
    


#### Memory for RAW Unpacking


      Memory for temporary buffer needed during RAW data unpacking may be allocated during the work of unpack() and freed before completion of this function. The sizes of the allocated
    buffers are small, up to tens of Kb. 
    


#### Memory for Postprocessing

During image postprocessing (inherited from dcraw), memory for the histogram (128 Kb) is allocated.
      This memory is allocated upon calling dcraw_document_mode_processing() and
      dcraw_process() and freed upon calling
      recycle().
    

      In addition, during the work of dcraw_process() and during the
   usage of some available possibilities, like
     

rotation of images from FUJI cameras;
correction of chromatic aberrations;
image size changes (including correction of non-square pixels);
highlight recovery;


     a temporary buffer with the size equal to the size of the resultant image (6-8 bytes per pixel for various processing stages)
 will be allocated. As soon as the intermediate substage of processing is completed, the buffer with the previous copy 
   of the image will be freed.
  If postprocessing is not used, then temporary buffers are not allocated.
    


#### Memory for File Writing


      Upon calling dcraw_ppm_tiff_writer(), memory for a single row of the
   output image is allocated. The allocated memory is freed before the end of this call. 
    


#### Unpacking into memory buffer


      Functons dcraw_make_mem_image() и 
      dcraw_make_mem_thumb() (and complementary calls in C-API)
      allocates memory for entire output datasets  (full RGB bitmap and thumbnail, respectively).
      Calling function should free() this memory themself.



## Incompatibilities with dcraw



### Processing of Thumbnails from Kodak cameras

In some Kodak cameras, the preview (thumbnail) is stored in the form of uncorrected image. During its extraction using
   dcraw -e, the white balance, color conversion, and other settings are the same as those used for extraction of the main RAW data
   (including defect removal and dark frame subtraction, which is erroneous, since the image size is different).
    
      In LibRaw::unpack_thumb() calls, the white balance taken from the camera ("as shot") is used and no settings from
     imgdata.params are considered.
    

      For all other cameras, thumbnails are extracted "as is," without any color conversions, both in dcraw and in LibRaw.
    
[back to Index]

LibRaw Team


Last modified: Sun Mar 28 22:08:30 MSD 2010



