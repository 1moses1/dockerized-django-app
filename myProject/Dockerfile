# Set the base image (host OS)
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the root directory into the working directory
COPY . .

# Command to run on the container to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

