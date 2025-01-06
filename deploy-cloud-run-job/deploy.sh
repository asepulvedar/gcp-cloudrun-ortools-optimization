# Description: Deploy the Cloud Run job
# Variables:
export PROJECT_ID=your-project-id
export REGION=your-region
export IMAGE_NAME=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/ortools-diet
export JOB_NAME=diet-optimization-realtime

# Set your project ID
gcloud config set project $PROJECT_ID

# Configure Docker to use the Google Artifact Registry
gcloud auth configure-docker \
    us-central1-docker.pkg.dev

# Build the Docker image
docker build -t ${IMAGE_NAME} .

# Push the Docker image to Google Container Registry
docker push ${IMAGE_NAME}

# Delete the Cloud Run job if exists
gcloud run jobs delete diet-optimization-realtime --region $REGION --quiet

# Create the Cloud Run job
gcloud beta run jobs create $JOB_NAME --image $IMAGE_NAME --region $REGION