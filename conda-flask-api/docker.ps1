# docker build
docker build -t demo/flask-api:0.0 .

# docker run
# --name assign name for ease of reference
# -d to run in detached mode
# -p to bind container:local ports
# container to run
docker run --name demo-flask-api -p 5000:5000 demo/flask-api:0.0