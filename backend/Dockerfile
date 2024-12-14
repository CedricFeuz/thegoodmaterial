# Base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy all application files into the container
COPY . .

# Command to start the Flask application
CMD ["python", "app.py"]

