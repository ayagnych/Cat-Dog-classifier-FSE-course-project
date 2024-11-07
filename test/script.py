import argparse
from PIL import Image
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.models import load_model

# Load model without compiling and disable custom objects (if any)
model = load_model('model.h5', compile=False, custom_objects={})

def process(input_dir, output_dir):
    # Run model inference on images in input folder and save raw results
    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        try:
            image = Image.open(img_path)
            image = np.array(image).reshape((1, 128, 128, 3))  # Assumes images are already resized to 128x128
            predictions = model.predict(image)

            # Format prediction as string with filename
            prediction_str = f"{img_name} {predictions}"
            output_path = os.path.join(output_dir, f"{img_name.split('.')[0]}_raw.txt")
            
            # Save the prediction to a text file
            with open(output_path, 'w') as f:
                f.write(prediction_str)
            
            print(f"Processed {img_name} and saved prediction to {output_path}")
        except Exception as e:
            print(f"Error processing image {img_name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--process', action='store_true', help='Run processing (inference) step')

    args = parser.parse_args()

    input_dir = './input'  # Adjusted to point to the directory with already resized images
    raw_output_dir = './output_raw'

    if args.process:
        process(input_dir, raw_output_dir)
        print('Processing completed.')
