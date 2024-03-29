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
- Make the application handle concurrent requests  
- Enable consensus to ensure reliability and fault tolerance   
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
docker image tag kvstore-service:v1 [docker-hub-username]/kvstore-service:v1
docker push [docker-hub-username]/kvstore-service:v1

# Replace the dockerhub username in image of manifests/ with your valid name

```
- run kvstore on top of Kubernetes with zero downtime deployment characteristics
```

############# NOTE  ################
The kvstore is an in memory key-value store and hence each replica pods of the kvstore deployment
have different key-value pairs in each pods, and there will be no downtime for the service but,
the pods get terminated the key value pairs in there memory also is lost


# To create deployment, service and ingress for single node cluster
kubectl create -f manifests/deploy-single-node.yaml

# To create deployment, service and ingress  for multi node cluster
kubectl create -f manifests/deploy-multi-node.yaml

# To create an ingress on Minikube
kubectl create -f manifests/ingress.yaml



# To create hpa and pdb for the app service
kubectl create -f manifests/hpa.yaml
kubectl create -f manifests/pdb.yaml

```
- sample prometheus metrics available at /metrics endpoint of kvstore-service
```
http_latency_status_keys_count{method="GET",no_of_keys="4",path_template="/get/{key}",status_code="200"} 1.0
http_latency_status_keys_sum{method="GET",no_of_keys="4",path_template="/get/{key}",status_code="200"} 0.0005483729764819145

http_response_total{method="GET",no_of_keys="4",path_template="/metrics",status_code="200"} 2.0
http_response_total{method="GET",no_of_keys="4",path_template="/get/{key}",status_code="404"} 1.0
```

# Status  
The kvstore is an in memory key-value store and hence each replica pods of the kvstore deployment
have different key-value pairs in each pods, and there will be no downtime for the service but,
the pods get terminated the key value pairs in there memory also is lost, and the response to each
request will completely depend on the key value pairs stored in teh pods that are processing those
requests.


# Links  
[Deep Dive: etcd - Jingyi Hu, Google](https://youtu.be/DrtdrdwDpZE)  
[https://etcd.io/docs/v2.3/benchmarks/etcd-storage-memory-benchmark/](https://etcd.io/docs/v2.3/benchmarks/etcd-storage-memory-benchmark/)  
[https://raft.github.io/](https://raft.github.io/)  
[https://github.com/memcached/memcached](https://github.com/memcached/memcached)  
[https://medium.com/fintechexplained/advanced-python-how-to-implement-caching-in-python-application-9d0a4136b845](https://medium.com/fintechexplained/advanced-python-how-to-implement-caching-in-python-application-9d0a4136b845)  
[https://medium.com/fintechexplained/advanced-python-learn-how-to-profile-python-code-1068055460f9](https://medium.com/fintechexplained/advanced-python-learn-how-to-profile-python-code-1068055460f9)  
[https://medium.com/fintechexplained/advanced-python-concurrency-and-parallelism-82e378f26ced](https://medium.com/fintechexplained/advanced-python-concurrency-and-parallelism-82e378f26ced)  
[https://medium.com/fintechexplained/advanced-python-metaprogramming-980da1be0c7d\9https://medium.com/fintechexplained/advanced-python-metaprogramming-980da1be0c7d)  
[https://towardsdev.com/how-to-package-your-python-code-1cdf8ceabf63](https://towardsdev.com/how-to-package-your-python-code-1cdf8ceabf63)  
[https://github.com/dianchengwangCHN/raft-key-value-store](https://github.com/dianchengwangCHN/raft-key-value-store)  
[https://www.fivetran.com/blog/databases-demystified-distributed-databases-part-3](https://www.fivetran.com/blog/databases-demystified-distributed-databases-part-3)  
[https://www.yugabyte.com/blog/how-does-consensus-based-replication-work-in-distributed-databases/](https://www.yugabyte.com/blog/how-does-consensus-based-replication-work-in-distributed-databases/)  

