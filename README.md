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

```