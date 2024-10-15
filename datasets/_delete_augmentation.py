import os
# os.remove("/tmp/<file_name>.txt")

path_images = './drones/images'
path_labels = './drones/labels'

for file in os.listdir(path_images):
    filename = file.split('.')[0]

    if 'aughor' in filename or 'inv' in filename:
        os.remove(f"{path_images}/{filename}.jpg")
        os.remove(f"{path_labels}/{filename}.txt")
    # break