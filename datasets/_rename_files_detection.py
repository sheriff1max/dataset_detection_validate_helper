"""Переименовывангие файлов в папке"""

import os


# DIR_NAMES = ['drones', ]
DIR_NAMES = 'drones'
NEW_NAME = 'img_'


# def main():

#     counter = 0
#     for dir_name in DIR_NAMES:
#         for filename in os.listdir(f'./{dir_name}/images/'):
#             filename = filename[:-4]

#             new_filename = f'{NEW_NAME}{counter}'
#             os.rename(f'./{dir_name}/images/{filename}.jpg', f'./{dir_name}/images/{new_filename}.jpg')
#             os.rename(f'./{dir_name}/labels/{filename}.txt', f'./{dir_name}/labels/{new_filename}.txt')
#             counter += 1

def main():

    counter = 0
    for filename in os.listdir(f'./{DIR_NAMES}/images/'):
        filename = filename[:-4]

        new_filename = f'{NEW_NAME}{counter}'
        os.rename(f'./{DIR_NAMES}/images/{filename}.jpg', f'./{DIR_NAMES}/images/{new_filename}.jpg')
        os.rename(f'./{DIR_NAMES}/labels/{filename}.txt', f'./{DIR_NAMES}/labels/{new_filename}.txt')
        counter += 1

if __name__ == '__main__':
    main()
