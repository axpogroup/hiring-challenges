# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the source code of the Storage API to the container
COPY src .

# Install the required dependencies
RUN pip3 install -e .

# Expose the port on which the API will run
EXPOSE 5000

# Start the Storage API when the container is run
CMD ["python3", "run.py"]