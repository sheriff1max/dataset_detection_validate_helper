import numpy as np
import cv2


def read_img(filename_image: str) -> np.ndarray:
    img = cv2.imread(filename_image)
    return img


def plot_bounding_box(
        filename_image: str,
        filename_label: str,
        labels_dict: dict,
) -> np.ndarray:
    """Отрисовка bbox и label на исходной картинке."""
    img = cv2.imread(filename_image)
    dh, dw, _ = img.shape
    with open(filename_label, 'r') as f:
        list_labels_txt = f.readlines()

    list_labels = []
    list_boxes = []
    for row in list_labels_txt:
        label = row[0]
        coords = row[2:].replace('\n', '')
        list_labels.append(label)
        list_boxes.append(coords.split())

    for i in range(len(list_labels)):
        box = list_boxes[i]
        label = labels_dict[list_labels[i]]

        x, y, w, h = box
        x, y, w, h = float(x), float(y), float(w), float(h)

        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)

        if l < 0: l = 0
        if r > dw - 1: r = dw - 1
        if t < 0: t = 0
        if b > dh - 1: b = dh - 1

        color = (0, 0, 255)

        img = cv2.putText(
            img, label, (int(l), int(t - 10)),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
            color=color, thickness=3,
        )
        img = cv2.rectangle(img, (l, t), (r, b), color=color, thickness=3)
    return img


if __name__ == '__main__':
    plot_bounding_box(
        './datasets/grenades/images/000008_jpg.rf.680c747d93d7430a4978d3e1480b8291.jpg',
        './datasets/grenades/labels/000008_jpg.rf.680c747d93d7430a4978d3e1480b8291.txt',
        {'0': 'grenade'}
    )
