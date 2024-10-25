# Define variables
DOCKER_IMAGE_NAME = final_project_image
CONTAINER_NAME = final_project_cont

# Target: Build Docker image
build:
	@docker build -t $(DOCKER_IMAGE_NAME) .

# Target: Build Docker image
run:
	@docker run -it --name=$(CONTAINER_NAME) -v .:/mount $(DOCKER_IMAGE_NAME)


# Target: Preprocess data
process:
	@docker exec $(CONTAINER_NAME) python /mount/script.py
