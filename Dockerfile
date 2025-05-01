FROM python:3-slim

WORKDIR /pki
COPY pki/ .
COPY .env .

RUN apt update &&\
   apt install -y openjdk-17-jdk &&\
   apt clean all

RUN /pki/config.sh
RUN python3 /pki/ca.py
RUN echo '#!/bin/bash\n/usr/local/bin/python3 /pki/certificat.py' > /usr/bin/certificat
RUN chmod +x /usr/bin/certificat
