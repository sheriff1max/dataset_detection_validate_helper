"""
Бутстрапирование выборок.
"""

import numpy as np
import os
import shutil


DIR_ORIGINAL_NAME = 'full_version1'
COUNT_BOOTRAP = 2


def main():
    """"""

    path_original_dataset_imgs = os.path.join(DIR_ORIGINAL_NAME, 'images')
    path_original_dataset_labels = os.path.join(DIR_ORIGINAL_NAME, 'labels')

    dataset_imgs = np.array(os.listdir(path_original_dataset_imgs))
    dataset_labels = np.array(os.listdir(path_original_dataset_labels))

    for i in range(COUNT_BOOTRAP):
        path_new_dataset = f'{DIR_ORIGINAL_NAME}_bootstrap_{i}'
        os.mkdir(path_new_dataset)

        path_new_dataset_imgs = os.path.join(path_new_dataset, f'images')
        os.mkdir(path_new_dataset_imgs)

        path_new_dataset_labels = os.path.join(path_new_dataset, f'labels')
        os.mkdir(path_new_dataset_labels)

        indeces_new_data = np.random.choice(
            np.arange(len(dataset_imgs)),
            replace=True,
            size=len(dataset_imgs)
        )

        new_dataset_imgs = dataset_imgs[indeces_new_data]

        for i, filename in enumerate(new_dataset_imgs):
            only_filename = filename[:-4]
            shutil.copyfile(
                os.path.join(path_original_dataset_imgs, f'{only_filename}.jpg'),
                os.path.join(path_new_dataset_imgs, f'{only_filename}{i}.jpg'),
            )
            shutil.copyfile(
                os.path.join(path_original_dataset_labels, f'{only_filename}.txt'),
                os.path.join(path_new_dataset_labels, f'{only_filename}{i}.txt'),
            )


if __name__ == '__main__':
    main()
