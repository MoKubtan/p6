# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED True

# Install pip requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy local code to the container image.
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Run the web service on container startup. Here we use the gunicorn
# web server, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app

EXPOSE 8000