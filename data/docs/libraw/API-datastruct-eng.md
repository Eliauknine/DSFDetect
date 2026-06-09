


LibRaw: Data Structures and Constants



[back to Index]

# LibRaw: Data Structures and Constants


      LibRaw data structures are defined in header file libraw/libraw_types.h
      Constants used in its work are defined in file libraw/libraw_const.h
    






## Data Structures



### libraw_data_t: Main Data Structure of LibRaw


      Structure libraw_data_t is a "wrapping" for data structures accessible to the user of the library.
      When one uses C++ API, it is accessible as LibRaw::imgdata (class_instance.imgdata). The data in this structure appear after
      a file is opened through open_file (and other open_ calls), except for the image itself (filled by unpack()) and data containing
the preview information (filled by calling unpack_thumb()).
     Data fields:
    


**unsigned int                progress_flags;**
: This field records the pastphases of image processing.

**unsigned int                progress_flags;**
: This field recordssuspicious situations (warnings)that have emerged during image processing.

**libraw_iparams_t            idata;**
: The structure describes the main image parameters retrieved from the RAW file. Fields of this structure 
are described in detailbelow.

**libraw_image_sizes_t        sizes;**
: The structure describes the geometrical parameters of the image. Fields of this structure
 are described in detailbelow.

**libraw_colordata_t          color;**
: The structure contains color data retrieved from the file. Fields of this structure
are described in detailbelow.

**libraw_imgother_t           other;**
: Data structure for information purposes: it contains the image parameters that have been extracted from the file but are
not needed in further file processing. Fields of this structure are described in detailbelow.

**libraw_thumbnail_t          thumbnail;**
: Data structure containing information on the preview and the preview data themselves. All fields of this
        structure but thumbnail itself are filled when open_file() is called. Thumbnail readed by unpack_thumb() call.
        The fields are described in detailbelow.

**libraw_masked_t             masked_pixels;**
: Structure containing pixel data for black (masked) border pixels.
        Fields of this structure are describedbelow. It is filled
        when unpack() is called.

**ushort                      (*image)[4];**
: The memory area that contains the image pixels per se. It is filled when unpack() is called.

**libraw_output_params_t     params;**
: Data structure intended for management of image postprocessing (using the dcraw emulator).
Fields of this structure are described in detailbelow.




###  Structure libraw_iparams_t: Main Parameters of the Image





**char        make[64];**
: Camera manufacturer.

**char        model[64];**
: Camera model.

**unsigned    raw_count;**
: Number of  RAW images in file (0 means that the file has not been recognized).

**unsigned    dng_version;**
: DNG version (for the DNG format).

**int         colors;**
: Number of colors in the file.

**unsigned    filters;**
: Bit mask describing the order of color pixels in the matrix (0 for full-color images). 32 bits of this field describe 16 pixels
(8 rows with two pixels in each, from left to right and from top to bottom). Each two bits have values 0 to 3, which
correspond to four possible colors. Convenient work with this field is ensured by the COLOR(row,column) function,
which returns the number of the active color for a given pixel.

**char        cdesc[5];**
: Description of colors numbered from 0 to 3 (RGBG,RGBE,GMCY, or GBTG).




### Structure libraw_image_sizes_t: Image Dimensions

Structure libraw_image_sizes_t is a collection of all file data that describe the size of the image.
      Data fields: 
      


**ushort    raw_height, raw_width;**
: Full size of RAW image (including the frame) in pixels.

**ushort    height, width;**
: Size of visible ("meaningful") part of the image (without the frame).

**ushort    top_margin, left_margin;**
: Coordinates of the top left corner of the frame (the second corner is calculated from the full size of the image and size of its visible part).

**ushort    bottom_margin, right_margin;**
: Width (in pixels) of bottom and right part of masked pixels area.

**ushort      iheight, iwidth;**
: Size of the output image (may differ from height/width for cameras that require image rotation or have non-square pixels).

