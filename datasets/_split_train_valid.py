"""Разделение данных на train/valid"""


import os
import random
import shutil


DATASET_DIR = 'full_version1'
SIZE_VALID = 0.12


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

    images = os.listdir(path_images)

    valid_images = random.sample(images, int(len(images) * SIZE_VALID))
    print(len(valid_images))
    for filename in images:
        only_filename = filename[:-4]

        if filename in valid_images:
            shutil.copyfile(
                os.path.join(path_images, f'{only_filename}.jpg'),
                os.path.join(path_valid_images, f'{only_filename}.jpg'),
            )
            shutil.copyfile(
                os.path.join(path_labels, f'{only_filename}.txt'),
                os.path.join(path_valid_labels, f'{only_filename}.txt'),
            )
        else:
            shutil.copyfile(
                os.path.join(path_images, f'{only_filename}.jpg'),
                os.path.join(path_train_images, f'{only_filename}.jpg'),
            )
            shutil.copyfile(
                os.path.join(path_labels, f'{only_filename}.txt'),
                os.path.join(path_train_labels, f'{only_filename}.txt'),
            )


if __name__ == '__main__':
    main()
