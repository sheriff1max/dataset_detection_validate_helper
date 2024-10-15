import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from tqdm import tqdm


path_labels = './drones/labels'
path_images = './drones/images'

path_class0 = './drones/0'
os.mkdir(path_class0)
path_class1 = './drones/1'
os.mkdir(path_class1)


for txtfile in tqdm(os.listdir(path_labels)[::-1]):
    filename = txtfile.split('.')[0]

    with open(f'{path_labels}/{txtfile}') as f:
        lines = f.readlines()

    img = cv2.imread(f'{path_images}/{filename}.jpg')
    try:
        height, width = img.shape[:2]
    except:
        continue

    for idx, line in enumerate(lines):
        li = line.split(' ')
        # print(li[0], li[1], li[2], li[3], li[4])  # Change according to its own TXT content format

        center_x = int(float(li[1]) * width)
        center_y = int(float(li[2]) * height)
        w = int(float(li[3]) * width)
        h = int(float(li[4]) * height)
        x = int(center_x - w / 2)
        y = int(center_y - h / 2)


        label = li[0]
        xmin, ymin, xmax, ymax = x, y, x + w, y + h
        if xmax - xmin < 10:
            xmin = xmin - (xmax - xmin)
            xmax = xmax + (xmax - xmin)

        if ymax - ymin < 10:
            ymin = ymin - (ymax - ymin)
            ymax = ymax + (ymax - ymin)

        try:
            cropped_image = img[ymin:ymax, xmin:xmax]
        except:
            continue

        # image = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
        # cv2.imwrite(f'{path_class0}/{filename + str(idx)}.jpg', image)

        if label == '0':
            cv2.imwrite(f'{path_class0}/{filename + str(idx)}.jpg', cropped_image)
        else:
            cv2.imwrite(f'{path_class1}/{filename + str(idx)}.jpg', cropped_image)
    # break
