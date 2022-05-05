import random
import os
from glob import glob
from tqdm import tqdm
from shutil import copyfile

count = 10000
DATA_PATH = "/home/coep/deblurring/dataset/clear/*"
NEW_DATA_PATH = "/home/coep/deblurring/dataset/clear_small/"

os.makedirs(NEW_DATA_PATH, exist_ok=True)

files = glob(DATA_PATH)
random.shuffle(files)

subset_of_files = files[:count]

for i in tqdm(subset_of_files):
    copyfile(i, os.path.join(NEW_DATA_PATH, os.path.basename(i)))

