import cv2
import sys
import glob
import os
from tabulate import tabulate
from texttable import Texttable

# Get user supplied values
#imagePath = sys.argv[1]
#cascPath = sys.argv[2]
def detect():
	imagePath = '../data/test/'
	cascPath = 'cascade.xml'

	# Create the haar cascade
	ProtozoaCascade = cv2.CascadeClassifier(cascPath)

	# Read the image
	imagefiles = glob.glob(imagePath +'*.jpg')
	for img in imagefiles:
		image = cv2.imread(img)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# Detect protozoa in the image
		protozoa = ProtozoaCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=5,
		    minSize=(30, 30),
		    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		if len(protozoa)>0:
			names = os.path.basename(img)
			t = Texttable()
			t.add_rows([['Image Name', 'Result'], [names, 'Infected']])
			print t.draw()
		else:
			t = Texttable()
			t.add_rows([['Image Name', 'Result'], [names, 'Not Infected']])
			print t.draw()
		print "Found {0} protozoa!".format(len(protozoa))

		# Draw a rectangle around the protozoa
		for (x, y, w, h) in protozoa:
		    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

		cv2.imshow("Protozoa found", image)
		cv2.waitKey(0
			)
detect()


