import streamlit as st
import tkinter as tk
from tkinter import filedialog

import os
import shutil
import yaml

from utils import plot_bounding_box


if 'path_dataset' not in st.session_state:
    st.session_state['path_dataset'] = None
if 'yaml_filename' not in st.session_state:
    st.session_state['yaml_filename'] = None
if 'new_good_path_dir' not in st.session_state:
    st.session_state['new_good_path_dir'] = None
if 'new_bad_path_dir' not in st.session_state:
    st.session_state['new_bad_path_dir'] = None
if 'list_last_images' not in st.session_state:
    st.session_state['list_last_images'] = []
if 'list_last_labels' not in st.session_state:
    st.session_state['list_last_labels'] = []


# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title('Помощник валидации датасета детекции')
st.write('Выбери путь до датасета:')
clicked = st.button('Выбрать папку')
if clicked:
    path_dataset = st.text_input('Выбранная папка:', filedialog.askdirectory(master=root))
    st.session_state['path_dataset'] = path_dataset

    yaml_filename = [filename for filename in os.listdir(path_dataset) if '.yaml' in filename][0]
    st.session_state['yaml_filename'] = yaml_filename

    path_parent = '/'.join(path_dataset.split('/')[:-1])
    dir_name = path_dataset.split('/')[-1]

    new_good_path_dir = os.path.join(path_parent, f'{dir_name}_good')
    st.session_state['new_good_path_dir'] = new_good_path_dir
    if not os.path.isdir(new_good_path_dir):
        os.mkdir(new_good_path_dir)

        path_images = os.path.join(new_good_path_dir, f'images')
        if not os.path.isdir(path_images):
            os.mkdir(path_images)
        path_labels = os.path.join(new_good_path_dir, f'labels')
        if not os.path.isdir(path_labels):
            os.mkdir(path_labels)

    new_bad_path_dir = os.path.join(path_parent, f'{dir_name}_bad')
    st.session_state['new_bad_path_dir'] = new_bad_path_dir
    if not os.path.isdir(new_bad_path_dir):
        os.mkdir(new_bad_path_dir)

        path_images = os.path.join(new_bad_path_dir, f'images')
        if not os.path.isdir(path_images):
            os.mkdir(path_images)
        path_labels = os.path.join(new_bad_path_dir, f'labels')
        if not os.path.isdir(path_labels):
            os.mkdir(path_labels)
else:
    path_dataset = None

if st.session_state['path_dataset']:
    path_images = os.path.join(st.session_state['path_dataset'], 'images')
    path_labels = os.path.join(st.session_state['path_dataset'], 'labels')

    list_path_images = os.listdir(path_images)
    list_path_labels = os.listdir(path_labels)
    with open(os.path.join(st.session_state['path_dataset'], st.session_state['yaml_filename'])) as f:
        read_data = yaml.load(f, Loader=yaml.FullLoader)
    labels_dict = {str(i): label for i, label in enumerate(read_data['names'])}

    st.write(f'Осталось картинок: {len(list_path_images)}')
    st.write(f'Обработано картинок: {len(st.session_state["list_last_images"])}')

    i = 0

    cur_path_image = os.path.join(path_images, list_path_images[i])
    cur_path_label = os.path.join(path_labels, list_path_labels[i])
    img = plot_bounding_box(
        cur_path_image,
        cur_path_label,
        labels_dict,
    )
    widget_img = st.image(img, width=440, channels='BGR')

    btn = st.button('Картинка хорошая, сохраняем', type="primary")
    if btn:

        new_path_good_image = os.path.join(
            os.path.join(st.session_state['new_good_path_dir'], 'images'),
            list_path_images[i]
        )
        shutil.move(
            cur_path_image,
            new_path_good_image
        )
        new_path_good_label = os.path.join(
            os.path.join(st.session_state['new_good_path_dir'], 'labels'),
            list_path_labels[i]
        )
        shutil.move(
            cur_path_label,
            new_path_good_label
        )
        st.session_state['list_last_images'].append(new_path_good_image)
        st.session_state['list_last_labels'].append(new_path_good_label)
        st.experimental_rerun()

    btn = st.button('Удалить')
    if btn:
        new_path_bad_image = os.path.join(
            os.path.join(st.session_state['new_bad_path_dir'], 'images'),
            list_path_images[i]
        )
        shutil.move(
            cur_path_image,
            new_path_bad_image
        )
        new_path_bad_label = os.path.join(
            os.path.join(st.session_state['new_bad_path_dir'], 'labels'),
            list_path_labels[i]
        )
        shutil.move(
            cur_path_label,
            new_path_bad_label
        )
        st.session_state['list_last_images'].append(new_path_bad_image)
        st.session_state['list_last_labels'].append(new_path_bad_label)
        st.experimental_rerun()

    btn = st.button('Вернуться на шаг назад')
    if btn:
        shutil.move(
            st.session_state['list_last_images'][-1],
            os.path.join(st.session_state['path_dataset'], 'images')
        )
        shutil.move(
            st.session_state['list_last_labels'][-1],
            os.path.join(st.session_state['path_dataset'], 'labels')
        )
        st.session_state['list_last_images'].pop(-1)
        st.session_state['list_last_labels'].pop(-1)
        st.experimental_rerun()
