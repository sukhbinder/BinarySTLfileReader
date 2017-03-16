# BinarySTLFileReader

Binary STL File Reader in Pure numpy

Back in 2013, wrote this small little python program to read in binary STL file.

This was lying on my [blog](https://wordpress.com/post/sukhbinder.wordpress.com/2065), thought it might be of some use for others, so putting it on github.

![image](https://github.com/sukhbinder/BinarySTLfileReader/blob/master/images/bent_plate.png)

Added a new code to visualize

## Example

~~~ python

from binarySTLreader import BinarySTL,ShowSTLFile
h,p,n,v1,v2,v3=BinarySTL('bent_plate.stl')
ShowSTLFile(v1,v2,v3)

~~~