**double      pixel_aspect;**
: Pixel width/height ratio. If it is not unity, scaling of the image along one of the axes is required during output.

**int         flip;**
: Image orientation (0 if does not require rotation; 3 if requires 180-deg rotation; 5 if 90 deg counterclockwise, 6 if 90 deg clockwise).




### Structure libraw_colordata_t: Color Information

Structure libraw_colordata_t unites all color data, both retrieved from the RAW file and calculated on the basis of the
image itself. For different cameras, there are different ways of color handling.     
     Data fields:
    


**color_data_state_t   color_flags;**
: Data structure describing the sources of color data. Describedbelowin more detail.

**ushort      white[8][8];**
: Block of white pixels extracted from files CIFF/CRW. Not extracted for other formats. Used to calculate white
balance coefficients.

**float       cam_xyz[4][3];**
: Camera RGB - XYZ conversion matrix. This matrix is constant (different for different models).
        Last row is zero for RGB cameras and non-zero for different color models (CMYG and so on).

**float       cam_mul[4];**
: White balance coefficients (as shot). Either read from file or calculated.

**float       pre_mul[4];**
: White balance coefficients for daylight (daylight balance). Either read from file, or calculated on the basis of file data, 
or taken from hardcoded constants.

**float       cmatrix[3][4];**
: White balance matrix. Read from file for some cameras, calculated for others.

**float       rgb_cam[3][4];**
: Another white balance matrix, read from file for Leaf and Kodak cameras.

**ushort      curve[0x4001];**
: Camera tone curve, read from file for Nikon, Sony and some other cameras.

**unsigned    black;**
: Black level. Depending on the camera, it may be zero (this means that black has been subtracted at the unpacking stage 
or by the camera itself), calculated at the unpacking stage, read from the RAW file, or hardcoded.

**unsigned    cblack[8];**
: Per-channel black level. Items 0-3 are black pixels values (averaged), items 4-7 are per-channel counts.

**unsigned    maximum;**
: Maximum pixel value. Calculated from the data for most cameras, hardcoded for others. 
        This value may be changed on postprocessing stage (when black subtraction performed) and by 
        automated maximum adjustment (this adjustment performed ifparams.adjust_maximum_thris set to nonzero).

**unsigned    channel_maximum[4];**
: Per channel maximum pixel value. Calculated from RAW data on unpack stage.

**ph1_t       phase_one_data;**
: Color data block that is read for Phase One cameras.

**float       flash_used;**
: Fields used for white balance calculations (for some P&S Canon cameras).

**float       canon_ev;**
: Fields used for white balance calculations (for some P&S Canon cameras).

**char          model2[64];**
: Firmware revision (for some cameras).

**void    *profile;**
: Pointer to the retrieved ICC profile (if it is present in the RAW file).

**unsigned    profile_length;**
: Length of ICC profile in bytes.




### Structure  color_data_state_t: Description of Color Data Source

This structure (actually, a bit field) describes the source of color data for each field of structure libraw_colordata_t, which may be obtained from different data sources.
      Data fields:
    

```

        unsigned curve_state        : 3;
        unsigned rgb_cam_state      : 3;
        unsigned cmatrix_state      : 3;
        unsigned pre_mul_state      : 3;
        unsigned cam_mul_state      : 3;
    
```


   Each field assumes one of the values that are possible for enum LibRaw_colorstate. 
    


### Structure  libraw_imgother_t: Other Parameters of the Image


      Structure libraw_imgother_t is a collection of data that have been read from the RAW file but are not needed for image postprocessing.
      Data fields:
    


**float       iso_speed;**
: ISO sensitivity.

**float       shutter;**
: Shutter speed.

**float       aperture;**
: Aperture.

**float       focal_len;**
: Focal length.

**time_t      timestamp;**
: Date of shooting.

**unsigned    shot_order;**
: Serial number of image.

**unsigned    gpsdata[32];**
: GPS data.

**char        desc[512];**
: Image description.

**char          artist[64];**
: Author of image.




