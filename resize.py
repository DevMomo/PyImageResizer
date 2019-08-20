import sys
import os
from PIL import Image 

"""
This script will resize one or more images to a set percentage using the Python Imaging Library
"""

if __name__ == "__main__":
	try:
		images = sys.argv[1:-1]
		percentage = float(sys.argv[-1])
	except IndexError:
		print ("Usage: " + os.path.basename(__file__) + " <image files> <percentage>")	
		sys.exit(1)
	except ValueError:
		print ("Usage: " + os.path.basename(__file__) + " <image files> <percentage>")
		sys.exit(1)



