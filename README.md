# Key-Value Store Service

## Features

Create an in-memory key-value store HTTP API Service which implements:

- /get/<key> → Return value of the key
- /set → Post call which sets the key/value pair
- /search → Search for keys using the following filters
  - Assume you have keys: abc-1, abc-2, xyz-1, xyz-2
  - /search?prefix=abc would return abc-1 and abc-2
  - /search?suffix=-1 would return abc-1 and xyz-1
  - implementation of prefix & suffix functionality for search
- Prometheus exporter for service which measures:
  - latency of each endpoint
  - http status codes for each endpoint hit
  - total no. of keys in the DB
- Kubernetes deployment spec for 0 downtime deployments, service spec and ingress spec

## Quickstart

- clone this repository
```
git clone https://github.com/AgathEmmanuel/key-value-store.git
```
- run the service locally
```
pip install virtualenv
virtualenv [name of your new virtual environment]
source [name of your new virtual environment]/bin/activate
pip install -r requirements.txt

python3 app/kvstore.py

deactivate
```
- run test locally
```
pip install pytest
pytest
```
- build the docker image locally
```
docker build -t kvstore-service:v1 .
```
- run the app as a docker service  
```
docker run kvstore-service:v1
```
- to get the ip-address of the kvstore-service docker container
```
# to get the container id
docker ps 

# to get ip address of container
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <contaniner id>
```
- to push the image to dockerhub  
```
docker image tag scraper_service:v1 [docker-hub-username]/kvstore-service:v1
docker push [docker-hub-username]/kvstore-service:v1

# Replace the dockerhub username in manifests/scraper-deploy.yaml with you valid name

```
- run kvstore on top of Kubernetes with zero downtime during deployments  
```
# To create deployment, service and ingress 
kubectl create -f manifests/deploy.yaml
kubectl create -f manifests/ingress.yaml

# To create hpa and pdb for the app service
kubectl create -f manifests/hpa.yaml
kubectl create -f manifests/pdb.yaml

```