成功提取并保存了919条记录到data/groundtruths/libraw_functions_gt.csv

成功提取并保存了465条记录到data/groundtruths/libtiff_functions_gt.csv

成功提取并保存了854条记录到data/groundtruths/imagemagick_functions_gt.csv

上面是LibRaw的API文档，内容以md的形式提供，现在想进行有关漏洞方面的信息提取，请你根据上面的内容，结合你的判断，请输出你觉得可能导致漏洞发生的函数名

需要新建一个csv文件用于存放ground truths，需要如下几列：function_name, doc_name, content
-----------------------------------------------------------------------
从CSV中提取到 363 个唯一的函数名

在文档中找到 12 个函数，LibRaw有16条数据:

函数: LibRaw::dcraw_clear_mem
出现在 1 个文档中:
  - API-CXX-eng.md

函数: LibRaw::dcraw_document_mode_processing
出现在 2 个文档中:
  - API-C-eng.md
  - API-CXX-eng.md

函数: LibRaw::dcraw_make_mem_image
出现在 1 个文档中:
  - API-C-eng.md

函数: LibRaw::dcraw_make_mem_thumb
出现在 1 个文档中:
  - API-C-eng.md

函数: LibRaw::dcraw_process
出现在 2 个文档中:
  - API-C-eng.md
  - API-CXX-eng.md

函数: LibRaw::dcraw_thumb_writer
出现在 2 个文档中:
  - API-C-eng.md
  - API-CXX-eng.md

函数: LibRaw::subtract_black
出现在 1 个文档中:
  - API-CXX-eng.md

函数: LibRaw::unpack
出现在 1 个文档中:

  - API-datastruct-eng.md


函数: LibRaw::unpack_thumb
出现在 4 个文档中:

  - API-CXX-eng.md
  - API-datastruct-eng.md
  - API-notes-eng.md

函数: bad_pixels
出现在 1 个文档中:
  - API-datastruct-eng.md



函数: green_matching
出现在 2 个文档中:
  - API-datastruct-eng.md




函数: scale_colors
出现在 1 个文档中:
  - API-datastruct-eng.md



总结:
总函数数: 363
在文档中找到的函数数: 12
未找到的函数数: 342
-----------------------------------------------------------------------

/Users/mycp/opt/anaconda3/bin/python /Users/mycp/PycharmProjects/pythonProject/extract/test/test.py 
从CSV中提取到 304 个唯一的函数名

在文档中找到 21 个函数:

函数: ChopUpSingleUncompressedStrip
出现在 1 个文档中:
  - v3.8.0.md

函数: EstimateStripByteCounts
出现在 1 个文档中:
  - v3.9.0beta.md

函数: TIFFCheckDirOffset
出现在 1 个文档中:
  - v3.9.0beta.md

函数: TIFFComputeStrip
出现在 2 个文档中:
  - man/TIFFstrip.3tiff.md
  - man/libtiff.3tiff.md

函数: TIFFFetchData
出现在 1 个文档中:
  - v3.8.1.md

函数: TIFFFetchDirectory
出现在 1 个文档中:
  - v3.9.0beta.md

函数: TIFFFetchNormalTag
出现在 2 个文档中:
  - v3.7.0alpha.md
  - v3.7.4.md

函数: TIFFNumberOfStrips
出现在 5 个文档中:
  - libtiff.md
  - man/TIFFReadDirectory.3tiff.md
  - man/TIFFstrip.3tiff.md
  - man/libtiff.3tiff.md
  - v3.7.0alpha.md

函数: TIFFRasterScanlineSize
出现在 1 个文档中:
  - man/TIFFsize.3tiff.md

函数: TIFFRawStripSize
出现在 3 个文档中:
  - man/TIFFstrip.3tiff.md
  - man/libtiff.3tiff.md
  - v3.6.1.md

函数: TIFFReadCustomDirectory
出现在 1 个文档中:
  - v3.9.0beta.md

