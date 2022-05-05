import os
from sys import argv
from math import ceil
from tqdm import tqdm
import cv2

WIDTH = 256
HEIGHT = 256
RATIO = WIDTH/HEIGHT
WHITE = (255, 255, 255)

def resize(directory, filename):
    path = os.path.join(directory, filename)
    img = cv2.imread(path)
    h, w, _ = img.shape

    if h >= 256 and w >= 256:
        return
    if h > w:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        w, h = h, w

    if h < 256 and w >= 256:
        new_h = h
        new_w = w
    else:
        if w / h < RATIO:
            new_w = ceil(w * (HEIGHT / h))
            new_h = int(h * (HEIGHT / h))
        else:
            new_w = int(w * (WIDTH / w))
            new_h = ceil(h * (WIDTH / w))
        dim = (new_w, new_h)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    diff_vert = HEIGHT - new_h
    pad_top = max(diff_vert // 2, 0)
    pad_bottom = max(diff_vert - pad_top, 0)

    diff_hori = WIDTH - new_w
    pad_left = max(diff_hori // 2, 0)
    pad_right = max(diff_hori - pad_left, 0)



    img_padded = cv2.copyMakeBorder(img, pad_top,
                                    pad_bottom, pad_left, pad_right,
                                    cv2.BORDER_CONSTANT,
                                    value=WHITE)

    cv2.imwrite(path, img_padded)

for base_dir, dirs, files in tqdm(os.walk(argv[1])):
    for file in tqdm(files):
        resize(base_dir, file)
