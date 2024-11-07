.PHONY: test

# Variables
CC = g++
CFLAGS = -std=c++17 `pkg-config --cflags opencv4`
LDFLAGS = `pkg-config --libs opencv4`
PREPROCESSING_SRC = preprocessing.cpp
POSTPROCESSING_SRC = postprocessing.cpp
PREPROCESSING_EXEC = preprocessing
POSTPROCESSING_EXEC = postprocessing
INPUT_RAW_DIR = input_raw              # Input directory path
INPUT_DIR = input        # Processed input directory path
OUTPUT_RAW_DIR = output_raw
OUTPUT_DIR = output

all: prereqs build preprocess process postprocess

# Prerequisites target to install dependencies
prereqs:
	@echo "Installing prerequisites..."
	@if [ "$(shell uname)" = "Linux" ]; then \
		echo "Detected Linux OS. Installing dependencies with apt-get..."; \
		apt-get update && apt-get install -y \
		python3 \
		python3-pip \
		vim \
		libopencv-dev \
		libboost-filesystem-dev \
		libboost-system-dev; \
		pip install pytest; \
		pip install -r requirements.txt; \
	elif [ "$(shell uname)" = "Darwin" ]; then \
		echo "Detected macOS. Installing dependencies with brew..."; \
		brew update && brew install \
		python3 \
		opencv \
		boost; \
	elif [ "$(shell uname -o)" = "Msys" ]; then \
		echo "Detected Windows. Installing dependencies with choco..."; \
		choco install -y python git vim opencv boost-msvc-14.1; \
	else \
		echo "Unsupported OS. Please install dependencies manually."; \
	fi

# Build target to compile the preprocessing executable
build: 
	@mkdir -p $(INPUT_DIR) $(OUTPUT_RAW_DIR) $(OUTPUT_DIR)
	@$(CC) -c $(PREPROCESSING_SRC) -o $(PREPROCESSING_EXEC).o $(CFLAGS)
	@chmod +x $(PREPROCESSING_EXEC).o
	@$(CC) $(PREPROCESSING_EXEC).o -o $(PREPROCESSING_EXEC) $(LDFLAGS)
	@chmod +x $(PREPROCESSING_EXEC)
	@$(CC) -c $(POSTPROCESSING_SRC) -o $(POSTPROCESSING_EXEC).o $(CFLAGS)
	@chmod +x $(POSTPROCESSING_EXEC).o
	@$(CC) $(POSTPROCESSING_EXEC).o -o $(POSTPROCESSING_EXEC) $(LDFLAGS)
	@chmod +x $(POSTPROCESSING_EXEC)
	@echo "Build completed successfully."

#Run all below
run: build preprocess process postprocess

# Run Preprocessing
preprocess:
	@echo "Running data preprocessing..."
	@./$(PREPROCESSING_EXEC)

# Process placeholder
process:
	@echo "Running data processing (classification)..."
	@python3 script.py --process

# Postprocess placeholder
postprocess:
	@echo "Running data postprocessing..."
	@./$(POSTPROCESSING_EXEC)

# Clean target to remove executables and artifacts
clean:
	@echo "Cleaning up build artifacts..."
	@rm -f $(PREPROCESSING_EXEC)
	@rm -f $(PREPROCESSING_EXEC).o
	@rm -f $(POSTPROCESSING_EXEC)
	@rm -f $(POSTPROCESSING_EXEC).o
	@rm -f ./input/*
	@rm -f ./output/*
	@rm -f ./output_raw/*
	@echo "Cleanup completed."

# Testing part
test:
	@echo "Testing..."
	python3 -m pytest test/test_preprocess.py
	python3 -m pytest test/test_process.py
	python3 -m pytest test/test_postprocess.py
	@echo "Tests completed."
