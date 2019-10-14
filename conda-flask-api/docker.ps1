# docker build
# --rm to remove any intermediate containers built during build.
docker build --rm -t demo/flask-api:0.0 .

# docker run
# --rm remove the container once it is stopped.
# --name assign name for ease of reference
# -d to run in detached mode
# -p to bind container:local ports
# container to run
docker run --rm --name demo-flask-api -p 5000:5000 demo/flask-api:0.0