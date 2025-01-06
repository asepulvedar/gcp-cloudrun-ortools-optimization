curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
          "overrides": {
            "containerOverrides": {
              "env": [
                {"name": "OPTIMIZATION_ID", "value": "2"},
                {"name": "CALORIES", "value": "5"},
                {"name": "PROTEIN", "value": "89"},
                {"name": "CALCIUM", "value": "0.9"},
                {"name": "IRON", "value": "13"},
                {"name": "VITAMIN_A", "value": "4"},
                {"name": "VITAMIN_B1", "value": "1.4"},
                {"name": "VITAMIN_B2", "value": "2.2"},
                {"name": "NIACIN", "value": "18"},
                {"name": "VITAMIN_C", "value": "3.5"}
              ]
            }
          }
        }' \
    "https://run.googleapis.com/v2/projects/alan-sandbox-393620/locations/us-central1/jobs/diet-optimization-realtime:run"
