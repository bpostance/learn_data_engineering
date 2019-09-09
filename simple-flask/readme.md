## *Flask in Docker*

A simple [flask application][1] containerized in docker.

### Files:
------------

    │
    ├── Dockerfile           <- Makefile with commands like `make data` or `make train`
    ├── launch.sh          <- Facade to start application in either dev or prod mode.
    ├── nginx.conf          <- The top-level README for developers using this project.
    ├── app
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org

 - https://hub.docker.com/r/continuumio/miniconda3
 - https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

[1]:https://stackabuse.com/dockerizing-python-applications/