# tests/test_preprocess.py
import os
import subprocess

def test_preprocess1():
    # Ensure input_raw contains at least one image
    input_raw_dir = './input_raw'
    processed_dir = './input'

    # Run the preprocessing executable
    subprocess.run(['./preprocessing', input_raw_dir, processed_dir])

    # Check if processed directory contains processed images
    processed_images = os.listdir(processed_dir)
    assert len(processed_images) > 0, "No images processed in preprocess step"

def test_preprocess2():
    processed_dir = './input'

    # Check if processed directory contains processed images
    processed_images = os.listdir(processed_dir)
    assert all(img.endswith('.jpeg') for img in processed_images), "Processed files are not in JPEG format"
