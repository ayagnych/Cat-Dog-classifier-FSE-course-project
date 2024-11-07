# tests/test_process.py
import os
import subprocess
import numpy as np

def test_process1():
    # Ensure input directory contains at least one preprocessed image
    input_dir = './input'
    output_raw_dir = './output_raw'

    # Run the script.py process command
    subprocess.run(['python3', 'script.py', '--process'])

    # Check if output_raw directory contains prediction files
    prediction_files = os.listdir(output_raw_dir)
    assert len(prediction_files) > 0, "No prediction files generated in process step"

def test_process2():
    output_raw_dir = './output_raw'

    # Check if output_raw directory contains prediction files
    prediction_files = os.listdir(output_raw_dir)
    assert all(file.endswith('.txt') for file in prediction_files), "Output files are not in .txt format"
