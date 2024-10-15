"""Разделение данных на train/valid"""


import os
import random
import shutil
from tqdm import tqdm


DATASET_DIR = 'drones'



def main():
    path_train = os.path.join(DATASET_DIR, 'train')
    os.mkdir(path_train)
    path_train_images = os.path.join(path_train, 'images')
    os.mkdir(path_train_images)
    path_train_labels = os.path.join(path_train, 'labels')
    os.mkdir(path_train_labels)

    path_valid = os.path.join(DATASET_DIR, 'valid')
    os.mkdir(path_valid)
    path_valid_images = os.path.join(path_valid, 'images')
    os.mkdir(path_valid_images)
    path_valid_labels = os.path.join(path_valid, 'labels')
    os.mkdir(path_valid_labels)

    path_images = os.path.join(DATASET_DIR, 'images')
    path_labels = os.path.join(DATASET_DIR, 'labels')

    for idx in tqdm(range(len(os.listdir(path_images)))):
        filename = f'img_{idx}'

        if idx % 5 == 0:
            shutil.copyfile(
                os.path.join(path_images, f'{filename}.jpg'),
                os.path.join(path_valid_images, f'{filename}.jpg'),
            )
            shutil.copyfile(
                os.path.join(path_labels, f'{filename}.txt'),
                os.path.join(path_valid_labels, f'{filename}.txt'),
            )
        else:
            shutil.copyfile(
                os.path.join(path_images, f'{filename}.jpg'),
                os.path.join(path_train_images, f'{filename}.jpg'),
            )
            shutil.copyfile(
                os.path.join(path_labels, f'{filename}.txt'),
                os.path.join(path_train_labels, f'{filename}.txt'),
            )


if __name__ == '__main__':
    main()
