# BMP Image Framework
A rudimentary way to handle 24-bit BMP files as sets of pixels with Python, without any libraries.

## Starting out 
The framework is comprised of a single python file named image.py. Download the file and add it to your project's directory.
It provides 2 classes. One called `Pixel` which is just a way to arrange the red, blue and green channels of the image, and
another called `Image`, which is the main class of the library, the one that does the image handling.

## Usage
In order to start using the framework, you must first import it into your project
```
from image import *
```
The `Pixel` class is structured as follows:
```
Pixel.red   # red color   (0-255)
Pixel.green # green color (0-255)
Pixel.blue  # blue color  (0-255)
```
The image class has the following functionality:

```
Image(width = 0, height = 0) # constructor for the Image class; starts as a white image
Image.open(path) # opens the bmp file at the given path, creates the pixel matrix, sets width and height
Image.save(path) # saves the pixel matrix as a bmp file at the given path
Image.getWidth() # returns width of image
Image.getHeight() # returns height of image
Image.getPixel(pozX, pozY) # returns the pixel object at the given location
Image.setPixel(Pixel, pozX, pozY) # sets the pixel at the given location
```

The pixel matrix (0, 0) is at the top left of the image.

## What I learned
- BMP File Structure; image color channels;
- Python Programming (Object-Oriented Design);
- Working with bits and bytes (Everything was read and written as `"wb"` or `"rb"`, byte by byte).
