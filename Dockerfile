FROM python:3-slim

WORKDIR /pki
COPY pki/ .
COPY .env .

RUN apt update && \
   apt install -y dos2unix && \
   apt clean all

RUN dos2unix config.sh
RUN /pki/config.sh
RUN python3 /pki/ca.py
RUN echo '#!/bin/bash\n/usr/local/bin/python3 /pki/certificat.py' > /usr/bin/certificat
RUN chmod +x /usr/bin/certificat