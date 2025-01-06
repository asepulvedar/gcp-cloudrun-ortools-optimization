# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
EXPOSE $PORT

# Run the Flask Service
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080" ]