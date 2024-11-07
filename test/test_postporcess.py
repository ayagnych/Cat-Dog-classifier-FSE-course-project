# tests/test_postprocess.py
import os
import subprocess

def test_postprocess1():
    # Ensure output_raw directory contains prediction files
    output_raw_dir = './output_raw'
    output_dir = './output'

    # Run the postprocessing executable
    subprocess.run(['./postprocessing'])

    # Check if output directory contains labeled text files
    labeled_files = os.listdir(output_dir)
    assert len(labeled_files) > 0, "No labeled files generated in postprocess step"

def test_postprocess2():
    output_dir = './output'
    labeled_files = os.listdir(output_dir)
    assert all(file.endswith('_label.txt') for file in labeled_files), "Labeled files are not in .txt format"

def test_postprocess3():
    output_dir = './output'
    labeled_files = os.listdir(output_dir)
    # Check contents of a labeled file
    with open(os.path.join(output_dir, labeled_files[0]), 'r') as f:
        content = f.read()
        assert " --> " in content, "Labeled file does not contain expected format"

def test_postprocess4():
    output_dir = './output'
    labeled_files = os.listdir(output_dir)
    # Check contents of a labeled file
    with open(os.path.join(output_dir, labeled_files[0]), 'r') as f:
        content = f.read()
        assert "Cat" in content or "Dog" in content, "Label not correctly assigned as Cat or Dog"
