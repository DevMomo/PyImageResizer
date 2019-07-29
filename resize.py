import sys
from PIL import Image 

if (sys.argv):
	im = Image.open(sys.argv[1])
	im.show()


