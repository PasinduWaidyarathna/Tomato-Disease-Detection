# ml_module.py

import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input

class MLModel:
    def __init__(self, model_path='testx.hdf5', class_names=None):
        self.model = tf.keras.models.load_model(model_path)
        self.class_names = class_names or ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]

    def predict_image(self, img_array):
        predictions = self.model.predict(img_array)
        predicted_class = np.argmax(predictions)
        predicted_probability = predictions[0, predicted_class]

        return self.class_names[predicted_class], predicted_probability * 100
