# Multi-Container Application with [docker-compose](https://docs.docker.com/compose/)

An example of a multi-container application using docker-compose. The docker-compose.yml is used to spin up several containers including:
 - postgres db.
 - elasticsearch instance.
 - ubuntu:manager to perform data ETL and analysis.
 - ubunut:flask-bokeh to host a simple dashboard using Python Flask and Bokeh.

The kaggle [wine-reviews](https://www.kaggle.com/zynicide/wine-reviews#winemag-data_first150k.csv) dataset is used as an example as it include numeric and text data for statistical and or unstructured data mining, textual analysis, and natural language processing. 

```
# build and run docker-compose
docker-compose up -d --build


```

## References:
### docker-compose
 - [getting started with docker-compose](https://docs.docker.com/compose/gettingstarted/)
 - [example of pull & build commands](https://docs.docker.com/compose/reference/pull/)
 - [naming containers](https://stackoverflow.com/a/35662191/4538066)
 - [how to use multiple "Dockerfile" with docker-compose](https://nickjanetakis.com/blog/docker-tip-10-project-structure-with-multiple-dockerfiles-and-docker-compose)
 - [use "depends_on" to control running order of containers](https://docs.docker.com/compose/compose-file/#dependson)


### Postgres
  - [dont install postgres, use docker](https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198)
  - [official postgres docker files](https://github.com/docker-library/postgres/blob/cad3d8b1f7ee31f3592c2911e014e81b9b2a1c8d/10/alpine/Dockerfile)
  - [docker-compose postgres, server fails to start when mounting Windows dir for postgres/data](https://forums.docker.com/t/data-directory-var-lib-postgresql-data-pgdata-has-wrong-ownership/17963/24). Using a docker volume to persist data works fine within docker. However, you will hit issues when trying to use a mounted volume between OS e.g. linux:windows file systems.
  - [docker-compose postgres build does not notice .env variables](https://github.com/docker-library/postgres/issues/537)

```
# connect to the docker db 
psql -h localhost -p 5433 -U postgres -d postgres
```

### Elasticsearch

```
# connect to elastic @
http://localhost:9200/
```

 
### Manager Application
  - [Executing PostgreSQL via SQLalchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/)


### Bokeh Application
 - [flask & bokeh](http://biobits.org/bokeh-flask.html)
 - when working across operating systems, ensure to remove DOS/UNIX line endings.

```
# connect to bokeh-application @
http://localhost:5000/
```

