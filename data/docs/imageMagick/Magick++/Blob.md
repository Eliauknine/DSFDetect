# Magick::Blob  
  
Blob provides the means to contain any opaque data. It is named after the term "Binary Large OBject" commonly used to describe unstructured data (such as encoded images) which is stored in a database. While the function of Blob is very simple (store a pointer and and size associated with allocated data), the Blob class provides some very useful capabilities. In particular, it is fully reference counted just like the Image class.

The Blob class supports value assignment while preserving any outstanding earlier versions of the object. Since assignment is via a pointer internally, Blob is efficient enough to be stored directly in an STL container or any other data structure which requires assignment. In particular, by storing a Blob in an [associative container](http://www.sgi.com/tech/stl/AssociativeContainer.html) (such as STL's '[_map_](http://www.sgi.com/tech/stl/Map.html)') it is possible to create simple indexed in-memory "database" of Blobs.

Magick++ currently uses Blob to contain encoded images (e.g. JPEG) as well as ICC and IPTC profiles. Since Blob is a general-purpose class, it may be used for other purposes as well.

The methods Blob provides are shown in the following table:

  


**Blob Methods**

**Method** |  **Return Type** |  **Signature(s)** |  **Description**  
---|---|---|---  
Blob |  |  void |  Default constructor  
const void* data_, size_t length_ |  Construct object with data, making a copy of the supplied data  
const Blob& blob_ |  Copy constructor (reference counted)  
operator= |  Blob |  const Blob& blob_ |  Assignment operator (reference counted)  
update |  void |  const void* data_, size_t length_ |  Update object contents, making a copy of the supplied data. Any existing data in the object is deallocated.  
data |  const void* |  void |  Obtain pointer to data  
length |  size_t |  void |  Obtain data length  
updateNoCopy |  void |  void* data_, size_t length_, Blob::Allocator allocator_ = Blob::NewAllocator |  Update object contents, using supplied pointer directly (no copy) Any existing data in the object is deallocated. The user must ensure that the pointer supplied is not deleted or otherwise modified after it has been supplied to this method. The optional allocator_ parameter allows the user to specify if the C (MallocAllocator) or C++ (NewAllocator) memory allocation system was used to allocate the memory. The default is to use the C++ memory allocator.
