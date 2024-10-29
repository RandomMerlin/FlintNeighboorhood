# main.py
import os
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
from datetime import timedelta

app = Flask(__name__)

# Replace 'your-bucket-name' with your actual GCS bucket name.
GCS_BUCKET = 'flint-floral-park'

# The starting directory
ROOT_DIRECTORY = 'UncompressedDisplay/'

# Initialize Google Cloud Storage client
client = storage.Client()

# Function to get the list of blobs (files) in a directory
def list_files(prefix=None):
    """Lists all files in the given folder in the GCS bucket."""
    bucket = client.bucket(GCS_BUCKET)
    
    if prefix is None:
        prefix = ROOT_DIRECTORY
    
    blobs = bucket.list_blobs(prefix=prefix)  # Prefix is like folder path
    return blobs

@app.route('/')
def index():
    # List all top-level folders in the UncompressedDisplay directory
    blobs = list_files()
    directories = set()
    
    # Extract directories from blobs (folders in GCS are implicit by blob prefixes)
    printed_first_blob = False  # Flag to check if the first blob has been printed
    for blob in blobs:
        # Only get the directories that are directly under the UncompressedDisplay root
        if '/' in blob.name and blob.name.startswith(ROOT_DIRECTORY):
            # Strip 'UncompressedDisplay/' and get top-level directories
            directory = blob.name[len(ROOT_DIRECTORY):].split('/')[0]
            directories.add(directory)

            # Print the first blob found
            if not printed_first_blob:
                print("First blob in index:", blob.name)
                printed_first_blob = True
    
    return render_template('index.html', directories=directories)

@app.route('/<path:directory>')
def view_directory(directory):
    # List files in the selected directory within UncompressedDisplay
    full_prefix = ROOT_DIRECTORY + directory + '/'
    blobs = list_files(prefix=full_prefix)
    
    images = []
    subdirectories = set()

    # Collect the image files and subdirectories to display in the directory
    printed_first_blob = False  # Flag for this context as well
    for blob in blobs:
        relative_path = blob.name[len(full_prefix):]
        
        # Print the first blob found in this context
        if not printed_first_blob:
            print("First blob in view_directory:", blob.name)
            printed_first_blob = True
        
        # Check if this is a subdirectory (it has more path components)
        if '/' in relative_path:
            # Extract subdirectory name (everything before the first '/')
            subdirectory = relative_path.split('/')[0]
            subdirectories.add(subdirectory)
        elif relative_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.tif')):
            # It's an image file
            signed_url = blob.generate_signed_url(expiration=timedelta(days=1))
            images.append(signed_url)

    return render_template('directory.html', directory=directory, images=images, subdirectories=subdirectories, gcs_bucket=GCS_BUCKET)
    print("Using service account:", storage.Client().get_service_account_email())
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
