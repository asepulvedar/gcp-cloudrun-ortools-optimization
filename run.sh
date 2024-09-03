# Execute the job
export REGION=us-central1

# delete the job if exists
gcloud run jobs execute diet-optimization-realtime --update-env-vars OPTIMIZATION_ID=100 --region ${REGION}

