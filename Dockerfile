# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock /app/

# Install dependencies
RUN pipenv install --system --dev --skip-lock

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
