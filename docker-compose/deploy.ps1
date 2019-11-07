# point to Linux box daemon
# In this case the host runs a Linux OS and normally provided the basic Linux packages
$env:DOCKER_HOST='tcp://host:2375'

# compose in detached mode
docker-compose up -d

# force rebuild
#docker-compose up --force-recreate --build

# stop
docker-compose down