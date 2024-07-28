import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.preprocessing import image

# Load the saved model
model = tf.keras.models.load_model('saved_model/my_model')

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Function to make predictions
def predict_traffic_sign(img_path):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    return predicted_class

# Example usage
img_path = 'path_to_image.jpg'
predicted_class = predict_traffic_sign(img_path)
print(f'Predicted class: {predicted_class}')

# Data analysis example (assuming you have a dataset)
data = {
    'Image': ['img1.jpg', 'img2.jpg', 'img3.jpg'],
    'TrueLabel': [0, 1, 2]
}
df = pd.DataFrame(data)

# Function to get predictions for a dataframe of images
def get_predictions(df):
    df['PredictedLabel'] = df['Image'].apply(predict_traffic_sign)
    return df

# Get predictions for the dataset
df = get_predictions(df)
print(df)

# Analyze the accuracy
accuracy = np.mean(df['TrueLabel'] == df['PredictedLabel'])
print(f'Accuracy: {accuracy}')

# Plot some sample images and their predictions
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, img_path in enumerate(df['Image']):
    img = image.load_img(img_path, target_size=(224, 224))
    axes[i].imshow(img)
    axes[i].set_title(f"True: {df['TrueLabel'][i]}, Pred: {df['PredictedLabel'][i]}")
    axes[i].axis('off')
plt.show()
