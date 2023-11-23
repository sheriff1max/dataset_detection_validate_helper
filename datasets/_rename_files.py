"""Переименовывангие файлов в папке"""

import os


DIR_NAMES = ['Кирпич_картинки', ]
NEW_NAME = 'hack'


def main():
    counter = 0
    for dir_name in DIR_NAMES:
        for filename in os.listdir(f'./{dir_name}/'):
            filename = filename[:-4]

            new_filename = f'{NEW_NAME}{counter}'
            os.rename(f'./{dir_name}/{filename}.jpg', f'./{dir_name}/{new_filename}.jpg')
            counter += 1


if __name__ == '__main__':
    main()
