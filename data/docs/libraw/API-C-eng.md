


LibRaw: C API



[back to Index]

# LibRaw: C API

LibRaw C API is a wrapper around C++ API; therefore, virtually all documentation to C 
      API functions  is represented by a set of hyperlinks to the corresponding places in the description of C++ API.
    
Contents

Initialization:  libraw_data_t       *libraw_init(unsigned int flags);
Returned values
Data loading
Auxiliary Functions
Data Postprocessing, Emulation of dcraw Behavior

Setting of Parameters
Emulation of dcraw Behavior


Writing to Output Files
Writing processing results to memory buffer



## Initialization:  libraw_data_t       *libraw_init(unsigned int flags);


      The function returns the pointer to the instance of
        libraw_data_t structure.
      The resultant pointer should be passed as the first argument to all C API functions (except for libraw_strerror).
    
Returns NULL in case of error, pointer to the structure in all other cases.


## Returned values

Functions of C API return EINVAL (see errno.h) if the null pointer was passed to them as the first argument. 
In all other cases, the C++ API return code is returned.
    


## Data Loading from a File



**int libraw_open_file(libraw_data_t*, const char *)**
: SeeLibRaw::open_file()

**int libraw_open_file_ex(libraw_data_t*, const char *,INT64 bigfile_size)**
: SeeLibRaw::open_file()

**int libraw_open_buffer(libraw_data_t*, void *buffer, size_t bufsize)**
: SeeLibRaw::open_buffer()

**int                 libraw_unpack(libraw_data_t*);**
: SeeLibRaw::unpack()

**int                 libraw_unpack_thumb(libraw_data_t*);**
: SeeLibRaw::unpack_thumb()




## Auxiliary Functions



**const char* libraw_version()**
: SeeLibRaw::version()

**const char* libraw_versionNumber()**
: SeeLibRaw::versionNumber()

**bool LIBRAW_CHECK_VERSION(major,minor,patch)**
: SeeLIBRAW_CHECK_VERSIONв описании C++ API

**int libraw_cameraCount()**
: SeeLibRaw::cameraCount()

**int libraw_cameraList()**
: SeeLibRaw::cameraList()

**void                libraw_unpack_function_name(libraw_data_t*);**
: SeeLibRaw::unpack_function_name()

**void                libraw_subtract_black(libraw_data_t*);**
: SeeLibRaw::subtract_black()

**void                libraw_add_masked_borders_to_bitmap(libraw_data_t*);**
: SeeLibRaw::add_masked_borders_to_bitmap()

**void                libraw_rotate_fuji_raw(libraw_data_t*);**
: SeeLibRaw::rotate_fuji_raw()

**void                libraw_recycle(libraw_data_t*);**
: SeeLibRaw::recycle()

**void                libraw_close(libraw_data_t*);**
: SeeLibRaw::~LibRaw()

**const char          *libraw_strerror(int errorcode);**
: SeeLibRaw::strerror

**const char          *libraw_strprogress(enum LibRaw_progress);**
: SeeLibRaw::strprogress

**void                libraw_set_memerror_handler(libraw_data_t*, memory_callback cb);**
: SeeLibRaw::set_memerror_handler()

**void                libraw_set_dataerror_handler(libraw_data_t*,data_callback func);**
: SeeLibRaw::set_dataerror_handler()

**void                libraw_set_progress_handler(libraw_data_t*,progress_callback func);**
: SeeLibRaw::set_progress_handler()




## Data Postprocessing, Emulation of dcraw Behavior



### Setting of Parameters


      The postprocessing parameters for the calls described below are set, just as for C++ API, via setting of fields in the
      libraw_output_params_t structure:
    

```

 libraw_data_t *ptr = libraw_init(0);
 ptr->params.output_tiff = 1; //  output to TIFF
    
```


    Fields of this structure are described in the documentation to
      libraw_output_params_t. For notes on their use, see API notes.
    


### Emulation of dcraw Behavior



**int                 libraw_adjust_sizes_info_only(libraw_data_t*);**
: SeeLibRaw::adjust_sizes_info_only()

**int                 libraw_dcraw_document_mode_processing(libraw_data_t*);**
: SeeLibRaw::dcraw_document_mode_processing()

**int                 libraw_dcraw_process(libraw_data_t* lr);**
: SeeLibRaw::dcraw_process()



## Writing to Output Files



**int                 libraw_dcraw_ppm_tiff_writer(libraw_data_t* lr,const char *filename);**
: SeeLibRaw::dcraw_ppm_tiff_writer()

**int                 libraw_dcraw_thumb_writer(libraw_data_t* lr,const char *fname);**
: SeeLibRaw::dcraw_thumb_writer()



## Writing processing results to memory buffer



**libraw_processed_image_t *libraw_dcraw_make_mem_image(libraw_data_t* lr,int * errcode)**
: SeeLibRaw::dcraw_make_mem_image()

**libraw_processed_image_t *libraw_dcraw_make_mem_thumb(libraw_data_t* lr,int * errcode)**
: SeeLibRaw::dcraw_make_mem_thumb()






