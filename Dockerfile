# Start with a base Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container
COPY model.h5 script.py /app/
COPY requirements.txt /app/
COPY input /app/input

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create necessary directories
RUN mkdir -p /app/input_raw /app/output_raw /app/output

# Set the default command to run when the container starts
CMD ["bash"]

