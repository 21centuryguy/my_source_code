"""https://gist.github.com/mcchae/0a30383dbddd90adf7a426a8e94c4c46"""

# USAGE
# python image_diff.py --first "origianl image path" --second "modified iamge path"
# python image_diff2.py --first "/sample_images/image1.png" --second "/sample_images/image2.png"

# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2 ### python install opencv_python (py3) / python install numpy
import os

# get current path
current_path = os.getcwd()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="first input image")
ap.add_argument("-s", "--second", required=True,
	help="second")
args = vars(ap.parse_args())

args["first"] = current_path + args["first"]
args["second"] = current_path + args["second"]

# load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

# convert the images to grayscale
# next line make error
# OpenCV Error: Assertion failed (scn == 3 || scn == 4) in cvtColor
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

if str(format(score)) == str(1.0):
	print ("Two images are Same !")
	print("SSIM: {}".format(score))
else:
	print ("Two images are Not Same -_-;")
	print("SSIM: {}".format(score))


# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

### save the output images
cv2.imwrite(current_path+"/result/Original.png", imageA)
cv2.imwrite(current_path+"/result/Modified.png", imageB)
cv2.imwrite(current_path+"/result/diff.png", diff)
cv2.imwrite(current_path+"/result/Thresh.png", thresh)

### show the output images
# cv2.imshow("Original", imageA)
# cv2.imshow("Modified", imageB)
# cv2.imshow("Diff", diff)
# cv2.imshow(current_path+"/sample_images/diff.png", diff)
# cv2.imshow("Thresh", thresh)
# cv2.waitKey(0)

# end
