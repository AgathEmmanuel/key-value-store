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

## Quickstart

- clone this repository
- run the service locally
- run test locally
- build the docker image locally
- deployment spec with 0 downtime deployments, service spec and ingress spec