函数: TIFFReadDirectory
出现在 13 个文档中:
  - addingtags.md
  - libtiff.md
  - man/TIFFGetField.3tiff.md
  - man/TIFFPrintDirectory.3tiff.md
  - man/TIFFReadDirectory.3tiff.md
  - man/TIFFSetDirectory.3tiff.md
  - man/TIFFSetField.3tiff.md
  - man/TIFFWriteDirectory.3tiff.md
  - man/index.md
  - man/libtiff.3tiff.md
  - v3.7.1.md
  - v3.8.2.md
  - v3.9.0beta.md

函数: TIFFReadEXIFDirectory
出现在 1 个文档中:
  - v3.8.1.md

函数: TIFFScanlineSize
出现在 6 个文档中:
  - libtiff.md
  - man/TIFFReadScanline.3tiff.md
  - man/TIFFsize.3tiff.md
  - man/libtiff.3tiff.md
  - v3.8.2.md
  - v4.0.0.md

函数: TIFFScanlineSize64
出现在 1 个文档中:
  - v4.0.0.md

函数: TIFFStripSize
出现在 5 个文档中:
  - libtiff.md
  - man/TIFFReadEncodedStrip.3tiff.md
  - man/TIFFReadRawStrip.3tiff.md
  - man/TIFFstrip.3tiff.md
  - man/libtiff.3tiff.md

函数: TIFFVStripSize
出现在 2 个文档中:
  - man/TIFFstrip.3tiff.md
  - man/libtiff.3tiff.md

函数: _TIFFDefaultStripSize
出现在 1 个文档中:
  - man/TIFFstrip.3tiff.md

函数: main
出现在 25 个文档中:
  - BigTIFFProposal.md
  - TIFFTechNote2.md
  - addingtags.md
  - bigtiffpr.md
  - build.md
  - document.md
  - index.md
  - internals.md
  - libtiff.md
  - man/TIFFReadRGBAStrip.3tiff.md
  - man/TIFFReadRGBATile.3tiff.md
  - man/fax2tiff.1.md
  - man/tiffcp.1.md
  - tools.md
  - v3.4beta031.md
  - v3.4beta036.md
  - v3.5.2.md
  - v3.5.3.md
  - v3.5.7.md
  - v3.6.1.md
  - v3.7.0.md
  - v3.7.0alpha.md
  - v3.7.2.md
  - v3.8.0.md
  - v3.9.0beta.md

函数: tiffcp
出现在 37 个文档中:
  - build.md
  - images.md
  - man/fax2tiff.1.md
  - man/gif2tiff.1.md
  - man/index.md
  - man/pal2rgb.1.md
  - man/ppm2tiff.1.md
  - man/ras2tiff.1.md
  - man/raw2tiff.1.md
  - man/rgb2ycbcr.1.md
  - man/sgi2tiff.1.md
  - man/tiff2bw.1.md
  - man/tiff2pdf.1.md
  - man/tiff2ps.1.md
  - man/tiffcmp.1.md
  - man/tiffcp.1.md
  - man/tiffcrop.1.md
  - man/tiffdither.1.md
  - man/tiffgt.1.md
  - man/tiffinfo.1.md
  - man/tiffmedian.1.md
  - man/tiffset.1.md
  - man/tiffsplit.1.md
  - man/tiffsv.1.md
  - tools.md
  - v3.4beta007.md
  - v3.4beta028.md
  - v3.5.5.md
  - v3.5.7.md
  - v3.6.0.md
  - v3.7.0alpha.md
  - v3.7.4.md
  - v3.8.0.md
  - v3.8.1.md
  - v3.8.2.md
  - v3.9.0beta.md
  - v4.0.0.md

函数: usage
出现在 10 个文档中:
  - build.md
  - libtiff.md
  - man/TIFFRGBAImage.3tiff.md
  - man/TIFFbuffer.3tiff.md
  - man/TIFFquery.3tiff.md
  - man/libtiff.3tiff.md
  - man/tiff2pdf.1.md
  - v3.4beta036.md
  - v3.5.4.md
  - v3.8.2.md

总结:
总函数数: 304
在文档中找到的函数数: 21
未找到的函数数: 283

-----------------------------------------------------------------------
