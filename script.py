import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np
import os

path_to_model = './model.h5'
path_to_image = './input/images2.jpeg'
input_dir = "input"
output_raw_dir = '/output_raw'
output_dir = "output_raw"

model = keras.models.load_model(path_to_model)

os.makedirs(output_dir, exist_ok=True)

def preprocess(input_dir, output_dir):
    # Load images from input_raw, resize them, and save them in input folder
    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        image = Image.open(img_path)
        image = image.resize((128, 128))  # Resize to fit the model input
        image.save(os.path.join(output_dir, img_name))

def process(input_dir, output_dir):
    # Run model inference on images in input folder and save raw results
    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        image = Image.open(img_path)
        img_array = np.array(image)
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        np.save(os.path.join(output_dir, f"{img_name.split('.')[0]}_raw.npy"), predictions)

def postprocess(input_dir):
    # Postprocess raw results (this step is optional and depends on the output format)
    for result_name in os.listdir(input_dir):
        result_path = os.path.join(input_dir, result_name)
        result = np.load(result_path)
        # For demonstration, we'll just print the raw results
        print(f"Postprocessing result for {result_name}: {result}")


print('started')
preprocess(input_dir, output_raw_dir)
print('preprocess complited')
process(output_raw_dir, output_dir)
print('process complited')
postprocess(output_dir)
print('finished')
