#!/bin/bash

# Create a clean directory for the build
mkdir -p tempdir
mkdir -p tempdir/static
mkdir -p tempdir/templates

# Copy your app assets to the temporary directory
# This ensures the Docker 'build context' has everything it needs
cp sample_app.py tempdir/
cp -r static/* tempdir/static/
cp -r templates/* tempdir/templates/

# --- Step 3: Create the Dockerfile ---
# These commands 'echo' the Docker instructions into the Dockerfile

echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

# --- Optional Step 4: Build the Container ---
# This part actually uses the Dockerfile we just created
# docker build -t sample-app tempdir
# docker run -t -d -p 8080:8080 --name samplerunning sample-app#!/bin/bash

# Create a clean directory for the build
mkdir -p tempdir
mkdir -p tempdir/static
mkdir -p tempdir/templates

# Copy your app assets to the temporary directory
# This ensures the Docker 'build context' has everything it needs
cp sample_app.py tempdir/
cp -r static/* tempdir/static/
cp -r templates/* tempdir/templates/

# --- Step 3: Create the Dockerfile ---
# These commands 'echo' the Docker instructions into the Dockerfile

echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

# --- Optional Step 4: Build the Container ---
# This part actually uses the Dockerfile we just created
# docker build -t sample-app tempdir
# docker run -t -d -p 8080:8080 --name samplerunning sample-app
docker run -t -d -p 8080:8080 --name samplerunning sampleapp