# Import and Install Dependencies
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense
import trained as tk


fileName = 'testos6'
trainedWords = tk.testo[fileName]

# Setup Folders for Collection
actions = np.array(trainedWords) # Actions that we try to detect
no_sequences = 500  # Thirty videos worth of data
sequence_length = 15  # Videos are going to be 30 frames in length

# Build and Train LSTM Neural Network
model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(15,1629)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))


# load weights
model.load_weights(fileName+'.h5')

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
converter.allow_custom_ops = True  # Allow custom ops
tflite_model = converter.convert()

# Save the model to a file
with open(fileName+'.tflite', 'wb') as f:
    f.write(tflite_model)
  