# use docker image
FROM continuumio/miniconda3

# set user
MAINTAINER Ben Postance "benpostance@gmail.com"

# update linux
RUN apt-get update -y

# create conda environment
RUN conda create -n env python=3.6 pip

# activate conda env
RUN echo "source activate env" > ~/.bashrc

# set path
ENV PATH /opt/conda/envs/env/bin:$PATH

# make directories on container
RUN mkdir docker_app docker_app/app && cd docker_app

# copy file to container
COPY ./requirements.txt ./docker_app
COPY ./app/app.py ./docker_app/app

# install requirements
RUN pip install -r ./docker_app/requirements.txt

RUN ls
RUN ls ./docker_app

# expose container port
EXPOSE 8080
CMD ["python", "./docker_app/app/app.py"]