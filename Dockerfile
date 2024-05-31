# Use the tiangolo/uvicorn-gunicorn-fastapi image as the base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application code to the working directory
COPY ./app /app/app

# Expose the required port
EXPOSE 80

# Set the default command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
