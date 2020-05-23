FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update

RUN apt-get update && apt-get install -y \
        build-essential\
        autoconf\
        libtool\
        pkg-config\
        dirmngr\
        libcurl4-openssl-dev \
        libnlopt-dev \
        lsb-release\
        python3.7-dev \
        python3-pip


RUN apt-get update
RUN python3.7 -m pip install pip
RUN apt-get update && apt-get install -y \
        python3-distutils \
        python3-setuptools

COPY .. /api
WORKDIR /api
RUN python3.7 -m pip install -r requirements.txt
ENTRYPOINT ["python3.7"]
CMD ["main.py"]