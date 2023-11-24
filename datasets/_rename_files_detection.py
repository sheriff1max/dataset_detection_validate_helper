"""Переименовывангие файлов в папке"""

import os


DIR_NAMES = ['brick_detection', ]
NEW_NAME = 'brick_'


def main():

    counter = 0
    for dir_name in DIR_NAMES:
        for filename in os.listdir(f'./{dir_name}/images/'):
            filename = filename[:-4]

            new_filename = f'{NEW_NAME}{counter}'
            os.rename(f'./{dir_name}/images/{filename}.jpg', f'./{dir_name}/images/{new_filename}.jpg')
            os.rename(f'./{dir_name}/labels/{filename}.txt', f'./{dir_name}/labels/{new_filename}.txt')
            counter += 1

if __name__ == '__main__':
    main()
