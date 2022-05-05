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

def psnr(img1, img2):
	mse = numpy.mean( (img1 - img2) ** 2 )
	if mse == 0:
		return 100
	PIXEL_MAX = 255.0
	return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

im = 0
c = 0
deblurval = []
blurrval = []
splitnames = []

for fullname in onlyfiles:
	parts = fullname.split("_")
	common = parts[0] + "_" + parts[1] + "_" + parts[2] + "_" + parts[3]
	splitnames.append(common)

splitnames = list(set(splitnames)) 
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
		#print("Img " + str(im))
		im = im + 1
		b = psnr(clear, blurr)
		#print("Blurred image " + buf + " PSNR => " + str(b))
		d = psnr(clear, deblur)
		#print("Deblurred image " + buf + " PSNR => " + str(d))
		deblurval.append(d)
		blurrval.append(b)
		if(b < d):
			c = c  + 1
		#print("____________________________________________________________________________________")
	except:
		print("____________________________________________________________________________________")

avgdeb = sum(deblurval)/len(deblurval)
avgblu = sum(blurrval)/len(blurrval)
print()
per = c/len(splitnames) * 100
print(str(per) + " deblurred images have more PSNR")
print("Average PSNR of Blurred Images => " + str(avgblu))
print("Average PSNR of Delurred Images => " + str(avgdeb))

