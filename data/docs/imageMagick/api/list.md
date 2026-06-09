[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AppendImageToList](list.html#AppendImageToList) • [CloneImageList](list.html#CloneImageList) • [CloneImages](list.html#CloneImages) • [DeleteImageFromList](list.html#DeleteImageFromList) • [DeleteImages](list.html#DeleteImages) • [DestroyImageList](list.html#DestroyImageList) • [DuplicateImages](list.html#DuplicateImages) • [GetFirstImageInList](list.html#GetFirstImageInList) • [GetImageFromList](list.html#GetImageFromList) • [GetImageIndexInList](list.html#GetImageIndexInList) • [GetImageListLength](list.html#GetImageListLength) • [GetLastImageInList](list.html#GetLastImageInList) • [GetNextImageInList](list.html#GetNextImageInList) • [GetPreviousImageInList](list.html#GetPreviousImageInList) • [ImageListToArray](list.html#ImageListToArray) • [InsertImageInList](list.html#InsertImageInList) • [NewImageList](list.html#NewImageList) • [PrependImageToList](list.html#PrependImageToList) • [RemoveImageFromList](list.html#RemoveImageFromList) • [RemoveFirstImageFromList](list.html#RemoveFirstImageFromList) • [RemoveLastImageFromList](list.html#RemoveLastImageFromList) • [ReplaceImageInList](list.html#ReplaceImageInList) • [ReplaceImageInListReturnLast](list.html#ReplaceImageInListReturnLast) • [ReverseImageList](list.html#ReverseImageList) • [SpliceImageIntoList](list.html#SpliceImageIntoList) • [SplitImageList](list.html#SplitImageList)

## [AppendImageToList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

AppendImageToList() appends the second image list to the end of the first list. The given image list pointer is left unchanged, unless it was empty.

The format of the AppendImageToList method is:
    
    
    AppendImageToList(Image *images,const Image *image)
    

A description of each parameter follows:

    
    

images
    the image list to be appended to. 
    
image
    the appended image or image list. 
    

## [CloneImageList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

CloneImageList() returns a duplicate of the image list.

The format of the CloneImageList method is:
    
    
    Image *CloneImageList(const Image *images,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image list. 
    
exception
    return any errors or warnings in this structure. 
    

## [CloneImages](http://www.imagemagick.org/api/MagickCore/list_8c.html)

CloneImages() clones one or more images from an image sequence, using a comma separated list of image numbers or ranges.

The numbers start at 0 for the first image in the list, while negative numbers refer to images starting counting from the end of the range. Images may be refered to multiple times to clone them multiple times. Images refered beyond the available number of images in list are ignored.

Images referenced may be reversed, and results in a clone of those images also being made with a reversed order.

The format of the CloneImages method is:
    
    
    Image *CloneImages(const Image *images,const char *scenes,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
scenes
    This character string specifies which scenes to clone (e.g. 1,3-5,7-3,2). 
    
exception
    return any errors or warnings in this structure. 
    

## [DeleteImageFromList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

DeleteImageFromList() deletes an image from the list. List pointer is moved to the next image, if one is present. See RemoveImageFromList().

The format of the DeleteImageFromList method is:
    
    
    DeleteImageFromList(Image **images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [DeleteImages](http://www.imagemagick.org/api/MagickCore/list_8c.html)

DeleteImages() deletes one or more images from an image sequence, using a comma separated list of image numbers or ranges.

The numbers start at 0 for the first image, while negative numbers refer to images starting counting from the end of the range. Images may be refered to multiple times without problems. Image refered beyond the available number of images in list are ignored.

If the referenced images are in the reverse order, that range will be completely ignored, unlike CloneImages().

The format of the DeleteImages method is:
    
    
    DeleteImages(Image **images,const char *scenes,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
scenes
    This character string specifies which scenes to delete (e.g. 1,3-5,-2-6,2). 
    
exception
    return any errors or warnings in this structure. 
    

## [DestroyImageList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

DestroyImageList() destroys an image list.

The format of the DestroyImageList method is:
    
    
    Image *DestroyImageList(Image *image)
    

A description of each parameter follows:

    
    

image
    the image sequence. 
    

## [DuplicateImages](http://www.imagemagick.org/api/MagickCore/list_8c.html)

DuplicateImages() duplicates one or more images from an image sequence, using a count and a comma separated list of image numbers or ranges.

The numbers start at 0 for the first image, while negative numbers refer to images starting counting from the end of the range. Images may be refered to multiple times without problems. Image refered beyond the available number of images in list are ignored.

The format of the DuplicateImages method is:
    
    
    Image *DuplicateImages(Image *images,const size_t number_duplicates,
      const char *scenes,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

images
    the image sequence. 
    
number_duplicates
    duplicate the image sequence this number of times. 
    
scenes
    This character string specifies which scenes to duplicate (e.g. 1,3-5,-2-6,2). 
    
exception
    return any errors or warnings in this structure. 
    

## [GetFirstImageInList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

GetFirstImageInList() returns a pointer to the first image in the list.

The format of the GetFirstImageInList method is:
    
    
    Image *GetFirstImageInList(const Image *images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [GetImageFromList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

GetImageFromList() returns an image at the specified index from the image list. Starting with 0 as the first image in the list.

A negative offset will return the image from the end of the list, such that an index of -1 is the last image.

If no such image exists at the specified offset a NULL image pointer is returned. This will only happen if index is less that the negative of the list length, or larger than list length -1. EG: ( -N to N-1 )

The format of the GetImageFromList method is:
    
    
    Image *GetImageFromList(const Image *images,const ssize_t index)
    

A description of each parameter follows:

    
    

images
    the image list. 
    
index
    the position within the list. 
    

## [GetImageIndexInList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

GetImageIndexInList() returns the offset in the list of the specified image.

The format of the GetImageIndexInList method is:
    
    
    ssize_t GetImageIndexInList(const Image *images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [GetImageListLength](http://www.imagemagick.org/api/MagickCore/list_8c.html)

GetImageListLength() returns the length of the list (the number of images in the list).

The format of the GetImageListLength method is:
    
    
    size_t GetImageListLength(const Image *images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [GetLastImageInList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

GetLastImageInList() returns a pointer to the last image in the list.

The format of the GetLastImageInList method is:
    
    
    Image *GetLastImageInList(const Image *images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [GetNextImageInList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

GetNextImageInList() returns the next image in the list.

The format of the GetNextImageInList method is:
    
    
    Image *GetNextImageInList(const Image *images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [GetPreviousImageInList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

GetPreviousImageInList() returns the previous image in the list.

The format of the GetPreviousImageInList method is:
    
    
    Image *GetPreviousImageInList(const Image *images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [ImageListToArray](http://www.imagemagick.org/api/MagickCore/list_8c.html)

ImageListToArray() is a convenience method that converts an image list to a sequential array, with a NULL image pointer at the end of the array.

The images remain part of the original image list, with the array providing an alternative means of indexing the image array.

group = ImageListToArray(images, exception); while (i = 0; group[i] != (Image *) NULL; i++) printf("s\n", group[i]->filename); printf("d images\n", i); group = RelinquishMagickMemory(group);

The format of the ImageListToArray method is:
    
    
    Image **ImageListToArray(const Image *images,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

image
    the image list. 
    
exception
    return any errors or warnings in this structure. 
    

## [InsertImageInList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

InsertImageInList() insert the given image or image list, into the first image list, immediately AFTER the image pointed to. The given image list pointer is left unchanged unless previously empty.

The format of the InsertImageInList method is:
    
    
    InsertImageInList(Image **images,Image *insert)
    

A description of each parameter follows:

    
    

images
    the image list to insert into. 
    
insert
    the image list to insert. 
    

## [NewImageList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

NewImageList() creates an empty image list.

The format of the NewImageList method is:
    
    
    Image *NewImageList(void)
    

## [PrependImageToList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

PrependImageToList() prepends the image to the beginning of the list.

The format of the PrependImageToList method is:
    
    
    PrependImageToList(Image *images,Image *image)
    

A description of each parameter follows:

    
    

images
    the image list. 
    
image
    the image. 
    

## [RemoveImageFromList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

RemoveImageFromList() removes and returns the image pointed to.

The given image list pointer is set to point to the next image in list if it exists, otherwise it is set to the previous image, or NULL if list was emptied.

The format of the RemoveImageFromList method is:
    
    
    Image *RemoveImageFromList(Image **images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [RemoveFirstImageFromList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

RemoveFirstImageFromList() removes and returns the first image in the list.

If the given image list pointer pointed to the removed first image, it is set to the new first image of list, or NULL if list was emptied, otherwise it is left as is.

The format of the RemoveFirstImageFromList method is:
    
    
    Image *RemoveFirstImageFromList(Image **images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [RemoveLastImageFromList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

RemoveLastImageFromList() removes and returns the last image from the list.

If the given image list pointer pointed to the removed last image, it is set to the new last image of list, or NULL if list was emptied, otherwise it is left as is.

The format of the RemoveLastImageFromList method is:
    
    
    Image *RemoveLastImageFromList(Image **images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [ReplaceImageInList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

ReplaceImageInList() replaces an image in the list with the given image, or list of images. Old image is destroyed.

The images list pointer is set to point to the first image of the inserted list of images.

The format of the ReplaceImageInList method is:
    
    
    ReplaceImageInList(Image **images,Image *replace)
    

A description of each parameter follows:

    
    

images
    the list and pointer to image to replace 
    
replace
    the image or image list replacing the original 
    

## [ReplaceImageInListReturnLast](http://www.imagemagick.org/api/MagickCore/list_8c.html)

ReplaceImageInListReturnLast() is exactly as ReplaceImageInList() except the images pointer is set to the last image in the list of replacemen images.

This allows you to simply use GetNextImageInList() to go to the image that follows the just replaced image, even if a list of replacement images was inserted.

The format of the ReplaceImageInList method is:
    
    
    ReplaceImageInListReturnLast(Image **images,Image *replace)
    

A description of each parameter follows:

    
    

images
    the list and pointer to image to replace 
    
replace
    the image or image list replacing the original 
    

## [ReverseImageList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

ReverseImageList() reverses the order of an image list. The list pointer is reset to that start of the re-ordered list.

The format of the ReverseImageList method is:
    
    
    void ReverseImageList(Image **images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

## [SpliceImageIntoList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

SpliceImageIntoList() removes 'length' images from the list and replaces them with the specified splice. Removed images are returned.

The format of the SpliceImageIntoList method is:
    
    
    SpliceImageIntoList(Image **images,const size_t,
      const Image *splice)
    

A description of each parameter follows:

    
    

images
    the image list. 
    
length
    the length of the image list to remove. 
    
splice
    Replace the removed image list with this list. 
    

## [SplitImageList](http://www.imagemagick.org/api/MagickCore/list_8c.html)

SplitImageList() splits an image into two lists, after given image The list that was split off is returned, which may be empty.

The format of the SplitImageList method is:
    
    
    Image *SplitImageList(Image *images)
    

A description of each parameter follows:

    
    

images
    the image list. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](list.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
