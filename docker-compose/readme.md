# Multi-Container Application with [docker-compose](https://docs.docker.com/compose/)

 - [getting started](https://docs.docker.com/compose/gettingstarted/)
 - [example of pull & build ](https://docs.docker.com/compose/reference/pull/)
 - [name containers](https://stackoverflow.com/a/35662191/4538066)
 - [how to use multiple "Dockerfile"](https://nickjanetakis.com/blog/docker-tip-10-project-structure-with-multiple-dockerfiles-and-docker-compose)


 - [Docker use "depends_on" to control container running order](https://docs.docker.com/compose/compose-file/#dependson)

 - [Executing PostgreSQL via SQLalchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/)


### description of containers in this application

#### Postgres
  - [dont install postgres, use docker](https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198)
  
```
# connect to the db 
psql -h localhost -p 5433 -U postgres -d postgres
```

***postgres issues***
 1. [docker-compose postgres, server fails to start when mounting Windows dir for postgres/data](https://forums.docker.com/t/data-directory-var-lib-postgresql-data-pgdata-has-wrong-ownership/17963/24)
  - however a docker volume works fine. We can preserve the data on docker, just no on linux:windows file systems.
 2. [docker-compose postgres build does not notice .env variables](https://github.com/docker-library/postgres/issues/537)
  - [postgres docker files](https://github.com/docker-library/postgres/blob/cad3d8b1f7ee31f3592c2911e014e81b9b2a1c8d/10/alpine/Dockerfile)

#### Elasticsearch

```
# connect to elastic @
http://localhost:9200/
```

#### Bokeh Application

```
# connect to bokeh-application @
http://localhost:5000/
```

***bokeh issues***
 - when working across operating systems, ensure to remove DOS/UNIX line endings.
 
#### Manager Application