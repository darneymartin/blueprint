FROM python:3.13.7

# Set a label for the image
LABEL maintainer="Darnell Martin"
LABEL description="Dockerfile to run Blueprint"

# Upgrade pip
RUN pip install --upgrade pip

# Set the Working Directory
WORKDIR /app

COPY requirements.txt .

# Install Requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy Source
COPY src .

# Copy Configuration
COPY kube_config.yml kube_config.yml 
COPY blueprint.yml blueprint.yml 

# Run the application
CMD ["python", "app.py"]