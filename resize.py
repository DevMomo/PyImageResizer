import os, sys
from PIL import Image 

"""
This script will resize one or more images to a set percentage using the Python Imaging Library.
Output images are converted to JPG.
"""

def resizeImage(images, percentage):
	for image in images:

		output = os.path.splitext(image)[0] + "_RESIZED" + str(percentage) + ".jpg" # output file name
		
		if image != output:
			try:
				im = Image.open(image)

				# Calculate new size of resized image
				maxSize = max(im.height, im.width)
				maxSize = maxSize * percentage # shrink by given percentage
				size = (maxSize, maxSize)

				im.thumbnail(size, Image.BICUBIC)
				im.save(output, "JPEG")

			except IOError:
				print ("File error for %s" % image)

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

	resizeImage(images, percentage)






