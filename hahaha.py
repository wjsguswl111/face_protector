import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, BatchNormalization
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array

path_dir = os.getcwd() + "\image\\"
file_list = os.listdir(path_dir)
file_num = len(file_list)

num=0
all_img = np.float32(np.zeros(file_num, 224, 224, 3))
all_label = np.float64(np.zeros(file_num, 1))

for img_name in file_list:
    img_path = path_dir + img_name
    img = load_img(img_path, target_size=(224, 224))

    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)