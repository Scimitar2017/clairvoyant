#!/bin/bash

#start container
docker-compose build
docker-compose up -d

# Wait for the container to start
sleep 5

docker-compose logs -f

# Stop container
docker-compose down
