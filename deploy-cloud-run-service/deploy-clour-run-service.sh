#!/bin/bash

# Deploy to Cloud Run
export PROJECT_ID=your-project
export REGION=your-region
export IMAGE_NAME=${REGION}-docker.pkg.dev/$PROJECT_ID/docker-repo/diet-model-service:latest
export JOB_NAME=diet-model-service
export SERVICE_ACCOUNT=projects/$PROJECT_ID/serviceAccounts/your-service-account
export BUILD_LOGS_BUCKET=your-build-logs-bucket

# Set your project ID
gcloud config set project $PROJECT_ID

# Configure Docker to use the Google Artifact Registry
gcloud auth configure-docker \
    us-central1-docker.pkg.dev

# Build the Docker image and Push the Docker image to Artifact  Registry using Cloud Build
gcloud builds submit --tag ${IMAGE_NAME} \
    --project $PROJECT_ID \
    --timeout=30m \
    --gcs-log-dir="${BUILD_LOGS_BUCKET}" \
    --region=$REGION .


# Run the service Locally
# docker run us-central1-docker.pkg.dev/alan-sandbox-393620/docker-repo/diet-model-service

gcloud run deploy diet-model-service --image $IMAGE_NAME --platform managed --region us-central1 --allow-unauthenticated

