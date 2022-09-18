# First Approach

# Step-1 - Build the image 
docker build -t demo-app-cloudrun

# Step-2 - Test the image locally 
docker run -p 8081:8081 demo-app-cloudrun

# Step-3 - Tag the image locally 
docker tag demo-app-cloudrun gcr.io/gcp-data-processing/demo-app-cloudrun

# Step-4 - Push the image to Google Cloud Registry 
docker push gcr.io/gcp-data-processing/demo-app-cloudrun


# Second Approach 
gcloud run deploy python-bigquery-api \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --max-instances 4 \
  --min-instances 2 