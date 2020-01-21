FROM continuumio/miniconda3:4.5.12

# adds metadata to the image
LABEL MAINTAINER="Ben Postance"
LABEL GitHub="https://github.com/bpostance/training.docker"
LABEL version="0.0"
LABEL description="A Docker container to run a simple python script"

## Override the default shell (not supported on older docker, prepend /bin/bash -c )
SHELL ["/bin/bash", "-c"]

# Update Env, Install utils
RUN apt-get update && \
    apt-get install zip unzip && \
    apt-get clean

# Set WORKDIR - the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
WORKDIR /home/working-dir

# ADD - copies files and directories from <src> and adds them to  the filesystem of the container at <dest>.
ADD manager-py ./manager-py

# RUN bash to curl the data
# you can download the data from kaggle: 
# https://www.kaggle.com/zynicide/wine-reviews
# OR from google
# https://drive.google.com/file/d/1pqZvEIMKehdoiCNaob2HutHTdvCbtLub/view?usp=sharing
RUN chmod +x ./manager-py/gdrive.sh && \
    ./manager-py/gdrive.sh && \
    unzip ./wine-reviews.zip && \
    rm ./wine-reviews.zip && \
    mkdir ./data && \
    mv ./wine-reviews ./data/wine-reviews

# conda set-config and create environment based on .yml
# conda update -n base -c defaults conda && \
RUN    conda env update --file ./manager-py/environment.yml && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate" >> ~/.bashrc

# Command 
CMD ["python","/home/working-dir/manager-py/main.py"]
