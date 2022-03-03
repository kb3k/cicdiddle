docker build -t gcr.io/alpine-beacon-336222/flaskapp_cr:v5 -f Dockerfile .
docker push gcr.io/alpine-beacon-336222/flaskapp_cr:v5
gcloud run deploy flaskapp-cr-v5 --image gcr.io/alpine-beacon-336222/flaskapp_cr:v5  --region us-east1  --platform managed  --memory 128Mi
https://medium.com/fullstackai/how-to-deploy-a-simple-flask-app-on-cloud-run-with-cloud-endpoint-e10088170eb7
ab -c 10 -n 200 https://flaskapp-cr-v5-gjpc6msfrq-ue.a.run.app//
