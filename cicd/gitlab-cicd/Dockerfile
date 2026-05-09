# Docker image that will have git and python3 installed.
# Settled for below being the latest and runs an app not just basic /bin/bash.
# Build image using : docker build -t ci_cd/docker-image .

# docker build -t ubuntu-image-with-git-python3 .

# You can push a new image to this repository using the CLI
# https://docs.docker.com/engine/reference/commandline/push/
# docker tag local-image:tagname new-repo:tagname
# docker push new-repo:tagname
# Example
# $ docker tag ubuntu-image-with-git-python3:latest 254in61/ubuntu-python3-git:v1
# $ docker push 254in61/ubuntu-python3-git:v1
# $ docker push 254in61/ubuntu-python3-git:v1



FROM ubuntu:22.04
RUN apt -y update
RUN apt -y install git python3
# RUN git clone -b develop https://github.com/254In61/mysql_using_python.git
# ENV MY_APP=myapp.cpp
RUN apt -y install python3-pip
RUN pip3 install black && pip3 install pytest
RUN useradd -ms /bin/bash allan
RUN mkdir /home/allan/app && chmod 777 -R /home/allan/app
USER allan
