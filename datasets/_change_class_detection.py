"""Меняем датасет файлы"""


import os
import shutil


DIR_NAMES = ['brick_detection', ]

FIND_CLASS = ['0', ]
NEW_CLASS = ['1', ]


def main():

    for dir_name in DIR_NAMES:

        if not os.path.isdir(f'./{dir_name}/new_labels'):
            os.mkdir(f'./{dir_name}/new_labels')

        for filename in os.listdir(f'./{dir_name}/labels'):

            with open(f'./{dir_name}/labels/{filename}') as f:
                text = []
                for row in f.readlines():
                    if row[0] in FIND_CLASS:
                        idx_find_class = FIND_CLASS.index(row[0])
                        row = f'{NEW_CLASS[idx_find_class]}{row[1:]}'
                        text.append(row)

            if text:
                with open(f'./{dir_name}/new_labels/{filename}', 'w') as f:
                    f.writelines(text)


if __name__ == '__main__':
    main()
