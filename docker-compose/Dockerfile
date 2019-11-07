FROM continuumio/miniconda3:4.5.12

# adds metadata to the image
LABEL MAINTAINER="Ben Postance"
LABEL GitHub="https://github.com/bpostance/training.docker"
LABEL version="0.0"
LABEL description="A Docker container to serve a simple Python Flask API"

## Override the default shell (not supported on older docker, prepend /bin/bash -c )
SHELL ["/bin/bash", "-c"]

# Set WORKDIR - the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
WORKDIR /home/working-dir

# COPY - copies files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
ADD simple-app ./simple-app

# chmod - modifies the bokeh-entrypoint.sh file 
# so it can be recognized as an executable file.
COPY bokeh-entrypoint.sh ./
RUN chmod +x bokeh-entrypoint.sh

# DOS line endings are not compatible with Linux
# use sed to remove them
RUN sed -i 's/^M$//' bokeh-entrypoint.sh

# TIP!
# print directories if you need to debug
#RUN pwd && ls -a
#RUN ls ./simple-app

# Update Env, Install utils
RUN apt-get update

# conda set-config and create environment based on .yml
RUN conda env update --file ./simple-app/environment.yml

# set env variables
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate" >> ~/.bashrc

# EXPOSE - informs Docker that the container listens on the specified network ports at runtime
EXPOSE 5000

# ENTRYPOINT - allows you to configure a container that will run as an executable.
ENTRYPOINT ["./bokeh-entrypoint.sh"]
