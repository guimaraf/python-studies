from PIL import Image
import os
import sys

equalSize = [420, 420]
dividerSize = 2
directorys = ['tempImage', 'converted']

for file_name in os.listdir(directorys[0]):
  print("Processing %s" % file_name)
  image = Image.open(os.path.join(directorys[0], file_name))
  x,y = image.size
  newDimensions = (equalSize[0], equalSize[1]) if (x == y) else (int(x/dividerSize), int(y/dividerSize))

  output = image.resize(newDimensions, resample=0, box=None)
  output_file_name = os.path.join(directorys[1], "small_" + file_name)
  output.save(output_file_name, format=None)
print("All done")