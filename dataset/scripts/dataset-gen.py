import cv2 
import numpy as np 
from sys import argv
from tqdm import tqdm
import os
from random import randint as ri

def blur(base_dir, file, i):
    name = os.path.join(base_dir, file)

    img = cv2.imread(name)
    os.remove(name)

    new_name = "{0:07d}".format(i)
    new_name = os.path.join(base_dir, new_name)
    cv2.imwrite('{}.jpg'.format(new_name), img)  
    print(new_name)
    horizontal_kernel_size = int(argv[2])
    kernel_h = np.zeros((horizontal_kernel_size, horizontal_kernel_size))
    kernel_h[int((horizontal_kernel_size - 1) / 2), :] = np.ones(horizontal_kernel_size)
    kernel_h /= horizontal_kernel_size 
    horizontal_mb = cv2.filter2D(img, -1, kernel_h) 
    cv2.imwrite('{}_horizontal_{}.jpg'.format(new_name, horizontal_kernel_size), horizontal_mb)

    vertical_kernel_size = int(argv[2])
    kernel_v = np.zeros((vertical_kernel_size, vertical_kernel_size)) 
    kernel_v[:, int((vertical_kernel_size - 1) / 2)] = np.ones(vertical_kernel_size) 
    kernel_v /= vertical_kernel_size 
    vertical_mb = cv2.filter2D(img, -1, kernel_v)  
    cv2.imwrite('{}_vertical_{}.jpg'.format(new_name, vertical_kernel_size), vertical_mb) 
    
    blur_kernel = int(argv[2])
    blurImg = cv2.blur(img, (blur_kernel, blur_kernel))
    cv2.imwrite('{}_focus_{}.jpg'.format(new_name, blur_kernel), blurImg)

i = 35000
for base_dir, dirs, files in tqdm(os.walk(argv[1])):
    for file in tqdm(files):
        blur(base_dir, file, i)
        i += 1
