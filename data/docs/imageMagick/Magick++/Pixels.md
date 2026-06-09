# Magick::Pixels

The _Pixels_ class provides efficient access to raw image pixels. Image pixels (of type [_PixelPacket_](PixelPacket.html)) may be accessed directly via the _Image Pixel Cache_. The image pixel cache is a rectangular window (a view) into the actual image pixels (which may be in memory, memory-mapped from a disk file, or entirely on disk). Obtain existing image pixels via _get()_. Create a new pixel region using _set()._

Depending on the capabilities of the operating system, and the relationship of the window to the image, the pixel cache may be a copy of the pixels in the selected window, or it may be the actual image pixels. In any case calling _sync()_ insures that the base image is updated with the contents of the modified pixel cache. The method _decode()_ supports copying foreign pixel data formats into the pixel cache according to the _QuantumTypes_. The method _encode()_ supports copying the pixels in the cache to a foreign pixel representation according to the format specified by _QuantumTypes_. 

Setting a view using the Pixels class does not cause the number of references to the underlying image to be reduced to one. Therefore, in order to ensure that only the current generation of the image is modified, the Image's [modifyImage()](Image++.html#modifyImage) method should be invoked to reduce the reference count on the underlying image to one. If this is not done, then it is possible for a previous generation of the image to be modified due to the use of reference counting when copying or constructing an Image. 

The _PixelPacket_ * returned by the _set_ and _get_ methods, and the _IndexPacket_ * returned by the _indexes_ method point to pixel data managed by the _Pixels_ class. The _Pixels_ class is responsible for releasing resources associated with the pixel view. This means that the pointer should never be passed to delete() or free(). 

The pixel view is a small image in which the pixels may be accessed, addressed, and updated, as shown in the following example, which produces an image similar to the one on the right (minus lines and text): 

![](Cache.png)

// Create base image Image image(Geometry(254,218), "white"); // Set the image type to TrueColor DirectClass representation. image.type(TrueColorType); // Ensure that there is only one reference to underlying image // If this is not done, then image pixels will not be modified. image.modifyImage(); // Allocate pixel view Pixels view(image); // Set all pixels in region anchored at 38x36, with size 160x230 to green. size_t columns = 196; size_t rows = 162; Color green("green"); PixelPacket *pixels = view.get(38,36,columns,rows); for ( ssize_t row = 0; row < rows ; ++row ) for ( ssize_t column = 0; column < columns ; ++column ) *pixels++=green; // Save changes to image. view.sync(); // Set all pixels in region anchored at 86x72, with size 108x67 to yellow. columns = 108; rows = 67; Color yellow("yellow"); pixels = view.get(86,72,columns,rows); for ( ssize_t row = 0; row < rows ; ++row ) for ( ssize_t column = 0; column < columns ; ++column ) *pixels++=yellow; view.sync(); // Set pixel at position 108,94 to red *(view.get(108,94,1,1)) = Color("red"); // Save changes to image. view.sync(); 

_Pixels_ supports the following methods: 

**Pixel Cache Methods**

**Method** |  **Returns** |  **Signature** |  **Description**  
---|---|---|---  
get |  [PixelPacket](PixelPacket.html)* |  const ssize_t x_, const ssize_t y_, const size_t columns_, const size_t rows_ |  Transfers read-write pixels from the image to the pixel cache as defined by the specified rectangular region. Modified pixels may be subsequently transferred back to the image via _sync_. The value returned is intended for pixel access only. It should never be deallocated.  
getConst |  const [PixelPacket](PixelPacket.html)* |  const ssize_t x_, const ssize_t y_, const size_t columns_, const size_t rows_ |  Transfers read-only pixels from the image to the pixel cache as defined by the specified rectangular region.  
set |  [PixelPacket](PixelPacket.html)* |  const ssize_t x_, const ssize_t y_, const size_t columns_, const size_t rows_ |  Allocates a pixel cache region to store image pixels as defined by the region rectangle.Â This area is subsequently transferred from the pixel cache to the image via _sync_. The value returned is intended for pixel access only. It should never be deallocated.  
sync |  void |  void |  Transfers the image cache pixels to the image.  
indexes |  IndexPacket* |  void |  Returns the PsuedoColor pixel indexes corresponding to the pixel region defined by the last [get](Pixels.html#get) , [getConst](Pixels.html#getConst), or [set](Pixels.html#set) call. Only valid for PseudoColor and CMYKA images. The pixel indexes (an array of type _IndexPacket_ , which is typedef _Quantum_ , which is itself typedef _unsigned char_ , or _unsigned short_ , depending on the value of the _QuantumDepth_ define) provide the colormap index (see [colorMap](Image++.html#colorMap)) for each pixel in the image. For CMYKA images, the indexes represent the black channel. The value returned is intended for pixel access only. It should never be deallocated.  
x |  int |  void |  Left ordinate of view  
y |  int |  void |  Top ordinate of view  
columns |  size_t |  void |  Width of view  
rows |  size_t |  void |  Height of view
