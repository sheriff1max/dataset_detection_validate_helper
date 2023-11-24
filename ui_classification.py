import streamlit as st
import tkinter as tk
from tkinter import filedialog

import os
import shutil
import yaml

from utils import read_img


if 'path_dataset' not in st.session_state:
    st.session_state['path_dataset'] = None
if 'new_good_path_dir' not in st.session_state:
    st.session_state['new_good_path_dir'] = None
if 'new_bad_path_dir' not in st.session_state:
    st.session_state['new_bad_path_dir'] = None
if 'list_last_images' not in st.session_state:
    st.session_state['list_last_images'] = []


# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title('Помощник валидации датасета классификации')
st.write('Выбери путь до датасета:')
clicked = st.button('Выбрать папку')
if clicked:
    path_dataset = st.text_input('Выбранная папка:', filedialog.askdirectory(master=root))
    st.session_state['path_dataset'] = path_dataset

    path_parent = '/'.join(path_dataset.split('/')[:-1])
    dir_name = path_dataset.split('/')[-1]

    new_good_path_dir = os.path.join(path_parent, f'{dir_name}_good')
    st.session_state['new_good_path_dir'] = new_good_path_dir
    if not os.path.isdir(new_good_path_dir):
        os.mkdir(new_good_path_dir)

    new_bad_path_dir = os.path.join(path_parent, f'{dir_name}_bad')
    st.session_state['new_bad_path_dir'] = new_bad_path_dir
    if not os.path.isdir(new_bad_path_dir):
        os.mkdir(new_bad_path_dir)

else:
    path_dataset = None

if st.session_state['path_dataset']:
    path_images = st.session_state['path_dataset']

    list_path_images = os.listdir(path_images)

    st.write(f'Осталось картинок: {len(list_path_images)}')
    st.write(f'Обработано картинок: {len(st.session_state["list_last_images"])}')

    i = 0

    cur_path_image = os.path.join(path_images, list_path_images[i])
    st.write(f'Текущий файл: {list_path_images[i]}')
    img = read_img(cur_path_image)
    widget_img = st.image(img, width=440, channels='BGR')

    btn = st.button('Картинка хорошая, сохраняем', type="primary")
    if btn:

        new_path_good_image = os.path.join(
            st.session_state['new_good_path_dir'],
            list_path_images[i]
        )
        shutil.move(
            cur_path_image,
            new_path_good_image
        )
        st.session_state['list_last_images'].append(new_path_good_image)
        st.experimental_rerun()

    btn = st.button('Удалить')
    if btn:
        new_path_bad_image = os.path.join(
            st.session_state['new_bad_path_dir'],
            list_path_images[i]
        )
        shutil.move(
            cur_path_image,
            new_path_bad_image
        )
        st.session_state['list_last_images'].append(new_path_bad_image)
        st.experimental_rerun()

    btn = st.button('Вернуться на шаг назад')
    if btn:
        shutil.move(
            st.session_state['list_last_images'][-1],
            st.session_state['path_dataset'],
        )
        st.session_state['list_last_images'].pop(-1)
        st.experimental_rerun()
