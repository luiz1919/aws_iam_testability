import boto3
from datetime import datetime
import os

def create_and_upload_file():
    """
    Creates a dummy text file with timestamp and uploads it to S3.
    Uses environment variables for AWS configuration.
    """
    # Create a dummy file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dummy_file_{timestamp}.txt"
    
    # Write some content to the file
    with open(filename, 'w') as f:
        f.write(f"This is a dummy file created at {timestamp}\n")
        f.write("Hello from the containerized Python app!")
    
    # Get the bucket name from environment variable
    bucket_name = os.environ.get('AWS_S3_BUCKET')
    if not bucket_name:
        raise ValueError("AWS_S3_BUCKET environment variable is not set")
    
    # Upload to S3
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(filename, bucket_name, filename)
        print(f"Successfully uploaded {filename} to {bucket_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
    finally:
        # Clean up the local file
        os.remove(filename)

if __name__ == "__main__":
    create_and_upload_file()