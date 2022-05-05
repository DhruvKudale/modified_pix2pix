import os
import cv2
from tqdm import tqdm
PATH = "/home/coep/deblurring/dataset"
c = 0
for base, dirs, files in os.walk(PATH):
    for filename in tqdm(files):
        file_path = os.path.join(base, filename)
        img = cv2.imread(file_path)
        h, w, _ = img.shape
        if h < 256 or w < 256:
            c += 1
            print(c, file_path)