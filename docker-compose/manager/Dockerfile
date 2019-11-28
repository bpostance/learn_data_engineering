FROM continuumio/miniconda3:4.5.12

# adds metadata to the image
LABEL MAINTAINER="Ben Postance"
LABEL GitHub="https://github.com/bpostance/training.docker"
LABEL version="0.0"
LABEL description="A Docker container to run a simple python script"

## Override the default shell (not supported on older docker, prepend /bin/bash -c )
SHELL ["/bin/bash", "-c"]

# Set WORKDIR - the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
WORKDIR /home/working-dir

# ADD - copies files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
ADD manager-py ./manager-py

# COPY DATA
# you can download the data from kaggle: 
# https://www.kaggle.com/zynicide/wine-reviews
COPY wine-reviews.zip ./data

# unzip
RUN unzip ./datawine-reviews.zip && \
	rm ./datawine-reviews.zip

# TIP!
# print directories if you need to debug
RUN pwd && ls -a
RUN ls ./manager-py
RUN ls ./data

# Update Env, Install utils
RUN apt-get update

# conda set-config and create environment based on .yml
RUN conda env update --file ./manager-py/environment.yml

# set env variables
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate" >> ~/.bashrc

# Command 
CMD [ "python", "./main.py" ]
