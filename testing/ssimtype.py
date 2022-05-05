
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import numpy 
import math
import cv2
from os import listdir
from os.path import isfile, join
import sys

#path = sys.argv[1] 
#print(path)

path = "/home/dhruv/Project/FINALTESTING3/finalimages/"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

def ssimtype(blurtype):
	c = 0
	count = 1
	deblurval = []
	blurrval = []
	splitnames = []
	for fullname in onlyfiles:
		parts = fullname.split("_")
		common = parts[0] + "_" + parts[1] + "_" + parts[2] + "_" + parts[3]
		if(parts[1] == blurtype):
			splitnames.append(common)

	splitnames = list(set(splitnames)) 
	den = len(splitnames)
	for i in splitnames:
		s1 = "_fake_B.png"
		s2 = "_real_B.png"
		s3 = "_real_A.png"
		buf = str(i)
		file1 = path + buf + s1
		file2 = path + buf + s2
		file3 = path + buf + s3
		try:
			deblur = cv2.imread(file1)
			clear = cv2.imread(file2)
			blurr = cv2.imread(file3)

			gdeblur = cv2.cvtColor(deblur, cv2.COLOR_BGR2GRAY)
			gclear = cv2.cvtColor(clear, cv2.COLOR_BGR2GRAY)
			gblurr = cv2.cvtColor(blurr, cv2.COLOR_BGR2GRAY)

			#print("Image " + str(count) + " " + str(buf))
			count = count + 1

			(scoreblu, dif) = compare_ssim(gblurr, gclear, full=True)
			#print("SSIM for blurred wrt clear : {}".format(scoreblu))
			blurrval.append(scoreblu)
			
			(scoredeb, dif) = compare_ssim(gdeblur, gclear, full=True)
			#print("SSIM for deblurred wrt clear : {}".format(scoredeb))
			deblurval.append(scoredeb)
			
			if(scoreblu < scoredeb):
				c = c  + 1
			
			#print("____________________________________________________________________________________")
		except:
			print("____________________________________________________________________________________")

	avgdeb = sum(deblurval)/len(deblurval)
	avgblu = sum(blurrval)/len(blurrval)
	print()
	per = float(c/den) * 100
	print(str(per) + "% deblurred images have more SSIM than blurred of the type " + str(blurtype))
	print("Average SSIM of Blurred Images => " + str(avgblu))
	print("Average SSIM of Delurred Images => " + str(avgdeb))


ssimtype("focus")
ssimtype("horizontal")
ssimtype("vertical")











