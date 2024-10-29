# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Set working directory.
WORKDIR /app

# Copy requirements.txt and install dependencies.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and key file.
COPY main.py main.py
COPY authentication/newkey.json /newkey.json
COPY templates/ templates/
# Set the port Flask will run on.
ENV PORT=8080

# Expose the port for the application.
EXPOSE 8080

# Command to run the app.
CMD ["python", "main.py"]
