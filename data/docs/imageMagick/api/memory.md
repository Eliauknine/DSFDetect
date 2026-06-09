[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireAlignedMemory](memory.html#AcquireAlignedMemory) • [AcquireMagickMemory](memory.html#AcquireMagickMemory) • [AcquireQuantumMemory](memory.html#AcquireQuantumMemory) • [AcquireVirtualMemory](memory.html#AcquireVirtualMemory) • [CopyMagickMemory](memory.html#CopyMagickMemory) • [GetMagickMemoryMethods](memory.html#GetMagickMemoryMethods) • [GetVirtualMemoryBlob](memory.html#GetVirtualMemoryBlob) • [RelinquishAlignedMemory](memory.html#RelinquishAlignedMemory) • [RelinquishMagickMemory](memory.html#RelinquishMagickMemory) • [RelinquishVirtualMemory](memory.html#RelinquishVirtualMemory) • [ResetMagickMemory](memory.html#ResetMagickMemory) • [ResizeMagickMemory](memory.html#ResizeMagickMemory) • [ResizeQuantumMemory](memory.html#ResizeQuantumMemory) • [SetMagickMemoryMethods](memory.html#SetMagickMemoryMethods)

## [AcquireAlignedMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

AcquireAlignedMemory() returns a pointer to a block of memory at least size bytes whose address is a multiple of 16*sizeof(void *).

The format of the AcquireAlignedMemory method is:
    
    
    void *AcquireAlignedMemory(const size_t count,const size_t quantum)
    

A description of each parameter follows:

    
    

count
    the number of quantum elements to allocate. 
    
quantum
    the number of bytes in each quantum. 
    

## [AcquireMagickMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

AcquireMagickMemory() returns a pointer to a block of memory at least size bytes suitably aligned for any use.

The format of the AcquireMagickMemory method is:
    
    
    void *AcquireMagickMemory(const size_t size)
    

A description of each parameter follows:

    
    

size
    the size of the memory in bytes to allocate. 
    

## [AcquireQuantumMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

AcquireQuantumMemory() returns a pointer to a block of memory at least count * quantum bytes suitably aligned for any use.

The format of the AcquireQuantumMemory method is:
    
    
    void *AcquireQuantumMemory(const size_t count,const size_t quantum)
    

A description of each parameter follows:

    
    

count
    the number of quantum elements to allocate. 
    
quantum
    the number of bytes in each quantum. 
    

## [AcquireVirtualMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

AcquireVirtualMemory() allocates a pointer to a block of memory at least size bytes suitably aligned for any use.

The format of the AcquireVirtualMemory method is:
    
    
    MemoryInfo *AcquireVirtualMemory(const size_t count,const size_t quantum)
    

A description of each parameter follows:

    
    

count
    the number of quantum elements to allocate. 
    
quantum
    the number of bytes in each quantum. 
    

## [CopyMagickMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

CopyMagickMemory() copies size bytes from memory area source to the destination. Copying between objects that overlap will take place correctly. It returns destination.

The format of the CopyMagickMemory method is:
    
    
    void *CopyMagickMemory(void *destination,const void *source,
      const size_t size)
    

A description of each parameter follows:

    
    

destination
    the destination. 
    
source
    the source. 
    
size
    the size of the memory in bytes to allocate. 
    

## [GetMagickMemoryMethods](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

GetMagickMemoryMethods() gets the methods to acquire, resize, and destroy memory.

The format of the GetMagickMemoryMethods() method is:
    
    
    void GetMagickMemoryMethods(AcquireMemoryHandler *acquire_memory_handler,
      ResizeMemoryHandler *resize_memory_handler,
      DestroyMemoryHandler *destroy_memory_handler)
    

A description of each parameter follows:

    
    

acquire_memory_handler
    method to acquire memory (e.g. malloc). 
    
resize_memory_handler
    method to resize memory (e.g. realloc). 
    
destroy_memory_handler
    method to destroy memory (e.g. free). 
    

## [GetVirtualMemoryBlob](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

GetVirtualMemoryBlob() returns the virtual memory blob associated with the specified MemoryInfo structure.

The format of the GetVirtualMemoryBlob method is:
    
    
    void *GetVirtualMemoryBlob(const MemoryInfo *memory_info)
    

A description of each parameter follows:

    
    

memory_info
    The MemoryInfo structure. 

## [RelinquishAlignedMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

RelinquishAlignedMemory() frees memory acquired with AcquireAlignedMemory() or reuse.

The format of the RelinquishAlignedMemory method is:
    
    
    void *RelinquishAlignedMemory(void *memory)
    

A description of each parameter follows:

    
    

memory
    A pointer to a block of memory to free for reuse. 
    

## [RelinquishMagickMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

RelinquishMagickMemory() frees memory acquired with AcquireMagickMemory() or AcquireQuantumMemory() for reuse.

The format of the RelinquishMagickMemory method is:
    
    
    void *RelinquishMagickMemory(void *memory)
    

A description of each parameter follows:

    
    

memory
    A pointer to a block of memory to free for reuse. 
    

## [RelinquishVirtualMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

RelinquishVirtualMemory() frees memory acquired with AcquireVirtualMemory().

The format of the RelinquishVirtualMemory method is:
    
    
    MemoryInfo *RelinquishVirtualMemory(MemoryInfo *memory_info)
    

A description of each parameter follows:

    
    

memory_info
    A pointer to a block of memory to free for reuse. 
    

## [ResetMagickMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

ResetMagickMemory() fills the first size bytes of the memory area pointed to by memory with the constant byte c.

The format of the ResetMagickMemory method is:
    
    
    void *ResetMagickMemory(void *memory,int byte,const size_t size)
    

A description of each parameter follows:

    
    

memory
    a pointer to a memory allocation. 
    
byte
    set the memory to this value. 
    
size
    size of the memory to reset. 
    

## [ResizeMagickMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

ResizeMagickMemory() changes the size of the memory and returns a pointer to the (possibly moved) block. The contents will be unchanged up to the lesser of the new and old sizes.

The format of the ResizeMagickMemory method is:
    
    
    void *ResizeMagickMemory(void *memory,const size_t size)
    

A description of each parameter follows:

    
    

memory
    A pointer to a memory allocation. 
    
size
    the new size of the allocated memory. 
    

## [ResizeQuantumMemory](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

ResizeQuantumMemory() changes the size of the memory and returns a pointer to the (possibly moved) block. The contents will be unchanged up to the lesser of the new and old sizes.

The format of the ResizeQuantumMemory method is:
    
    
    void *ResizeQuantumMemory(void *memory,const size_t count,
      const size_t quantum)
    

A description of each parameter follows:

    
    

memory
    A pointer to a memory allocation. 
    
count
    the number of quantum elements to allocate. 
    
quantum
    the number of bytes in each quantum. 
    

## [SetMagickMemoryMethods](http://www.imagemagick.org/api/MagickCore/memory_8c.html)

SetMagickMemoryMethods() sets the methods to acquire, resize, and destroy memory. Your custom memory methods must be set prior to the MagickCoreGenesis() method.

The format of the SetMagickMemoryMethods() method is:
    
    
    SetMagickMemoryMethods(AcquireMemoryHandler acquire_memory_handler,
      ResizeMemoryHandler resize_memory_handler,
      DestroyMemoryHandler destroy_memory_handler)
    

A description of each parameter follows:

    
    

acquire_memory_handler
    method to acquire memory (e.g. malloc). 
    
resize_memory_handler
    method to resize memory (e.g. realloc). 
    
destroy_memory_handler
    method to destroy memory (e.g. free). 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](memory.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