### Structure libraw_thumbnail_t: Description of Thumbnail

Structure libraw_thumbnail_t describes all parameters associated with the preview saved in the RAW file.
      Data fields:
    


**LibRaw_thumbnail_formats tformat;**
: Thumbnail data format. One of the values among enumLibRaw_thumbnail_formats.

**ushort      twidth, theight;**
: Dimensions of the preview image in pixels.

**unsigned    tlength;**
: Thumbnail length in bytes.

**int         tcolors;**
: Number of colors in the preview.

**char       *thumb;**
: Pointer to thumbmail, extracted from the data file.




### Structure libraw_output_params_t: Management of dcraw-Style Postprocessing

Structure libraw_output_params_t is used for management of dcraw-compatible calls dcraw_process(),
      dcraw_ppm_tiff_writer(), dcraw_thumb_writer(), and dcraw_document_mode_processing(). Fields of this structure
correspond to command line keys of dcraw.
      Data fields:
    


**unsigned    greybox[4];**
: dcraw keys:-A  x y w h4 numbers corresponding to the coordinates (in pixels) of the rectangle that is used to calculate the white
        balance. X and Y are coordinates of the left-top rectangle corner; w and h are the rectangle's width and
        height, respectively.

**unsigned    cropbox[4];**
: Ключи dcraw:нетThis field sets the image cropping rectangle. Cropbox[0] and cropbox[1] are the rectangle's top-left
        corner coordinates, remaining two values are width and height respectively. All coordinates are
        applied before any image rotation.

**double      aber[4];**
: dcraw keys:-CCorrection of chromatic aberrations; the only specified values areaber[0], the red multiplieraber[2], the green multiplier.
        For some formats, it affectsRAW data reading, since correction of aberrations
changes the output size.

**double      gamm[6];**
: dcraw keys:-g power toe_slopeSets user gamma-curve. Library user should set first two fields of gamm array:gamm[0] -invertedgamma value)gamm[1] - slope for linear part (so called toe slope). Set to zero for simple power curve.Remaining 4 values are filled automatically.By default settings for rec. BT.709 are used: power 2.222 (i.e. gamm[0]=1/2.222) and slope 4.5. 
          For sRGB curve use gamm[0]=1/2.4 and gamm[1]=12.92, for linear curve set gamm[0]/gamm[1] to 1.0.

**float       user_mul[4];**
: dcraw keys:-r mul0 mul1 mul2 mul34 multipliers (r,g,b,g) of the user's white balance.

**unsigned    shot_select, multi_out;**
: dcraw keys:-sSelection of image number for processing (for formats that contain several RAW images in one file). The
        multi_out ( -s all) mode should be programmed by the user, since dcraw_process() does not support it.

**float       bright;**
: dcraw keys:-bBrightness (default 1.0).

**float       threshold;**
: dcraw keys:-nParameter for noise reduction through wavelet denoising.

**int         half_size;**
: dcraw keys:-hOutputs the image in 50% size. For some formats, it affectsRAW data reading.

**int         four_color_rgb;**
: dcraw keys:-fSwitches on separate interpolations for two green components.

**int         document_mode;**
: dcraw keys:-d/-D0: standard processing (with white balance)1: corresponds to -d (without color processing or debayer)2: corresponds to -D (-d without white balance).

**int         highlight;**
: dcraw keys:-H0-9: Highlight mode (0=clip, 1=unclip, 2=blend, 3+=rebuild).

**int         use_auto_wb;**
: dcraw keys:-aUse automatic white balance obtained after averaging over the entire image.

**int         use_camera_wb;**
: dcraw keys:-wIf possible, use the white balance from the camera.

**int         use_camera_matrix;**
: dcraw keys:+M/-MUse (1)/don't use camera color matrix.

**int         output_color;**
: dcraw keys:-o[0-5]  Output colorspace (raw, sRGB, Adobe, Wide, ProPhoto, XYZ).

