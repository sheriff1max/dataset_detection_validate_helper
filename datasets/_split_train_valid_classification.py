"""Разделение данных на train/valid"""


import os
import random
import shutil


DATASET_DIR = 'drones'
# SIZE_VALID = 0.2


def main():
    path_train = os.path.join(DATASET_DIR, 'train')
    os.mkdir(path_train)
    path_train_class0 = os.path.join(path_train, '0')
    os.mkdir(path_train_class0)
    path_train_class1 = os.path.join(path_train, '1')
    os.mkdir(path_train_class1)

    path_valid = os.path.join(DATASET_DIR, 'valid')
    os.mkdir(path_valid)
    path_valid_class0 = os.path.join(path_valid, '0')
    os.mkdir(path_valid_class0)
    path_valid_class1 = os.path.join(path_valid, '1')
    os.mkdir(path_valid_class1)

    path_class0 = os.path.join(DATASET_DIR, '0')
    path_class1 = os.path.join(DATASET_DIR, '1')

    images_class0 = os.listdir(path_class0)
    images_class1 = os.listdir(path_class1)

    valid_images_class0 = random.sample(images_class0, 15415 - 4000)
    print(len(valid_images_class0))
    for filename in images_class0:
        only_filename = filename[:-4]

        if filename in valid_images_class0:
            shutil.copyfile(
                os.path.join(path_class0, f'{only_filename}.jpg'),
                os.path.join(path_valid_class0, f'{only_filename}.jpg'),
            )
        else:
            shutil.copyfile(
                os.path.join(path_class0, f'{only_filename}.jpg'),
                os.path.join(path_train_class0, f'{only_filename}.jpg'),
            )

    valid_images_class1 = random.sample(images_class1, 4990 - 4000)
    print(len(valid_images_class1))
    for filename in images_class1:
        only_filename = filename[:-4]

        if filename in valid_images_class1:
            shutil.copyfile(
                os.path.join(path_class1, f'{only_filename}.jpg'),
                os.path.join(path_valid_class1, f'{only_filename}.jpg'),
            )
        else:
            shutil.copyfile(
                os.path.join(path_class1, f'{only_filename}.jpg'),
                os.path.join(path_train_class1, f'{only_filename}.jpg'),
            )


if __name__ == '__main__':
    main()
