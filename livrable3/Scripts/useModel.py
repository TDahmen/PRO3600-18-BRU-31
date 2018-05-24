from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import InputLayer, Input
from tensorflow.python.keras.layers import Reshape, MaxPooling2D
from tensorflow.python.keras.layers import Conv2D, Dense, Flatten
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.regularizers import l2
import time
import numpy as np

model = load_model('model')

#teX = np.load('gamesData.npy')
#teY = np.load('oneHotEncoded3.npy')
#
#prediction = model.predict_classes(np.array(teX[100000:101000]))
#
#print(prediction)

# for k in range(0, len(prediction)):
#     if prediction[k] == 2:
#         print(k+100000)