**char*         output_profile;**
: dcraw keys:-o filenamePath to output profile ICC file (used only if LibRaw compiled with LCMS support)

**char*         camera_profile;**
: dcraw keys:-o filePath to input (camera) profile ICC file (or 'embed' for embedded profile). Used only if LCMS support compiled in.

**char*         bad_pixels;**
: dcraw keys:-P filePath to file with bad pixels map (in dcraw format: "column row date-of-pixel-death-in-UNIX-format", one pixel
        per row).

**char*         dark_frame;**
: dcraw keys:-K filePath to dark frame file (in 16-bit PGM format)

**enum LibRaw_filtering  filtering_mode;**
: dcraw keys:noneSets RAW data filtering mode (black level subtraction, zero pixels cleaning, tone curve processing)
        See details infiltration modes descriptionand inmode list below.

**int         output_bps;**
: dcraw keys:-48 bit (default)/16 bit (key -4).

**int         output_tiff;**
: dcraw keys:-T0/1: output PPM/TIFF.

**int         user_flip;**
: dcraw keys:-t[0-7]  Flip image (0=none, 3=180, 5=90CCW, 6=90CW).
        Default -1, which means taking the corresponding value from RAW.For some formats,affects RAW data reading, e.g., unpacking of thumbnails
      from Kodak cameras.

**int         user_qual;**
: dcraw keys:-q0-3: interpolation quality (0 - linear, 1- VNG, 2 - PPG, 3 - AHD).

**int         user_black;**
: dcraw keys:-kUser black level.

**int         user_sat;**
: dcraw keys:-SSaturation adjustment.

**int         med_passes;**
: dcraw keys:-mNumber of median filter passes.

**int         no_auto_bright;**
: dcraw keys:-WDon't use automatic increase of brightness by histogram.

**float         auto_bright_thr;**
: dcraw keys:nonePortion of clipped pixels when auto brighness increase is used. Default value is 0.01 (1%) for dcraw
        compatibility. Recommended value for modern low-noise multimegapixel cameras depends on shooting style. Values
        in 0.001-0.00003 range looks reasonable.

**float         adjust_maximum_thr;**
: dcraw keys:noneThis parameters controls auto-adjusting of maximum value based on channel_maximum[] data, calculated from
        real frame data. If calculated maximum is greater than adjust_maximum_thr*maximum, than maximum is
        set to calculated_maximum.Default: 0.75. If you set this value above 0.99999, than default value will be used. If you set
        this value below 0.00001, than no maximum adjustment will be performed.Adjusting maximum should not damage any picture (esp. if you use default value) and is very useful for 
        correcting channel overflow problems (magenta clouds on landscape shots, green-blue highlights for
        indoor shots).

**int         use_fuji_rotate;**
: dcraw keys:-jDefault -1 (use), 0 - don't use rotation for cameras on a Fuji sensor.

**char        *bpfile;**
: dcraw keys:-PName of file with bad pixel map.

**char        *dark_frame;**
: dcraw keys:-KName of file with dark frame.

**int         green_matching;**
: Turns on fixing of green channels disbalance.dcraw keys:noneDefault:  0 (not use), 1 - turns on this postprocessing stage. green_matching requires additional memory for
        image data.




### Structure libraw_masked_t - saved masked pixels (black frame) data


      Structure libraw_masked_t designed for storing pixel data for dark frame (black or masked pixels, not included
      in active image sensor area). These pixel values can be used for black level subtraction, noise and banding
      removal and so on.
      Unlike imgdata.image bitmap which has 4-component pixels, masked pixel data stored in 1-component 16-bit values.
      Different parts of border are stored in different buffers within libraw_masked_t structure, see picture:
    


      Data fields:
    


**ushort  *buffer;**
: Whole allocated buffer. Buffer size is (raw_width*raw_height - width*height).

**ushort  *tl;**
: Pointer to part of buffer designated for storing top-left corner of black frame.
        Data size equal to (top_margin*left_margin).

