# PixelPacket Structure

The _PixelPacket_ structure is used to represent pixels in ImageMagick. ImageMagick may be compiled to support 32 or 64 bit pixels. The size of PixelPacket is controlled by the value of the _QuantumDepth_ define. The default is 64 bit pixels, which provide the best accuracy. If memory consumption must be minimized, or processing time must be minimized, then ImageMagick may be compiled with QuantumDepth=8. The following table shows the relationship between _QuantumDepth_ , the type of _Quantum_ , and the overall _PixelPacket_ size.

  


**Effect Of QuantumDepth Values**

**QuantumDepth** |  **Quantum Type** |  **PixelPacket Size**  
---|---|---  
8 |  unsigned char |  32 bits  
16 |  unsigned short |  64 bits  
  
The members of the _PixelPacket_ structure, and their interpretation, are shown in the following table:

  


**PixelPacket Structure Members**

**Member** |  **Type** |  **Interpretation**  
---|---|---  
[RGBColorspace](Enumerations.html#ColorspaceType) |  [RGBColorspace](Enumerations.html#ColorspaceType) + [matte](Image++.html#matte) |  [CMYKColorspace](Enumerations.html#ColorspaceType)  
red |  Quantum |  Red |  Red |  Cyan  
green |  Quantum |  Green |  Green |  Magenta  
blue |  Quantum |  Blue |  Blue |  Yellow  
opacity |  Quantum |  Ignored |  Opacity |  Ignored
