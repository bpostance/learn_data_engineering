# Examples and demo's of Docker containers


### *Common Commands*
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
```