**ushort  *top;**
: Pointer to part of buffer for storing top part of black frame. Size is (top_margin*width).

**ushort  *tr;**
: Pointer to right top corned data. Size is (top_margin*right_margin).

**ushort  *left;**
: Pointer to pixel data of left frame side. (left_margin*height) pixels.

**ushort  *right;**
: Right side of frame. (right_margin*height) pixels.

**ushort  *bl;**
: Bottom left corner of frame. (bottom_margin*left_margin) pixels.

**ushort  *bottom;**
: Bottom side of frame. Pixel count is (bottom_margin*width).

**ushort  *br;**
: Bottom right corner with (bottom_margin*right_margin) pixels.


Some cameras does not provide dark frame data. In this case buffer for frame data is not allocated and
      all pointers are initialized to zero.
      Also, structure data is not allocated if image is extracted into half-sized bitmap (i.e. if half_size,
      wavelet threshold or aber[] fields is set in processing options).
      Some cameras provides not full masked frame, but only several sides of it (only left and top for Canons, only
      left and right for some Nikons and so on). In this case all structure fields are initialized, but allocated
      size for this part of frame is equal to zero and corresponding size parameter (top_/left_/bottom_/right_margin)
      is set too zero too.
    


### Stucture libraw_processed_image_t - result set for  dcraw_make_mem_image()/dcraw_make_mem_thumb() functions

Structure libraw_processed_image_t is produced by call of dcraw_make_mem_image()/dcraw_make_mem_thumb() and contains
      in-memory image of interpolated data or thumbnail.
      Data fields:
    


**LibRaw_image_formats type**
: This field records type of data, containing in remaining fields of structure.LIBRAW_IMAGE_BITMAP- structure contains RGB bitmap. All metadata fields (see below) are valid
            and describes image data.LIBRAW_IMAGE_JPEG- structure contain in-memory image of JPEG file. Only type, data_size and
            data fields are valid (and nonzero);

**ushort height,width**
: Image size (in pixels). Valid only if  type==LIBRAW_IMAGE_BITMAP.

**ushort colors, bits**
: Number of colors components (1 or 3) and color depth in bits (8 or 16). These fields are valid only  if
        type==LIBRAW_IMAGE_BITMAP.

**ushort gamma_corrected**
: Is bitmap data gamma-corrected (always 1 for 8-bit data, may be 0 or 1 for 16-bit).
        Valid only if  type==LIBRAW_IMAGE_BITMAP.

**unsigned int data_size**
: Size ofdatafield (in bytes). For bitmap image equal to (height*width*colors * (bits/8)). 
        For JPEG image - exact JPEG size (i.e. extracted  thnumbnail size + JPEG header + EXIF header).

**unsigned char data[]**
: Data array itself. Should be interpreted as RGB triplets for bitmap type and as JPEG file for JPEG type.




## Input abstraction layer


      RAW data input (read) in LibRaw implemented by calling methods of object derived from 
      LibRaw_abstract_datastream abstract class. Full list of methods is described in 
        href="API-CXX-eng.html#datastream">C++ API reference. 
    

      There is two ready to use implementations of datastream objects:
    

LibRaw_file_datastream - file input (filename provided 
        to LibRaw).
LibRaw_buffer_datastream - input from memory buffer.


      LibRaw user can create own datastream object derived from 
      LibRaw_abstract_datastream. For example, such object may
      implement reading RAW data directly from camera (by remote interface). LibRaw can use these
      objects via 
      LibRaw::open_datastream() interface.
    

      Datastreams can be used either via 
      LibRaw::open_datastream() call (in this case datastream
      object should be created an maintained by user) or via 
      LibRaw::open_file() and
      LibRaw::open_buffer() shortcuts.
    

      Only C++ API users may use object-oriented interface and
      implement own input interfaces. For C API users only
      built-on libraw_open_file()/libraw_open_buffer() shortcuts are avaliable.
    


### Data fields

Definition:

```

class LibRaw_abstract_datastream {
...
protected:
    LibRaw_abstract_datastream *substream;
}

```

