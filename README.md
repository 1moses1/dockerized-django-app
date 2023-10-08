# Dockerized Django Application

## Overview

This project demonstrates how to Dockerize a Django application for easier deployment and management. It covers the following steps:

1. Creating a new Django application.
2. Preparing the Django app for Docker.
3. Building a Docker image.
4. Starting a Docker container.

## Technologies Used

- Python 3.7+
- Django 3.x
- Docker

## Prerequisites

Before running this application, make sure you have the following installed:

- Python: Install the latest Python version from [python.org](https://www.python.org/downloads/).
- Docker: Install Docker from [docker.com](https://www.docker.com/get-started).

## Getting Started

### Step 1: Create a New Django Application

- Install Python.
- Create a virtual environment for your project using `python3 -m venv env`.
- Activate the virtual environment with `source env/bin/activate` (Linux) or `.\env\Scripts\activate` (Windows).
- Install Django with `pip install django`.
- Create a new Django project using `django-admin startproject myProject`.
- Verify your project by running `python manage.py runserver` and accessing it in your browser.

### Step 2: Prepare the Django App for Docker

- Create a Django app with `python manage.py startapp myApp`.
- Define your views and URL patterns in the app.
- Create a `requirements.txt` file by running `pip freeze > requirements.txt`.
- Create a Dockerfile in the project root directory with the following content:

    ```dockerfile
    FROM python:3.7-slim

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install -r requirements.txt

    COPY . .

    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```

### Step 3: Build a Docker Image

- Build the Docker image with `docker build -t my-django-app .` (don't forget the dot at the end).

### Step 4: Start a New Docker Container

- Start a Docker container from the built image with:

    ```bash
    docker run --name my-django-app --publish 8000:8000 my-django-app
    ```

- Access the running Django application in your browser at `http://127.0.0.1:8000`.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
