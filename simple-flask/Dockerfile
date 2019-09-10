# use docker image
FROM continuumio/miniconda3

# set user
MAINTAINER Ben Postance "benpostance@gmail.com"

# update linux, install
RUN apt-get update -y && \
    apt-get install -y nginx uwsgi uwsgi-plugin-python3

# create conda environment
RUN conda create -n env python=3.6 pip

# activate conda env
RUN echo "source activate env" > ~/.bashrc

# set env path
ENV PATH /opt/conda/envs/env/bin:$PATH

# make directories on container and change_directory
RUN mkdir docker_app docker_app/app

# copy files to container
COPY ./requirements.txt ./docker_app
COPY ./app/app.py ./docker_app/app
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./launcher.sh ./docker_app

# install requirements
RUN pip install -r ./docker_app/requirements.txt

# expose container port
EXPOSE 8080

# add server user
RUN adduser --disabled-password --gecos '' nginx\
  && chown -R nginx:nginx /docker_app/app \
  && chmod 777 /run/ -R \
  && chmod 777 /root/ -R
  
# run commands
#CMD ["python", "./docker_app/app/app.py"]
ENTRYPOINT [ "./bin/bash", "./docker_app/launcher.sh"]