Description:
      Ojects derived from LibRaw_abstract_datastream always contains pointer to secondary data stream
      (substream). This substream initialized internally when needed (really used only for Sony RAW data) and
      used for temporary switch input stream to temporary memory buffer allocated internally in LibRaw.
    

      Substream usage details described more precisely in 
      own datastream objects creation guide.
    


## Constants



### enum LibRaw_errors: Error Codes

All functions returning integer numbers must return either errno or one of the following error codes (see also error code conventions).
Fatal errors (return of such an error code implies that file processing has to be terminated, since
the state of data structures is unknown).


**LIBRAW_UNSUFFICIENT_MEMORY**
: Attempt to get memory from the system has failed.All allocated resources will be freed,recycle()will be called, and the LibRaw 
object will be brought to the state "right after creation."

**LIBRAW_DATA_ERROR**
: A fatal error emerged during data unpacking.All allocated resources will be freed,recycle()will be called, and the LibRaw 
object will be brought to the state "right after creation."

**LIBRAW_IO_ERROR**
: A fatal error emerged during file reading (premature end-of-file encountered or file is corrupt).All allocated resources will be freed,recycle()will be called, and the LibRaw 
object will be brought to the state "right after creation."

**LIBRAW_CANCELLED_BY_CALLBACK**
: Processing cancelled due to calling application demand (by returning nonzero code fromprogress callback).All allocated resources will be freed,recycle()will be called, and
        the LibRaw  object will be brought to the state "right after creation."

**LIBRAW_BAD_CROP**
: The incorrect cropping coordinates are set via params.cropbox[]: the left-top corner of cropping
        rectangle is outside the image. 
        The processing will be cancelled, all allocated resources will be freed,recycle()will be called, and the LibRaw  object will be brought to the
        state "right after creation."


Non-Fatal Errors


**LIBRAW_SUCCESS=0**
: No error; function terminated successfully.

**LIBRAW_UNSPECIFIED_ERROR**
: An unknown error has been encountered. This code should never be generated.

**LIBRAW_FILE_UNSUPPORTED**
: Unsupported file format (attempt to open a RAW file with a format unknown to the program).

**LIBRAW_REQUEST_FOR_NONEXISTENT_IMAGE**
: Attempt to retrieve a RAW image with a number absent in the data file (only for formats supporting storage
      of several images in a file).

**LIBRAW_OUT_OF_ORDER_CALL**
: API functions have been called in wrong order (e.g.,unpack()beforeopen_file()) or the previous stage has ended with an error (e.g.,unpack()is called afteropen_file()has returned an error).

**LIBRAW_NO_THUMBNAIL**
: Returned upon an attempt to retrieve a thumbnail from a file containing no preview.

**LIBRAW_UNSUPPORTED_THUMBNAIL**
: RAW file contains a preview of unsupported format.




### enum LibRaw_progress: Current State of LibRaw Object

LibRaw::imgdata.progress_flags contains a bit mask describing all stages of file processing that have already been performed.
    
File opening and RAW data extraction phase.


**LIBRAW_PROGRESS_START=0**
: Object just created, no processing carried out.

**LIBRAW_PROGRESS_OPEN**
: File to be processed has been opened.

**LIBRAW_PROGRESS_IDENTIFY**
: Data identification performed, format recognized, metadata extracted.

**LIBRAW_PROGRESS_SIZE_ADJUST**
: Data sizes adjusted (for files that require such adjustment, namely, certain files from Kodak cameras).

**LIBRAW_PROGRESS_LOAD_RAW**
: RAW data loaded.


The following flags are set during usage of image processing that has been taken from dcraw.


**LIBRAW_PROGRESS_REMOVE_ZEROES**
: Zero values removed for cameras that require such removal (Panasonic cameras).

**LIBRAW_PROGRESS_BAD_PIXELS**
: Bad (dead) pixels removed.

