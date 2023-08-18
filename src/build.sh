_ENV=$(gcloud config get-value project | cut -d '-' -f 2)
gcloud builds submit --config cloudbuild.yaml --substitutions=TAG_NAME=$(cat myapp/version.txt),_ENV=$_ENV --region us-west1