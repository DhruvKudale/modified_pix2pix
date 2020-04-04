import os
import shutil
import random
from tqdm import tqdm

# DeBlurGANv2:
# 99195 TRAIN
# 28341 VAL
# 14171 TEST

# pix2pix:
# 340095 TRAIN
# 85026 TEST

path_combine = "D:\\Rucha\\BTechProject\\DeblurGANv2-master\\dataset\\FINAL\\combine"
path_test = "D:\\Rucha\\BTechProject\\DeblurGANv2-master\\dataset\\FINAL\\combine_final\\test"
dir_combine = os.listdir(path_combine)
test = set(random.sample(dir_combine, k = 85026))
print("Step 1 done.")
for x in tqdm(test):
	os.rename(path_combine + "\\" + x, path_test + "\\" + x)
print("fin")