**LIBRAW_PROGRESS_DARK_FRAME**
: Dark frame subtracted from RAW data.

**LIBRAW_PROGRESS_SCALE_COLORS**
: White balance performed.

**LIBRAW_PROGRESS_PRE_INTERPOLATE**
: Image size reduction (for the half_size mode) performed, as well as copying of 2nd green channel to the 1st one in points
    where the second channel is present and the first one is absent.

**LIBRAW_PROGRESS_INTERPOLATE**
: Interpolation (debayer) performed.

**LIBRAW_PROGRESS_MIX_GREEN**
: Averaging of green channels performed.

**LIBRAW_PROGRESS_MEDIAN_FILTER**
: Median filtration performed.

**LIBRAW_PROGRESS_HIGHLIGHTS**
: Work with highlights performed.

**LIBRAW_PROGRESS_FUJI_ROTATE**
: For images from Fuji cameras, rotation performed (or adjust_sizes_info_only() called).

**LIBRAW_PROGRESS_FLIP**
: Dimensions recalculated for images shot with a rotated camera (sizes.iwidth/sizes.iheight swapped).

**LIBRAW_PROGRESS_CONVERT_RGB**
: Conversion into output RGB space performed.

**LIBRAW_PROGRESS_STRETCH**
: Image dimensions changed for cameras with non-square pixels.

**LIBRAW_PROGRESS_STAGE17 - LIBRAW_PROGRESS_STAGE27**
: Reserved for possible appearance of other processing stages.


The following flags are set during loading of thumbnails.
LIBRAW_PROGRESS_THUMB_LOAD

        Thumbnail data have been loaded (for Kodak cameras, the necessary conversions have also been made).
      
LIBRAW_PROGRESS_TRESERVED1 - LIBRAW_PROGRESS_TRESERVED3

        Reserved for possible future processing stages.
      



### enum LibRaw_thumbnail_formats: Thumbnail Data Formats

Thumbnail data format is written in the imgdata.thumbnail.tformat data field.
      Presently LibRaw knows about four thumbnail formats, among which two are unpacked:
    


**LIBRAW_THUMBNAIL_UNKNOWN**
: Format unknown or thumbnail  not yet read.

**LIBRAW_THUMBNAIL_JPEG**
: The thumbnail buffer contains a JPEG file (read from the RAW file "as is," without any manipulations performed on it).

**LIBRAW_THUMBNAIL_BITMAP**
: The thumbnail buffer contains the gamma-adjusted RGB bitmap (for Kodak cameras, the gamma correction is performed with allowance
       for maximum values and the white balance is set in accordance with the camera settings).In this format, each pixel of the image is represented by a 8-bit RGB triplet.

**LIBRAW_THUMBNAIL_LAYER**
: Data format is presently recognized upon opening of RAW file but not supported: not unpacked into LibRaw::unpack_thumb.

**LIBRAW_THUMBNAIL_ROLLEI**
: Data format is presently recognized upon opening of RAW file but not supported: not unpacked into LibRaw::unpack_thumb.




### Nonstandard Situations (Warnings) during RAW Data Processing

Some suspicious situations emerging during image processing are not fatal but may affect the result of data
retrieval or postprocessing. Such states are indicated by setting a bit in the imgdata.process_warnings field.


**LIBRAW_WARN_BAD_CAMERA_WB**
: Postprocessing must use white balance of the camera but this balance is not suitable for use.

**LIBRAW_WARN_NO_METADATA**
: Only for cameras where the metadata are taken from an external JPEG file: metadata extraction has failed.

**LIBRAW_WARN_NO_JPEGLIB**
: Only for P&S Kodak cameras: data in JPEG format. At the same time, open_file() will return LIBRAW_FILE_UNSUPPORTED.

**LIBRAW_WARN_NO_EMBEDDED_PROFILE**
: (only if LCMS support compiled in).
        Caller set embedded input profile use, but no such profile exists in RAW.

