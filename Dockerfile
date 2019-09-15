# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM ubuntu:18.04
ARG CACHEBUST=1
# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=phase1 Version=0.0.1
EXPOSE 6969
# RUN sudo su
#grab msft stuff

#install python stuff
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip git curl build-essential ffmpeg

#clone git repo for app
RUN git clone https://github.com/blurredpixel/Youtube-convert-web.git
WORKDIR /Youtube-convert-web
#checkout proper branch
RUN git checkout master
ADD . /Youtube-convert-web
# RUN scl enable rh-python37 bash
#install prereqs for pyodbc

# Using pip:
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD ["form.py","-u"]

