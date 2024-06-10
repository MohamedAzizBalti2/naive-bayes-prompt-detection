# Prompt Detection Model

## Overview
This project aims to detect various types of prompts. The model is trained to classify phrases into different categories, such as "benign", "injection", and "jailbreak".

## Getting Started

### Prerequisites
Make sure you have Docker installed on your machine. You can download Docker from [here](https://www.docker.com/get-started).

### Build and Run the Project

1. **Build the Docker Image**

   Open your terminal and navigate to the project directory. Then, run the following command to build the Docker image:

   ```sh
   docker build -t naive-bayes-prompt-detection .
2. **Run the Docker Container**

After the image is built, run the following command to start the Docker container:

   ```sh
docker run -p 80:80 naive-bayes-prompt-detection .
   ```
**API Endpoints**
Once the Docker container is running, the FastAPI application will be accessible at http://localhost:80. You can use tools like Postman or cURL to interact with the API.

**Health Check**
To check the health of the API, send a GET request to the root endpoint:
   ```sh
GET http://localhost:80/
```
**Predict Endpoint**
To make a prediction, send a POST request to the /predict endpoint with the following JSON payload:

```json
{
  "text": "Your input text here"
}
```
**Example Response**
The response will be a JSON object with the predicted class probabilities:

```json
{
  "predictions": {
    "benign": 0.0022,
    "injection": 0.0167,
    "jailbreak": 0.9811
  }
}
```
