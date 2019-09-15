# Examples of common applications in Docker containers
 - conda-flask-api
```
│
├── conda-flask-api
│   ├ Dockerfile          <- Dockerfile instructions to build the container
│   ├ docker.psq          <- powershell commands to build & run the Dockerfile 
│   ├ env.yml             <- conda environment
│   ├ serve.sh            <- script to serve the app using gunicorn
│   ├── app
│   │   ├── flask-api.py  <- application file
```

##### *List of common Docker commands*
```
# list running containers
docker container ls

# list all containers
docker container ls -a

# stop all containers
docker stop $(docker ps -a -q)

# remove all containters
docker rm $(docker ps -a -q)


# build container
docker build -t tag_name:version .

# run container
docker run --name easy_name -d --restart=always -p 8080:8080 tag_name:version

# show log from container
docker logs --tail 50 easy_name


# list images 
docker images ls

# remove an image
docker rmi <image_id>

# Purge All Unused or Dangling Images, Containers, Volumes, and Networks
docker system prune
```
