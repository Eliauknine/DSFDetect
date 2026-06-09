[Home](../index.html) [Download](binary-releases.html) [Tools](command-line-tools.html) [Command-line](command-line-processing.html) [Resources](resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[The Fx Special Effects Image Operator](fx.html#fx) • [The Anatomy of an Fx Expression](fx.html#anatomy)

Use the Fx special effects image operator to apply a mathematical expression to an image or image channels. Use Fx to:

  * create canvases, gradients, mathematical colormaps
  * move color values between images and channels
  * translate, flip, mirror, rotate, scale, shear and generally distort images
  * merge or composite multiple images together
  * convolve or merge neighboring pixels together
  * generate image metrics or 'fingerprints'



The expression can be simple:
    
    
    convert -size 64x64 canvas:black -channel blue -fx "1/2" fx_navy.png
    

Here, we convert a black to a navy blue image:

[![black](../images/black.png)](../images/black.png) ![==>](../images/right.gif) [![navy](../images/navy.png)](../images/navy.png) 


Or the expression can be complex:
    
    
    convert rose.jpg \  
      -fx "(1.0/(1.0+exp(10.0*(0.5-u)))-0.006693)*1.0092503" \ 
      rose-sigmoidal.png'
    

This expression results in a high contrast version of the image:

[![rose](../images/rose.jpg)](../images/rose.jpg) ![==>](../images/right.gif) [![rose-sigmoidal](../images/rose-sigmoidal.png)](../images/rose-sigmoidal.png) 


The expression can include variable assignments. Assignments, in most cases, reduce the complexity of an expression and permit some operations that might not be possible any other way. For example, lets create a radial gradient:
    
    
    convert -size 70x70 canvas: \
      -fx "Xi=i-w/2; Yj=j-h/2; 1.2*(0.5-hypot(Xi,Yj)/70.0)+0.5" 
      radial-gradient.png'
    

The command above returns this image:

[![radial-gradient](../images/radial-gradient.png)](../images/radial-gradient.png) 


This FX expression adds random noise to an image:
    
    
    convert photo.jpg -fx \'iso=32; rone=rand(); rtwo=rand(); \
      myn=sqrt(-2*ln(rone))*cos(2*Pi*rtwo); myntwo=sqrt(-2*ln(rtwo))* \
      cos(2*Pi*rone); pnoise=sqrt(p)*myn*sqrt(iso)* \ 
      channel(4.28,3.86,6.68,0)/255; max(0,p+pnoise)\' noisy.png
    

See [Using FX, The Special Effects Image Operator](http://www.imagemagick.org/Usage/transform/index.html#fx) for more examples.

The next section discusses the Fx expression language.

## The Anatomy of an Fx Expression

### The Fx Expression Language

The formal Fx expression language is defined here:

numbers:
     integer, floating point, scientific notation (+/- required, e.g. 3.81469e-06), International System number postfixes (.e.g KB, Mib, GB, etc.)
constants: 
     E (Euler's number), Epsilon, QuantumRange, QuantumScale, Opaque, Phi (golden ratio), Pi, Transparent
Fx operators (in order of precedence): 
     ^ (power), unary -, *, /, % (modulo), +, -, <<, >>, <, <=, >, >=, ==, !=, & (bitwise AND), | (bitwise OR), && (logical AND), || (logical OR), ~ (logical NOT), ?: (ternary conditional)
math functions: 
     abs(), acos(), acosh(), airy(), alt(), asin(), asinh(), atan(), atanh(), atan2(), ceil(), clamp(), cos(), cosh(), debug(), drc(), exp(), floor(), gauss(), gcd(), hypot(), int(), isnan(), j0(), j1(), jinc(), ln(), log(), logtwo(), max(), min(), mod(), not(), pow(), rand(), round(), sign(), sin(), sinc(), sinh(), sqrt(), squish(), tan(), tanh(), trunc()
channel functions: 
     channel(r,g,b,a), channel(c,m,y,k,a)
color names:
     red, cyan, black, etc.
color functions:
     srgb(), srgba(), rgb(), rgba(), cmyk(), cmyka(), hsl(), hsla(), etc.
color hex values:
     #ccc, #cbfed0, #b9e1cc00, etc.
symbols:
    

* `u`=> first image in list
* `v`=> second image in list
* `s`=> current image in list (for %[fx:] otherwise = u)
* `t`=> index of current image (s) in list
* `n`=> number of images in list
* `i`=> column offset
* `j`=> row offset
* `p`=> pixel to use (absolute or relative to current pixel)
* `w`=> width of this image
* `h`=> height of this image
* `z`=> channel depth
* `r`=> red value (from RGBA), of a specific or current pixel
* `g`=> green ''
* `b`=> blue ''
* `a`=> alpha ''
* `o`=> opacity ''
* `c`=> cyan value of CMYK color of pixel
* `y`=> yellow ''
* `m`=> magenta ''
* `k`=> black ''
* `intensity`=> pixel intensity
* `hue`=> pixel hue
* `saturation`=> pixel saturation
* `lightness`=> pixel lightness
* `luma`=> pixel luma
* `page.width`=> page width
* `page.height`=> page height
* `page.x`=> page x offset
* `page.y`=> page y offset
* `resolution.x`=> x resolution
* `resolution.y`=> y resolution
* `depth`=> image depth
* `minima`=> image minima
* `maxima`=> image maxima
* `mean`=> image mean
* `standard_deviation`=> image standard deviation
* `kurtosis`=> image kurtosis
* `skewness`=> image skewness (add a channel specifier to compute a statistic for that channel, e.g. depth.r)
iterators:
     while()

### The Fx Expression

An Fx expression may include any combination of the following:

x `^` y
     exponentiation (xy)
`(` ... `)`
     grouping
x `*` y
     multiplication (the asterisk `*` is optional, for example, `2u` or `2(x+y)` are acceptable)
x `/` y
     division
x `%` y
     modulo
x `+` y
     addition
x `-` y
     subtraction
x `<<` y
     left shift
x `>>` y
     right shift
x `<` y
     boolean relation, return value 1.0 if x < y, otherwise 0.0
x `<=` y
     boolean relation, return value 1.0 if x <= y, otherwise 0.0
x `>` y
     boolean relation, return value 1.0 if x > y, otherwise 0.0
x `>=` y
     boolean relation, return value 1.0 if x >= y, otherwise 0.0
x `==` y
     boolean relation, return value 1.0 if x == y, otherwise 0.0
x `!=` y
     boolean relation, return value 1.0 if x != y, otherwise 0.0
x `&` y
     binary AND
x `|` y
     binary OR
x `&&` y
     logical AND connective, return value 1.0 if x > 0 and y > 0, otherwise 0.0
x `||` y
     logical OR connective (inclusive), return value 1.0 if x > 0 or y > 0 (or both), otherwise 0.0
`~`x
     logical NOT operator, return value 1.0 if not x > 0, otherwise 0.0
`+`x
     unary plus, return 1.0*value
`-`x
     unary minus, return -1.0*value
x `?` y
    z: ternary conditional expression, return value y if x != 0, otherwise z; only one ternary conditional permitted per statement
x `=` y
    assignment; assignment variables are restricted to letter combinations only (e.g. Xi not X1)
x `;` y
    statement separator 
`phi`
     constant (1.618034...)
`pi`
     constant (3.141659...)
`e`
     constant (2.71828...)
`QuantumRange`
     constant maximum pixel value (255 for Q8, 65535 for Q16)
`QuantumScale`
     constant 1.0/`QuantumRange`
`intensity`
     pixel intensity; equivalent to 0.299*red+0.587*green+0.114*blue
`hue`
     pixel hue
`saturation`
     pixel saturation
`lightness`
     pixel lightness; equivalent to 0.5*max(red,green,blue) + 0.5*min(red,green,blue)
`luminance`
     pixel luminance; equivalent to 0.212656*red + 0.715158*green + 0.072186*blue
`red, green, blue`, etc.
     color names
`#ccc, #cbfed0, #b9e1cc00`, etc.
     color hex values
`rgb(), rgba(), cmyk(), cmyka(), hsl(), hsla()`
     color functions
`s, t, u, v, n, i, j, w, h, z, r, g, b, a, o, c, y, m, k`
     symbols
`abs(`x`)`
     absolute value function
`acos(`x`)`
     arc cosine function
`acosh(`x`)`
     inverse hyperbolic cosine function
`airy(`x`)`
     Airy function (max=1, min=0); airy(x)=[jinc(x)]2=[2*j1(pi*x)/(pi*x)]2
`alt(`x`)`
     sign alternation function (return 1.0 if int(x) is even, -1.0 if int(x) is odd)
`asin(`x`)`
     arc sine function
`asinh(`x`)`
     inverse hyperbolic sine function
`atan(`x`)`
     arc tangent function
`atanh(`x`)`
     inverse hyperbolic tangent function
`atan2(`x,y`)`
     arc tangent function of two variables
`ceil(`x`)`
    smallest integral value not less than argument
`channel(`r,g,b,a`)`
    select numeric argument based on current channel
`channel(`c,m,y,k,a`)`
    select numeric argument based on current channel
`clamp(`x`)`
     clamp value
`cos(`x`)`
     cosine function
`cosh(`x`)`
     hyperbolic cosine function
`debug(`x`)`
     print x (useful for debugging your expression)
`drc(`x,y`)`
     dynamic range compression (knee curve); drc(x,y)=(x)/(y*(x-1)+1); -1<y<1 
`exp(`x`)`
     natural exponential function (ex)
`floor(`x`)`
     largest integral value not greater than argument
`gauss(`x`)`
     gaussian function; gauss(x)=exp(-x*x/2)/sqrt(2*pi)
`gcd(`x,y`)`
     greatest common denominator
`hypot(`x,y`)`
     the square root of x2+y2
`int(`x`)`
     greatest integer function (return greatest integer less than or equal to x)
`isnan(`x`)`
    return 1.0 if x is NAN, 0.0 otherwise
`j0(`x`)`
     Bessel functions of x of the first kind of order 0
`j1(`x`)`
     Bessel functions of x of the first kind of order 1
`jinc(`x`)`
     jinc function (max=1, min=-0.1323); jinc(x)=2*j1(pi*x)/(pi**x)
`ln(`x`)`
     natural logarithm function
`log(`x`)`
     logarithm base 10
`logtwo(`x`)`
     logarithm base 2
`ln(`x`)`
     natural logarithm
`max(`x, y`)`
     maximum of x and y
`min(`x, y`)`
     minimum of x and y
`mod(`x, y`)`
     floating-point remainder function
`not(`x`)`
     return 1.0 if x is zero, 0.0 otherwise
`pow(`x,y`)`
     power function (xy)
`rand()`
     value uniformly distributed over the interval [0.0, 1.0) with a 2 to the 128th-1 period
`round()`
     round to integral value, regardless of rounding direction
`sign(`x`)`
     return -1.0 if x is less than 0.0 otherwise 1.0
`sin(`x`)`
     sine function
`sinc(`x`)`
     sinc function (max=1, min=-0.21); sinc(x)=sin(pi*x)/(pi*x)
`squish(`x`)`
     squish function; squish(x)=1.0/(1.0+exp(-x))
`sinh(`x`)`
     hyperbolic sine function
`sqrt(`x`)`
     square root function
`tan(`x`)`
     tangent function
`tanh(`x`)`
     hyperbolic tangent function
`trunc(`x`)`
     round to integer, towards zero
`while(`condition,expression`)`
     iterate while the condition is not equal to 0
  


The expression semantics include these rules:

  * symbols are case insensitive
  * only one ternary conditional (e.g. x ? y : z) per statement
  * statements are assignments or the final expression to return
  * an assignment starts a statement, it is not an operator
  * assignments to built-ins do not throw an exception and have no effect; e.g. `r=3.0; r` returns the pixel red color value, not 3.0
  * Unary operators have a lower priority than binary operators, that is, the unary minus (negation) has lower precedence than exponentiation, so -3^2 is interpreted as -(3^2) = -9. Use parentheses to clarify your intent (e.g. (-3)^2 = 9).
  * Similarly, care must be exercised when using the slash ('/') symbol. The string of characters 1/2x is interpreted as (1/2)x. The contrary interpretation should be written explicitly as 1/(2x). Again, the use of parentheses helps clarify the meaning and should be used whenever there is any chance of misinterpretation.

  


### Source Images

The symbols `u` and `v` refer to the first and second images, respectively, in the current image sequence. Refer to a particular image in a sequence by appending its index to any image reference (usually `u`), with a zero index for the beginning of the sequence. A negative index counts from the end. For example, `u[0]` is the first image in the sequence, `u[2]` is the third, `u[-1]` is the last image, and `u[t]` is the current image. The current image can also be referenced by `s`. If the sequence number exceeds the length of the sequence, the count is wrapped. Thus in a 3-image sequence, `u[-1]`, `u[2]`, and `u[5]` all refer to the same (third) image.

As an example, we form an image by averaging the first image and third images (the second (index 1) image is ignored and just junked):
    
    
    convert image1.jpg image2.jpg image3.jpg -fx "(u+u[2])/2.0" image.jpg
    

By default, the image to which `p`, `r`, `g`, `b`, `a`, etc., are applied is the current image `s` in the image list. This is equivalent to `u` except when used in an escape sequence `%[fx:...]`. 

It is important to note the special role played by the first image. This is the only image in the image sequence that is modified, other images are used only for their data. As an illustrative example, consider the following, and note that the setting [-channel red](command-line-options.html#channel) instructs [-fx](command-line-options.html#fx) to modify only the red channel; nothing in the green or blue channels will change. It is instructive to ponder why the result is not symmetric.
    
    
    convert -channel red logo: -flop logo: -resize "20%" -fx "(u+v)/2" image.jpg
    

[![logo-sm-flop.png](../images/logo-sm-flop.png)](../images/logo-sm-flop.png) [![logo-sm.png](../images/logo-sm.png)](../images/logo-sm.png) ![==>](../images/right.gif) [![logo-sm-fx.png](../images/logo-sm-fx.png)](../images/logo-sm-fx.png) 
  


### Accessing Pixels

All color values are normalized to the range of 0.0 to 1.0. The alpha channel ranges from 0.0 (fully transparent) to 1.0 (fully opaque).

The pixels are processed one at a time, but a different pixel of an image can be specified using a pixel index represented by `p`. For example,
    
    
    p[-1].g      green value of pixel to the immediate left of the current pixel
    p[-1,-1].r   red value of the pixel diagonally left and up from current pixel
    

To specify an absolute position, use braces, rather than brackets.
    
    
    p{0,0}.r     red value of the pixel in the upper left corner of the image
    p{12,34}.b   blue pixel value at column number 12, row 34 of the image
    

Integer values of the position retrieve the color of the pixel referenced, while non-integer position values return a blended color according to the current [-interpolate](command-line-options.html#interpolate) setting.

A position outside the boundary of the image retrieves a value dictated by the [-virtual-pixel](command-line-options.html#virtual-pixel) option setting.

### Apply an Expression to Select Image Channels

Use the [-channel](command-line-options.html#channel) setting to specify the output channel of the result. If no output channel is given, the result is set over all channels except the opacity channel. For example, to replace the red channel of `alpha.png` with the average of the green channels from the images `alpha.png` and `beta.png`, use:
    
    
    convert alpha.png beta.png -channel red -fx "(u.g+v.g)/2" gamma.png
    

### Results

The [-fx](command-line-options.html#fx) operator evaluates the given expression for each channel (set by [-channel](command-line-options.html#channel)) of each pixel in the first image (`u`) in the sequence. The computed values are temporarily stored in a copy (clone) of that first image until all the pixels have been processed, after which this single new image replaces the list of images in the current image sequence. As such, in the previous example the updated version of `alpha.png` replaces both of the original images, `alpha.png` and `beta.png`, before being saved as `gamma.png`.

The current image `s` is set to the first image in the sequence (`u`), and `t` to its index, 0. The symbols `i` and `j` reference the current pixel being processed.

For use with [-format](command-line-options.html#format_identify_), the value-escape `%[fx:]` is evaluated just once for each image in the current image sequence. As each image in the sequence is being evaluated, `s` and `t` successively refer to the current image and its index, while `i` and `j` are set to zero, and the current channel set to red ([-channel](command-line-options.html#channel) is ignored). An example:
    
    
    convert  canvas:'rgb(25%,50%,75%)' rose: -colorspace rgb  \ 
      -format 'Red channel of NW corner of image #%[fx:t] is %[fx:s]' info:
    Red channel of NW corner of image #0 is 0.453758 
    Red channel of NW corner of image #1 is 0.184588
    

Here we use the image indexes to rotate each image differently, and use `-set` with the image index to set a different pause delay on the first image in the animation:
    
    
    convert rose: -duplicate 29 -virtual-pixel Gray -distort SRT '%[fx:360.0*t/n]' \
      -set delay '%[fx:t == 0 ? 240 : 10]' -loop 0 rose.gif"
    

The color-escape `%[pixel:]` is evaluated once per image and per color channel in that image ([-channel](command-line-options.html#channel) is ignored), The values generated are then converted into a color string (a named color or hex color value). The symbols `i` and `j` are set to zero, and `s` and `t` refer to each successively current image and index.

[Donate](support.html) • [Sitemap](sitemap.html) • [Related](links.html) • [Architecture](architecture.html)

[Back to top](fx.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
