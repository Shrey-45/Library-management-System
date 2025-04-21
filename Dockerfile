# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5656 for the Django app
EXPOSE 5656

# Define the default command to run the application
CMD ["gunicorn", "library_management.wsgi:application", "--bind", "0.0.0.0:5656", "--reload"]