**LIBRAW_WARN_NO_INPUT_PROFILE**
: (only if LCMS support compiled in).
        Error when opening input profile ICC file.

**LIBRAW_WARN_BAD_OUTPUT_PROFILE**
: (only if LCMS support compiled in).
        Error when opening output profile ICC file.

**LIBRAW_WARN_NO_BADPIXELMAP**
: Error when opening bad pixels map file.

**LIBRAW_WARN_BAD_DARKFRAME_FILE**
: Error when opening dark frame file.

**LIBRAW_WARN_BAD_DARKFRAME_DIM**
: Dark frame file either differs in dimensions from RAW-file processed, or have wrong format.
        Dark frame should be in 16-bit PGM format (one can generate it using simple_dcraw -4 -D).




### enum LibRaw_filtering - RAW data filtering settings


      This enum describes possible RAW data filtration modes during data unpacking and postprocessing.
      Usage recommendations are described in API comments. 
      Filtering mode should be set by altering filtering_mode option before 
      unpack() is called.
    


**LIBRAW_FILTERING_DEFAULT**
: Default value: dcraw filtration mode (for compatibility with previous LibRaw versions without
        data filtering options).

**LIBRAW_FILTERING_NOZEROES**
: If this bit set, then zero values in RAW data will not be cleared (averaged). Zero averaging
        is needed for some cameras, such as Point-and-Shot Canon cameras, Panasonic cameras and some other.

**LIBRAW_FILTERING_NORAWCURVE**
: This bit turns off tone curve processing (for tone curves read from file metadata or calculated from
        constants). This setting is supported only for bayer-pattern cameras with tone curve;

**LIBRAW_FILTERING_NONE**
: Equal to  (LIBRAW_FILTERING_NOZEROES|LIBRAW_FILTERING_NORAWCURVE)

**LIBRAW_FILTERING_LIBRAWOWN**
: This bit turns on LibRaw specialized functions for data filtering. These funcions will be made
        individually for each camera model (and, possibly, firmware version). For now, no such subroutines
        ready, so this parameter is reserved for future.

**LIBRAW_FILTERING_AUTOMATIC**
: Equals to LIBRAW_FILTERING_LIBRAWOWN with fallback to LIBRAW_FILTERING_DEFAULT if no
        specialized filtering function exists for given camera.

**LIBRAW_FILTERING_AUTOMATIC_BIT**
: This bit reserved for LIBRAW_FILTERING_AUTOMATIC support.



      Best possible setting for common RAW-processing software is LIBRAW_FILTERING_AUTOMATIC. 
      For RAW analyzers we recommend use LIBRAW_FILTERING_NONE.
    


### enum LibRaw_colorstate:  Types of Color Data Source

For each type of retrieved color information (see above for description of structure imgdata.color.color_flags), the
data source is recorded. The possible values are listed below. 
    


**LIBRAW_COLORSTATE_UNKNOWN**
: Data source unknown.

**LIBRAW_COLORSTATE_INIT**
: Data field initialized by default (the same value for all cameras) before opening the RAW file.

**LIBRAW_COLORSTATE_CONST**
: Data source is a hardcoded constant.

**LIBRAW_COLORSTATE_LOADED**
: Data loaded from RAW file.

**LIBRAW_COLORSTATE_CALCULATED**
: Data calculated on the basis of RAW data.

**LIBRAW_COLORSTATE_RESERVED1-LIBRAW_COLORSTATE_RESERVED3**
: Reserved.




### enum LibRaw_image_formats - possible types of data, contains in  libraw_processed_image_t structure

type field of  libraw_processed_image_t structure may have one of these values:
      


**LIBRAW_IMAGE_BITMAP**
: The structure contains RGB-bitmap, metadata described in other fields of  libraw_processed_image_t.

**LIBRAW_IMAGE_JPEG**
: libraw_processed_image_t structure contains JPEG image (in memory). Only data_size field is meaningful.


[back to Index]

LibRaw Team


Last modified: Sun Sep  5 18:25:49 MSD 2010



