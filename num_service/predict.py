import pandas as pd 
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import glob 

import warnings
warnings.filterwarnings('ignore')


model = load_model('model.h5')

true = 0 
length = 0 
error = []

numbers = [n.replace('\\', '/') for n in glob.glob('DUE_MNIST/convert2image/*')]

for number in numbers: 
    print(f'Predict with number {number}')
    n = number.split('/')[-1]
    print(f'Current in number {n}')

    images = [file.replace('\\', '/') for file in glob.glob(f'DUE_MNIST/convert2image/{n}/*.jpg')]

    for image in images: 
        img = cv2.imread(image)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY).reshape(-1, 28,  28)

        pred = model.predict(img)

        result = np.argmax(pred, axis = 1)

        if result == int(n): 
            true += 1 
        else: 
            error.append(image.split('/')[-1])
        length += 1

print(true)
print(f'Accuray: {round(true/length, 2)*100}%')
print(error)
