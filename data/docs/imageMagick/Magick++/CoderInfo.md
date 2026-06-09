### Magick::CoderInfo

The _CoderInfo_ class provides the means to provide information regarding ImageMagick support for an image format (designated by a magick string). It may be used to provide support for a specific named format (provided as an argument to the constructor), or as an element of a container when format support is queried using the [coderInfoList()](STL.html#coderInfoList) templated function.

The following code fragment illustrates how CoderInfo may be used.
    
    
    CoderInfo info("GIF"); 
    cout < info->name() << ": (" << info->description() << ") : "; 
    cout << "Readable = "; 
    if ( info->isReadable() ) 
      cout << "true"; 
    else 
      cout << "false"; 
    cout << ", "; 
    cout << "Writable = "; 
    if ( info->isWritable() ) 
      cout << "true"; 
    else 
      cout << "false"; 
    cout << ", "; 
    cout << "Multiframe = "; 
    if ( info->isMultiframe() ) 
      cout << "true"; 
    else 
      cout << "false"; 
    cout << endl;
    

The methods available in the _CoderInfo_ class are shown in the following table:

  


**CoderInfo Methods**

**Method** |  **Returns** |  **Signature** |  **Description**  
---|---|---|---  
CoderInfo |  |  void |  Construct object corresponding to named format (e.g. "GIF"). An exception is thrown if the format is not supported.  
name |  std::string |  void |  Format name (e.g. "GIF").  
description |  std::string |  void |  Format description (e.g. "CompuServe graphics interchange format").  
isReadable |  bool |  void |  Format is readable.  
isWritable |  bool |  void |  Format is writeable.  
isMultiFrame |  bool |  void |  Format supports multiple frames.  


