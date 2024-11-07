# FSE
Educational project for the course "Foundations of software engineering for AI". The project is designed for image processing and classification using a pretrained machine learning model.

# Running the project

### Clone the repo
```bash
git clone https://github.com/ayagnych/Cat-Dog-classifier-FSE-course-project
```

## Using inside Docker image
### Build the Docker image
```bash
docker build -t my_project_image .
```

### Run the Docker Container
```bash
docker run -it --name my_project_container my_project_image
```

## Building software using Makefile
That will work if you are already inside docker container or started it manually 

### Build all dependencies and executables

Here you run preprocess, process and postprocess parts

```bash
make run
```
OR
```bash
make build
make preprocess
make process
make postprocess
```
## Other Functions

### Run tests
```bash
make build
make test
```

### Clean files
```bash
make clean
```

### Project Structure

- input_raw - folder for initial images
- input - folder for preprocessed images
- output_raw - folder for intermediate processing results
- output - folder for final postprocessed results

## Examples of Inputs

### Input for preprocessing

The input_raw directory provides example images for cats and dogs in JPEG format, used throughout the entire preprocess-process-postprocess chain.

After preprocessing the image is resized to 128x128 format and being stored in input directory.

### Input for processing 

Here it uses the resized picture from input directory in order to make classification on cats vs dogs.

After processing the resized image is converted in class prediction using model.h5 in output_raw directory as .txt file. It is either [[1. 0.]] or [[0. 1.]].

### Input for postprocessing

Here it uses .txt file from output_raw and translates from model written format into readable by humans - whether it is cat or dog. For instance, it translates "[[1. 0.]]" into "Cat" and "[[0. 1.]]" into "Dog".

It stores the result of classification in output directory as .txt format.




