from tensorflow import keras
import numpy as np
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'emotiondetector.h5')
    print(f"Loading model from {model_path}")
    return keras.models.load_model(model_path)

def preprocess_image(img):
    img = img.convert('L')
    img = img.resize((48, 48))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array