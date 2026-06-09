# Special Format Characters

The Magick::Image methods [_annotate_](Image++.html#annotate), [_draw_](Image++.html#draw), [_label_](Image++.html#label), and the template function _montageImages_ support special format characters contained in the argument text. These format characters work similar to C's _printf_. Whenever a format character appears in the text, it is replaced with the equivalent attribute text. The available format characters are shown in the following table.

  


**Format Characters**

**Format Character** |  **Description**  
---|---  
%b |  file size  
%d |  directory  
%e |  filename extension  
%f |  filename  
%h |  height  
%m |  magick (e.g GIF)  
%p |  page number  
%s |  scene number  
%t |  top of filename  
%w |  width  
%x |  x resolution  
%y |  y resolution  
\n |  newline  
\r |  carriage return
