# Resize Image Version 1.0
Simple code for resize multiple images from a directory using Python

# Need Modules
<b>os, sys, Pillow</b><br>
pip install Pillow

Official documentation
https://pypi.org/project/Pillow/

# Usage
Create 2 directories, the first with the name <b>tempImage</b> the second directory with the name <b>converted</b>.<br><br>
Copy the images you want to resize to the <b>tempImage</b> directory, the <b>equalSize</b>" array you specify the final size of the file.

# Example
equalSize = [800, 800]<br>
The code will differentiate images with fixed and varied size, which solves a problem I had when I need to resize several images, but they are usually the same size.

The code is an update for Javier Tordable<br><br>
https://www.javiertordable.com/how-to-resize-all-images-in-a-directory/