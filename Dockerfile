FROM python:3-slim

COPY pki /pki
COPY .env /pki/.env

RUN /pki/config.sh
RUN python3 /pki/ca.py
RUN echo '#!/bin/bash\n/usr/local/bin/python3 /pki/certificat.py' > /usr/bin/certificat
RUN chmod +x /usr/bin/certificat

RUN apt update && \
    apt install -y openjdk-17-jdk && \
    apt clean all
