import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input

model = tf.keras.models.load_model('testx.hdf5')

# Load and preprocess the image
img_path = 'lb5.jpg'
img = image.load_img(img_path, target_size=(256, 256))
img_array = image.img_to_array(img)
img_array = preprocess_input(img_array)
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

# Make prediction
predictions = model.predict(img_array)

# Get predicted class index
predicted_class = np.argmax(predictions)

# Assuming you have a list of class names
class_names = ["Potato___Early_blight","Potato___Late_blight","Potato___healthy"]
predicted_probability = predictions[0, predicted_class]
# Print predicted class name and percentage
print(f"Predicted class: {class_names[predicted_class]}")
print(f"Predicted probability: {predicted_probability * 100:.2f}%")


#print(f"Predicted class index: {predicted_class}")