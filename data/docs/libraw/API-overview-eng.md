


Overview of LibRaw API (C++)



[back to Index]

# Overview of LibRaw API (C++)


## General Remarks


The entire processing is carried out by an instance of the LibRaw class, which is an image processor.
One image processor can simultaneously process only one data source file, but consecutive processing of any number of files
is possible.
There may be several simultaneously working image processors in a software program (e.g., in different threads), although one
should remember that each image processor may require much memory.
Reading of source data from the RAW file requires virtually no customization (see API Notes for exceptions to this rule).
All data extracted from the RAW file are accessible through data fields of the image processor (LibRaw class instance).
Although LibRaw is not intended for RAW data postprocessing, the library includes calls that enable complete
emulation of the dcraw utility.
      All customization for the processing is performed via data fields of the LibRaw class.


## Brief Demonstration

 
      The example below contains no error processing for the sake of brevity.
    

```

#include "libraw/libraw.h"
int process_image(char *file)
{
        // Let us create an image processor
        LibRaw iProcessor;

        // Open the file and read the metadata
        iProcessor.open_file(file);

        // The metadata are accessible through data fields of the class
        printf("Image size: %d x %d\n",iProcessor.imgdata.sizes.width,iProcessor.imgdata.sizes.height);

        // Let us unpack the image
        iProcessor.unpack();

        // And let us print its dump; the data are accessible through data fields of the class
        for(i = 0;i lt; iProcessor.imgdata.sizes.iwidth *  iProcessor.imgdata.sizes.iheight; i++)
           printf("i=%d R=%d G=%d B=%d G2=%d\n",
                        i,
                        iProcessor.imgdata.image[i][0],
                        iProcessor.imgdata.image[i][1],
                        iProcessor.imgdata.image[i][2],
                        iProcessor.imgdata.image[i][3]
                );

        // Finally, let us free the image processor for work with the next image
        iProcessor.recycle();
}

```


