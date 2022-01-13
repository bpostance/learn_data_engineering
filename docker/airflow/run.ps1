# run migrations
docker-compose up airflow-init

# run airflow-init
docker-compose up

# clean up
# docker-compose down --volumes --rmi all